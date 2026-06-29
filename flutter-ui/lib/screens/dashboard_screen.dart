import 'dart:convert';
import 'dart:math';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart' show rootBundle;
import 'package:provider/provider.dart';
import '../providers/game_provider.dart';
import '../models/models.dart';

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({Key? key}) : super(key: key);

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  String _activeView = 'TABLE'; // TABLE, CREATE, LOAD
  bool _mapLoading = true;
  bool _mapError = false;
  Map<String, dynamic>? _geoJsonData;

  String? _selectedStateName;
  int _selectedScenarioIndex = 0;
  int _selectedEra = 2001; // 2001 or 2006

  // Creation setup state
  final List<TextEditingController> _partyNameControllers = [
    TextEditingController(text: 'Party 1'),
    TextEditingController(text: 'Party 2'),
    TextEditingController(text: 'Party 3'),
  ];
  final List<String> _partyControllers = ['HUMAN', 'COMPUTER', 'COMPUTER'];
  final List<String> _partyAiProfiles = ['BALANCED_STRATEGIST', 'BALANCED_STRATEGIST', 'BALANCED_STRATEGIST'];
  final List<String> _partyColors = ['#E15554', '#3F88C5', '#17B890'];
  final List<String> _partySymbols = ['Tiger', 'Elephant', 'Peacock'];

  bool _retainInstitutions = false;

  final List<String> _presetColors = [
    '#E15554', // Orange-Red
    '#3F88C5', // Blue
    '#17B890', // Emerald Green
    '#FF9933', // Saffron (BJP)
    '#128807', // Dark Green (INC)
    '#D23F31', // Red (CPM)
    '#0095B6', // Cyan (TMC)
    '#FDD835', // Yellow (TDP)
  ];

  final List<String> _availableSymbols = [
    'Tiger', 'Elephant', 'Peacock', 'Lotus', 'Hand', 'Hammer',
    'Bicycle', 'Arrow', 'Lantern', 'Twin Flowers', 'Bow & Arrow',
    'Ceiling Fan', 'Two Leaves', 'Rising Sun', 'Star', 'Flag'
  ];

  @override
  void initState() {
    super.initState();
    _loadGeoJson();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final provider = Provider.of<GameProvider>(context, listen: false);
      provider.loadSavedGames();
      provider.loadScenarios();
    });
  }

  @override
  void dispose() {
    for (var controller in _partyNameControllers) {
      controller.dispose();
    }
    super.dispose();
  }

  Future<void> _loadGeoJson() async {
    try {
      final jsonStr = await rootBundle.loadString('assets/india_states.geojson');
      setState(() {
        _geoJsonData = json.decode(jsonStr);
        _mapLoading = false;
      });
    } catch (e) {
      debugPrint('Failed to load map GeoJSON: $e');
      setState(() {
        _mapLoading = false;
        _mapError = true;
      });
    }
  }

  void _onScenarioChanged(int idx, List<ScenarioProgress> activeScenarios) {
    if (idx < 0 || idx >= activeScenarios.length) return;
    final scenario = activeScenarios[idx];
    final def = scenario.scenarioDefinition;
    if (def != null && def.politicalParties.length == 3) {
      for (int i = 0; i < 3; i++) {
        final p = def.politicalParties[i];
        _partyNameControllers[i].text = p.name;
        _partyControllers[i] = p.controllerType;
        _partyColors[i] = p.color;
        _partySymbols[i] = p.symbol;
        if (p.aiProfile != null) {
          _partyAiProfiles[i] = p.aiProfile!['style'] ?? 'BALANCED_STRATEGIST';
        } else {
          _partyAiProfiles[i] = 'BALANCED_STRATEGIST';
        }
      }
    }
    setState(() {
      _selectedScenarioIndex = idx;
    });
  }

  Future<void> _handleStartGame(ScenarioProgress scenario) async {
    final provider = Provider.of<GameProvider>(context, listen: false);
    final def = scenario.scenarioDefinition;
    if (def == null) return;

    final partySetups = List.generate(3, (i) {
      final originalParty = def.politicalParties[i];
      return {
        'partyKey': originalParty.partyKey,
        'partyName': _partyNameControllers[i].text.trim(),
        'role': originalParty.role,
        'controllerType': _partyControllers[i],
        'color': _partyColors[i],
        'symbol': _partySymbols[i],
        'ideology': originalParty.ideology,
        'aiProfile': _partyControllers[i] == 'COMPUTER'
            ? {'style': _partyAiProfiles[i]}
            : null,
        'startingStats': originalParty.startingStats?.toJson()
      };
    });

    final payload = {
      'scenarioKey': scenario.scenarioKey,
      'retainInstitutions': _retainInstitutions,
      'partySetups': partySetups,
    };

    final success = await provider.createNewGame(payload);
    if (!success && mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(provider.errorMessage ?? 'Failed to start campaign')),
      );
    }
  }

  Future<void> _handleLoadGame(String gameId) async {
    final provider = Provider.of<GameProvider>(context, listen: false);
    final success = await provider.loadGame(gameId);
    if (!success && mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(provider.errorMessage ?? 'Failed to load campaign')),
      );
    }
  }

  Future<void> _handleDeleteGame(String gameId) async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Delete Campaign?'),
        content: const Text('Are you sure you want to delete this campaign? This action cannot be undone.'),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('Cancel')),
          TextButton(
            onPressed: () => Navigator.pop(ctx, true),
            style: TextButton.styleFrom(primary: Colors.red),
            child: const Text('Delete'),
          ),
        ],
      ),
    );

    if (confirmed == true && mounted) {
      final provider = Provider.of<GameProvider>(context, listen: false);
      await provider.deleteGame(gameId);
    }
  }

  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<GameProvider>(context);
    final isMobile = MediaQuery.of(context).size.width < 768;

    // Filter scenarios available for era selection
    final listScenarios = provider.scenarios.where((s) {
      final def = s.scenarioDefinition;
      if (def == null) return false;
      final startYear = int.tryParse(def.startDate.split('-')[0]) ?? 2001;
      return startYear == _selectedEra && s.status != 'LOCKED';
    }).toList();

    return Scaffold(
      backgroundColor: const Color(0xFFE6E6FA), // Lavender
      appBar: AppBar(
        backgroundColor: const Color(0xFF213C51),
        title: const Text('BHARAT RAJNEETI'),
        actions: [
          if (provider.user != null)
            Padding(
              padding: const EdgeInsets.only(right: 16),
              child: Center(
                child: Text(
                  'User: ${provider.user!.name}',
                  style: const TextStyle(fontWeight: FontWeight.bold),
                ),
              ),
            ),
          IconButton(
            onPressed: provider.logout,
            icon: const Icon(Icons.logout),
            tooltip: 'Logout',
          )
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            // Top Dashboard Banner
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(24),
              decoration: BoxDecoration(
                color: const Color(0xFF213C51), // Deep Blue
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: const Color(0xFFB0CBE0), width: 2),
              ),
              child: const Column(
                children: [
                  Text(
                    'Dashboard',
                    style: TextStyle(
                      fontSize: 32,
                      fontWeight: FontWeight.w900,
                      color: Colors.white,
                    ),
                  ),
                  SizedBox(height: 6),
                  Text(
                    'Select a campaign to manage or start a new political journey.',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontSize: 14,
                      color: Colors.whiteb8,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),

            // Content Grid
            isMobile
                ? Column(
                    children: [
                      _buildMapCard(provider.scenarios),
                      const SizedBox(height: 24),
                      _buildActionPanel(listScenarios, provider.savedGames, provider.isLoading),
                    ],
                  )
                : Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Expanded(
                        flex: 12,
                        child: _buildMapCard(provider.scenarios),
                      ),
                      const SizedBox(width: 24),
                      Expanded(
                        flex: 10,
                        child: _buildActionPanel(listScenarios, provider.savedGames, provider.isLoading),
                      ),
                    ],
                  ),
          ],
        ),
      ),
    );
  }

  Widget _buildMapCard(List<ScenarioProgress> allScenarios) {
    if (_mapLoading) {
      return Container(
        height: 480,
        decoration: BoxDecoration(
          color: Colors.white,
          border: Border.all(color: const Color(0xFFB0CBE0), width: 2),
          borderRadius: BorderRadius.circular(12),
        ),
        child: const Center(
          child: CircularProgressIndicator(),
        ),
      );
    }

    if (_mapError || _geoJsonData == null) {
      return Container(
        height: 480,
        decoration: BoxDecoration(
          color: Colors.white,
          border: Border.all(color: const Color(0xFFB0CBE0), width: 2),
          borderRadius: BorderRadius.circular(12),
        ),
        child: const Center(
          child: Text(
            '⚠️ Failed to load map coordinates.',
            style: TextStyle(color: Colors.red, fontWeight: FontWeight.bold),
          ),
        ),
      );
    }

    // Find clicked scenario
    ScenarioProgress? selectedScenario;
    if (_selectedStateName != null) {
      selectedScenario = allScenarios.firstWhere(
        (s) => s.stateName.toLowerCase() == _selectedStateName!.toLowerCase() &&
               (s.scenarioDefinition != null &&
                (int.tryParse(s.scenarioDefinition!.startDate.split('-')[0]) ?? 2001) == _selectedEra),
        orElse: () => ScenarioProgress(scenarioKey: '', name: '', description: '', stateName: '', status: 'LOCKED'),
      );
    }

    final activeGameForState = selectedScenario != null && selectedScenario.scenarioKey.isNotEmpty
        ? context.read<GameProvider>().savedGames.firstWhere((g) => g.scenarioKey == selectedScenario!.scenarioKey && g.status == 'ACTIVE', orElse: () => GameSessionSummary(id: '', scenarioKey: '', currentDate: '', turnNumber: 0, status: ''))
        : null;

    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        border: Border.all(color: const Color(0xFFB0CBE0), width: 2),
        borderRadius: BorderRadius.circular(12),
      ),
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Map Header bar
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Row(
                children: [
                  Text('🗺️', style: TextStyle(fontSize: 18)),
                  SizedBox(width: 8),
                  Text(
                    'India Campaign Map',
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFF213C51),
                    ),
                  ),
                ],
              ),
              Row(
                children: [
                  const Text(
                    'ERA: ',
                    style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF475569)),
                  ),
                  DropdownButton<int>(
                    value: _selectedEra,
                    dropdownColor: Colors.white,
                    style: const TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                    onChanged: (val) {
                      if (val != null) {
                        setState(() {
                          _selectedEra = val;
                          _selectedStateName = null;
                        });
                      }
                    },
                    items: const [
                      DropdownMenuItem(value: 2001, child: Text('2001 Era')),
                      DropdownMenuItem(value: 2006, child: Text('2006 Era')),
                    ],
                  ),
                ],
              ),
            ],
          ),
          const SizedBox(height: 12),

          // Interactive Map Area
          Container(
            height: 480,
            decoration: BoxDecoration(
              color: const Color(0xFFF8FAFC),
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: const Color(0xFFB0CBE0), width: 1),
            ),
            child: InteractiveViewer(
              maxScale: 5.0,
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: LayoutBuilder(
                  builder: (ctx, constraints) {
                    return GestureDetector(
                      onTapDown: (details) {
                        _handleMapTap(details.localPosition, constraints.size);
                      },
                      child: CustomPaint(
                        size: Size(constraints.maxWidth, constraints.maxHeight),
                        painter: IndiaMapPainter(
                          geoJson: _geoJsonData!,
                          scenarios: allScenarios,
                          era: _selectedEra,
                          selectedStateName: _selectedStateName,
                        ),
                      ),
                    );
                  },
                ),
              ),
            ),
          ),
          const SizedBox(height: 12),

          // Map Legends
          _buildMapLegends(),

          // Scenario Info Box
          if (selectedScenario != null && selectedScenario.scenarioKey.isNotEmpty) ...[
            const SizedBox(height: 16),
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: const Color(0x1AB0CBE0),
                border: Border.all(color: const Color(0xFFB0CBE0), width: 1.5),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            selectedScenario.stateName,
                            style: const TextStyle(
                              fontSize: 16,
                              fontWeight: FontWeight.bold,
                              color: Color(0xFF213C51),
                            ),
                          ),
                          Text(
                            selectedScenario.name,
                            style: const TextStyle(fontSize: 12, color: Color(0xFF475569), fontWeight: FontWeight.bold),
                          ),
                        ],
                      ),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                        decoration: BoxDecoration(
                          color: selectedScenario.status == 'WON'
                              ? const Color(0xFFDBEAFE)
                              : selectedScenario.status == 'LOCKED'
                                  ? const Color(0xFFF1F5F9)
                                  : const Color(0xFFDCFCE7),
                          border: Border.all(
                            color: selectedScenario.status == 'WON'
                                ? const Color(0xFFBFDBFE)
                                : selectedScenario.status == 'LOCKED'
                                    ? const Color(0xFFE2E8F0)
                                    : const Color(0xFFBBF7D0),
                          ),
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: Text(
                          selectedScenario.status == 'IN_PROGRESS' ? 'In Progress' : selectedScenario.status,
                          style: TextStyle(
                            fontSize: 10,
                            fontWeight: FontWeight.bold,
                            color: selectedScenario.status == 'WON'
                                ? const Color(0xFF1E40AF)
                                : selectedScenario.status == 'LOCKED'
                                    ? const Color(0xFF64748B)
                                    : const Color(0xFF15803D),
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  Text(
                    selectedScenario.description,
                    style: const TextStyle(fontSize: 12, color: Color(0xFF475569), height: 1.4),
                  ),
                  const SizedBox(height: 12),
                  Row(
                    children: [
                      if (selectedScenario.status != 'LOCKED')
                        ElevatedButton(
                          onPressed: () {
                            final idx = allScenarios.indexWhere((s) => s.scenarioKey == selectedScenario!.scenarioKey);
                            if (idx != -1) {
                              _onScenarioChanged(idx, allScenarios);
                              setState(() {
                                _activeView = 'CREATE';
                              });
                            }
                          },
                          style: ElevatedButton.styleFrom(
                            primary: const Color(0xFF213C51),
                            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                          ),
                          child: Text(
                            selectedScenario.status == 'WON' ? '🔄 Replay Campaign' : '🎮 Start Campaign',
                            style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
                          ),
                        ),
                      if (activeGameForState != null && activeGameForState.id.isNotEmpty) ...[
                        const SizedBox(width: 10),
                        ElevatedButton(
                          onPressed: () => _handleLoadGame(activeGameForState.id),
                          style: ElevatedButton.styleFrom(
                            primary: const Color(0xFF22C55E),
                            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                          ),
                          child: const Text(
                            '📂 Resume Session',
                            style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
                          ),
                        ),
                      ],
                    ],
                  ),
                ],
              ),
            ),
          ]
        ],
      ),
    );
  }

  Widget _buildMapLegends() {
    return const Wrap(
      spacing: 12,
      runSpacing: 6,
      alignment: WrapAlignment.center,
      children: [
        MapLegendPill(color: Color(0xFF22C55E), label: 'Available'),
        MapLegendPill(color: Color(0xFFF59E0B), label: 'In Progress'),
        MapLegendPill(color: Color(0xFF3B82F6), label: 'Won'),
        MapLegendPill(color: Color(0xFFCBD5E1), label: 'Locked'),
        MapLegendPill(color: Color(0xFFF1F5F9), label: 'No Campaign'),
      ],
    );
  }

  Widget _buildActionPanel(
    List<ScenarioProgress> activeScenarios,
    List<GameSessionSummary> savedGames,
    bool isLoading,
  ) {
    if (_activeView == 'CREATE') {
      return _buildCreateCampaignPanel(activeScenarios, isLoading);
    }
    if (_activeView == 'LOAD') {
      return _buildLoadCampaignPanel(savedGames, isLoading);
    }
    return _buildCampaignsStatusPanel(savedGames, isLoading);
  }

  Widget _buildCampaignsStatusPanel(List<GameSessionSummary> savedGames, bool isLoading) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        border: Border.all(color: const Color(0xFFB0CBE0), width: 2),
        borderRadius: BorderRadius.circular(12),
      ),
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          const Text(
            '📊 Campaigns Status',
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
              color: Color(0xFF213C51),
            ),
          ),
          const SizedBox(height: 12),
          savedGames.isEmpty
              ? const Padding(
                  padding: EdgeInsets.symmetric(vertical: 24),
                  child: Center(
                    child: Text(
                      'No saved campaigns found.',
                      style: TextStyle(color: Color(0xFF475569), fontStyle: FontStyle.italic),
                    ),
                  ),
                )
              : ListView.builder(
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  itemCount: savedGames.length,
                  itemBuilder: (ctx, idx) {
                    final game = savedGames[idx];
                    return Container(
                      padding: const EdgeInsets.all(12),
                      margin: const EdgeInsets.only(bottom: 8),
                      decoration: const BoxDecoration(
                        border: Border(bottom: BorderSide(color: Color(0x1A6594B1))),
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                game.scenarioName ?? game.scenarioKey,
                                style: const TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                              ),
                              Text(
                                'Turn ${game.turnNumber} | Date: ${game.currentDate}',
                                style: const TextStyle(fontSize: 11, color: Color(0xFF475569)),
                              ),
                            ],
                          ),
                          Text(
                            game.status,
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.bold,
                              color: game.status == 'COMPLETED' ? Colors.grey : const Color(0xFF22C55E),
                            ),
                          ),
                        ],
                      ),
                    );
                  },
                ),
          const SizedBox(height: 24),
          Row(
            children: [
              Expanded(
                child: ElevatedButton(
                  onPressed: () {
                    if (activeScenarios.isNotEmpty) {
                      _onScenarioChanged(0, activeScenarios);
                    }
                    setState(() {
                      _activeView = 'CREATE';
                    });
                  },
                  style: ElevatedButton.styleFrom(
                    primary: const Color(0xFF213C51),
                    padding: const EdgeInsets.symmetric(vertical: 14),
                  ),
                  child: const Text('🎮 Create Campaign'),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: ElevatedButton(
                  onPressed: () {
                    setState(() {
                      _activeView = 'LOAD';
                    });
                  },
                  style: ElevatedButton.styleFrom(
                    primary: const Color(0xFF213C51),
                    padding: const EdgeInsets.symmetric(vertical: 14),
                  ),
                  child: const Text('📂 Load Saved'),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildCreateCampaignPanel(List<ScenarioProgress> activeScenarios, bool isLoading) {
    if (activeScenarios.isEmpty) {
      return Container(
        decoration: BoxDecoration(
          color: Colors.white,
          border: Border.all(color: const Color(0xFFB0CBE0), width: 2),
          borderRadius: BorderRadius.circular(12),
        ),
        padding: const EdgeInsets.all(20),
        child: const Center(child: Text('No active scenarios available.')),
      );
    }

    final currentScenario = activeScenarios[_selectedScenarioIndex];
    final isEra2006 = currentScenario.scenarioKey.endsWith('_2006');

    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        border: Border.all(color: const Color(0xFFB0CBE0), width: 2),
        borderRadius: BorderRadius.circular(12),
      ),
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text(
                'Create New Campaign',
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: Color(0xFF213C51),
                ),
              ),
              IconButton(
                onPressed: () => setState(() => _activeView = 'TABLE'),
                icon: const Icon(Icons.close, color: Color(0xFF213C51)),
              ),
            ],
          ),
          const SizedBox(height: 12),

          // Scenario Selector
          const Text('Select Scenario:', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFF213C51))),
          const SizedBox(height: 6),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 10),
            decoration: BoxDecoration(
              color: const Color(0xFF213C51),
              borderRadius: BorderRadius.circular(8),
            ),
            child: DropdownButton<int>(
              value: _selectedScenarioIndex,
              isExpanded: true,
              dropdownColor: const Color(0xFF213C51),
              underline: const SizedBox(),
              style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
              onChanged: (val) {
                if (val != null) {
                  _onScenarioChanged(val, activeScenarios);
                }
              },
              items: List.generate(
                activeScenarios.length,
                (i) => DropdownMenuItem(
                  value: i,
                  child: Text(activeScenarios[i].name, overflow: TextOverflow.ellipsis),
                ),
              ),
            ),
          ),
          const SizedBox(height: 20),

          // Custom Party Setups Checklist
          const Text('Configure Political Parties:', style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: Color(0xFF213C51))),
          const SizedBox(height: 10),
          ...List.generate(3, (idx) {
            final role = idx == 0 ? 'Government' : idx == 1 ? 'Opposition' : 'Third Party';
            return Container(
              margin: const EdgeInsets.only(bottom: 12),
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                border: Border.all(color: const Color(0xFFB0CBE0)),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Party ${idx + 1} ($role)',
                    style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 12, color: Color(0xFF213C51)),
                  ),
                  const SizedBox(height: 8),
                  TextField(
                    controller: _partyNameControllers[idx],
                    style: const TextStyle(color: Colors.white),
                    decoration: InputDecoration(
                      filled: true,
                      fillColor: const Color(0xFF213C51),
                      isDense: true,
                      contentPadding: const EdgeInsets.all(10),
                      border: OutlineInputBorder(borderRadius: BorderRadius.circular(6)),
                    ),
                  ),
                  const SizedBox(height: 8),
                  Row(
                    children: [
                      Expanded(
                        child: DropdownButtonFormField<String>(
                          value: _partyControllers[idx],
                          decoration: const InputDecoration(isDense: true, contentPadding: EdgeInsets.all(6)),
                          dropdownColor: const Color(0xFF213C51),
                          style: const TextStyle(color: Color(0xFF213C51), fontWeight: FontWeight.bold),
                          onChanged: (val) {
                            if (val != null) {
                              setState(() {
                                _partyControllers[idx] = val;
                              });
                            }
                          },
                          items: const [
                            DropdownMenuItem(value: 'HUMAN', child: Text('Player')),
                            DropdownMenuItem(value: 'COMPUTER', child: Text('AI')),
                          ],
                        ),
                      ),
                      if (_partyControllers[idx] == 'COMPUTER') ...[
                        const SizedBox(width: 8),
                        Expanded(
                          child: DropdownButtonFormField<String>(
                            value: _partyAiProfiles[idx],
                            decoration: const InputDecoration(isDense: true, contentPadding: EdgeInsets.all(6)),
                            dropdownColor: const Color(0xFF213C51),
                            style: const TextStyle(color: Color(0xFF213C51), fontWeight: FontWeight.bold),
                            onChanged: (val) {
                              if (val != null) {
                                setState(() {
                                  _partyAiProfiles[idx] = val;
                                });
                              }
                            },
                            items: const [
                              DropdownMenuItem(value: 'BALANCED_STRATEGIST', child: Text('Balanced')),
                              DropdownMenuItem(value: 'STRENGTH_BUILDER', child: Text('Builder')),
                              DropdownMenuItem(value: 'AGGRESSIVE_ATTACKER', child: Text('Attacker')),
                              DropdownMenuItem(value: 'LATE_STRIKER', child: Text('Late Striker')),
                              DropdownMenuItem(value: 'AGGRESSIVE_BIDDER', child: Text('Bidder')),
                            ],
                          ),
                        ),
                      ]
                    ],
                  ),
                  const SizedBox(height: 8),
                  
                  // Preset Colors selector
                  const Text('Party Primary Color:', style: TextStyle(fontSize: 10, color: Color(0xFF475569))),
                  const SizedBox(height: 4),
                  Row(
                    children: _presetColors.map((colorHex) {
                      final c = Color(int.parse(colorHex.replaceFirst('#', '0xFF')));
                      final isSelected = _partyColors[idx] == colorHex;
                      return GestureDetector(
                        onTap: () => setState(() => _partyColors[idx] = colorHex),
                        child: Container(
                          margin: const EdgeInsets.only(right: 6),
                          width: 18,
                          height: 18,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: c,
                            border: Border.all(
                              color: isSelected ? Colors.black : Colors.transparent,
                              width: 1.5,
                            ),
                          ),
                        ),
                      );
                    }).toList(),
                  ),
                  const SizedBox(height: 8),

                  // Symbol selector
                  const Text('Party Symbol Badge:', style: TextStyle(fontSize: 10, color: Color(0xFF475569))),
                  const SizedBox(height: 4),
                  Container(
                    height: 32,
                    child: ListView.builder(
                      scrollDirection: Axis.horizontal,
                      itemCount: _availableSymbols.length,
                      itemBuilder: (context, sIdx) {
                        final sym = _availableSymbols[sIdx];
                        final isSelected = _partySymbols[idx] == sym;
                        return GestureDetector(
                          onTap: () => setState(() => _partySymbols[idx] = sym),
                          child: Container(
                            margin: const EdgeInsets.only(right: 6),
                            padding: const EdgeInsets.symmetric(horizontal: 8),
                            decoration: BoxDecoration(
                              color: isSelected ? const Color(0xFF213C51) : Colors.transparent,
                              border: Border.all(color: const Color(0xFFB0CBE0)),
                              borderRadius: BorderRadius.circular(16),
                            ),
                            alignment: Alignment.center,
                            child: Text(
                              sym,
                              style: TextStyle(
                                fontSize: 10,
                                fontWeight: FontWeight.bold,
                                color: isSelected ? Colors.white : const Color(0xFF213C51),
                              ),
                            ),
                          ),
                        );
                      },
                    ),
                  ),
                ],
              ),
            );
          }),

          // Carry forward completed institutions checkbox
          if (isEra2006) ...[
            Row(
              children: [
                Checkbox(
                  value: _retainInstitutions,
                  onChanged: (val) {
                    if (val != null) {
                      setState(() {
                        _retainInstitutions = val;
                      });
                    }
                  },
                ),
                const Expanded(
                  child: Text(
                    'Carry forward completed public institutions from previous campaign',
                    style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
          ],

          // Start Game Trigger Button
          ElevatedButton(
            onPressed: isLoading ? null : () => _handleStartGame(currentScenario),
            style: ElevatedButton.styleFrom(
              primary: const Color(0xFF22C55E),
              padding: const EdgeInsets.symmetric(vertical: 16),
            ),
            child: isLoading
                ? const SizedBox(
                    width: 20,
                    height: 20,
                    child: CircularProgressIndicator(strokeWidth: 2, valueColor: AlwaysStoppedAnimation<Color>(Colors.white)),
                  )
                : const Text(
                    'Start Game',
                    style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                  ),
          ),
        ],
      ),
    );
  }

  Widget _buildLoadCampaignPanel(List<GameSessionSummary> savedGames, bool isLoading) {
    final activeGames = savedGames.where((g) => g.status == 'ACTIVE').toList();

    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        border: Border.all(color: const Color(0xFFB0CBE0), width: 2),
        borderRadius: BorderRadius.circular(12),
      ),
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text(
                'Load Saved Campaign',
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: Color(0xFF213C51),
                ),
              ),
              IconButton(
                onPressed: () => setState(() => _activeView = 'TABLE'),
                icon: const Icon(Icons.close, color: Color(0xFF213C51)),
              ),
            ],
          ),
          const SizedBox(height: 12),
          activeGames.isEmpty
              ? const Padding(
                  padding: EdgeInsets.symmetric(vertical: 24),
                  child: Center(
                    child: Text(
                      'No active saved campaigns found.',
                      style: TextStyle(color: Color(0xFF475569), fontStyle: FontStyle.italic),
                    ),
                  ),
                )
              : Column(
                  children: activeGames.map((game) {
                    return Container(
                      padding: const EdgeInsets.all(12),
                      margin: const EdgeInsets.only(bottom: 12),
                      decoration: BoxDecoration(
                        border: Border.all(color: const Color(0xFFB0CBE0)),
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: [
                          Text(
                            game.scenarioName ?? game.scenarioKey,
                            style: const TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                          ),
                          const SizedBox(height: 4),
                          Text(
                            'Turn ${game.turnNumber} | Started: ${game.currentDate}',
                            style: const TextStyle(fontSize: 11, color: Color(0xFF475569)),
                          ),
                          const SizedBox(height: 12),
                          Row(
                            children: [
                              Expanded(
                                child: ElevatedButton(
                                  onPressed: () => _handleLoadGame(game.id),
                                  style: ElevatedButton.styleFrom(
                                    primary: const Color(0xFF213C51),
                                    isDense: true,
                                  ),
                                  child: const Text('Load Game', style: TextStyle(fontSize: 11)),
                                ),
                              ),
                              const SizedBox(width: 8),
                              Expanded(
                                child: ElevatedButton(
                                  onPressed: () => _handleDeleteGame(game.id),
                                  style: ElevatedButton.styleFrom(
                                    primary: const Color(0xFFD9534F),
                                    isDense: true,
                                  ),
                                  child: const Text('🗑️ Delete', style: TextStyle(fontSize: 11)),
                                ),
                              ),
                            ],
                          ),
                        ],
                      ),
                    );
                  }).toList(),
                ),
        ],
      ),
    );
  }

  // --- Map Click Coordinates Matching Ray-cast ---
  void _handleMapTap(Offset tapPosition, Size mapSize) {
    if (_geoJsonData == null) return;

    // First: calculate geo bounds
    double minLng = 180, maxLng = -180, minLat = 90, maxLat = -90;
    final List<dynamic> features = _geoJsonData!['features'];
    for (var feature in features) {
      final geometry = feature['geometry'];
      if (geometry == null) continue;
      final coords = geometry['coordinates'];
      final type = geometry['type'];

      void checkCoord(List<dynamic> c) {
        double lng = double.parse(c[0].toString());
        double lat = double.parse(c[1].toString());
        if (lng < minLng) minLng = lng;
        if (lng > maxLng) maxLng = lng;
        if (lat < minLat) minLat = lat;
        if (lat > maxLat) maxLat = lat;
      }

      if (type == 'Polygon') {
        for (var ring in coords) {
          for (var c in ring) {
            checkCoord(c);
          }
        }
      } else if (type == 'MultiPolygon') {
        for (var poly in coords) {
          for (var ring in poly) {
            for (var c in ring) {
              checkCoord(c);
            }
          }
        }
      }
    }

    final double pad = 15;
    final double innerW = mapSize.width - 2 * pad;
    final double innerH = mapSize.height - 2 * pad;

    final double lngDelta = maxLng - minLng;
    final double latDelta = maxLat - minLat;
    final double latToLngRatio = cos((minLat + maxLat) / 2 * pi / 180);

    final double scaleX = innerW / lngDelta;
    final double scaleY = innerH / (latDelta / latToLngRatio);
    final double scale = min(scaleX, scaleY);

    final double offsetX = pad + (innerW - lngDelta * scale) / 2;
    final double offsetY = pad + (innerH - (latDelta / latToLngRatio) * scale) / 2;

    // Check click hit inside constructed Paths
    String? hitStateName;

    for (var feature in features) {
      final properties = feature['properties'] ?? {};
      final stateName = properties['ST_NM'];
      final geometry = feature['geometry'];
      if (geometry == null) continue;
      final coords = geometry['coordinates'];
      final type = geometry['type'];

      Offset project(List<dynamic> c) {
        double lng = double.parse(c[0].toString());
        double lat = double.parse(c[1].toString());
        double x = offsetX + (lng - minLng) * scale;
        double y = mapSize.height - (offsetY + (lat - minLat) * latToLngRatio * scale);
        return Offset(x, y);
      }

      Path path = Path();

      if (type == 'Polygon') {
        final ring = coords[0];
        if (ring.isNotEmpty) {
          path.moveTo(project(ring[0]).dx, project(ring[0]).dy);
          for (int i = 1; i < ring.length; i++) {
            path.lineTo(project(ring[i]).dx, project(project(ring[i]).dy).dy);
            // wait, lineTo expects dx/dy correctly:
            path.lineTo(project(ring[i]).dx, project(ring[i]).dy);
          }
          path.close();
        }
      } else if (type == 'MultiPolygon') {
        for (var poly in coords) {
          final ring = poly[0];
          if (ring.isNotEmpty) {
            path.moveTo(project(ring[0]).dx, project(ring[0]).dy);
            for (int i = 1; i < ring.length; i++) {
              path.lineTo(project(ring[i]).dx, project(ring[i]).dy);
            }
            path.close();
          }
        }
      }

      // Check if tap inside state path
      if (path.contains(tapPosition)) {
        hitStateName = stateName;
        break;
      }
    }

    if (hitStateName != null) {
      // Confirm there is an active scenario config for this state in the active Era
      final hasScenario = context.read<GameProvider>().scenarios.any(
            (s) => s.stateName.toLowerCase() == hitStateName!.toLowerCase() &&
                   s.scenarioDefinition != null &&
                   (int.tryParse(s.scenarioDefinition!.startDate.split('-')[0]) ?? 2001) == _selectedEra,
          );
      if (hasScenario) {
        setState(() {
          _selectedStateName = hitStateName;
        });
      }
    }
  }
}

