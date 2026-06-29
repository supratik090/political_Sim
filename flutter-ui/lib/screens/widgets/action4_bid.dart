import 'dart:math';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../models/models.dart';
import '../../providers/game_provider.dart';

class Action4Bid extends StatelessWidget {
  final TurnView turnData;
  final Party activeParty;

  const Action4Bid({
    Key? key,
    required this.turnData,
    required this.activeParty,
  }) : super(key: key);

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

    final bidMetric = turnData.biddingMetric;
    final stats = activeParty.stats;

    // Map metric keys to reserves limit
    int maxBid = stats.coins;
    if (bidMetric.toUpperCase() == 'MORALE') {
      maxBid = stats.partyMorale;
    } else if (bidMetric.toUpperCase() == 'CORRUPTION') {
      maxBid = max(0, 95 - stats.corruptionScore);
    } else if (bidMetric.toUpperCase() == 'MEDIA') {
      maxBid = stats.mediaImage;
    } else if (bidMetric.toUpperCase() == 'PUBLIC_SUPPORT') {
      maxBid = stats.publicSupport;
    }

    final partyColor = parseHexColor(activeParty.color);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        if (turnData.turnNumber <= 2)
          const Padding(
            padding: EdgeInsets.only(bottom: 12),
            child: Text(
              'Lock in your bid value to compete with AI controllers for this cycle\'s reward.',
              style: TextStyle(fontSize: 11.5, color: Color(0xFF475569), fontStyle: FontStyle.italic),
            ),
          ),

