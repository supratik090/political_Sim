import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../models/models.dart';
import '../../providers/game_provider.dart';
import '../../api/api_service.dart';
import 'action_accordion.dart';
import 'action1_card_selection.dart';
import 'action2_news_reaction.dart';
import 'action3_party_decision.dart';
import 'action4_bid.dart';
import 'action5_play_reward.dart';
import 'action6_party_building.dart';
import 'action7_cooperation.dart';

class ActionsView extends StatefulWidget {
  final TurnView turnData;
  final Party activeParty;

  const ActionsView({
    Key? key,
    required this.turnData,
    required this.activeParty,
  }) : super(key: key);

  @override
  State<ActionsView> createState() => _ActionsViewState();
}

class _ActionsViewState extends State<ActionsView> {
  int _expandedIndex = 1; // Accordion step expanded (1 to 7)

  Map<String, dynamic> _projectDefs = {};
  bool _projectsLoading = true;
  String? _projectsError;

  @override
  void initState() {
    super.initState();
    _loadProjectDefinitions();
  }

  Future<void> _loadProjectDefinitions() async {
    try {
      final defs = await ApiService.instance.fetchBuildingProjects();
      if (mounted) {
        setState(() {
          _projectDefs = defs;
          _projectsLoading = false;
        });
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _projectsError = e.toString();
          _projectsLoading = false;
        });
      }
    }
  }

  static Color parseHexColor(String hex) {
    try {
      return Color(int.parse(hex.replaceFirst('#', '0xFF')));
    } catch (_) {
      return const Color(0xFF213C51);
    }
  }

  List<String> _getMissingRequirements(GameProvider provider) {
    final List<String> list = [];
    final turn = widget.turnData;

    // 1. Card selection
    if (provider.selectedCard == null) {
      list.add('Step 1: Choose a strategy card to deploy.');
    } else if (provider.selectedCard!.requiresTarget && (provider.targetPartyId == null || provider.targetPartyId!.isEmpty)) {
      list.add('Step 1: Strategy card requires selecting an opponent target.');
    }

    // 2. News reaction
    for (var news in turn.currentNews) {
      if (!provider.selectedNewsReactions.containsKey(news.newsKey)) {
        list.add('Step 2: Press reaction missing for Headline "${news.title}".');
      }
    }

    // 3. Issue option
    if (turn.currentIssue != null && provider.selectedIssueOptionKey == null) {
      list.add('Step 3: Directive choice missing for Report "${turn.currentIssue!.title}".');
    }

    // 4. Bid confirmation
    if (!provider.bidConfirmed) {
      list.add('Step 4: Lock in your blind bidding amount.');
    }

    // 5. Reward confirmation
    if (provider.selectedRewardKey != null && provider.selectedRewardKey!.isNotEmpty) {
      final reward = turn.activePlayerHeldRewards.firstWhere((r) => r.rewardKey == provider.selectedRewardKey);
      if (reward.requiresTarget && (provider.rewardTargetPartyId == null || provider.rewardTargetPartyId!.isEmpty)) {
        list.add('Step 5: Active reward requires selecting a target.');
      }
      if (!provider.rewardConfirmed) {
        list.add('Step 5: Lock in your active reward play choice.');
      }
    }

    // 6. Party building confirmation
    final hasDraft = provider.draftProjectKeys.isNotEmpty || provider.fundingContributions.values.any((v) => v > 0);
    if (hasDraft && !provider.partyBuildingConfirmed) {
      list.add('Step 6: Lock in your infrastructure building selections.');
    }

    return list;
  }

  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<GameProvider>(context);
    final turn = widget.turnData;
    final activeParty = widget.activeParty;

    final partyColor = parseHexColor(activeParty.color);

    if (_projectsLoading) {
      return const Center(
        child: Padding(
          padding: EdgeInsets.symmetric(vertical: 40),
          child: Column(
            children: [
              CircularProgressIndicator(),
              SizedBox(height: 12),
              Text('Fetching Project Infrastructure definitions...', style: TextStyle(color: Colors.grey, fontSize: 13)),
            ],
          ),
        ),
      );
    }

    // A. Verify step completions
    final step1Done = provider.selectedCard != null && (!provider.selectedCard!.requiresTarget || provider.targetPartyId != null);
    final step2Done = turn.currentNews.every((news) => provider.selectedNewsReactions.containsKey(news.newsKey));
    final step3Done = turn.currentIssue == null || provider.selectedIssueOptionKey != null;
    final step4Done = provider.bidConfirmed;
    final step5Done = provider.selectedRewardKey == null || provider.selectedRewardKey!.isEmpty || provider.rewardConfirmed;
    final step6Done = (provider.draftProjectKeys.isEmpty && provider.fundingContributions.values.every((v) => v == 0)) || provider.partyBuildingConfirmed;
    const step7Done = true; // Optional

    final missingReqs = _getMissingRequirements(provider);
    final readyToAdvance = provider.isReadyToSubmit;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        // 1. Play Strategic Card
        ActionAccordion(
          num: 1,
          title: 'Play Strategic Card',
          isCompleted: step1Done,
          isExpanded: _expandedIndex == 1,
          onToggle: (val) => setState(() => _expandedIndex = val ? 1 : 0),
          child: Action1CardSelection(turnData: turn),
        ),

        // 2. Respond to Newspaper
        ActionAccordion(
          num: 2,
          title: 'Respond to State Chronicle',
          isCompleted: step2Done,
          isExpanded: _expandedIndex == 2,
          onToggle: (val) => setState(() => _expandedIndex = val ? 2 : 0),
          child: Action2NewsReaction(turnData: turn),
        ),

        // 3. Urgencies & Directives
        ActionAccordion(
          num: 3,
          title: 'Urgencies & Directives',
          isCompleted: step3Done,
          isExpanded: _expandedIndex == 3,
          onToggle: (val) => setState(() => _expandedIndex = val ? 3 : 0),
          child: Action3PartyDecision(turnData: turn),
        ),

        // 4. Cycle Blind Bidding
        ActionAccordion(
          num: 4,
          title: 'Cycle Blind Bidding',
          isCompleted: step4Done,
          isExpanded: _expandedIndex == 4,
          onToggle: (val) => setState(() => _expandedIndex = val ? 4 : 0),
          child: Action4Bid(turnData: turn, activeParty: activeParty),
        ),

        // 5. Inventory Cycle Rewards
        ActionAccordion(
          num: 5,
          title: 'Inventory Cycle Rewards',
          isOptional: true,
          isCompleted: step5Done,
          isExpanded: _expandedIndex == 5,
          onToggle: (val) => setState(() => _expandedIndex = val ? 5 : 0),
          child: Action5PlayReward(turnData: turn),
        ),

        // 6. Public Infrastructure
        ActionAccordion(
          num: 6,
          title: 'Public Infrastructure',
          isOptional: true,
          isCompleted: step6Done,
          isExpanded: _expandedIndex == 6,
          onToggle: (val) => setState(() => _expandedIndex = val ? 6 : 0),
          child: Action6PartyBuilding(turnData: turn, activeParty: activeParty, projectDefs: _projectDefs),
        ),

        // 7. Cooperation Hub
        ActionAccordion(
          num: 7,
          title: 'Diplomatic Cooperation',
          isOptional: true,
          isCompleted: step7Done,
          isExpanded: _expandedIndex == 7,
          onToggle: (val) => setState(() => _expandedIndex = val ? 7 : 0),
          child: Action7Cooperation(turnData: turn, projectDefs: _projectDefs),
        ),

        const SizedBox(height: 24),

        // Error message readout if API throws error
        if (provider.errorMessage != null) ...[
          Container(
            padding: const EdgeInsets.all(12),
            margin: const EdgeInsets.only(bottom: 16),
            decoration: BoxDecoration(
              color: const Color(0x1AD23F31),
              border: Border.all(color: const Color(0xFFD23F31)),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Text(
              '⚠️ Error: ${provider.errorMessage}',
              style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFFD23F31)),
            ),
          ),
        ],

        // Validation Bullet Box
        if (missingReqs.isNotEmpty) ...[
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: const Color(0x0A213C51),
              border: Border.all(color: const Color(0xFFB0CBE0)),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                const Text(
                  '📋 Pending Choices Required to Finish Turn:',
                  style: TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                ),
                const SizedBox(height: 8),
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: missingReqs.map((req) {
                    return Padding(
                      padding: const EdgeInsets.only(bottom: 4.0),
                      child: Text(
                        '• $req',
                        style: const TextStyle(fontSize: 11, color: Color(0xFF475569)),
                      ),
                    );
                  }).toList(),
                ),
              ],
            ),
          ),
          const SizedBox(height: 16),
        ],

        // Advance submit actions row
        Row(
          children: [
            Expanded(
              child: ElevatedButton(
                onPressed: provider.isLoading ? null : () async {
                  // Skip turn: assemble default reactions
                  final defaultReactions = <String, String>{};
                  for (var news in turn.currentNews) {
                    defaultReactions[news.newsKey] = news.options[0].optionKey;
                  }
                  final defaultIssue = turn.currentIssue != null ? turn.currentIssue!.options[0].optionKey : 'routine_maintenance';

                  final confirmed = await showDialog<bool>(
                    context: context,
                    builder: (ctx) => AlertDialog(
                      title: const Text('Skip Turn / Autoplay?'),
                      content: const Text('This will pass on playing cards, set bid to 0, and select the default neutral stance on news events. Do you wish to continue?'),
                      actions: [
                        TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('Cancel')),
                        TextButton(onPressed: () => Navigator.pop(ctx, true), child: const Text('Skip Turn')),
                      ],
                    ),
                  );

                  if (confirmed == true) {
                    await provider.skipTurn(defaultReactions, defaultIssue);
                  }
                },
                style: ElevatedButton.styleFrom(
                  primary: Colors.white,
                  onPrimary: const Color(0xFF213C51),
                  side: const BorderSide(color: Color(0xFF213C51)),
                  padding: const EdgeInsets.symmetric(vertical: 16),
                ),
                child: const Text('💤 Autoplay / Pass Turn', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: ElevatedButton(
                onPressed: (!readyToAdvance || provider.isLoading)
                    ? null
                    : () async {
                        final success = await provider.submitTurn();
                        if (success) {
                          setState(() {
                            _expandedIndex = 1; // reset step accordion view
                          });
                        }
                      },
                style: ElevatedButton.styleFrom(
                  primary: const Color(0xFF22C55E),
                  padding: const EdgeInsets.symmetric(vertical: 16),
                ),
                child: provider.isLoading
                    ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 2, valueColor: AlwaysStoppedAnimation<Color>(Colors.white)))
                    : const Text('➔ SUBMIT ALL DECISIONS', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
              ),
            ),
          ],
        ),

        // C. Forfeit game button
        const SizedBox(height: 24),
        Center(
          child: TextButton.icon(
            onPressed: provider.isLoading
                ? null
                : () async {
                    final confirmed = await showDialog<bool>(
                      context: context,
                      builder: (ctx) => AlertDialog(
                        title: const Text('Forfeit Campaign?'),
                        content: const Text('Are you sure you want to forfeit this campaign? You will immediately lose the campaign and return to the dashboard.'),
                        actions: [
                          TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('Cancel')),
                          TextButton(
                            onPressed: () => Navigator.pop(ctx, true),
                            style: TextButton.styleFrom(primary: Colors.red),
                            child: const Text('Forfeit'),
                          ),
                        ],
                      ),
                    );
                    if (confirmed == true) {
                      await provider.forfeitActiveGame();
                    }
                  },
            icon: const Icon(Icons.flag_outlined, color: Color(0xFFD23F31), size: 14),
            label: const Text(
              'Forfeit Campaign & Resign',
              style: TextStyle(color: Color(0xFFD23F31), fontWeight: FontWeight.bold, fontSize: 11.5),
            ),
          ),
        ),
      ],
    );
  }
}
