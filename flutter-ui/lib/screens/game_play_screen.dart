import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/game_provider.dart';
import '../models/models.dart';
import 'widgets/stats_view.dart';
import 'widgets/actions_view.dart';

class GamePlayScreen extends StatefulWidget {
  const GamePlayScreen({Key? key}) : super(key: key);

  @override
  State<GamePlayScreen> createState() => _GamePlayScreenState();
}

class _GamePlayScreenState extends State<GamePlayScreen> {
  String _activeView = 'INFO'; // INFO or ACTION

  // Preset party symbols and icons
  static const Map<String, IconData> _symbolIcons = {
    'lotus': Icons.filter_vintage,
    'hand': Icons.front_hand,
    'hammer': Icons.gavel,
    'fist': Icons.pan_tool,
    'tiger': Icons.pets,
    'elephant': Icons.pets,
    'peacock': Icons.flutter_dash,
    'bicycle': Icons.directions_bike,
    'arrow': Icons.navigation,
    'lantern': Icons.lightbulb,
    'flower': Icons.local_florist,
    'bow': Icons.architecture,
    'fan': Icons.toys,
    'leaves': Icons.eco,
    'sun': Icons.wb_sunny,
    'star': Icons.star,
    'flag': Icons.flag
  };

  static IconData getSymbolIcon(String symbol) {
    final s = symbol.toLowerCase().trim();
    if (s.contains('lotus') || s == 'bjp') return _symbolIcons['lotus']!;
    if (s.contains('hand') || s == 'inc' || s == 'congress') return _symbolIcons['hand']!;
    if (s.contains('hammer') || s.contains('sickle') || s == 'cpim' || s == 'cpi') return _symbolIcons['hammer']!;
    if (s.contains('fist')) return _symbolIcons['fist']!;
    if (s.contains('tiger')) return _symbolIcons['tiger']!;
    if (s.contains('elephant') || s == 'bsp') return _symbolIcons['elephant']!;
    if (s.contains('peacock')) return _symbolIcons['peacock']!;
    if (s.contains('bicycle') || s == 'tdp' || s == 'sp') return _symbolIcons['bicycle']!;
    if (s.contains('arrow') || s == 'jdu') return _symbolIcons['arrow']!;
    if (s.contains('lantern') || s == 'rjd') return _symbolIcons['lantern']!;
    if (s.contains('flower') || s == 'tmc') return _symbolIcons['flower']!;
    if (s.contains('bow') || s.contains('shiv') || s == 'sena') return _symbolIcons['bow']!;
    if (s.contains('fan') || s.contains('ysr')) return _symbolIcons['fan']!;
    if (s.contains('leaf') || s.contains('leaves') || s == 'aiadmk') return _symbolIcons['leaves']!;
    if (s.contains('sun') || s == 'dmk') return _symbolIcons['sun']!;
    if (s.contains('star')) return _symbolIcons['star']!;
    return _symbolIcons['flag']!;
  }

  static Color parseHexColor(String hex) {
    try {
      return Color(int.parse(hex.replaceFirst('#', '0xFF')));
    } catch (_) {
      return const Color(0xFF213C51);
    }
  }

  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<GameProvider>(context);
    final turnData = provider.currentTurnView;
    if (turnData == null) {
      return const Scaffold(
        backgroundColor: Color(0xFFE6E6FA),
        body: Center(child: Text('Loading Campaign State...')),
      );
    }

    final mediaQuery = MediaQuery.of(context);
    final isMobile = mediaQuery.size.width < 768;

    // Find active playing party
    final activeParty = turnData.parties.firstWhere(
      (p) => p.id == turnData.activeHumanPartyId,
      orElse: () => turnData.parties.firstWhere((p) => p.playerControlled),
    );

    final partyColor = parseHexColor(activeParty.color);
    final symbolIcon = getSymbolIcon(activeParty.symbol);

    // If campaign ends (Victory or Defeat)
    if (turnData.status == 'VICTORY' ||
        turnData.status == 'DEFEAT' ||
        turnData.status == 'GAME_OVER' ||
        turnData.status == 'FORFEITED') {
      return _buildEndGameScreen(turnData, activeParty);
    }

