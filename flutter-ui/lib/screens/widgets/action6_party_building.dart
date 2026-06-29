import 'dart:math';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../models/models.dart';
import '../../providers/game_provider.dart';

class Action6PartyBuilding extends StatefulWidget {
  final TurnView turnData;
  final Party activeParty;
  final Map<String, dynamic> projectDefs;

  const Action6PartyBuilding({
    Key? key,
    required this.turnData,
    required this.activeParty,
    required this.projectDefs,
  }) : super(key: key);

  @override
  State<Action6PartyBuilding> createState() => _Action6PartyBuildingState();
}

class _Action6PartyBuildingState extends State<Action6PartyBuilding> {
  String _projectCategoryFilter = 'BUILD'; // BUILD or OFFENSIVE

  static Color parseHexColor(String hex) {
    try {
      return Color(int.parse(hex.replaceFirst('#', '0xFF')));
    } catch (_) {
      return const Color(0xFF213C51);
    }
  }

  // Helper mapping yields
  Map<String, dynamic> _calculateProgressCost(Map<String, dynamic> pDef, int progress) {
    final costCoins = (pDef['costCoins'] ?? 0) as int;
    final costMorale = (pDef['costMorale'] ?? 0) as int;
    final costCorruption = (pDef['costCorruption'] ?? 0) as int;
    final costMedia = (pDef['costMedia'] ?? 0) as int;
    final costSupport = (pDef['costSupport'] ?? 0) as int;

    final factor = progress / 100.0;
    return {
      'coins': (costCoins * factor).ceil(),
      'morale': (costMorale * factor).ceil(),
      'corruption': (costCorruption * factor).ceil(),
      'media': (costMedia * factor).ceil(),
      'support': (costSupport * factor).ceil(),
    };
  }

  bool _canAfford(Map<String, dynamic> cost, PartyStats stats) {
    if (stats.coins < (cost['coins'] ?? 0)) return false;
    if (stats.partyMorale < (cost['morale'] ?? 0)) return false;
    if (stats.mediaImage < (cost['media'] ?? 0)) return false;
    if (stats.publicSupport < (cost['support'] ?? 0)) return false;
    return true;
  }

  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<GameProvider>(context);
    final isMobile = MediaQuery.of(context).size.width < 768;

    final activeParty = widget.activeParty;
    final activeProjects = activeParty.projects;

    final completedProjects = activeProjects.where((p) => p.progressPercent >= 100).toList();
    final selectedProjects = activeProjects.where((p) => p.progressPercent < 100 && (p.progressPercent > 0 || provider.draftProjectKeys.contains(p.id) || provider.draftProjectKeys.contains(p.projectKey))).toList();

    // Map project definitions to available checklist
    final List<Map<String, dynamic>> availableProjects = [];
    widget.projectDefs.forEach((key, def) {
      final existing = activeProjects.firstWhere((p) => p.projectKey == key && p.progressPercent < 100, orElse: () => PartyProject(id: '', projectKey: '', progressPercent: 100));
      final isDraft = provider.draftProjectKeys.contains(key);
      if (existing.id.isEmpty && !isDraft) {
        availableProjects.add({
          'key': key,
          'name': def['name'] ?? key,
          'cost': def['cost'] ?? 'Free',
          'costCoins': def['costCoins'] ?? 0,
          'costMorale': def['costMorale'] ?? 0,
          'costCorruption': def['costCorruption'] ?? 0,
          'costMedia': def['costMedia'] ?? 0,
          'costSupport': def['costSupport'] ?? 0,
          'yield': def['yield'] ?? 'None',
          'offensive': def['offensive'] ?? false,
        });
      }
    });

    final filteredAvail = availableProjects.where((p) {
      if (_projectCategoryFilter == 'BUILD') return !(p['offensive'] as bool);
      return (p['offensive'] as bool);
    }).toList();

    final partyColor = parseHexColor(activeParty.color);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        if (widget.turnData.turnNumber <= 2)
          const Padding(
            padding: EdgeInsets.only(bottom: 12),
            child: Text(
              'Fund long-term construction projects for passive campaign yields or offensive targets.',
              style: TextStyle(fontSize: 11.5, color: Color(0xFF475569), fontStyle: FontStyle.italic),
            ),
          ),

