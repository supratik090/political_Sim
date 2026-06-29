import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../models/models.dart';
import '../../providers/game_provider.dart';

class Action2NewsReaction extends StatelessWidget {
  final TurnView turnData;

  const Action2NewsReaction({Key? key, required this.turnData}) : super(key: key);

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
    final newsItems = turnData.currentNews;

    final activeParty = turnData.parties.firstWhere(
      (p) => p.id == turnData.activeHumanPartyId,
      orElse: () => turnData.parties.firstWhere((p) => p.playerControlled),
    );
    final partyColor = parseHexColor(activeParty.color);

    return Container(
      decoration: BoxDecoration(
        color: const Color(0xFFFDFBF7), // Newspaper sepia
        border: Border.all(color: const Color(0xFFDCD7CA), width: 1.5),
        borderRadius: BorderRadius.circular(12),
        boxShadow: const [
          BoxShadow(
            color: Color(0x0D000000),
            blurRadius: 15,
            offset: Offset(0, 5),
          ),
        ],
      ),
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Newspaper Masthead Header
          const Center(
            child: Text(
              'THE STATE CHRONICLE',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontFamily: 'Playfair Display', // fallback serif representation
                fontSize: 22,
                fontWeight: FontWeight.w900,
                color: Color(0xFF1C1917),
                letterSpacing: 1.0,
              ),
            ),
          ),
          const SizedBox(height: 6),

          // Date Bar
          Container(
            padding: const EdgeInsets.symmetric(vertical: 4),
            decoration: const BoxDecoration(
              border: Border(
                top: BorderSide(color: Color(0xFFD6D3D1)),
                bottom: BorderSide(color: Color(0xFFD6D3D1)),
              ),
            ),
            alignment: Alignment.center,
            child: Text(
              '📅 ${turnData.currentDate}',
              style: const TextStyle(
                fontSize: 9.5,
                fontWeight: FontWeight.bold,
                color: Color(0xFF57534E),
                letterSpacing: 0.5,
              ),
            ),
          ),
          const SizedBox(height: 20),

          // Articles list
          newsItems.isEmpty
              ? const Padding(
                  padding: EdgeInsets.symmetric(vertical: 24),
                  child: Center(
                    child: Text(
                      'No breaking news articles published in this edition.',
                      style: TextStyle(color: Color(0xFF78716C), fontStyle: FontStyle.italic, fontSize: 13),
                    ),
                  ),
                )
              : Column(
                  children: List.generate(newsItems.length, (idx) {
                    final news = newsItems[idx];
                    final currentReaction = provider.selectedNewsReactions[news.newsKey];

                    return Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        if (idx > 0)
                          const Padding(
                            padding: EdgeInsets.symmetric(vertical: 16),
                            child: Center(
                              child: Text(
                                '•••',
                                style: TextStyle(color: Color(0xFFA8A29E), fontSize: 14, letterSpacing: 6),
                              ),
                            ),
                          ),

                        // Headline
                        Text(
                          news.title,
                          textAlign: TextAlign.center,
                          style: const TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                            color: Color(0xFF0C0A09),
                            height: 1.3,
                          ),
                        ),
                        const SizedBox(height: 12),

                        // Body text
                        Text(
                          news.description,
                          textAlign: TextAlign.justify,
                          style: const TextStyle(
                            fontSize: 13.5,
                            color: Color(0xFF292524),
                            height: 1.55,
                          ),
                        ),
                        const SizedBox(height: 20),

                        // Options form box
                        Container(
                          padding: const EdgeInsets.all(15),
                          decoration: BoxDecoration(
                            color: const Color(0xFFF5F5F4),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.stretch,
                            children: [
                              const Text(
                                '📢 OFFICIAL PARTY RESPONSE CHANNELS',
                                textAlign: TextAlign.center,
                                style: TextStyle(
                                  fontSize: 10,
                                  fontWeight: FontWeight.w900,
                                  color: Color(0xFF57534E),
                                  letterSpacing: 0.5,
                                ),
                              ),
                              const SizedBox(height: 12),
                              Column(
                                children: news.options.map((opt) {
                                  final isSelected = currentReaction == opt.optionKey;

                                  return Padding(
                                    padding: const EdgeInsets.only(bottom: 8.0),
                                    child: InkWell(
                                      onTap: () {
                                        provider.selectNewsReaction(news.newsKey, opt.optionKey);
                                      },
                                      borderRadius: BorderRadius.circular(6),
                                      child: Container(
                                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                                        decoration: BoxDecoration(
                                          color: isSelected ? partyColor : Colors.white,
                                          border: Border.all(
                                            color: isSelected ? partyColor : const Color(0xFFD6D3D1),
                                          ),
                                          borderRadius: BorderRadius.circular(6),
                                        ),
                                        alignment: Alignment.centerLeft,
                                        child: Text(
                                          '${isSelected ? "🖋️ [Selected] " : "○ "}${opt.text}',
                                          style: TextStyle(
                                            fontSize: 11.5,
                                            fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                                            color: isSelected ? Colors.white : const Color(0xFF1C1917),
                                          ),
                                        ),
                                      ),
                                    ),
                                  );
                                }).toList(),
                              ),
                            ],
                          ),
                        ),
                      ],
                    );
                  }),
                ),
        ],
      ),
    );
  }
}
