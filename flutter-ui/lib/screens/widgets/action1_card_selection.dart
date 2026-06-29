import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../models/models.dart';
import '../../providers/game_provider.dart';

class Action1CardSelection extends StatelessWidget {
  final TurnView turnData;

  const Action1CardSelection({Key? key, required this.turnData}) : super(key: key);

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

  // Mappings of category keys to labels
  static final List<Map<String, String>> _categories = [
    {'key': 'agitation_movement', 'label': 'Agitation ✊'},
    {'key': 'governance', 'label': 'Governance 🏛️'},
    {'key': 'positive_service', 'label': 'Welfare 🤝'},
    {'key': 'media_narrative', 'label': 'Media 📢'},
    {'key': 'organization_resource', 'label': 'Organization 🏢'},
    {'key': 'ideology_identity', 'label': 'Ideology ⚡'},
    {'key': 'scandal_accusation', 'label': 'Scandal 🔍'},
    {'key': 'defensive_counter', 'label': 'Defense 🛡️'},
    {'key': 'ALL', 'label': 'All 🃏'},
  ];

  String _formatEffects(Map<String, dynamic>? effects) {
    if (effects == null || effects.isEmpty) return 'None';
    final List<String> list = [];
    effects.forEach((key, value) {
      final val = int.tryParse(value.toString()) ?? 0;
      if (val == 0) return;
      final labelMap = {
        'coins': 'Coins',
        'partyMorale': 'Morale',
        'corruptionScore': 'Corr.',
        'mediaImage': 'Media',
        'publicSupport': 'Support'
      };
      final displayLabel = labelMap[key] ?? key;
      list.add('$displayLabel: ${val > 0 ? "+" : ""}$val');
    });
    return list.join('  ');
  }

  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<GameProvider>(context);
    final activeParty = turnData.parties.firstWhere(
      (p) => p.id == turnData.activeHumanPartyId,
      orElse: () => turnData.parties.firstWhere((p) => p.playerControlled),
    );

    final partyColor = parseHexColor(activeParty.color);
    final isMobile = MediaQuery.of(context).size.width < 768;

    // Filter available cards based on provider category filter
    final activeFilter = provider.selectedRewardKey ?? 'ALL'; // Reuse filter fields dynamically
    final cardFilter = provider.selectedRewardKey != null && provider.selectedRewardKey!.isNotEmpty
        ? provider.selectedRewardKey!
        : 'agitation_movement'; // Default start filter matches React

    final List<StrategicCard> filteredCards = (turnData.availableCards).where((card) {
      if (cardFilter == 'ALL') return true;
      return card.category.toLowerCase() == cardFilter.toLowerCase();
    }).toList();

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        if (turnData.turnNumber <= 2)
          const Padding(
            padding: EdgeInsets.only(bottom: 12),
            child: Text(
              'Draft and execute a political action card. Offensive cards require targeting an opponent.',
              style: TextStyle(fontSize: 11.5, color: Color(0xFF475569), fontStyle: FontStyle.italic),
            ),
          ),

