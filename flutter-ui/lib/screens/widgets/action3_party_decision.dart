import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../models/models.dart';
import '../../providers/game_provider.dart';

class Action3PartyDecision extends StatelessWidget {
  final TurnView turnData;

  const Action3PartyDecision({Key? key, required this.turnData}) : super(key: key);

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
    final issue = turnData.currentIssue;

    final activeParty = turnData.parties.firstWhere(
      (p) => p.id == turnData.activeHumanPartyId,
      orElse: () => turnData.parties.firstWhere((p) => p.playerControlled),
    );
    final partyColor = parseHexColor(activeParty.color);

    if (turnData.turnNumber <= 2) ...[
      const Padding(
        padding: EdgeInsets.only(bottom: 12),
        child: Text(
          'Directive: Review internal party developments and issue executive policy responses.',
          style: TextStyle(fontSize: 11, color: Color(0xFF64748B), fontStyle: FontStyle.italic),
        ),
      ),
    ];

    if (issue == null) {
      // Retro Standby TV Screen
      return Container(
        decoration: BoxDecoration(
          color: const Color(0xFF0F172A),
          border: Border.all(color: const Color(0xFF475569), width: 3),
          borderRadius: BorderRadius.circular(12),
        ),
        clipBehavior: Clip.antiAlias,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Color Bars Strip
            Row(
              children: [
                Expanded(child: Container(height: 120, color: const Color(0xFFE2E8F0))),
                Expanded(child: Container(height: 120, color: const Color(0xFFEAB308))),
                Expanded(child: Container(height: 120, color: const Color(0xFF06B6D4))),
                Expanded(child: Container(height: 120, color: const Color(0xFF10B981))),
                Expanded(child: Container(height: 120, color: const Color(0xFFEC4899))),
                Expanded(child: Container(height: 120, color: const Color(0xFFEF4444))),
                Expanded(child: Container(height: 120, color: const Color(0xFF3B82F6))),
              ],
            ),
            Container(
              color: const Color(0xFF0F172A),
              padding: const EdgeInsets.symmetric(vertical: 24, horizontal: 16),
              child: Column(
                children: [
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                    decoration: BoxDecoration(
                      color: const Color(0xFF1E293B),
                      border: Border.all(color: Colors.white12),
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: const Text(
                      '📡 STANDBY',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w900,
                        color: Color(0xFF94A3B8),
                        letterSpacing: 2.0,
                      ),
                    ),
                  ),
                  const SizedBox(height: 10),
                  const Text(
                    'No Active Broadcasting Needed',
                    style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: Color(0xFFF1F5F9)),
                  ),
                  const SizedBox(height: 2),
                  const Text(
                    'Routine communications operating on nominal channels.',
                    style: TextStyle(fontSize: 11, color: Color(0xFF94A3B8)),
                  ),
                ],
              ),
            ),
          ],
        ),
      );
    }

    // High-tech TV News Broadcast Style
    return Container(
      decoration: BoxDecoration(
        gradient: const RadialGradient(
          colors: [Color(0xFF1E1B4B), Color(0xFF09090B)],
        ),
        border: Border.all(color: partyColor, width: 3),
        borderRadius: BorderRadius.circular(12),
      ),
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Broadcast Header Bar
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
            decoration: BoxDecoration(
              color: partyColor,
              borderRadius: BorderRadius.circular(6),
            ),
            child: const Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  children: [
                    Text('📺', style: TextStyle(fontSize: 10)),
                    SizedBox(width: 6),
                    Text(
                      'INTERNAL REPORT',
                      style: TextStyle(fontWeight: FontWeight.w900, color: Colors.white, fontSize: 10, letterSpacing: 0.5),
                    ),
                  ],
                ),
                Text(
                  'LIVE FEED',
                  style: TextStyle(fontWeight: FontWeight.w900, color: Colors.white, fontSize: 8),
                ),
              ],
            ),
          ),
          const SizedBox(height: 16),

          // Headline
          Text(
            '🚨 URGENT: ${issue.title.toUpperCase()}',
            style: const TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.w900,
              color: Color(0xFFFEF08A), // bright yellow
              letterSpacing: 0.5,
            ),
          ),
          const SizedBox(height: 12),

          // Briefing Desk Box
          Container(
            padding: const EdgeInsets.all(12),
            decoration: const BoxDecoration(
              color: Color(0x9909090B),
              border: Border(left: BorderSide(color: Color(0xFF3B82F6), width: 4)),
              borderRadius: BorderRadius.only(
                topRight: Radius.circular(6),
                bottomRight: Radius.circular(6),
              ),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  '🎙️ BRIEFING DESK:',
                  style: TextStyle(fontSize: 9.5, fontWeight: FontWeight.bold, color: Color(0xFF60A5FA), letterSpacing: 0.5),
                ),
                const SizedBox(height: 4),
                Text(
                  issue.description,
                  style: const TextStyle(fontSize: 12.5, color: Color(0xFFE4E4E7), height: 1.5),
                ),
              ],
            ),
          ),
          const SizedBox(height: 20),

          // Action Options Selector List
          const Text(
            '📡 SELECT EXECUTIVE ACTION:',
            style: TextStyle(fontSize: 9.5, fontWeight: FontWeight.bold, color: Color(0xFFA1A1AA), letterSpacing: 0.5),
          ),
          const SizedBox(height: 8),
          Column(
            children: List.generate(issue.options.length, (i) {
              final opt = issue.options[i];
              final isSelected = provider.selectedIssueOptionKey == opt.optionKey;

              return Padding(
                padding: const EdgeInsets.only(bottom: 8.0),
                child: InkWell(
                  onTap: () {
                    provider.setIssueOption(opt.optionKey);
                  },
                  borderRadius: BorderRadius.circular(8),
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                    decoration: BoxDecoration(
                      color: isSelected ? partyColor : const Color(0xFF1F2937),
                      border: Border.all(
                        color: isSelected ? partyColor : const Color(0x1F293780),
                      ),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Row(
                      children: [
                        // Circular Choice index bubble
                        Container(
                          width: 20,
                          height: 20,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: isSelected ? Colors.white : Colors.white10,
                          ),
                          child: Center(
                            child: Text(
                              isSelected ? '✓' : '${i + 1}',
                              style: TextStyle(
                                fontSize: 9.5,
                                fontWeight: FontWeight.bold,
                                color: isSelected ? partyColor : Colors.white,
                              ),
                            ),
                          ),
                        ),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Text(
                            opt.text,
                            style: const TextStyle(
                              fontSize: 12.5,
                              color: Colors.white,
                              height: 1.3,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              );
            }),
          ),
        ],
      ),
    );
  }
}
