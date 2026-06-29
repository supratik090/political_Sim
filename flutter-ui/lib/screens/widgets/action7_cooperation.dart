import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../models/models.dart';
import '../../providers/game_provider.dart';

class Action7Cooperation extends StatefulWidget {
  final TurnView turnData;
  final Map<String, dynamic> projectDefs;

  const Action7Cooperation({
    Key? key,
    required this.turnData,
    required this.projectDefs,
  }) : super(key: key);

  @override
  State<Action7Cooperation> createState() => _Action7CooperationState();
}

class _Action7CooperationState extends State<Action7Cooperation> {
  // Workshop Form State
  String? _recipientId;
  String _offerType = 'EXCHANGE'; // EXCHANGE or NON_AGGRESSION

  // Exchange Give
  int _offeredCoins = 0;
  int _offeredMorale = 0;
  int _offeredSupport = 0;
  final List<String> _offeredBuildingKeys = [];

  // Exchange Take
  int _requestedCoins = 0;
  int _requestedMorale = 0;
  int _requestedSupport = 0;

  // Non aggression details
  int _durationTurns = 10;
  bool _includePayment = false;
  bool _senderPaysPact = true; // true = We Pay, false = They Pay
  String _pactPaymentResource = 'COINS';
  int _pactPaymentValue = 0;
  final List<String> _pactPaymentBuildingKeys = [];

  String? _successMsg;
  String? _errorMsg;
  bool _loading = false;

  @override
  void initState() {
    super.initState();
    final otherParties = widget.turnData.parties.where((p) => p.id != widget.turnData.activeHumanPartyId).toList();
    if (otherParties.isNotEmpty) {
      _recipientId = otherParties[0].id;
    }
  }

  void _resetForm() {
    setState(() {
      _offeredCoins = 0;
      _offeredMorale = 0;
      _offeredSupport = 0;
      _offeredBuildingKeys.clear();
      _requestedCoins = 0;
      _requestedMorale = 0;
      _requestedSupport = 0;
      _includePayment = false;
      _pactPaymentValue = 0;
      _pactPaymentBuildingKeys.clear();
    });
  }

  static Color parseHexColor(String hex) {
    try {
      return Color(int.parse(hex.replaceFirst('#', '0xFF')));
    } catch (_) {
      return const Color(0xFF213C51);
    }
  }

  Future<void> _handleRespond(String offerId, bool accept) async {
    setState(() {
      _loading = true;
      _successMsg = null;
      _errorMsg = null;
    });

    final provider = Provider.of<GameProvider>(context, listen: false);
    final success = await provider.respondToCooperationOffer(offerId, accept);

    if (!mounted) return;
    setState(() {
      _loading = false;
    });

    if (success) {
      setState(() {
        _successMsg = 'Offer successfully ${accept ? "accepted" : "rejected"}!';
      });
    } else {
      setState(() {
        _errorMsg = provider.errorMessage ?? 'Failed to respond to offer.';
      });
    }
  }

