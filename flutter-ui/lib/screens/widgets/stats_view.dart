import 'dart:async';
import 'package:flutter/material.dart';
import '../../models/models.dart';

class StatsView extends StatefulWidget {
  final TurnView turnData;
  final Party activeParty;

  const StatsView({
    Key? key,
    required this.turnData,
    required this.activeParty,
  }) : super(key: key);

  @override
  State<StatsView> createState() => _StatsViewState();
}

class _StatsViewState extends State<StatsView> {
  bool _commentaryExpanded = false;
  String _commentaryFilter = 'ALL';

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

  // Helper to render metric changes (+/-)
  Widget _buildMetricDelta(dynamic delta, {bool isCorruption = false, bool isSupport = false}) {
    if (delta == null) return const SizedBox();
    final d = int.tryParse(delta.toString()) ?? 0;
    if (d == 0) return const SizedBox();

    final isPositive = d > 0;
    // For corruption, negative change is good (green), positive is bad (red)
    final isGood = isCorruption ? !isPositive : isPositive;

    final color = isGood ? const Color(0xFF22C55E) : const Color(0xFFD23F31);
    final text = '${isPositive ? "+" : ""}$d${isSupport ? "%" : ""}';

    return Text(
      text,
      style: TextStyle(
        fontSize: 10,
        fontWeight: FontWeight.bold,
        color: color,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final turnData = widget.turnData;
    final isMobile = MediaQuery.of(context).size.width < 768;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        // Standings Title Header
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Expanded(
              child: Text(
                '📊 Standing (Turn ${turnData.turnNumber} - ${turnData.stateName})',
                style: const TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: Color(0xFF213C51),
                ),
              ),
            ),
            const SizedBox(width: 8),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
              decoration: BoxDecoration(
                color: const Color(0xFF213C51),
                borderRadius: BorderRadius.circular(20),
              ),
              child: Text(
                turnData.currentDate,
                style: const TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Colors.white),
              ),
            ),
          ],
        ),
        const SizedBox(height: 16),

        // 1. Election Results Banner (If early election resolved)
        if (turnData.lastElectionHeld && turnData.lastElectionWinner != null)
          _buildElectionBanner(turnData),

        // 2. Early Election constitutional warning
        if (!turnData.lastElectionHeld && _hasNoConfidenceWarning(turnData))
          _buildNoConfidenceWarning(),

        // 3. Defeat hazard notifications
        _buildDefeatWarnings(turnData),

        // 4. 3 Party statistics grid cards
        GridView.builder(
          shrinkWrap: true,
          physics: const NeverScrollableScrollPhysics(),
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: isMobile ? 1 : 3,
            crossAxisSpacing: 16,
            mainAxisSpacing: 16,
            childAspectRatio: isMobile ? 1.6 : 1.05,
          ),
          itemCount: turnData.parties.length,
          itemBuilder: (context, idx) {
            final party = turnData.parties[idx];
            final stats = party.stats;
            final isPlayer = party.id == turnData.activeHumanPartyId;
            final pColor = parseHexColor(party.color);
            final pIcon = getSymbolIcon(party.symbol);

            final delta = turnData.lastMetricDeltas[party.id] ?? {};
            final lastBid = turnData.lastRoundBids[party.id];
            final isBidWinner = turnData.lastRoundWinnerPartyId == party.id;

            final lastSub = turnData.lastRoundSubmissions.firstWhere(
              (sub) => sub['partyId'] == party.id,
              orElse: () => null,
            );
            final lastPlayedCardName = lastSub != null ? lastSub['cardName'] ?? 'Pass' : 'Pass';

            final isDefeated = party.role == 'DEFEATED';

            return Container(
              decoration: BoxDecoration(
                color: isDefeated ? const Color(0xFFF1F5F9) : Colors.white,
                border: Border.all(
                  color: isDefeated
                      ? const Color(0xFFEF4444)
                      : (isPlayer ? pColor : const Color(0xFFB0CBE0)),
                  width: isPlayer ? 2.5 : 1.5,
                ),
                borderRadius: BorderRadius.circular(12),
                boxShadow: [
                  if (isPlayer)
                    BoxShadow(
                      color: pColor.withOpacity(0.12),
                      blurRadius: 10,
                      offset: const Offset(0, 4),
                    ),
                ],
              ),
              clipBehavior: Clip.antiAlias,
              child: Stack(
                children: [
                  // Faint Watermark emblem
                  Positioned(
                    top: 10,
                    right: 10,
                    child: Opacity(
                      opacity: 0.04,
                      child: Icon(pIcon, size: 64, color: pColor),
                    ),
                  ),
                  // Diagonal color ribbon corner
                  Positioned(
                    bottom: 0,
                    right: 0,
                    child: CustomPaint(
                      size: const Size(25, 25),
                      painter: StatsCornerRibbonPainter(color: pColor),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(12.0),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                if (isPlayer)
                                  Container(
                                    padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                                    decoration: BoxDecoration(
                                      color: const Color(0xFF22C55E),
                                      borderRadius: BorderRadius.circular(8),
                                    ),
                                    child: const Text(
                                      'YOU',
                                      style: TextStyle(fontSize: 8, fontWeight: FontWeight.bold, color: Colors.white),
                                    ),
                                  )
                                else
                                  const SizedBox(),
                                if (isDefeated)
                                  Container(
                                    padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                                    decoration: BoxDecoration(
                                      color: const Color(0xFFEF4444),
                                      borderRadius: BorderRadius.circular(8),
                                    ),
                                    child: const Text(
                                      'DEFEATED',
                                      style: TextStyle(fontSize: 8, fontWeight: FontWeight.bold, color: Colors.white),
                                    ),
                                  ),
                              ],
                            ),
                            const SizedBox(height: 4),
                            Row(
                              children: [
                                Container(
                                  width: 8,
                                  height: 8,
                                  decoration: BoxDecoration(shape: BoxShape.circle, color: pColor),
                                ),
                                const SizedBox(width: 6),
                                Expanded(
                                  child: Text(
                                    party.name,
                                    overflow: TextOverflow.ellipsis,
                                    style: const TextStyle(
                                      fontSize: 14,
                                      fontWeight: FontWeight.w900,
                                      color: Color(0xFF213C51),
                                    ),
                                  ),
                                ),
                              ],
                            ),
                            const SizedBox(height: 2),
                            Text(
                              '${party.role} | ${party.controllerType}',
                              style: const TextStyle(fontSize: 9, color: Color(0xFF64748B), fontWeight: FontWeight.bold),
                            ),
                            const SizedBox(height: 8),

                            // Metric rows
                            _buildStatRow('💰 Coins', stats.coins.toString(), _buildMetricDelta(delta['coins'])),
                            _buildStatRow('✊ Morale', stats.partyMorale.toString(), _buildMetricDelta(delta['partyMorale'])),
                            _buildStatRow('⚖️ Corruption', '${stats.corruptionScore}%', _buildMetricDelta(delta['corruptionScore'], isCorruption: true)),
                            _buildStatRow('📢 Media Image', stats.mediaImage.toString(), _buildMetricDelta(delta['mediaImage'])),
                            _buildStatRow('📈 Support', '${stats.publicSupport}%', _buildMetricDelta(delta['publicSupport'], isSupport: true)),
                          ],
                        ),
                        // Last Round Actions
                        Container(
                          padding: const EdgeInsets.only(top: 8),
                          decoration: const BoxDecoration(
                            border: Border(top: BorderSide(color: Color(0x0D213C51))),
                          ),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                'Last Card: $lastPlayedCardName',
                                maxLines: 1,
                                overflow: TextOverflow.ellipsis,
                                style: const TextStyle(fontSize: 10, color: Color(0xFF475569)),
                              ),
                              Row(
                                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                children: [
                                  Text(
                                    'Last Bid: ${lastBid ?? 0} ${turnData.lastRoundBiddingMetric ?? ""}',
                                    style: const TextStyle(fontSize: 10, color: Color(0xFF475569)),
                                  ),
                                  if (isBidWinner)
                                    const Text(
                                      '🏆 WON',
                                      style: TextStyle(fontSize: 9, fontWeight: FontWeight.bold, color: Color(0xFF22C55E)),
                                    ),
                                ],
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            );
          },
        ),
        const SizedBox(height: 20),

        // 5. Active Cycle Bidding details bar
        Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: Colors.white,
            border: Border.all(color: const Color(0xFFB0CBE0), width: 1.5),
            borderRadius: BorderRadius.circular(12),
          ),
          child: isMobile
              ? Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    _buildBiddingMetricLabel(turnData.biddingMetric),
                    const SizedBox(height: 12),
                    const Divider(),
                    const SizedBox(height: 12),
                    _buildRewardDetailsLabel(turnData.currentRewardName, turnData.currentRewardDescription),
                  ],
                )
              : Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Expanded(
                      flex: 4,
                      child: _buildBiddingMetricLabel(turnData.biddingMetric),
                    ),
                    Container(
                      width: 1.5,
                      height: 80,
                      color: const Color(0x1F6594B1),
                      margin: const EdgeInsets.symmetric(horizontal: 20),
                    ),
                    Expanded(
                      flex: 6,
                      child: _buildRewardDetailsLabel(turnData.currentRewardName, turnData.currentRewardDescription),
                    ),
                  ],
                ),
        ),
        const SizedBox(height: 20),

        // 6. TV Breaking News (If turn advance results are logged)
        if (turnData.lastResults.isNotEmpty)
          _buildTvBreakingNews(turnData.lastResults),

        const SizedBox(height: 20),

        // 7. Collapsible Commentary Feed
        _buildCommentaryFeed(turnData),
      ],
    );
  }

  Widget _buildStatRow(String label, String value, Widget deltaWidget) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 2.5),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(label, style: const TextStyle(fontSize: 11, color: Color(0xFF475569))),
          Row(
            children: [
              Text(
                value,
                style: const TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
              ),
              const SizedBox(width: 4),
              deltaWidget,
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildBiddingMetricLabel(String metric) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text(
          'ACTIVE CYCLE BIDDING METRIC',
          style: TextStyle(fontSize: 9, fontWeight: FontWeight.bold, color: Color(0xFF64748B), letterSpacing: 0.5),
        ),
        const SizedBox(height: 4),
        Text(
          '🎯 $metric',
          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF22C55E)),
        ),
        const SizedBox(height: 2),
        const Text(
          'Submit bids using this metric to win five-turn cycle rewards.',
          style: TextStyle(fontSize: 10, color: Color(0xFF64748B)),
        ),
      ],
    );
  }

  Widget _buildRewardDetailsLabel(String? name, String? description) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text(
          'CURRENT CYCLE REWARD',
          style: TextStyle(fontSize: 9, fontWeight: FontWeight.bold, color: Color(0xFF64748B), letterSpacing: 0.5),
        ),
        const SizedBox(height: 4),
        Text(
          '🏆 ${name ?? "None"}',
          style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
        ),
        const SizedBox(height: 4),
        Text(
          description ?? 'No reward description',
          style: const TextStyle(fontSize: 11, color: Color(0xFF475569), height: 1.3),
        ),
      ],
    );
  }

  Widget _buildElectionBanner(TurnView turnData) {
    final votesShares = turnData.lastElectionVoteShares ?? {};

    return Container(
      margin: const EdgeInsets.only(bottom: 20),
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          colors: [Color(0xFF1E3A8A), Color(0xFF0F172A)],
        ),
        border: Border.all(color: const Color(0xFF3B82F6), width: 2),
        borderRadius: BorderRadius.circular(16),
      ),
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          const Row(
            children: [
              Text('🗳️', style: TextStyle(fontSize: 24)),
              SizedBox(width: 10),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'STATE ELECTION RESULTS',
                    style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15, color: Color(0xFF60A5FA), letterSpacing: 0.5),
                  ),
                  Text(
                    'The voters have spoken. A new government has been formed.',
                    style: TextStyle(fontSize: 11, color: Colors.white70),
                  ),
                ],
              ),
            ],
          ),
          const SizedBox(height: 15),
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.05),
              border: Border.all(color: Colors.white.withOpacity(0.1)),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  '👑 Winner: ${turnData.lastElectionWinner}',
                  style: const TextStyle(fontWeight: FontWeight.bold, color: Color(0xFFFBBF24), fontSize: 14),
                ),
                if (turnData.lastResults.isNotEmpty) ...[
                  const SizedBox(height: 4),
                  Text(
                    turnData.lastResults[0],
                    style: const TextStyle(color: Colors.whitee4, fontSize: 11),
                  ),
                ],
              ],
            ),
          ),
          const SizedBox(height: 15),
          const Text(
            'FINAL VOTE SHARE',
            style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF94A3B8), letterSpacing: 0.5),
          ),
          const SizedBox(height: 8),
          ...votesShares.entries.map((e) {
            final partyName = e.key;
            final share = e.value;
            final partyObj = turnData.parties.firstWhere((p) => p.name == partyName, orElse: () => turnData.parties[0]);
            final color = parseHexColor(partyObj.color);

            return Padding(
              padding: const EdgeInsets.only(bottom: 8.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Row(
                        children: [
                          Container(
                            width: 8,
                            height: 8,
                            decoration: BoxDecoration(shape: BoxShape.circle, color: color),
                          ),
                          const SizedBox(width: 6),
                          Text(
                            partyName,
                            style: const TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold),
                          ),
                        ],
                      ),
                      Text('$share%', style: const TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold)),
                    ],
                  ),
                  const SizedBox(height: 4),
                  Container(
                    height: 8,
                    decoration: BoxDecoration(
                      color: Colors.white10,
                      borderRadius: BorderRadius.circular(4),
                    ),
                    child: FractionallySizedBox(
                      alignment: Alignment.centerLeft,
                      widthFactor: share / 100.0,
                      child: Container(
                        decoration: BoxDecoration(color: color, borderRadius: BorderRadius.circular(4)),
                      ),
                    ),
                  ),
                ],
              ),
            );
          }).toList(),
        ],
      ),
    );
  }

  bool _hasNoConfidenceWarning(TurnView turnData) {
    final hasNCCommentary = turnData.lastRoundCommentary.any((c) => c.toLowerCase().contains('no-confidence'));
    final hasNCResult = turnData.lastResults.any((r) => r.toLowerCase().contains('no-confidence'));
    return hasNCCommentary || hasNCResult;
  }

  Widget _buildNoConfidenceWarning() {
    return Container(
      margin: const EdgeInsets.only(bottom: 20),
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          colors: [Color(0xFF1E3A8A), Color(0xFF3B82F6)],
        ),
        border: Border.all(color: const Color(0xFF2563EB), width: 2),
        borderRadius: BorderRadius.circular(12),
      ),
      padding: const EdgeInsets.all(15),
      child: const Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            '⚡ SPECIAL CONSTITUTIONAL EVENT: No-Confidence Vote',
            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14, color: Colors.white),
          ),
          SizedBox(height: 4),
          Text(
            'The Opposition successfully triggered a No-Confidence Motion, leading to early state elections. Voting results determined the new Government!',
            style: TextStyle(color: Colors.whitef2, fontSize: 12, height: 1.4),
          ),
        ],
      ),
    );
  }

  Widget _buildDefeatWarnings(TurnView turnData) {
    final List<String> playerWarnings = [];
    for (var party in turnData.parties) {
      if (party.playerControlled) {
        if (party.stats.coins <= 15) {
          playerWarnings.add('Coins reserve is critically low (${party.stats.coins}). Reaching 0 triggers immediate defeat (Bankruptcy).');
        }
        if (party.stats.partyMorale <= 15) {
          playerWarnings.add('Party morale is dangerously low (${party.stats.partyMorale}). Reaching less than 10 triggers cadre collapse.');
        }
        if (party.stats.publicSupport <= 12) {
          playerWarnings.add('Voter support is dangerously low (${party.stats.publicSupport}%). Reaching less than 10% triggers party elimination.');
        }
      }
    }

    if (playerWarnings.isEmpty) return const SizedBox();

    return Container(
      margin: const EdgeInsets.only(bottom: 20),
      decoration: BoxDecoration(
        color: const Color(0x1AD23F31),
        border: Border.all(color: const Color(0xFFD23F31), width: 2),
        borderRadius: BorderRadius.circular(12),
      ),
      padding: const EdgeInsets.all(15),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Row(
            children: [
              Text('⚠️', style: TextStyle(fontSize: 16)),
              SizedBox(width: 8),
              Text(
                'Defeat Hazard Warnings',
                style: TextStyle(fontWeight: FontWeight.bold, color: Color(0xFFD23F31), fontSize: 14),
              ),
            ],
          ),
          const SizedBox(height: 8),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: playerWarnings.map((warn) {
              return Padding(
                padding: const EdgeInsets.only(bottom: 4.0),
                child: Text(
                  '• $warn',
                  style: const TextStyle(fontSize: 12, color: Color(0xFF213C51), fontWeight: FontWeight.bold),
                ),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }

  Widget _buildTvBreakingNews(List<String> lastResults) {
    return Container(
      decoration: BoxDecoration(
        color: const Color(0xFF090D16),
        border: Border.all(color: const Color(0xFFEF4444), width: 3),
        borderRadius: BorderRadius.circular(12),
        boxShadow: const [
          BoxShadow(
            color: Color(0x26EF4444),
            blurRadius: 20,
            offset: Offset(0, 8),
          ),
        ],
      ),
      clipBehavior: Clip.antiAlias,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Header Bar
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                colors: [Color(0xFFEF4444), Color(0xFFB91C1C), Color(0xFF7F1D1D)],
              ),
            ),
            child: const Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  children: [
                    FlashingDot(),
                    SizedBox(width: 8),
                    Text(
                      '📺 BREAKING NEWS',
                      style: TextStyle(fontWeight: FontWeight.w900, color: Colors.white, fontSize: 12, letterSpacing: 1.0),
                    ),
                  ],
                ),
                Container(
                  padding: EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.all(Radius.circular(3)),
                  ),
                  child: Text(
                    'LIVE',
                    style: TextStyle(fontWeight: FontWeight.w900, color: Color(0xFFEF4444), fontSize: 9),
                  ),
                ),
              ],
            ),
          ),

          // Content body
          Container(
            padding: const EdgeInsets.all(16),
            decoration: const BoxDecoration(
              gradient: RadialGradient(
                colors: [Color(0xFF1E293B), Color(0xFF0F172A)],
              ),
            ),
            child: Column(
              children: lastResults.map((res) {
                return Container(
                  margin: const EdgeInsets.only(bottom: 10),
                  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                  decoration: BoxDecoration(
                    color: const Color(0x990F172A),
                    border: Border(left: BorderSide(color: const Color(0xFFEF4444), width: 4)),
                  ),
                  child: Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 2),
                        decoration: BoxDecoration(
                          color: const Color(0xFFEF4444),
                          borderRadius: BorderRadius.circular(2),
                        ),
                        child: const Text(
                          'FLASH',
                          style: TextStyle(fontSize: 8, color: Colors.white, fontWeight: FontWeight.bold),
                        ),
                      ),
                      const SizedBox(width: 10),
                      Expanded(
                        child: Text(
                          res,
                          style: const TextStyle(
                            color: Color(0xFFF1F5F9),
                            fontSize: 13,
                            fontWeight: FontWeight.bold,
                            height: 1.4,
                          ),
                        ),
                      ),
                    ],
                  ),
                );
              }).toList(),
            ),
          ),

          // Scrolling news ticker footer
          Container(
            height: 32,
            color: const Color(0xFFB91C1C),
            child: Row(
              children: [
                Container(
                  height: 32,
                  padding: const EdgeInsets.symmetric(horizontal: 12),
                  color: const Color(0xFF0F172A),
                  alignment: Alignment.center,
                  child: const Text(
                    'TV FEED',
                    style: TextStyle(fontSize: 10, fontWeight: FontWeight.w900, color: Colors.white, letterSpacing: 0.5),
                  ),
                ),
                Expanded(
                  child: TickerMarquee(
                    text: '✦ CAMPAIGN BULLETIN: ${lastResults.join("   ✦   ")}',
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildCommentaryFeed(TurnView turnData) {
    final activeParties = turnData.parties;
    final filteredLines = (turnData.lastRoundCommentary).where((line) {
      if (_commentaryFilter == 'ALL') return true;
      return line.toLowerCase().contains(_commentaryFilter.toLowerCase());
    }).toList();

    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        border: Border.all(color: const Color(0xFFB0CBE0)),
        borderRadius: BorderRadius.circular(12),
      ),
      clipBehavior: Clip.antiAlias,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Expandable Header trigger
          InkWell(
            onTap: () => setState(() => _commentaryExpanded = !_commentaryExpanded),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 15),
              color: const Color(0x0D6594B1),
              child: Row(
                children: [
                  Icon(
                    _commentaryExpanded ? Icons.keyboard_arrow_down : Icons.keyboard_arrow_right,
                    color: const Color(0xFF213C51),
                    size: 18,
                  ),
                  const SizedBox(width: 8),
                  const Expanded(
                    child: Text(
                      '📢 Political Commentary Feed',
                      style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF213C51), letterSpacing: 0.5),
                    ),
                  ),
                  // Dropdown filters
                  GestureDetector(
                    onTap: () {}, // Stop tap propagation
                    child: DropdownButton<String>(
                      value: _commentaryFilter,
                      underline: const SizedBox(),
                      dropdownColor: Colors.white,
                      style: const TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                      onChanged: (val) {
                        if (val != null) {
                          setState(() {
                            _commentaryFilter = val;
                            _commentaryExpanded = true;
                          });
                        }
                      },
                      items: [
                        const DropdownMenuItem(value: 'ALL', child: Text('All Parties')),
                        ...activeParties.map(
                          (p) => DropdownMenuItem(value: p.name, child: Text(p.name)),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),

          // Lines list
          if (_commentaryExpanded)
            Container(
              maxHeight: 280,
              padding: const EdgeInsets.all(16),
              child: filteredLines.isEmpty
                  ? const Text(
                      'No commentary matching this filter available.',
                      style: TextStyle(color: Colors.red, fontStyle: FontStyle.italic, fontSize: 12),
                    )
                  : ListView.builder(
                      shrinkWrap: true,
                      itemCount: filteredLines.length,
                      itemBuilder: (ctx, idx) {
                        return Container(
                          padding: const EdgeInsets.symmetric(vertical: 8),
                          decoration: const BoxDecoration(
                            border: Border(bottom: BorderSide(color: Color(0x1F6594B1))),
                          ),
                          child: Text(
                            '💬 ${filteredLines[idx]}',
                            style: const TextStyle(fontSize: 12.5, color: Colors.black87, height: 1.4),
                          ),
                        );
                      },
                    ),
            ),
        ],
      ),
    );
  }
}

// Painter to draw corner ribbon triangles on cards
class StatsCornerRibbonPainter extends CustomPainter {
  final Color color;

  StatsCornerRibbonPainter({required this.color});

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = color.withOpacity(0.85)
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

// Widget to draw a flashing live dot animation on Breaking News
class FlashingDot extends StatefulWidget {
  const FlashingDot({Key? key}) : super(key: key);

  @override
  State<FlashingDot> createState() => _FlashingDotState();
}

class _FlashingDotState extends State<FlashingDot> with SingleTickerProviderStateMixin {
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 800),
    )..repeat(reverse: true);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (ctx, child) {
        return Opacity(
          opacity: _controller.value,
          child: Container(
            width: 8,
            height: 8,
            decoration: const BoxDecoration(
              shape: BoxShape.circle,
              color: Colors.white,
            ),
          ),
        );
      },
    );
  }
}