        // A. Past Round Bids
        if (turnData.lastRoundBids.isNotEmpty) ...[
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: const Color(0x03213C51),
              border: Border.all(color: const Color(0xFFB0CBE0), width: 1.5),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  '📊 Present Bidding Scenario (Last Round Bids)',
                  style: TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold, color: Color(0xFF213C51), letterSpacing: 0.5),
                ),
                const SizedBox(height: 8),
                Column(
                  children: turnData.parties.map((p) {
                    final bidVal = turnData.lastRoundBids[p.id] ?? 0;
                    final isWinner = turnData.lastRoundWinnerPartyId == p.id;
                    final isMe = p.id == turnData.activeHumanPartyId;
                    final color = parseHexColor(p.color);

                    return Padding(
                      padding: const EdgeInsets.symmetric(vertical: 2.0),
                      child: Row(
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
                                '${p.name} ${isMe ? "(You)" : ""}',
                                style: TextStyle(
                                  fontSize: 12,
                                  fontWeight: isMe ? FontWeight.bold : FontWeight.normal,
                                  color: const Color(0xFF213C51),
                                ),
                              ),
                            ],
                          ),
                          Row(
                            children: [
                              Text(
                                '$bidVal ${turnData.lastRoundBiddingMetric ?? ""}',
                                style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                              ),
                              if (isWinner)
                                const Padding(
                                  padding: EdgeInsets.only(left: 6.0),
                                  child: Text(
                                    '🏆 WINNER',
                                    style: TextStyle(fontSize: 9, fontWeight: FontWeight.bold, color: Color(0xFF22C55E)),
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
          ),
          const SizedBox(height: 12),
        ],

        // B. Current Cycle Standings
        Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: const Color(0x05213C51),
            border: Border.all(color: const Color(0xFFB0CBE0), style: BorderStyle.dashed),
            borderRadius: BorderRadius.circular(8),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                '🏆 Current 5-Turn Cycle Standings',
                style: TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold, color: Color(0xFF1E3A8A), letterSpacing: 0.5),
              ),
              const SizedBox(height: 8),
              Column(
                children: turnData.parties.map((p) {
                  final wins = turnData.partyRoundWins[p.id] ?? 0;
                  final isMe = p.id == turnData.activeHumanPartyId;
                  final color = parseHexColor(p.color);

                  return Padding(
                    padding: const EdgeInsets.symmetric(vertical: 2.0),
                    child: Row(
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
                              '${p.name} ${isMe ? "(You)" : ""}',
                              style: TextStyle(
                                fontSize: 12,
                                fontWeight: isMe ? FontWeight.bold : FontWeight.normal,
                                color: const Color(0xFF1E3A8A),
                              ),
                            ),
                          ],
                        ),
                        Text(
                          wins > 0 ? '⭐' * wins : '0 wins',
                          style: const TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold, color: Color(0xFF1E3A8A)),
                        ),
                      ],
                    ),
                  );
                }).toList(),
              ),
            ],
          ),
        ),
        const SizedBox(height: 12),

        // C. Reward details
        if (turnData.currentRewardName != null) ...[
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            decoration: const BoxDecoration(
              color: Color(0x0F6366F1),
              border: Border(left: BorderSide(color: Color(0xFF22C55E), width: 4)),
              borderRadius: BorderRadius.only(
                topRight: Radius.circular(8),
                bottomRight: Radius.circular(8),
              ),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  'BIDDING FOR:',
                  style: TextStyle(fontSize: 8.5, fontWeight: FontWeight.bold, color: Color(0xFF213C51), letterSpacing: 0.5),
                ),
                const SizedBox(height: 2),
                Text(
                  '🎯 ${turnData.currentRewardName}',
                  style: const TextStyle(fontSize: 13.5, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                ),
                const SizedBox(height: 2),
                Text(
                  turnData.currentRewardDescription ?? '',
                  style: const TextStyle(fontSize: 10.5, color: Color(0xFF475569), fontStyle: FontStyle.italic),
                ),
              ],
            ),
          ),
          const SizedBox(height: 12),
        ],

        // Metric info details
        Row(
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('Bidding Metric', style: TextStyle(fontSize: 10, color: Color(0xFF64748B))),
                Text(
                  '⚡ ${bidMetric.toUpperCase()}',
                  style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                ),
              ],
            ),
            const SizedBox(width: 32),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('Your Reserves', style: TextStyle(fontSize: 10, color: Color(0xFF64748B))),
                Text(
                  '💎 $maxBid',
                  style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                ),
              ],
            ),
          ],
        ),
        const SizedBox(height: 16),

        // Bid Stake readout
        Text(
          '🗳️ Stake: ${provider.bidAmount} / $maxBid ($bidMetric)   (Remaining: ${maxBid - provider.bidAmount})',
          style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
        ),
        const SizedBox(height: 12),

        // Stepper Selector input
        Row(
          children: [
            const Text(
              'Bid Amount: ',
              style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
            ),
            const SizedBox(width: 8),
            IconButton(
              onPressed: provider.bidConfirmed || provider.bidAmount <= 0
                  ? null
                  : () => provider.setBidAmount(provider.bidAmount - 1),
              icon: const Icon(Icons.remove_circle_outline),
              color: partyColor,
            ),
            Expanded(
              child: TextFormField(
                initialValue: provider.bidAmount.toString(),
                keyboardType: TextInputType.number,
                style: const TextStyle(color: Color(0xFF213C51), fontWeight: FontWeight.bold),
                enabled: !provider.bidConfirmed,
                textAlign: TextAlign.center,
                decoration: const InputDecoration(
                  filled: true,
                  fillColor: Colors.white,
                  contentPadding: EdgeInsets.zero,
                  isDense: true,
                ),
                key: ValueKey(provider.bidAmount),
                onChanged: (val) {
                  int v = int.tryParse(val) ?? 0;
                  if (v < 0) v = 0;
                  if (v > maxBid) v = maxBid;
                  provider.setBidAmount(v);
                },
              ),
            ),
            IconButton(
              onPressed: provider.bidConfirmed || provider.bidAmount >= maxBid
                  ? null
                  : () => provider.setBidAmount(provider.bidAmount + 1),
              icon: const Icon(Icons.add_circle_outline),
              color: partyColor,
            ),
          ],
        ),
        const SizedBox(height: 16),

        // Bidding buttons trigger
        Row(
          children: [
            Expanded(
              child: ElevatedButton(
                onPressed: provider.bidConfirmed
                    ? null
                    : () {
                        provider.setBidAmount(0);
                      },
                style: ElevatedButton.styleFrom(
                  primary: provider.bidAmount == 0 ? partyColor : Colors.white,
                  onPrimary: provider.bidAmount == 0 ? Colors.white : partyColor,
                  side: BorderSide(color: partyColor),
                  padding: const EdgeInsets.symmetric(vertical: 12),
                ),
                child: const Text('💤 Pass (Bid 0)', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
              ),
            ),
            const SizedBox(width: 10),
            Expanded(
              child: ElevatedButton(
                onPressed: () {
                  provider.setBidConfirmed(!provider.bidConfirmed);
                },
                style: ElevatedButton.styleFrom(
                  primary: provider.bidConfirmed ? const Color(0xFF22C55E) : partyColor,
                  onPrimary: provider.bidConfirmed ? const Color(0xFF213C51) : Colors.white,
                  padding: const EdgeInsets.symmetric(vertical: 12),
                ),
                child: Text(
                  provider.bidConfirmed ? '✅ Bid Locked' : '🔒 Confirm Bid',
                  style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
                ),
              ),
            ),
          ],
        ),
      ],
    );
  }
}