  Future<void> _handlePropose() async {
    if (_recipientId == null) return;
    setState(() {
      _loading = true;
      _successMsg = null;
      _errorMsg = null;
    });

    final provider = Provider.of<GameProvider>(context, listen: false);
    final activeParty = widget.turnData.parties.firstWhere((p) => p.id == widget.turnData.activeHumanPartyId);
    final recipientParty = widget.turnData.parties.firstWhere((p) => p.id == _recipientId);

    final payload = {
      'senderPartyId': activeParty.id,
      'senderPartyName': activeParty.name,
      'recipientPartyId': _recipientId,
      'recipientPartyName': recipientParty.name,
      'type': _offerType,
      'offeredCoins': _offerType == 'EXCHANGE' ? _offeredCoins : 0,
      'offeredMorale': _offerType == 'EXCHANGE' ? _offeredMorale : 0,
      'offeredSupport': _offerType == 'EXCHANGE' ? _offeredSupport : 0,
      'offeredBuildingKeys': _offerType == 'EXCHANGE' ? _offeredBuildingKeys : [],
      'requestedCoins': _offerType == 'EXCHANGE' ? _requestedCoins : 0,
      'requestedSupport': _offerType == 'EXCHANGE' ? _requestedSupport : 0,
      'requestedMorale': _offerType == 'EXCHANGE' ? _requestedMorale : 0,
      'durationTurns': _offerType == 'NON_AGGRESSION' ? _durationTurns : 0,
      'senderPaysPact': _offerType == 'NON_AGGRESSION' ? _includePayment && _senderPaysPact : false,
      'pactPaymentResource': _offerType == 'NON_AGGRESSION' && _includePayment ? _pactPaymentResource : null,
      'pactPaymentValue': _offerType == 'NON_AGGRESSION' && _includePayment && _pactPaymentResource != 'COMPLETED_BUILDING' ? _pactPaymentValue : 0,
      'pactPaymentBuildingKeys': _offerType == 'NON_AGGRESSION' && _includePayment && _pactPaymentResource == 'COMPLETED_BUILDING' ? _pactPaymentBuildingKeys : []
    };

    final success = await provider.proposeCooperationOffer(payload);

    if (!mounted) return;
    setState(() {
      _loading = false;
    });

    if (success) {
      // Find the last offer to see if computer resolved it immediately
      final updatedData = provider.currentTurnView;
      final newOffers = updatedData?.cooperationOffers ?? [];
      final created = newOffers.isNotEmpty ? newOffers.last : null;

      if (created != null && recipientParty.controllerType == 'COMPUTER') {
        if (created.status == 'ACCEPTED') {
          setState(() {
            _successMsg = '✅ Proposal accepted by ${recipientParty.name}! The transaction has been resolved.';
          });
        } else if (created.status == 'REJECTED') {
          setState(() {
            _errorMsg = '❌ Proposal rejected by ${recipientParty.name}.';
          });
        }
      } else {
        setState(() {
          _successMsg = '🤝 Proposal successfully sent to ${recipientParty.name}.';
        });
      }
      _resetForm();
    } else {
      setState(() {
        _errorMsg = provider.errorMessage ?? 'Failed to propose deal.';
      });
    }
  }

  String _getResourceString(CooperationOffer offer) {
    if (offer.type == 'NON_AGGRESSION') {
      String desc = '${offer.durationTurns}-turn Non-Aggression Pact';
      if (offer.pactPaymentValue > 0 || offer.pactPaymentBuildingKeys.isNotEmpty) {
        final payer = offer.senderPaysPact ? offer.senderPartyName : offer.recipientPartyName;
        desc += ' (Payment: ';
        if (offer.pactPaymentBuildingKeys.isNotEmpty) {
          final names = offer.pactPaymentBuildingKeys.map((k) {
            final def = widget.projectDefs[k];
            return def != null ? def['name'] ?? k : k;
          }).join(', ');
          desc += 'Buildings [$names]';
        } else {
          desc += '${offer.pactPaymentValue} ${offer.pactPaymentResource}';
        }
        desc += ' paid by $payer)';
      }
      return desc;
    } else {
      final List<String> giveParts = [];
      if (offer.offeredCoins > 0) giveParts.add('${offer.offeredCoins} Coins');
      if (offer.offeredMorale > 0) giveParts.add('${offer.offeredMorale} Morale');
      if (offer.offeredSupport > 0) giveParts.add('${offer.offeredSupport}% Support');
      if (offer.offeredBuildingKeys.isNotEmpty) {
        final names = offer.offeredBuildingKeys.map((k) {
          final def = widget.projectDefs[k];
          return def != null ? def['name'] ?? k : k;
        }).join(', ');
        giveParts.add('Buildings [$names]');
      }

      final List<String> reqParts = [];
      if (offer.requestedCoins > 0) reqParts.add('${offer.requestedCoins} Coins');
      if (offer.requestedSupport > 0) reqParts.add('${offer.requestedSupport}% Support');
      if (offer.requestedMorale > 0) reqParts.add('${offer.requestedMorale} Morale');

      return 'Exchange: GIVES {${giveParts.join(", ")}} in return for RECEIVING {${reqParts.join(", ")}}';
    }
  }

