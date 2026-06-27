import React, { useState, useEffect } from 'react';
import { createCooperationOffer, respondToCooperationOffer } from '../../api/apiClient';

export default function Action7Cooperation({ turnData, projectDefs: PROJECT_DEFS = {}, onActionComplete }) {
  const activePartyId = turnData.activeHumanPartyId;
  const activeParty = turnData.parties.find(p => p.id === activePartyId);
  const otherParties = turnData.parties.filter(p => p.id !== activePartyId);

  // Form State
  const [recipientId, setRecipientId] = useState(otherParties[0]?.id || '');
  const [offerType, setOfferType] = useState('EXCHANGE');

  // Exchange details
  const [offeredCoins, setOfferedCoins] = useState(0);
  const [offeredMorale, setOfferedMorale] = useState(0);
  const [offeredSupport, setOfferedSupport] = useState(0);
  const [offeredBuildingKeys, setOfferedBuildingKeys] = useState([]);
  
  const [requestedCoins, setRequestedCoins] = useState(0);
  const [requestedSupport, setRequestedSupport] = useState(0);
  const [requestedMorale, setRequestedMorale] = useState(0);

  // Non-aggression details
  const [durationTurns, setDurationTurns] = useState(10);
  const [includePayment, setIncludePayment] = useState(false);
  const [senderPaysPact, setSenderPaysPact] = useState(true); // true = We Pay, false = They Pay
  const [pactPaymentResource, setPactPaymentResource] = useState('COINS');
  const [pactPaymentValue, setPactPaymentValue] = useState(0);
  const [pactPaymentBuildingKeys, setPactPaymentBuildingKeys] = useState([]);

  // UI state
  const [loading, setLoading] = useState(false);
  const [successMsg, setSuccessMsg] = useState('');
  const [errorMsg, setErrorMsg] = useState('');

  const recipientParty = turnData.parties.find(p => p.id === recipientId);

  // Get completed projects for current player (We Pay)
  const myCompletedProjects = activeParty?.projects?.filter(p => p.progressPercent >= 100) || [];
  // Get completed projects for target party (They Pay)
  const targetCompletedProjects = recipientParty?.projects?.filter(p => p.progressPercent >= 100) || [];

  // Reset keys if target or type changes
  useEffect(() => {
    setOfferedBuildingKeys([]);
    setPactPaymentBuildingKeys([]);
    setSuccessMsg('');
    setErrorMsg('');
  }, [recipientId, offerType, includePayment, senderPaysPact]);

  // Active Pacts involving the player
  const myPacts = turnData.activePacts ? turnData.activePacts.filter(p => p.partyAId === activePartyId || p.partyBId === activePartyId) : [];

  // Pending Incoming Offers for player
  const incomingOffers = turnData.cooperationOffers ? turnData.cooperationOffers.filter(o => o.recipientPartyId === activePartyId && o.status === 'PENDING') : [];

  const handleRespond = async (offerId, accept) => {
    setLoading(true);
    setSuccessMsg('');
    setErrorMsg('');
    try {
      const updatedData = await respondToCooperationOffer(turnData.gameId, offerId, accept);
      onActionComplete(updatedData);
      setSuccessMsg(`Offer successfully ${accept ? 'accepted' : 'rejected'}!`);
    } catch (err) {
      setErrorMsg(err.message || 'Failed to respond to offer.');
    } finally {
      setLoading(false);
    }
  };

  const handlePropose = async () => {
    setLoading(true);
    setSuccessMsg('');
    setErrorMsg('');

    const payload = {
      senderPartyId: activePartyId,
      senderPartyName: activeParty?.name,
      recipientPartyId: recipientId,
      recipientPartyName: recipientParty?.name,
      type: offerType,
      offeredCoins: offerType === 'EXCHANGE' ? parseInt(offeredCoins) || 0 : 0,
      offeredMorale: offerType === 'EXCHANGE' ? parseInt(offeredMorale) || 0 : 0,
      offeredSupport: offerType === 'EXCHANGE' ? parseInt(offeredSupport) || 0 : 0,
      offeredBuildingKeys: offerType === 'EXCHANGE' ? offeredBuildingKeys : [],
      requestedCoins: offerType === 'EXCHANGE' ? parseInt(requestedCoins) || 0 : 0,
      requestedSupport: offerType === 'EXCHANGE' ? parseInt(requestedSupport) || 0 : 0,
      requestedMorale: offerType === 'EXCHANGE' ? parseInt(requestedMorale) || 0 : 0,
      durationTurns: offerType === 'NON_AGGRESSION' ? parseInt(durationTurns) || 10 : 0,
      senderPaysPact: offerType === 'NON_AGGRESSION' ? includePayment && senderPaysPact : false,
      pactPaymentResource: offerType === 'NON_AGGRESSION' && includePayment ? pactPaymentResource : null,
      pactPaymentValue: offerType === 'NON_AGGRESSION' && includePayment && pactPaymentResource !== 'COMPLETED_BUILDING' ? parseInt(pactPaymentValue) || 0 : 0,
      pactPaymentBuildingKeys: offerType === 'NON_AGGRESSION' && includePayment && pactPaymentResource === 'COMPLETED_BUILDING' ? pactPaymentBuildingKeys : []
    };

    try {
      const updatedData = await createCooperationOffer(turnData.gameId, payload);
      onActionComplete(updatedData);
      
      // Look at the status of the newly created offer to see if AI accepted/rejected
      const newOffers = updatedData.cooperationOffers || [];
      const created = newOffers[newOffers.length - 1];
      if (created && recipientParty?.controllerType === 'COMPUTER') {
        if (created.status === 'ACCEPTED') {
          setSuccessMsg(`✅ Proposal accepted by ${recipientParty.name}! The transaction has been resolved.`);
        } else if (created.status === 'REJECTED') {
          setErrorMsg(`❌ Proposal rejected by ${recipientParty.name}.`);
        }
      } else {
        setSuccessMsg(`🤝 Proposal successfully sent to ${recipientParty?.name || 'partner'}.`);
      }
      
      // Reset input fields
      setOfferedCoins(0);
      setOfferedMorale(0);
      setOfferedSupport(0);
      setOfferedBuildingKeys([]);
      setRequestedCoins(0);
      setRequestedSupport(0);
      setRequestedMorale(0);
      setIncludePayment(false);
      setPactPaymentValue(0);
      setPactPaymentBuildingKeys([]);
    } catch (err) {
      setErrorMsg(err.message || 'Failed to submit proposal.');
    } finally {
      setLoading(false);
    }
  };

  const toggleBuildingSelection = (key, type) => {
    if (type === 'OFFER') {
      setOfferedBuildingKeys(prev => 
        prev.includes(key) ? prev.filter(k => k !== key) : [...prev, key]
      );
    } else {
      setPactPaymentBuildingKeys(prev => 
        prev.includes(key) ? prev.filter(k => k !== key) : [...prev, key]
      );
    }
  };

  const getResourceString = (offer) => {
    if (offer.type === 'NON_AGGRESSION') {
      let desc = `${offer.durationTurns}-turn Non-Aggression Pact`;
      if (offer.pactPaymentValue > 0 || (offer.pactPaymentBuildingKeys && offer.pactPaymentBuildingKeys.length > 0)) {
        const payer = offer.senderPaysPact ? offer.senderPartyName : offer.recipientPartyName;
        desc += ` (Payment: `;
        if (offer.pactPaymentBuildingKeys && offer.pactPaymentBuildingKeys.length > 0) {
          const names = offer.pactPaymentBuildingKeys.map(k => PROJECT_DEFS[k]?.name || k).join(', ');
          desc += `Buildings [${names}]`;
        } else {
          desc += `${offer.pactPaymentValue} ${offer.pactPaymentResource}`;
        }
        desc += ` paid by ${payer})`;
      }
      return desc;
    } else {
      const giveParts = [];
      if (offer.offeredCoins > 0) giveParts.add(`${offer.offeredCoins} Coins`);
      if (offer.offeredMorale > 0) giveParts.add(`${offer.offeredMorale} Morale`);
      if (offer.offeredSupport > 0) giveParts.add(`${offer.offeredSupport}% Support`);
      if (offer.offeredBuildingKeys && offer.offeredBuildingKeys.length > 0) {
        const names = offer.offeredBuildingKeys.map(k => PROJECT_DEFS[k]?.name || k).join(', ');
        giveParts.push(`Buildings [${names}]`);
      }
      
      const reqParts = [];
      if (offer.requestedCoins > 0) reqParts.push(`${offer.requestedCoins} Coins`);
      if (offer.requestedSupport > 0) reqParts.push(`${offer.requestedSupport}% Support`);
      if (offer.requestedMorale > 0) reqParts.push(`${offer.requestedMorale} Morale`);

      return `Exchange: GIVES {${giveParts.join(', ')}} in return for RECEIVING {${reqParts.join(', ')}}`;
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
      
      {/* 1. Summit Header: Active Treaties */}
      <div style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '15px', background: '#ffffff' }}>
        <h4 style={{ margin: '0 0 12px 0', fontSize: '14px', color: 'var(--primary-dark)', display: 'flex', alignItems: 'center', gap: '6px' }}>
          🕊️ Active Non-Aggression Treaties
        </h4>
        {myPacts.length === 0 ? (
          <p style={{ margin: 0, fontSize: '13px', color: 'gray', fontStyle: 'italic', textAlign: 'center' }}>
            No active non-aggression treaties at this time.
          </p>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {myPacts.map(p => {
              const partner = p.partyAId === activePartyId ? p.partyBName : p.partyAName;
              return (
                <div key={p.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'rgba(34,197,94,0.06)', border: '1px solid #22c55e', padding: '10px 15px', borderRadius: '6px', fontSize: '13px', fontWeight: 'bold', color: '#166534' }}>
                  <span>🤝 Treaty with {partner}</span>
                  <span style={{ fontSize: '12px', background: '#22c55e', color: '#fff', padding: '2px 8px', borderRadius: '12px' }}>
                    ⏳ {p.turnsRemaining} Months Left
                  </span>
                </div>
              );
            })}
          </div>
        )}
      </div>

      {/* 2. Cooperation Inbox: Incoming Offers */}
      <div style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '15px', background: '#ffffff' }}>
        <h4 style={{ margin: '0 0 12px 0', fontSize: '14px', color: 'var(--primary-dark)', display: 'flex', alignItems: 'center', gap: '6px' }}>
          📥 Incoming Diplomatic Proposals
        </h4>
        {incomingOffers.length === 0 ? (
          <p style={{ margin: 0, fontSize: '13px', color: 'gray', fontStyle: 'italic', textAlign: 'center' }}>
            No incoming proposals from other parties.
          </p>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {incomingOffers.map(o => (
              <div key={o.id} style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '12px', background: 'rgba(0,0,0,0.02)' }}>
                <div style={{ fontSize: '12px', color: 'gray', fontWeight: 'bold' }}>Sender: {o.senderPartyName}</div>
                <div style={{ fontSize: '13px', fontWeight: 'bold', color: 'var(--primary-dark)', marginTop: '4px' }}>
                  {getResourceString(o)}
                </div>
                <div style={{ display: 'flex', gap: '10px', marginTop: '12px' }}>
                  <button
                    disabled={loading}
                    onClick={() => handleRespond(o.id, true)}
                    style={{ flex: 1, padding: '6px 12px', fontSize: '12px', fontWeight: 'bold', background: '#22c55e', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
                  >
                    ✅ Accept Offer
                  </button>
                  <button
                    disabled={loading}
                    onClick={() => handleRespond(o.id, false)}
                    style={{ flex: 1, padding: '6px 12px', fontSize: '12px', fontWeight: 'bold', background: '#e11d48', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
                  >
                    ❌ Reject Offer
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* 3. Diplomatic Deal Creator */}
      <div style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '15px', background: '#ffffff', display: 'flex', flexDirection: 'column', gap: '15px' }}>
        <h4 style={{ margin: 0, fontSize: '14px', color: 'var(--primary-dark)', display: 'flex', alignItems: 'center', gap: '6px' }}>
          🏛️ Treaty & Exchange Workshop
        </h4>

        {/* Step A: Choose Partner & Type */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', padding: '12px', background: 'rgba(0,0,0,0.01)', border: '1px solid var(--primary-border)', borderRadius: '8px' }}>
          <div>
            <label htmlFor="partner-select" style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '4px', color: 'gray' }}>Select Partner:</label>
            <select
              id="partner-select"
              value={recipientId}
              onChange={(e) => setRecipientId(e.target.value)}
              style={{ width: '100%', padding: '6px', fontSize: '13px', borderRadius: '4px', background: '#fff', border: '1px solid var(--primary-border)' }}
            >
              {otherParties.map(p => (
                <option key={p.id} value={p.id}>{p.name} ({p.role})</option>
              ))}
            </select>
          </div>
          <div style={{ marginTop: '5px' }}>
            <span style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '6px', color: 'gray' }}>Proposal Type:</span>
            <div style={{ display: 'flex', gap: '10px' }}>
              <label style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '6px', border: `1px solid ${offerType === 'EXCHANGE' ? 'var(--primary-dark)' : 'var(--primary-border)'}`, borderRadius: '4px', padding: '8px', cursor: 'pointer', background: offerType === 'EXCHANGE' ? 'rgba(33,60,81,0.05)' : '#fff', fontSize: '12px', fontWeight: 'bold' }}>
                <input type="radio" name="offerType" checked={offerType === 'EXCHANGE'} onChange={() => setOfferType('EXCHANGE')} style={{ display: 'none' }} />
                💱 Exchange Assets
              </label>
              <label style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '6px', border: `1px solid ${offerType === 'NON_AGGRESSION' ? 'var(--primary-dark)' : 'var(--primary-border)'}`, borderRadius: '4px', padding: '8px', cursor: 'pointer', background: offerType === 'NON_AGGRESSION' ? 'rgba(33,60,81,0.05)' : '#fff', fontSize: '12px', fontWeight: 'bold' }}>
                <input type="radio" name="offerType" checked={offerType === 'NON_AGGRESSION'} onChange={() => setOfferType('NON_AGGRESSION')} style={{ display: 'none' }} />
                🕊️ Non-Aggression Pact
              </label>
            </div>
          </div>
        </div>

        {/* Step B: What you Give (Offer) */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', padding: '12px', border: '1px solid var(--primary-border)', borderRadius: '8px' }}>
          <h5 style={{ margin: 0, fontSize: '12px', color: 'var(--primary-dark)', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '4px' }}>
            🎁 What You Offer (Give)
          </h5>

          {offerType === 'EXCHANGE' ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div style={{ display: 'flex', gap: '10px' }}>
                <div style={{ flex: 1 }}>
                  <label htmlFor="give-coins" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: 'gray' }}>Coins:</label>
                  <input id="give-coins" type="number" min="0" value={offeredCoins} onChange={(e) => setOfferedCoins(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '5px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }} />
                </div>
                <div style={{ flex: 1 }}>
                  <label htmlFor="give-morale" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: 'gray' }}>Morale:</label>
                  <input id="give-morale" type="number" min="0" value={offeredMorale} onChange={(e) => setOfferedMorale(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '5px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }} />
                </div>
                <div style={{ flex: 1 }}>
                  <label htmlFor="give-support" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: 'gray' }}>Support %:</label>
                  <input id="give-support" type="number" min="0" max="100" value={offeredSupport} onChange={(e) => setOfferedSupport(Math.min(100, Math.max(0, parseInt(e.target.value) || 0)))} style={{ width: '100%', padding: '5px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }} />
                </div>
              </div>

              {myCompletedProjects.length > 0 && (
                <div style={{ marginTop: '5px' }}>
                  <span style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '4px', color: 'gray' }}>Completed Buildings to Offer:</span>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '5px', maxHeight: '100px', overflowY: 'auto', padding: '6px', border: '1px solid var(--primary-border)', borderRadius: '4px' }}>
                    {myCompletedProjects.map(proj => {
                      const pDef = PROJECT_DEFS[proj.projectKey] || {};
                      return (
                        <label key={proj.id} style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px' }}>
                          <input type="checkbox" checked={offeredBuildingKeys.includes(proj.projectKey)} onChange={() => toggleBuildingSelection(proj.projectKey, 'OFFER')} />
                          🏗️ {pDef.name || proj.projectKey}
                        </label>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>
          ) : (
            // Non aggression details (duration & payments)
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div>
                <label htmlFor="duration-select" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: 'gray' }}>Pact Duration:</label>
                <select id="duration-select" value={durationTurns} onChange={(e) => setDurationTurns(parseInt(e.target.value))} style={{ width: '100%', padding: '6px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }}>
                  <option value={5}>5 Months</option>
                  <option value={10}>10 Months</option>
                  <option value={15}>15 Months</option>
                </select>
              </div>

              <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px', fontWeight: 'bold', marginTop: '5px' }}>
                <input type="checkbox" checked={includePayment} onChange={(e) => setIncludePayment(e.target.checked)} />
                Include Payment / Compensation with Pact
              </label>

              {includePayment && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', padding: '10px', background: 'rgba(0,0,0,0.01)', border: '1px solid var(--primary-border)', borderRadius: '6px' }}>
                  <div>
                    <span style={{ fontSize: '11px', display: 'block', marginBottom: '4px', color: 'gray' }}>Payment Direction:</span>
                    <div style={{ display: 'flex', gap: '10px' }}>
                      <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <input type="radio" checked={senderPaysPact} onChange={() => setSenderPaysPact(true)} />
                        We Pay Them
                      </label>
                      <label style={{ fontSize: '12px', display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <input type="radio" checked={!senderPaysPact} onChange={() => setSenderPaysPact(false)} />
                        They Pay Us
                      </label>
                    </div>
                  </div>

                  <div>
                    <label htmlFor="payment-asset" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: 'gray' }}>Asset Type:</label>
                    <select id="payment-asset" value={pactPaymentResource} onChange={(e) => setPactPaymentResource(e.target.value)} style={{ width: '100%', padding: '5px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }}>
                      <option value="COINS">Coins</option>
                      <option value="MORALE">Morale</option>
                      <option value="SUPPORT">Public Support</option>
                      <option value="COMPLETED_BUILDING">Completed Buildings</option>
                    </select>
                  </div>

                  {pactPaymentResource !== 'COMPLETED_BUILDING' ? (
                    <div>
                      <label htmlFor="payment-val" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: 'gray' }}>Amount:</label>
                      <input id="payment-val" type="number" min="0" value={pactPaymentValue} onChange={(e) => setPactPaymentValue(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '5px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }} />
                    </div>
                  ) : (
                    <div>
                      <span style={{ fontSize: '11px', display: 'block', marginBottom: '4px', color: 'gray' }}>Select completed projects:</span>
                      {senderPaysPact ? (
                        // We Pay -> player buildings
                        myCompletedProjects.length === 0 ? (
                          <p style={{ margin: 0, fontSize: '11px', color: 'gray', fontStyle: 'italic' }}>You own no completed buildings.</p>
                        ) : (
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '5px', maxHeight: '100px', overflowY: 'auto', padding: '6px', border: '1px solid var(--primary-border)', borderRadius: '4px' }}>
                            {myCompletedProjects.map(proj => {
                              const pDef = PROJECT_DEFS[proj.projectKey] || {};
                              return (
                                <label key={proj.id} style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px' }}>
                                  <input type="checkbox" checked={pactPaymentBuildingKeys.includes(proj.projectKey)} onChange={() => toggleBuildingSelection(proj.projectKey, 'PACT')} />
                                  🏗️ {pDef.name || proj.projectKey}
                                </label>
                              );
                            })}
                          </div>
                        )
                      ) : (
                        // They Pay -> recipient buildings
                        targetCompletedProjects.length === 0 ? (
                          <p style={{ margin: 0, fontSize: '11px', color: 'gray', fontStyle: 'italic' }}>{recipientParty?.name || 'Partner'} owns no completed buildings.</p>
                        ) : (
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '5px', maxHeight: '100px', overflowY: 'auto', padding: '6px', border: '1px solid var(--primary-border)', borderRadius: '4px' }}>
                            {targetCompletedProjects.map(proj => {
                              const pDef = PROJECT_DEFS[proj.projectKey] || {};
                              return (
                                <label key={proj.id} style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px' }}>
                                  <input type="checkbox" checked={pactPaymentBuildingKeys.includes(proj.projectKey)} onChange={() => toggleBuildingSelection(proj.projectKey, 'PACT')} />
                                  🏗️ {pDef.name || proj.projectKey}
                                </label>
                              );
                            })}
                          </div>
                        )
                      )}
                    </div>
                  )}
                </div>
              )}
            </div>
          )}
        </div>

        {/* Step C: What you Receive (Request) */}
        {offerType === 'EXCHANGE' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', padding: '12px', border: '1px solid var(--primary-border)', borderRadius: '8px' }}>
            <h5 style={{ margin: 0, fontSize: '12px', color: 'var(--primary-dark)', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '4px' }}>
              🤲 What You Request (Take)
            </h5>
            <div style={{ display: 'flex', gap: '10px' }}>
              <div style={{ flex: 1 }}>
                <label htmlFor="req-coins" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: 'gray' }}>Coins:</label>
                <input id="req-coins" type="number" min="0" value={requestedCoins} onChange={(e) => setRequestedCoins(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '5px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }} />
              </div>
              <div style={{ flex: 1 }}>
                <label htmlFor="req-morale" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: 'gray' }}>Morale:</label>
                <input id="req-morale" type="number" min="0" value={requestedMorale} onChange={(e) => setRequestedMorale(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '5px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }} />
              </div>
              <div style={{ flex: 1 }}>
                <label htmlFor="req-support" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: 'gray' }}>Support %:</label>
                <input id="req-support" type="number" min="0" max="100" value={requestedSupport} onChange={(e) => setRequestedSupport(Math.min(100, Math.max(0, parseInt(e.target.value) || 0)))} style={{ width: '100%', padding: '5px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }} />
              </div>
            </div>
          </div>
        )}

        {/* Success/Error Alerts */}
        {successMsg && (
          <div style={{ background: 'rgba(34,197,94,0.1)', color: '#166534', border: '1px solid #22c55e', padding: '10px 15px', borderRadius: '6px', fontSize: '12px', fontWeight: 'bold' }}>
            {successMsg}
          </div>
        )}
        {errorMsg && (
          <div style={{ background: 'rgba(225,29,72,0.1)', color: '#9f1239', border: '1px solid #e11d48', padding: '10px 15px', borderRadius: '6px', fontSize: '12px', fontWeight: 'bold' }}>
            {errorMsg}
          </div>
        )}

        {/* Propose Action Button */}
        <button
          onClick={handlePropose}
          disabled={loading || !recipientId}
          style={{
            width: '100%',
            padding: '10px 20px',
            fontSize: '13px',
            fontWeight: 'bold',
            background: 'var(--primary-dark)',
            color: '#ffffff',
            border: 'none',
            borderRadius: '6px',
            cursor: 'pointer',
            opacity: loading || !recipientId ? 0.6 : 1
          }}
        >
          {loading ? '⏳ Resolving summit proposal...' : '🤝 Propose Diplomatic Deal'}
        </button>
      </div>

    </div>
  );
}