        // A. Completed Projects
        if (completedProjects.isNotEmpty) ...[
          const Text('Completed Infrastructure', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF213C51))),
          const SizedBox(height: 8),
          ...completedProjects.map((proj) {
            final pDef = widget.projectDefs[proj.projectKey] ?? {'name': proj.projectKey, 'yield': 'None', 'costCoins': 0, 'offensive': false};
            final isOffensive = pDef['offensive'] ?? false;

            return Card(
              margin: const EdgeInsets.only(bottom: 10),
              color: const Color(0x0A22C55E),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(8),
                side: const BorderSide(color: Color(0xFF22C55E), width: 1.5),
              ),
              child: Padding(
                padding: const EdgeInsets.all(12),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      pDef['name'],
                      style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13, color: Color(0xFF1B5E20)),
                    ),
                    const SizedBox(height: 4),
                    Text('Yield: ${pDef["yield"]}', style: const TextStyle(fontSize: 11, color: Color(0xFF475569))),
                    const SizedBox(height: 8),
                    if (isOffensive) ...[
                      const Text('🎯 Target:', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Color(0xFF213C51))),
                      const SizedBox(height: 4),
                      DropdownButtonFormField<String>(
                        value: proj.targetPartyId,
                        dropdownColor: Colors.white,
                        style: const TextStyle(fontSize: 12, color: Color(0xFF213C51)),
                        decoration: const InputDecoration(isDense: true, contentPadding: EdgeInsets.all(6)),
                        hint: const Text('-- Select Target Opponent --'),
                        onChanged: provider.partyBuildingConfirmed
                            ? null
                            : (val) {
                                if (val != null) {
                                  provider.setProjectTarget(activeParty.id, proj.id, val);
                                }
                              },
                        items: widget.turnData.parties
                            .where((p) => p.id != widget.turnData.activeHumanPartyId)
                            .map((opp) => DropdownMenuItem(
                                  value: opp.id,
                                  child: Text(opp.name),
                                ))
                            .toList(),
                      ),
                    ] else ...[
                      const Row(
                        children: [
                          Icon(Icons.shield_outlined, size: 12, color: Color(0xFF22C55E)),
                          SizedBox(width: 4),
                          Text('Passive yield active', style: TextStyle(fontSize: 10, color: Color(0xFF22C55E), fontWeight: FontWeight.bold)),
                        ],
                      ),
                    ],
                    const SizedBox(height: 8),
                    ElevatedButton(
                      onPressed: provider.partyBuildingConfirmed
                          ? null
                          : () async {
                              final costCoins = pDef['costCoins'] ?? 0;
                              final confirmed = await showDialog<bool>(
                                context: context,
                                builder: (ctx) => AlertDialog(
                                  title: const Text('Destroy Project?'),
                                  content: Text('Are you sure you want to destroy completed project \'${pDef["name"]}\'? You will receive a refund of $costCoins Coins.'),
                                  actions: [
                                    TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('Cancel')),
                                    TextButton(onPressed: () => Navigator.pop(ctx, true), child: const Text('Destroy')),
                                  ],
                                ),
                              );
                              if (confirmed == true) {
                                provider.destroyProject(activeParty.id, proj.id);
                              }
                            },
                      style: ElevatedButton.styleFrom(
                        primary: const Color(0xFFEF4444),
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                      ),
                      child: Text('Destroy & Refund (${pDef["costCoins"]} 💰)', style: const TextStyle(fontSize: 10)),
                    ),
                  ],
                ),
              ),
            );
          }).toList(),
          const SizedBox(height: 16),
        ],

        // B. Selected / Draft Projects in Progress
        if (selectedProjects.isNotEmpty) ...[
          const Text('Projects in Progress', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF213C51))),
          const SizedBox(height: 8),
          ...selectedProjects.map((proj) {
            final pDef = widget.projectDefs[proj.projectKey] ?? {'name': proj.projectKey, 'yield': 'None', 'costCoins': 0, 'offensive': false};
            final isDraft = provider.draftProjectKeys.contains(proj.projectKey);
            final progress = proj.progressPercent;
            final remaining = 100 - progress;

            final List<int> presets = [0];
            for (final val in [20, 40, 60, 80, 100]) {
              if (val <= remaining) presets.add(val);
            }
            if (remaining > 0 && !presets.contains(remaining)) presets.add(remaining);
            presets.sort();

            final chosenContrib = provider.fundingContributions[proj.id] ?? provider.fundingContributions[proj.projectKey] ?? 0;
            final cost = _calculateProgressCost(pDef, chosenContrib);
            final canAfford = _canAfford(cost, activeParty.stats);

            return Card(
              margin: const EdgeInsets.only(bottom: 10),
              color: partyColor.withOpacity(0.04),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(8),
                side: BorderSide(color: partyColor, width: 1.5),
              ),
              child: Padding(
                padding: const EdgeInsets.all(12),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text(
                          pDef['name'],
                          style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13, color: partyColor),
                        ),
                        if (isDraft)
                          IconButton(
                            onPressed: provider.partyBuildingConfirmed
                                ? null
                                : () => provider.removeDraftProject(proj.projectKey),
                            icon: const Icon(Icons.close, size: 16, color: Color(0xFFD23F31)),
                            padding: EdgeInsets.zero,
                            constraints: const BoxConstraints(),
                          ),
                      ],
                    ),
                    const SizedBox(height: 2),
                    Text('Total Cost: ${pDef["cost"]} | Yield: ${pDef["yield"]}', style: const TextStyle(fontSize: 10.5, color: Color(0xFF475569))),
                    const SizedBox(height: 8),

                    // Progress indicators
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text('Funding: $progress%', style: const TextStyle(fontSize: 10, fontWeight: FontWeight.bold)),
                        if (chosenContrib > 0)
                          Text('+ $chosenContrib%', style: const TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Color(0xFF22C55E))),
                      ],
                    ),
                    const SizedBox(height: 4),
                    Container(
                      height: 8,
                      decoration: BoxDecoration(
                        color: Colors.black.withOpacity(0.1),
                        borderRadius: BorderRadius.circular(4),
                      ),
                      child: Row(
                        children: [
                          Container(
                            width: (MediaQuery.of(context).size.width - 100) * (progress / 100.0) / 2.5, // approximate scale
                            decoration: BoxDecoration(color: partyColor, borderRadius: BorderRadius.circular(4)),
                          ),
                          Container(
                            width: (MediaQuery.of(context).size.width - 100) * (chosenContrib / 100.0) / 2.5,
                            decoration: BoxDecoration(color: const Color(0xFF22C55E), borderRadius: BorderRadius.circular(4)),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 12),

                    // Selector
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Row(
                          children: [
                            const Text('Add Funding %: ', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Color(0xFF213C51))),
                            const SizedBox(width: 4),
                            DropdownButton<int>(
                              value: chosenContrib,
                              dropdownColor: Colors.white,
                              style: const TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                              onChanged: provider.partyBuildingConfirmed
                                  ? null
                                  : (val) {
                                      if (val != null) {
                                        provider.updateFundingContribution(proj.id.isNotEmpty ? proj.id : proj.projectKey, val);
                                      }
                                    },
                              items: presets
                                  .map((v) => DropdownMenuItem(
                                        value: v,
                                        child: Text('+$v%'),
                                      ))
                                  .toList(),
                            ),
                          ],
                        ),
                        Text(
                          'Cost: ${cost["coins"]} Coins',
                          style: TextStyle(
                            fontSize: 10,
                            fontWeight: FontWeight.bold,
                            color: canAfford ? const Color(0xFF213C51) : const Color(0xFFD23F31),
                          ),
                        ),
                      ],
                    ),
                    if (!canAfford && chosenContrib > 0)
                      const Text(
                        '⚠️ INSUFFICIENT RESERVES TO FUND',
                        style: TextStyle(fontSize: 9, fontWeight: FontWeight.bold, color: Color(0xFFD23F31)),
                      ),
                    const SizedBox(height: 8),

                    // Trigger row buttons
                    Row(
                      children: [
                        if (chosenContrib > 0 && canAfford)
                          ElevatedButton(
                            onPressed: () {
                              provider.fundProject(activeParty.id, proj.id.isNotEmpty ? proj.id : proj.projectKey, chosenContrib);
                            },
                            style: ElevatedButton.styleFrom(
                              primary: const Color(0xFF22C55E),
                              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                            ),
                            child: const Text('🏗️ Confirm Funding', style: TextStyle(fontSize: 10)),
                          ),
                        if (progress > 0) ...[
                          const SizedBox(width: 8),
                          ElevatedButton(
                            onPressed: provider.partyBuildingConfirmed
                                ? null
                                : () async {
                                    final refundCoins = ((pDef['costCoins'] ?? 0) * progress / 100.0).ceil();
                                    final confirmed = await showDialog<bool>(
                                      context: context,
                                      builder: (ctx) => AlertDialog(
                                        title: const Text('Scrap Project?'),
                                        content: Text('Are you sure you want to scrap project \'${pDef["name"]}\'? You will receive Z refund of $refundCoins Coins.'),
                                        actions: [
                                          TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('Cancel')),
                                          TextButton(onPressed: () => Navigator.pop(ctx, true), child: const Text('Scrap')),
                                        ],
                                      ),
                                    );
                                    if (confirmed == true) {
                                      provider.destroyProject(activeParty.id, proj.id);
                                    }
                                  },
                            style: ElevatedButton.styleFrom(
                              primary: const Color(0xFFEF4444),
                              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                            ),
                            child: Text('Scrap & Refund (${((pDef["costCoins"] ?? 0) * progress / 100.0).ceil()} 💰)', style: const TextStyle(fontSize: 10)),
                          ),
                        ],
                      ],
                    ),
                  ],
                ),
              ),
            );
          }).toList(),
          const SizedBox(height: 16),
        ],

        // C. Build Available Projects
        Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text('Build Infrastructure', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF213C51))),
                DropdownButton<String>(
                  value: _projectCategoryFilter,
                  dropdownColor: Colors.white,
                  style: const TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
                  onChanged: provider.partyBuildingConfirmed
                      ? null
                      : (val) {
                          if (val != null) {
                            setState(() {
                              _projectCategoryFilter = val;
                            });
                          }
                        },
                  items: const [
                    DropdownMenuItem(value: 'BUILD', child: Text('Build Party')),
                    DropdownMenuItem(value: 'OFFENSIVE', child: Text('Target Opponents')),
                  ],
                ),
              ],
            ),
            const SizedBox(height: 8),

            filteredAvail.isEmpty
                ? const Padding(
                    padding: EdgeInsets.symmetric(vertical: 20),
                    child: Center(
                      child: Text(
                        'No projects available in this category.',
                        style: TextStyle(color: Color(0xFF64748B), fontStyle: FontStyle.italic, fontSize: 11.5),
                      ),
                    ),
                  )
                : GridView.builder(
                    shrinkWrap: true,
                    physics: const NeverScrollableScrollPhysics(),
                    gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                      crossAxisCount: isMobile ? 2 : 4,
                      crossAxisSpacing: 8,
                      mainAxisSpacing: 8,
                      childAspectRatio: isMobile ? 1.0 : 1.1,
                    ),
                    itemCount: filteredAvail.length,
                    itemBuilder: (ctx, sIdx) {
                      final avail = filteredAvail[sIdx];
                      return Container(
                        decoration: BoxDecoration(
                          color: Colors.white,
                          border: Border.all(color: partyColor.withOpacity(0.2)),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        padding: const EdgeInsets.all(8),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.stretch,
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  avail['name'],
                                  maxLines: 2,
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 10.5, color: partyColor),
                                ),
                                const SizedBox(height: 2),
                                Text(
                                  'Cost: ${avail["cost"]}',
                                  maxLines: 1,
                                  overflow: TextOverflow.ellipsis,
                                  style: const TextStyle(fontSize: 8.5, color: Color(0xFF64748B)),
                                ),
                                const SizedBox(height: 2),
                                Text(
                                  'Yield: ${avail["yield"]}',
                                  maxLines: 2,
                                  overflow: TextOverflow.ellipsis,
                                  style: const TextStyle(fontSize: 8.5, color: Color(0xFF475569)),
                                ),
                              ],
                            ),
                            ElevatedButton(
                              onPressed: provider.partyBuildingConfirmed
                                  ? null
                                  : () => provider.addDraftProject(avail['key']),
                              style: ElevatedButton.styleFrom(
                                primary: partyColor,
                                padding: EdgeInsets.zero,
                                isDense: true,
                              ),
                              child: const Text('Select', style: TextStyle(fontSize: 9.5)),
                            ),
                          ],
                        ),
                      );
                    },
                  ),
          ],
        ),

        // Lock button
        const SizedBox(height: 20),
        Center(
          child: ElevatedButton(
            onPressed: () {
              provider.setPartyBuildingConfirmed(!provider.partyBuildingConfirmed);
            },
            style: ElevatedButton.styleFrom(
              primary: provider.partyBuildingConfirmed ? const Color(0xFF22C55E) : partyColor,
              onPrimary: provider.partyBuildingConfirmed ? const Color(0xFF213C51) : Colors.white,
              padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
            ),
            child: Text(
              provider.partyBuildingConfirmed ? '✅ Projects Choice Locked' : '🔒 Confirm Projects Choice',
              style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
            ),
          ),
        ),
      ],
    );
  }
}