  @override
  Widget build(BuildContext context) {
    final activePartyId = widget.turnData.activeHumanPartyId;
    final activeParty = widget.turnData.parties.firstWhere((p) => p.id == activePartyId);
    final otherParties = widget.turnData.parties.where((p) => p.id != activePartyId).toList();

    final myCompletedProjects = activeParty.projects.where((p) => p.progressPercent >= 100).toList();

    final recipientParty = _recipientId != null
        ? widget.turnData.parties.firstWhere((p) => p.id == _recipientId)
        : null;
    final targetCompletedProjects = recipientParty != null
        ? recipientParty.projects.where((p) => p.progressPercent >= 100).toList()
        : [];

    final myPacts = widget.turnData.activePacts.where((p) => p.partyAId == activePartyId || p.partyBId == activePartyId).toList();
    final incomingOffers = widget.turnData.cooperationOffers.where((o) => o.recipientPartyId == activePartyId && o.status == 'PENDING').toList();

    final partyColor = parseHexColor(activeParty.color);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        // 1. Active Non Aggression Pacts
        Container(
          decoration: BoxDecoration(
            color: Colors.white,
            border: Border.all(color: const Color(0xFFB0CBE0)),
            borderRadius: BorderRadius.circular(8),
          ),
          padding: const EdgeInsets.all(12),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                '🕊️ Active Non-Aggression Treaties',
                style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
              ),
              const SizedBox(height: 8),
              myPacts.isEmpty
                  ? const Center(
                      child: Text(
                        'No active non-aggression treaties at this time.',
                        style: TextStyle(fontSize: 11.5, color: Colors.grey, fontStyle: FontStyle.italic),
                      ),
                    )
                  : Column(
                      children: myPacts.map((p) {
                        final partner = p.partyAId == activePartyId ? p.partyBName : p.partyAName;
                        return Container(
                          margin: const EdgeInsets.only(bottom: 6),
                          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                          decoration: BoxDecoration(
                            color: const Color(0x0F22C55E),
                            border: Border.all(color: const Color(0xFF22C55E)),
                            borderRadius: BorderRadius.circular(6),
                          ),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text('🤝 Treaty with $partner', style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFF166534))),
                              Text('⏳ ${p.turnsRemaining} Months Left', style: const TextStyle(fontSize: 10.5, fontWeight: FontWeight.bold, color: Color(0xFF166534))),
                            ],
                          ),
                        );
                      }).toList(),
                    ),
            ],
          ),
        ),
        const SizedBox(height: 16),

        // 2. Incoming Proposals
        Container(
          decoration: BoxDecoration(
            color: Colors.white,
            border: Border.all(color: const Color(0xFFB0CBE0)),
            borderRadius: BorderRadius.circular(8),
          ),
          padding: const EdgeInsets.all(12),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                '📥 Incoming Diplomatic Proposals',
                style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
              ),
              const SizedBox(height: 8),
              incomingOffers.isEmpty
                  ? const Center(
                      child: Text(
                        'No incoming proposals from other parties.',
                        style: TextStyle(fontSize: 11.5, color: Colors.grey, fontStyle: FontStyle.italic),
                      ),
                    )
                  : Column(
                      children: incomingOffers.map((o) {
                        return Container(
                          margin: const EdgeInsets.only(bottom: 8),
                          padding: const EdgeInsets.all(10),
                          decoration: BoxDecoration(
                            color: Colors.black.withOpacity(0.02),
                            border: Border.all(color: const Color(0xFFB0CBE0)),
                            borderRadius: BorderRadius.circular(6),
                          ),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text('Sender: ${o.senderPartyName}', style: const TextStyle(fontSize: 10.5, fontWeight: FontWeight.bold, color: Colors.grey)),
                              const SizedBox(height: 4),
                              Text(_getResourceString(o), style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFF213C51))),
                              const SizedBox(height: 8),
                              Row(
                                children: [
                                  Expanded(
                                    child: ElevatedButton(
                                      onPressed: _loading ? null : () => _handleRespond(o.id, true),
                                      style: ElevatedButton.styleFrom(primary: const Color(0xFF22C55E), isDense: true),
                                      child: const Text('Accept Offer', style: TextStyle(fontSize: 11)),
                                    ),
                                  ),
                                  const SizedBox(width: 8),
                                  Expanded(
                                    child: ElevatedButton(
                                      onPressed: _loading ? null : () => _handleRespond(o.id, false),
                                      style: ElevatedButton.styleFrom(primary: const Color(0xFFEF4444), isDense: true),
                                      child: const Text('Reject Offer', style: TextStyle(fontSize: 11)),
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
        const SizedBox(height: 16),

        // 3. Workshop Proposal Form
        Container(
          decoration: BoxDecoration(
            color: Colors.white,
            border: Border.all(color: const Color(0xFFB0CBE0)),
            borderRadius: BorderRadius.circular(8),
          ),
          padding: const EdgeInsets.all(12),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const Text(
                '🏛️ Treaty & Exchange Workshop',
                style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFF213C51)),
              ),
              const SizedBox(height: 8),

              // Step A: choose partner & type
              DropdownButtonFormField<String>(
                value: _recipientId,
                dropdownColor: Colors.white,
                style: const TextStyle(fontSize: 12.5, color: Color(0xFF213C51)),
                decoration: const InputDecoration(isDense: true, contentPadding: EdgeInsets.all(8), labelText: 'Select Partner'),
                onChanged: (val) {
                  if (val != null) {
                    setState(() {
                      _recipientId = val;
                      _resetForm();
                    });
                  }
                },
                items: otherParties.map((p) => DropdownMenuItem(
                      value: p.id,
                      child: Text('${p.name} (${p.role})'),
                    )).toList(),
              ),
              const SizedBox(height: 12),

              Row(
                children: [
                  Expanded(
                    child: ChoiceChip(
                      label: const Center(child: Text('💱 Exchange Assets', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold))),
                      selected: _offerType == 'EXCHANGE',
                      selectedColor: const Color(0xFF213C51),
                      onSelected: (_) => setState(() => _offerType = 'EXCHANGE'),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Expanded(
                    child: ChoiceChip(
                      label: const Center(child: Text('🕊️ Non-Aggression', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold))),
                      selected: _offerType == 'NON_AGGRESSION',
                      selectedColor: const Color(0xFF213C51),
                      onSelected: (_) => setState(() => _offerType = 'NON_AGGRESSION'),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),

              // Step B: Offer details
              if (_offerType == 'EXCHANGE') ...[
                // EXCHANGE OFFER INPUTS
                const Text('🎁 What You Offer (Give):', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF213C51))),
                const SizedBox(height: 8),
                Row(
                  children: [
                    Expanded(
                      child: TextFormField(
                        initialValue: _offeredCoins.toString(),
                        keyboardType: TextInputType.number,
                        decoration: const InputDecoration(labelText: 'Coins', isDense: true, contentPadding: EdgeInsets.all(8)),
                        onChanged: (val) => _offeredCoins = int.tryParse(val) ?? 0,
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: TextFormField(
                        initialValue: _offeredMorale.toString(),
                        keyboardType: TextInputType.number,
                        decoration: const InputDecoration(labelText: 'Morale', isDense: true, contentPadding: EdgeInsets.all(8)),
                        onChanged: (val) => _offeredMorale = int.tryParse(val) ?? 0,
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: TextFormField(
                        initialValue: _offeredSupport.toString(),
                        keyboardType: TextInputType.number,
                        decoration: const InputDecoration(labelText: 'Support %', isDense: true, contentPadding: EdgeInsets.all(8)),
                        onChanged: (val) => _offeredSupport = int.tryParse(val) ?? 0,
                      ),
                    ),
                  ],
                ),
                if (myCompletedProjects.isNotEmpty) ...[
                  const SizedBox(height: 10),
                  const Text('Completed Buildings to Offer:', style: TextStyle(fontSize: 10, color: Colors.grey)),
                  const SizedBox(height: 4),
                  Container(
                    height: 80,
                    decoration: BoxDecoration(border: Border.all(color: Colors.grey.withOpacity(0.3)), borderRadius: BorderRadius.circular(4)),
                    child: ListView(
                      padding: const EdgeInsets.all(4),
                      children: myCompletedProjects.map((p) {
                        final pDef = widget.projectDefs[p.projectKey] ?? {'name': p.projectKey};
                        final isChecked = _offeredBuildingKeys.contains(p.projectKey);
                        return CheckboxListTile(
                          title: Text(pDef['name'], style: const TextStyle(fontSize: 11)),
                          value: isChecked,
                          dense: true,
                          contentPadding: EdgeInsets.zero,
                          controlAffinity: ListTileControlAffinity.leading,
                          onChanged: (val) {
                            setState(() {
                              if (val == true) {
                                _offeredBuildingKeys.add(p.projectKey);
                              } else {
                                _offeredBuildingKeys.remove(p.projectKey);
                              }
                            });
                          },
                        );
                      }).toList(),
                    ),
                  ),
                ],
                const SizedBox(height: 16),

                // REQUEST ASSETS INPUTS
                const Text('🤲 What You Request (Take):', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF213C51))),
                const SizedBox(height: 8),
                Row(
                  children: [
                    Expanded(
                      child: TextFormField(
                        initialValue: _requestedCoins.toString(),
                        keyboardType: TextInputType.number,
                        decoration: const InputDecoration(labelText: 'Coins', isDense: true, contentPadding: EdgeInsets.all(8)),
                        onChanged: (val) => _requestedCoins = int.tryParse(val) ?? 0,
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: TextFormField(
                        initialValue: _requestedMorale.toString(),
                        keyboardType: TextInputType.number,
                        decoration: const InputDecoration(labelText: 'Morale', isDense: true, contentPadding: EdgeInsets.all(8)),
                        onChanged: (val) => _requestedMorale = int.tryParse(val) ?? 0,
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: TextFormField(
                        initialValue: _requestedSupport.toString(),
                        keyboardType: TextInputType.number,
                        decoration: const InputDecoration(labelText: 'Support %', isDense: true, contentPadding: EdgeInsets.all(8)),
                        onChanged: (val) => _requestedSupport = int.tryParse(val) ?? 0,
                      ),
                    ),
                  ],
                ),
              ] else ...[
                // NON_AGGRESSION INPUTS
                DropdownButtonFormField<int>(
                  value: _durationTurns,
                  dropdownColor: Colors.white,
                  style: const TextStyle(fontSize: 12.5, color: Color(0xFF213C51)),
                  decoration: const InputDecoration(labelText: 'Pact Duration', isDense: true, contentPadding: EdgeInsets.all(8)),
                  onChanged: (val) {
                    if (val != null) {
                      setState(() {
                        _durationTurns = val;
                      });
                    }
                  },
                  items: const [
                    DropdownMenuItem(value: 5, child: Text('5 Months')),
                    DropdownMenuItem(value: 10, child: Text('10 Months')),
                    DropdownMenuItem(value: 15, child: Text('15 Months')),
                  ],
                ),
                const SizedBox(height: 10),
                CheckboxListTile(
                  title: const Text('Include Payment / Compensation with Pact', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
                  value: _includePayment,
                  contentPadding: EdgeInsets.zero,
                  controlAffinity: ListTileControlAffinity.leading,
                  onChanged: (val) {
                    if (val != null) {
                      setState(() {
                        _includePayment = val;
                      });
                    }
                  },
                ),
                if (_includePayment) ...[
                  const SizedBox(height: 8),
                  Container(
                    padding: const EdgeInsets.all(10),
                    decoration: BoxDecoration(color: Colors.black.withOpacity(0.01), border: Border.all(color: Colors.grey.withOpacity(0.3)), borderRadius: BorderRadius.circular(6)),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text('Payment Direction:', style: TextStyle(fontSize: 10, color: Colors.grey)),
                        Row(
                          children: [
                            Radio<bool>(value: true, groupValue: _senderPaysPact, onChanged: (val) => setState(() => _senderPaysPact = val!)),
                            const Text('We Pay Them', style: TextStyle(fontSize: 11)),
                            const SizedBox(width: 16),
                            Radio<bool>(value: false, groupValue: _senderPaysPact, onChanged: (val) => setState(() => _senderPaysPact = val!)),
                            const Text('They Pay Us', style: TextStyle(fontSize: 11)),
                          ],
                        ),
                        const SizedBox(height: 8),
                        DropdownButtonFormField<String>(
                          value: _pactPaymentResource,
                          dropdownColor: Colors.white,
                          style: const TextStyle(fontSize: 12.5, color: Color(0xFF213C51)),
                          decoration: const InputDecoration(labelText: 'Asset Type', isDense: true, contentPadding: EdgeInsets.all(6)),
                          onChanged: (val) => setState(() => _pactPaymentResource = val!),
                          items: const [
                            DropdownMenuItem(value: 'COINS', child: Text('Coins')),
                            DropdownMenuItem(value: 'MORALE', child: Text('Morale')),
                            DropdownMenuItem(value: 'SUPPORT', child: Text('Public Support')),
                            DropdownMenuItem(value: 'COMPLETED_BUILDING', child: Text('Completed Buildings')),
                          ],
                        ),
                        const SizedBox(height: 8),
                        if (_pactPaymentResource != 'COMPLETED_BUILDING')
                          TextFormField(
                            initialValue: _pactPaymentValue.toString(),
                            keyboardType: TextInputType.number,
                            decoration: const InputDecoration(labelText: 'Amount', isDense: true, contentPadding: EdgeInsets.all(6)),
                            onChanged: (val) => _pactPaymentValue = int.tryParse(val) ?? 0,
                          )
                        else ...[
                          const Text('Select completed projects:', style: TextStyle(fontSize: 10, color: Colors.grey)),
                          const SizedBox(height: 4),
                          Container(
                            height: 80,
                            decoration: BoxDecoration(border: Border.all(color: Colors.grey.withOpacity(0.3)), borderRadius: BorderRadius.circular(4)),
                            child: ListView(
                              padding: const EdgeInsets.all(4),
                              children: (_senderPaysPact ? myCompletedProjects : targetCompletedProjects).map((p) {
                                final pDef = widget.projectDefs[p.projectKey] ?? {'name': p.projectKey};
                                final isChecked = _pactPaymentBuildingKeys.contains(p.projectKey);
                                return CheckboxListTile(
                                  title: Text(pDef['name'], style: const TextStyle(fontSize: 11)),
                                  value: isChecked,
                                  dense: true,
                                  contentPadding: EdgeInsets.zero,
                                  controlAffinity: ListTileControlAffinity.leading,
                                  onChanged: (val) {
                                    setState(() {
                                      if (val == true) {
                                        _pactPaymentBuildingKeys.add(p.projectKey);
                                      } else {
                                        _pactPaymentBuildingKeys.remove(p.projectKey);
                                      }
                                    });
                                  },
                                );
                              }).toList(),
                            ),
                          ),
                        ]
                      ],
                    ),
                  ),
                ],
              ],
              const SizedBox(height: 16),

              // Alerts Success / Errors
              if (_successMsg != null)
                Container(
                  padding: const EdgeInsets.all(10),
                  margin: const EdgeInsets.only(bottom: 12),
                  decoration: BoxDecoration(color: const Color(0x1F22C55E), border: Border.all(color: const Color(0xFF22C55E)), borderRadius: BorderRadius.circular(6)),
                  child: Text(_successMsg!, style: const TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold, color: Color(0xFF166534))),
                ),
              if (_errorMsg != null)
                Container(
                  padding: const EdgeInsets.all(10),
                  margin: const EdgeInsets.only(bottom: 12),
                  decoration: BoxDecoration(color: const Color(0x1FE11D48), border: Border.all(color: const Color(0xFFE11D48)), borderRadius: BorderRadius.circular(6)),
                  child: Text(_errorMsg!, style: const TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold, color: Color(0xFF9F1239))),
                ),

              // Submit Deal button
              ElevatedButton(
                onPressed: _loading || _recipientId == null ? null : _handlePropose,
                style: ElevatedButton.styleFrom(
                  primary: const Color(0xFF213C51),
                  padding: const EdgeInsets.symmetric(vertical: 14),
                ),
                child: _loading
                    ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 2, valueColor: AlwaysStoppedAnimation<Color>(Colors.white)))
                    : const Text('🤝 Propose Diplomatic Deal', style: TextStyle(fontSize: 12.5, fontWeight: FontWeight.bold)),
              ),
            ],
          ),
        ),
      ],
    );
  }
}
