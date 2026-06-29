import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../models/models.dart';
import '../../providers/game_provider.dart';

class Action5PlayReward extends StatelessWidget {
  final TurnView turnData;

  const Action5PlayReward({Key? key, required this.turnData}) : super(key: key);

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
    final rewards = turnData.activePlayerHeldRewards;

    final activeParty = turnData.parties.firstWhere(
      (p) => p.id == turnData.activeHumanPartyId,
      orElse: () => turnData.parties.firstWhere((p) => p.playerControlled),
    );
    final partyColor = parseHexColor(activeParty.color);

    if (rewards.isEmpty) {
      return const Padding(
        padding: EdgeInsets.symmetric(vertical: 12),
        child: Center(
          child: Text(
            'No inventory rewards held. Win bidding rounds to earn rewards!',
            textAlign: TextAlign.center,
            style: TextStyle(color: Color(0xFF64748B), fontStyle: FontStyle.italic, fontSize: 13),
          ),
        ),
      );
    }

    final selectedReward = rewards.firstWhere(
      (r) => r.rewardKey == provider.selectedRewardKey,
      orElse: () => HeldReward(rewardKey: '', name: '', description: '', turnsLeft: 0, requiresTarget: false),
    );

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        const Text(
          '🎁 Select a Reward to Play:',
          style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
        ),
        const SizedBox(height: 6),
        DropdownButtonFormField<String>(
          value: provider.selectedRewardKey != null && provider.selectedRewardKey!.isNotEmpty ? provider.selectedRewardKey : null,
          dropdownColor: Colors.white,
          style: const TextStyle(fontSize: 13, color: Color(0xFF213C51)),
          decoration: const InputDecoration(
            isDense: true,
            contentPadding: EdgeInsets.all(10),
          ),
          hint: const Text('-- Do Not Play Any Reward --'),
          onChanged: provider.rewardConfirmed
              ? null
              : (val) {
                  provider.selectReward(val);
                },
          items: [
            const DropdownMenuItem<String>(
              value: null,
              child: Text('-- Do Not Play Any Reward --'),
            ),
            ...rewards.map((r) => DropdownMenuItem(
                  value: r.rewardKey,
                  child: Text('🎁 ${r.name} (Turns left: ${r.turnsLeft})'),
                )),
          ],
        ),

        // Reward descriptions & targeting
        if (selectedReward.rewardKey.isNotEmpty) ...[
          const SizedBox(height: 16),
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Colors.black.withOpacity(0.02),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Effect: ${selectedReward.description}',
                  style: const TextStyle(fontSize: 12, color: Color(0xFF213C51), fontWeight: FontWeight.bold),
                ),
                if (selectedReward.requiresTarget) ...[
                  const SizedBox(height: 12),
                  const Text(
                    '🎯 Select Target Party:',
                    style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                  ),
                  const SizedBox(height: 6),
                  DropdownButtonFormField<String>(
                    value: provider.rewardTargetPartyId,
                    dropdownColor: Colors.white,
                    style: const TextStyle(fontSize: 13, color: Color(0xFF213C51)),
                    decoration: const InputDecoration(
                      isDense: true,
                      contentPadding: EdgeInsets.all(10),
                    ),
                    hint: const Text('-- Choose Target Party --'),
                    onChanged: provider.rewardConfirmed
                        ? null
                        : (val) {
                            provider.setRewardTarget(val);
                          },
                    items: turnData.parties.map((p) {
                      final isMe = p.id == turnData.activeHumanPartyId;
                      // Filter by target allowances
                      if (selectedReward.allowedTargets == 'opponent' && isMe) return null;
                      if (selectedReward.allowedTargets == 'self' && !isMe) return null;

                      return DropdownMenuItem(
                        value: p.id,
                        child: Text('${p.name} ${isMe ? "(Self)" : "(${p.role})"}'),
                      );
                    }).whereType<DropdownMenuItem<String>>().toList(),
                  ),
                ],
              ],
            ),
          ),
        ],

        // Locked Confirmation button
        const SizedBox(height: 16),
        Center(
          child: ElevatedButton(
            onPressed: provider.selectedRewardKey == null || provider.selectedRewardKey!.isEmpty
                ? null
                : () {
                    provider.setRewardConfirmed(!provider.rewardConfirmed);
                  },
            style: ElevatedButton.styleFrom(
              primary: provider.rewardConfirmed ? const Color(0xFF22C55E) : partyColor,
              onPrimary: provider.rewardConfirmed ? const Color(0xFF213C51) : Colors.white,
              padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
            ),
            child: Text(
              provider.rewardConfirmed ? '✅ Reward Locked' : '🔒 Confirm Reward Selection',
              style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
            ),
          ),
        ),
      ],
    );
  }
}