// Animated marquee scrolling ticker widget
class TickerMarquee extends StatefulWidget {
  final String text;

  const TickerMarquee({Key? key, required this.text}) : super(key: key);

  @override
  State<TickerMarquee> createState() => _TickerMarqueeState();
}

class _TickerMarqueeState extends State<TickerMarquee> {
  late ScrollController _scrollController;
  Timer? _timer;

  @override
  void initState() {
    super.initState();
    _scrollController = ScrollController();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _startScrolling();
    });
  }

  void _startScrolling() {
    _timer = Timer.periodic(const Duration(milliseconds: 40), (timer) {
      if (!_scrollController.hasClients) return;
      double maxScroll = _scrollController.position.maxScrollExtent;
      double currentScroll = _scrollController.offset;

      if (currentScroll >= maxScroll) {
        _scrollController.jumpTo(0.0);
      } else {
        _scrollController.jumpTo(currentScroll + 1.0);
      }
    });
  }

  @override
  void dispose() {
    _timer?.cancel();
    _scrollController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Generate text buffer sequence to allow wrap around scrolling feel
    final bufferText = '${widget.text}      ' * 4;
    return ListView(
      controller: _scrollController,
      scrollDirection: Axis.horizontal,
      physics: const NeverScrollableScrollPhysics(),
      children: [
        Center(
          child: Padding(
            padding: const EdgeInsets.only(left: 10),
            child: Text(
              bufferText,
              style: const TextStyle(
                fontSize: 10.5,
                color: Colors.white,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ),
      ],
    );
  }
}