    return Scaffold(
      backgroundColor: const Color(0xFFE6E6FA), // Lavender background
      body: SafeArea(
        child: Stack(
          children: [
            SingleChildScrollView(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  // Game Header Banner
                  _buildHeaderBanner(activeParty.name, partyColor),
                  const SizedBox(height: 16),

                  // View Toggle Bar
                  _buildViewToggleBar(partyColor),
                  const SizedBox(height: 16),

                  // Curved Layout Wrapper
                  Container(
                    decoration: BoxDecoration(
                      color: Colors.white,
                      border: Border.all(color: partyColor, width: 2),
                      borderRadius: BorderRadius.circular(20),
                      boxShadow: const [
                        BoxShadow(
                          color: Color(0x14213C51),
                          blurRadius: 30,
                          offset: Offset(0, 10),
                        ),
                      ],
                    ),
                    clipBehavior: Clip.antiAlias,
                    child: isMobile
                        ? Column(
                            crossAxisAlignment: CrossAxisAlignment.stretch,
                            children: [
                              // Mobile horizontal sidebar strip
                              Container(
                                height: 60,
                                color: partyColor,
                                padding: const EdgeInsets.symmetric(horizontal: 20),
                                child: Row(
                                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                  children: [
                                    Container(
                                      width: 40,
                                      height: 40,
                                      decoration: const BoxDecoration(
                                        shape: BoxShape.circle,
                                        color: Colors.white,
                                      ),
                                      child: Icon(symbolIcon, color: partyColor, size: 24),
                                    ),
                                    Text(
                                      activeParty.role,
                                      style: const TextStyle(
                                        color: Colors.white,
                                        fontWeight: FontWeight.bold,
                                        fontSize: 12,
                                        letterSpacing: 1.0,
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                              Container(
                                padding: const EdgeInsets.all(16),
                                child: _buildActiveViewContent(provider, turnData, activeParty),
                              ),
                            ],
                          )
                        : Row(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              // Desktop vertical sidebar strip
                              Container(
                                width: 76,
                                height: 600, // min height representation
                                color: partyColor,
                                padding: const EdgeInsets.only(top: 30),
                                child: Column(
                                  children: [
                                    Container(
                                      width: 50,
                                      height: 50,
                                      decoration: const BoxDecoration(
                                        shape: BoxShape.circle,
                                        color: Colors.white,
                                      ),
                                      child: Icon(symbolIcon, color: partyColor, size: 30),
                                    ),
                                  ],
                                ),
                              ),
                              // Right main content panel
                              Expanded(
                                child: Container(
                                  padding: const EdgeInsets.all(30),
                                  decoration: BoxDecoration(
                                    border: Border(
                                      left: BorderSide(
                                        color: partyColor,
                                        width: 4,
                                        style: BorderStyle.double,
                                      ),
                                    ),
                                  ),
                                  child: _buildActiveViewContent(provider, turnData, activeParty),
                                ),
                              ),
                            ],
                          ),
                  ),
                ],
              ),
            ),

            // Floating green navigation arrow (Proceed to Actions)
            if (_activeView == 'INFO')
              Positioned(
                right: isMobile ? 12 : 25,
                top: mediaQuery.size.height * 0.45,
                child: GestureDetector(
                  onTap: () {
                    setState(() {
                      _activeView = 'ACTION';
                    });
                  },
                  child: Container(
                    width: isMobile ? 48 : 64,
                    height: isMobile ? 48 : 64,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      gradient: const LinearGradient(
                        colors: [Color(0xFF22C55E), Color(0xFF15803D)],
                      ),
                      border: Border.all(color: Colors.white, width: isMobile ? 2 : 3),
                      boxShadow: const [
                        BoxShadow(
                          color: Color(0x6622C55E),
                          blurRadius: 15,
                          offset: Offset(0, 4),
                        ),
                      ],
                    ),
                    child: Center(
                      child: Icon(
                        Icons.arrow_forward_rounded,
                        color: Colors.white,
                        size: isMobile ? 20 : 28,
                      ),
                    ),
                  ),
                ),
              ),
          ],
        ),
      ),
    );
  }