class MapLegendPill extends StatelessWidget {
  final Color color;
  final String label;

  const MapLegendPill({Key? key, required this.color, required this.label}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Container(
          width: 12,
          height: 12,
          decoration: BoxDecoration(
            color: color,
            borderRadius: BorderRadius.circular(3),
            border: Border.all(color: const Color(0xFF94A3B8)),
          ),
        ),
        const SizedBox(width: 5),
        Text(
          label,
          style: const TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
        ),
      ],
    );
  }
}

// Custom painter to draw interactive GeoJSON boundaries of India
class IndiaMapPainter extends CustomPainter {
  final Map<String, dynamic> geoJson;
  final List<ScenarioProgress> scenarios;
  final int era;
  final String? selectedStateName;

  IndiaMapPainter({
    required this.geoJson,
    required this.scenarios,
    required this.era,
    required this.selectedStateName,
  });

  @override
  void paint(Canvas canvas, Size size) {
    // 1. Calculate bounding box of coordinates
    double minLng = 180, maxLng = -180, minLat = 90, maxLat = -90;
    final List<dynamic> features = geoJson['features'];
    for (var feature in features) {
      final geometry = feature['geometry'];
      if (geometry == null) continue;
      final coords = geometry['coordinates'];
      final type = geometry['type'];

      void checkCoord(List<dynamic> c) {
        double lng = double.parse(c[0].toString());
        double lat = double.parse(c[1].toString());
        if (lng < minLng) minLng = lng;
        if (lng > maxLng) maxLng = lng;
        if (lat < minLat) minLat = lat;
        if (lat > maxLat) maxLat = lat;
      }

      if (type == 'Polygon') {
        for (var ring in coords) {
          for (var c in ring) {
            checkCoord(c);
          }
        }
      } else if (type == 'MultiPolygon') {
        for (var poly in coords) {
          for (var ring in poly) {
            for (var c in ring) {
              checkCoord(c);
            }
          }
        }
      }
    }

    final double pad = 15;
    final double innerW = size.width - 2 * pad;
    final double innerH = size.height - 2 * pad;

    final double lngDelta = maxLng - minLng;
    final double latDelta = maxLat - minLat;
    final double latToLngRatio = cos((minLat + maxLat) / 2 * pi / 180);

    final double scaleX = innerW / lngDelta;
    final double scaleY = innerH / (latDelta / latToLngRatio);
    final double scale = min(scaleX, scaleY);

    final double offsetX = pad + (innerW - lngDelta * scale) / 2;
    final double offsetY = pad + (innerH - (latDelta / latToLngRatio) * scale) / 2;

    // Paint paths
    final paintFill = Paint()..style = PaintingStyle.fill;
    final paintBorder = Paint()
      ..style = PaintingStyle.stroke
      ..color = const Color(0xFF94A3B8)
      ..strokeWidth = 0.5;

    for (var feature in features) {
      final properties = feature['properties'] ?? {};
      final stateName = properties['ST_NM'];
      final geometry = feature['geometry'];
      if (geometry == null) continue;
      final coords = geometry['coordinates'];
      final type = geometry['type'];

      Offset project(List<dynamic> c) {
        double lng = double.parse(c[0].toString());
        double lat = double.parse(c[1].toString());
        double x = offsetX + (lng - minLng) * scale;
        double y = size.height - (offsetY + (lat - minLat) * latToLngRatio * scale);
        return Offset(x, y);
      }

      Path path = Path();

      if (type == 'Polygon') {
        final ring = coords[0];
        if (ring.isNotEmpty) {
          path.moveTo(project(ring[0]).dx, project(ring[0]).dy);
          for (int i = 1; i < ring.length; i++) {
            path.lineTo(project(ring[i]).dx, project(ring[i]).dy);
          }
          path.close();
        }
      } else if (type == 'MultiPolygon') {
        for (var poly in coords) {
          final ring = poly[0];
          if (ring.isNotEmpty) {
            path.moveTo(project(ring[0]).dx, project(ring[0]).dy);
            for (int i = 1; i < ring.length; i++) {
              path.lineTo(project(ring[i]).dx, project(ring[i]).dy);
            }
            path.close();
          }
        }
      }

      // Check scenario status for color coding
      final scenario = scenarios.firstWhere(
        (s) => s.stateName.toLowerCase() == stateName.toString().toLowerCase() &&
               s.scenarioDefinition != null &&
               (int.tryParse(s.scenarioDefinition!.startDate.split('-')[0]) ?? 2001) == era,
        orElse: () => ScenarioProgress(scenarioKey: '', name: '', description: '', stateName: '', status: 'LOCKED'),
      );

      Color fillColor = const Color(0xFFF1F5F9);
      if (scenario.scenarioKey.isNotEmpty) {
        if (scenario.status == 'LOCKED') {
          fillColor = const Color(0xFFCBD5E1);
        } else if (scenario.status == 'IN_PROGRESS') {
          fillColor = const Color(0xFFF59E0B);
        } else if (scenario.status == 'AVAILABLE') {
          fillColor = const Color(0xFF22C55E);
        } else if (scenario.status == 'WON') {
          fillColor = const Color(0xFF3B82F6);
        }
      }

      final isSelected = selectedStateName != null && selectedStateName!.toLowerCase() == stateName.toString().toLowerCase();

      paintFill.color = fillColor;
      canvas.drawPath(path, paintFill);

      if (isSelected) {
        final selectedBorder = Paint()
          ..style = PaintingStyle.stroke
          ..color = const Color(0xFF0F172A)
          ..strokeWidth = 2.0;
        canvas.drawPath(path, selectedBorder);
      } else {
        canvas.drawPath(path, paintBorder);
      }
    }
  }

  @override
  bool shouldRepaint(covariant IndiaMapPainter oldDelegate) {
    return oldDelegate.selectedStateName != selectedStateName ||
        oldDelegate.era != era ||
        oldDelegate.scenarios != scenarios;
  }
}