        // Category scroll bar
        Container(
          height: 38,
          margin: const EdgeInsets.only(bottom: 16),
          child: ListView.builder(
            scrollDirection: Axis.horizontal,
            itemCount: _categories.length,
            itemBuilder: (context, idx) {
              final cat = _categories[idx];
              final isCatActive = cardFilter == cat['key'];
              return Padding(
                padding: const EdgeInsets.only(right: 8.0),
                child: ChoiceChip(
                  label: Text(
                    cat['label']!,
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.bold,
                      color: isCatActive ? Colors.white : partyColor,
                    ),
                  ),
                  selected: isCatActive,
                  selectedColor: partyColor,
                  backgroundColor: Colors.white,
                  pressElevation: 1,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(20),
                    side: BorderSide(color: partyColor.withOpacity(0.4)),
                  ),
                  onSelected: (_) {
                    // Temporarily store category filter in selectedRewardKey (to avoid creating extra properties)
                    provider.selectReward(cat['key']);
                  },
                ),
              );
            },
          ),
        ),

        // Cards grid
        filteredCards.isEmpty
            ? const Padding(
                padding: EdgeInsets.symmetric(vertical: 40),
                child: Center(
                  child: Text(
                    'No cards available in this category.',
                    style: TextStyle(color: Color(0xFF64748B), fontStyle: FontStyle.italic, fontSize: 13),
                  ),
                ),
              )
            : GridView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: isMobile ? 1 : 3,
                  crossAxisSpacing: 12,
                  mainAxisSpacing: 12,
                  childAspectRatio: isMobile ? 2.5 : 1.35,
                ),
                itemCount: filteredCards.length,
                itemBuilder: (context, idx) {
                  final card = filteredCards[idx];
                  final isCardSelected = provider.selectedCard?.cardKey == card.cardKey;

                  return InkWell(
                    onTap: () {
                      provider.selectCard(card);
                    },
                    borderRadius: BorderRadius.circular(10),
                    child: Container(
                      decoration: BoxDecoration(
                        color: isCardSelected ? partyColor.withOpacity(0.08) : Colors.white,
                        border: Border.all(
                          color: isCardSelected ? partyColor : partyColor.withOpacity(0.15),
                          width: isCardSelected ? 2.5 : 1.0,
                        ),
                        borderRadius: BorderRadius.circular(10),
                        boxShadow: isCardSelected
                            ? [
                                BoxShadow(
                                  color: partyColor.withOpacity(0.12),
                                  blurRadius: 10,
                                  offset: const Offset(0, 4),
                                ),
                              ]
                            : null,
                      ),
                      clipBehavior: Clip.antiAlias,
                      child: Stack(
                        children: [
                          // Faint watermark
                          Positioned(
                            bottom: 8,
                            right: 8,
                            child: Opacity(
                              opacity: 0.04,
                              child: Icon(getSymbolIcon(activeParty.symbol), size: 64, color: partyColor),
                            ),
                          ),
                          // Corner Ribbon
                          Positioned(
                            bottom: 0,
                            right: 0,
                            child: CustomPaint(
                              size: const Size(18, 18),
                              painter: CardCornerRibbonPainter(color: partyColor),
                            ),
                          ),

                          Padding(
                            padding: const EdgeInsets.all(10.0),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Column(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(
                                      card.category.toUpperCase().replaceAll('_', ' '),
                                      style: TextStyle(fontSize: 8, fontWeight: FontWeight.bold, color: partyColor, letterSpacing: 0.5),
                                    ),
                                    const SizedBox(height: 2),
                                    Text(
                                      card.name,
                                      maxLines: 1,
                                      overflow: TextOverflow.ellipsis,
                                      style: const TextStyle(
                                        fontSize: 12.5,
                                        fontWeight: FontWeight.bold,
                                        color: Color(0xFF213C51),
                                      ),
                                    ),
                                    const SizedBox(height: 2),
                                    Text(
                                      'Cost: ${card.cost} Coins',
                                      style: const TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Color(0xFF475569)),
                                    ),
                                  ],
                                ),
                                Container(
                                  padding: const EdgeInsets.all(6),
                                  decoration: BoxDecoration(
                                    color: Colors.black.withOpacity(0.03),
                                    borderRadius: BorderRadius.circular(6),
                                  ),
                                  child: Column(
                                    crossAxisAlignment: CrossAxisAlignment.stretch,
                                    children: [
                                      Text(
                                        'Self: ${_formatEffects(card.selfEffects)}',
                                        style: const TextStyle(fontSize: 9.5, color: Color(0xFF0D9488), fontWeight: FontWeight.bold),
                                      ),
                                      const SizedBox(height: 2),
                                      Text(
                                        'Opposition: ${_formatEffects(card.opponentEffects)}',
                                        style: const TextStyle(fontSize: 9.5, color: Color(0xFFBE123C), fontWeight: FontWeight.bold),
                                      ),
                                    ],
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),

        // Target Party select box
        if (provider.selectedCard != null && provider.selectedCard!.requiresTarget) ...[
          const SizedBox(height: 16),
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: const Color(0x056594B1),
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: const Color(0xFFB0CBE0), style: BorderStyle.dashed),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  '🎯 Select Opponent Target:',
                  style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                ),
                const SizedBox(height: 6),
                DropdownButtonFormField<String>(
                  value: provider.targetPartyId,
                  dropdownColor: Colors.white,
                  style: const TextStyle(fontSize: 13, color: Color(0xFF213C51)),
                  decoration: const InputDecoration(
                    isDense: true,
                    contentPadding: EdgeInsets.all(10),
                  ),
                  hint: const Text('-- Choose Opponent Party --'),
                  onChanged: (val) {
                    provider.selectCardTarget(val);
                  },
                  items: turnData.parties
                      .where((p) => p.id != turnData.activeHumanPartyId && p.role != 'DEFEATED')
                      .map((opp) => DropdownMenuItem(
                            value: opp.id,
                            child: Text('${opp.name} (${opp.role})'),
                          ))
                      .toList(),
                ),
              ],
            ),
          ),
        ],

        // Card Details panel
        if (provider.selectedCard != null) ...[
          const SizedBox(height: 16),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Expanded(
                child: Text(
                  'Selected Move: ${provider.selectedCard!.name}',
                  style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                ),
              ),
              const SizedBox(width: 8),
              ElevatedButton(
                onPressed: () {
                  provider.selectCard(null);
                },
                style: ElevatedButton.styleFrom(
                  primary: Colors.white,
                  onPrimary: const Color(0xFFD23F31),
                  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                  side: const BorderSide(color: Color(0xFFD23F31)),
                ),
                child: const Text('Deselect', style: TextStyle(fontSize: 11)),
              ),
            ],
          ),
        ],
      ],
    );
  }
}

class CardCornerRibbonPainter extends CustomPainter {
  final Color color;

  CardCornerRibbonPainter({required this.color});

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = color
      ..style = PaintingStyle.fill;

    final path = Path()
      ..moveTo(size.width, 0)
      ..lineTo(0, size.height)
      ..lineTo(size.width, size.height)
      ..close();

    canvas.drawPath(path, paint);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