  Widget _buildHeaderBanner(String partyName, Color partyColor) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
      decoration: BoxDecoration(
        color: partyColor,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: const Color(0xFF213C51), width: 2),
      ),
      child: Column(
        children: [
          const Text(
            'GRAND CAMPAIGN BOARD',
            textAlign: TextAlign.center,
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.w900,
              color: Colors.white,
              letterSpacing: 2.0,
            ),
          ),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
            decoration: BoxDecoration(
              color: const Color(0xFF213C51),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: Colors.white24),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  width: 10,
                  height: 10,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: partyColor,
                  ),
                ),
                const SizedBox(width: 8),
                Text(
                  'PLAYING AS: ${partyName.toUpperCase()}',
                  style: const TextStyle(
                    fontSize: 11,
                    fontWeight: FontWeight.w900,
                    color: Colors.white,
                    letterSpacing: 0.5,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildViewToggleBar(Color partyColor) {
    return Row(
      children: [
        Expanded(
          child: _buildToggleTabButton('📊 Stats & Commentary', _activeView == 'INFO', partyColor, () {
            setState(() {
              _activeView = 'INFO';
            });
          }),
        ),
        const SizedBox(width: 10),
        Expanded(
          child: _buildToggleTabButton('🃏 Actions & Cards', _activeView == 'ACTION', partyColor, () {
            setState(() {
              _activeView = 'ACTION';
            });
          }),
        ),
      ],
    );
  }

  Widget _buildToggleTabButton(String label, bool isSelected, Color partyColor, VoidCallback onTap) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(8),
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 16),
        decoration: BoxDecoration(
          color: isSelected ? const Color(0xFF213C51) : Colors.white,
          border: Border.all(
            color: isSelected ? const Color(0xFF213C51) : const Color(0xFFB0CBE0),
            width: 1.5,
          ),
          borderRadius: BorderRadius.circular(8),
        ),
        child: Center(
          child: Text(
            label,
            style: TextStyle(
              fontSize: 13,
              fontWeight: FontWeight.bold,
              color: isSelected ? Colors.white : const Color(0xFF213C51),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildActiveViewContent(GameProvider provider, TurnView turnData, Party activeParty) {
    if (_activeView == 'INFO') {
      return StatsView(turnData: turnData, activeParty: activeParty);
    }
    return ActionsView(turnData: turnData, activeParty: activeParty);
  }

  Widget _buildEndGameScreen(TurnView turnData, Party activeParty) {
    final isVictory = turnData.status == 'VICTORY';
    final resultMsg = turnData.lastResults.isNotEmpty ? turnData.lastResults[0] : 'The campaign has concluded.';

    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: isVictory
                ? [const Color(0xFF15803D), const Color(0xFF166534)]
                : [const Color(0xFF991B1B), const Color(0xFF7F1D1D)],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
        ),
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(24.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  isVictory ? '🏆' : '💀',
                  style: const TextStyle(fontSize: 96),
                ),
                const SizedBox(height: 16),
                Text(
                  isVictory ? 'CAMPAIGN VICTORY!' : 'CAMPAIGN FAILED',
                  style: const TextStyle(
                    fontSize: 36,
                    fontWeight: FontWeight.w900,
                    color: Colors.white,
                    letterSpacing: 1.5,
                  ),
                ),
                const SizedBox(height: 20),
                Container(
                  constraints: const BoxConstraints(maxWidth: 600),
                  child: Text(
                    resultMsg,
                    textAlign: TextAlign.center,
                    style: const TextStyle(
                      fontSize: 16,
                      color: Colors.whitee4,
                      height: 1.5,
                    ),
                  ),
                ),
                const SizedBox(height: 30),

                // Election Results Board
                Container(
                  constraints: const BoxConstraints(maxWidth: 500),
                  padding: const EdgeInsets.all(24),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(16),
                    boxShadow: const [
                      BoxShadow(
                        color: Color(0x33000000),
                        blurRadius: 30,
                        offset: Offset(0, 10),
                      ),
                    ],
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      const Text(
                        '🗳️ Final Election Results',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 15,
                          fontWeight: FontWeight.bold,
                          color: Color(0xFF213C51),
                          letterSpacing: 0.5,
                        ),
                      ),
                      const SizedBox(height: 8),
                      const Divider(),
                      const SizedBox(height: 12),
                      ...turnData.parties.map((party) {
                        final support = party.stats.publicSupport;
                        final pColor = parseHexColor(party.color);
                        return Padding(
                          padding: const EdgeInsets.only(bottom: 15),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.stretch,
                            children: [
                              Row(
                                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                children: [
                                  Row(
                                    children: [
                                      Container(
                                        width: 10,
                                        height: 10,
                                        decoration: BoxDecoration(
                                          shape: BoxShape.circle,
                                          color: pColor,
                                        ),
                                      ),
                                      const SizedBox(width: 8),
                                      Text(
                                        '${party.name} ${party.playerControlled ? "(You)" : ""}',
                                        style: const TextStyle(
                                          fontSize: 13,
                                          fontWeight: FontWeight.bold,
                                          color: Color(0xFF213C51),
                                        ),
                                      ),
                                    ],
                                  ),
                                  Text(
                                    '$support%',
                                    style: const TextStyle(
                                      fontSize: 13,
                                      fontWeight: FontWeight.bold,
                                      color: Color(0xFF213C51),
                                    ),
                                  ),
                                ],
                              ),
                              const SizedBox(height: 6),
                              Container(
                                height: 12,
                                decoration: BoxDecoration(
                                  color: const Color(0x1F213C51),
                                  borderRadius: BorderRadius.circular(6),
                                ),
                                child: FractionallySizedBox(
                                  alignment: Alignment.centerLeft,
                                  widthFactor: support / 100.0,
                                  child: Container(
                                    decoration: BoxDecoration(
                                      color: pColor,
                                      borderRadius: BorderRadius.circular(6),
                                    ),
                                  ),
                                ),
                              ),
                            ],
                          ),
                        );
                      }).toList(),
                      if (turnData.publicState.undecidedSupport > 0) ...[
                        const SizedBox(height: 8),
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.stretch,
                          children: [
                            Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                const Text(
                                  'Undecided Voters',
                                  style: TextStyle(
                                    fontSize: 13,
                                    fontWeight: FontWeight.bold,
                                    color: Color(0xFF475569),
                                  ),
                                ),
                                Text(
                                  '${turnData.publicState.undecidedSupport}%',
                                  style: const TextStyle(
                                    fontSize: 13,
                                    fontWeight: FontWeight.bold,
                                    color: Color(0xFF475569),
                                  ),
                                ),
                              ],
                            ),
                            const SizedBox(height: 6),
                            Container(
                              height: 12,
                              decoration: BoxDecoration(
                                color: const Color(0x1F213C51),
                                borderRadius: BorderRadius.circular(6),
                              ),
                              child: FractionallySizedBox(
                                alignment: Alignment.centerLeft,
                                widthFactor: turnData.publicState.undecidedSupport / 100.0,
                                child: Container(
                                  decoration: BoxDecoration(
                                    color: const Color(0xFF94A3B8),
                                    borderRadius: BorderRadius.circular(6),
                                  ),
                                ),
                               ),
                            ),
                          ],
                        ),
                      ],
                    ],
                  ),
                ),
                const SizedBox(height: 36),

                ElevatedButton(
                  onPressed: () {
                    context.read<GameProvider>().exitGame();
                  },
                  style: ElevatedButton.styleFrom(
                    primary: Colors.white,
                    onPrimary: isVictory ? const Color(0xFF166534) : const Color(0xFF7F1D1D),
                    padding: const EdgeInsets.symmetric(horizontal: 40, vertical: 16),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    elevation: 5,
                  ),
                  child: const Text(
                    '➔ Return to Dashboard',
                    style: TextStyle(fontSize: 15, fontWeight: FontWeight.w900),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
