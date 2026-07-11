import React, { useState, useEffect } from 'react';
import { createCooperationOffer, respondToCooperationOffer, bribeFaction } from '../../api/apiClient';

export default function Action7Cooperation({ turnData, projectDefs: PROJECT_DEFS = {}, onActionComplete }) {
  const activePartyId = turnData.activeHumanPartyId;
  const activeParty = turnData.parties.find(p => p.id === activePartyId);
  const otherParties = turnData.parties.filter(p => p.id !== activePartyId);

  // Form State - default to empty/blank partner selection
  const [recipientId, setRecipientId] = useState('');
  const [offerType, setOfferType] = useState('EXCHANGE');

  // Lobbying details
  const [scenarioBills, setScenarioBills] = useState([]);
  const [lobbyBillKey, setLobbyBillKey] = useState('');
  const [offeredMedia, setOfferedMedia] = useState(0);

  useEffect(() => {
    if (turnData.scenarioKey) {
      import('../../api/apiClient').then(client => {
        if (client.fetchBillsForGameplay) {
          client.fetchBillsForGameplay(turnData.scenarioKey)
            .then(data => setScenarioBills(data || []))
            .catch(err => console.error("Failed to load scenario bills:", err));
        }
      });
    }
  }, [turnData.scenarioKey]);

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

  // Sabotage / Bribe details
  const [selectedFactionKey, setSelectedFactionKey] = useState('');
  const [bribeCoins, setBribeCoins] = useState(0);

  // UI state
  const [loading, setLoading] = useState(false);
  const [successMsg, setSuccessMsg] = useState('');
  const [errorMsg, setErrorMsg] = useState('');
  const [feedback, setFeedback] = useState(null); // { status: 'SUCCESS' | 'REJECTED' | 'BRIBE_SUCCESS' | 'BRIBE_SCANDAL', title: '', message: '' }

  const recipientParty = turnData.parties.find(p => p.id === recipientId);
  const targetFactions = recipientParty?.factions || [];

  // Get completed projects for current player (We Offer)
  const myCompletedProjects = activeParty?.projects?.filter(p => p.progressPercent >= 100) || [];
  // Get completed projects for target party (We Request)
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

  // Accepted Lobbying Agreements
  const acceptedLobbyAgreements = turnData.cooperationOffers ? turnData.cooperationOffers.filter(o => o.type === 'LOBBYING' && o.status === 'ACCEPTED' && (o.senderPartyId === activePartyId || o.recipientPartyId === activePartyId)) : [];

  // Filter bills based on proposing role (only opposition sponsors for opposition, only government sponsors for government)
  const myRole = activeParty?.role; // "GOVERNMENT", "OPPOSITION", or "THIRD_PARTY"
  const targetBillRole = myRole === 'GOVERNMENT' ? 'GOVERNMENT' : 'OPPOSITION';
  const myRoleBills = (scenarioBills || []).filter(b => b.proposingRole === targetBillRole);

  const getBillName = (billKey) => {
    const bill = (scenarioBills || []).find(b => b.billKey === billKey);
    return bill ? bill.name : billKey;
  };

  const handleRespond = async (offerId, accept) => {
    setLoading(true);
    setSuccessMsg('');
    setErrorMsg('');
    try {
      const updatedData = await respondToCooperationOffer(turnData.gameId, offerId, accept);
      onActionComplete(updatedData);
      setFeedback({
        status: accept ? 'SUCCESS' : 'REJECTED',
        title: accept ? 'Deal Accepted!' : 'Deal Rejected',
        message: `You have successfully ${accept ? 'accepted' : 'rejected'} the diplomatic proposal.`
      });
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

    // Payload formatted based on rules (hiding duration / pact payment attributes for non-pact types)
    const payload = {
      senderPartyId: activePartyId,
      senderPartyName: activeParty?.name,
      recipientPartyId: recipientId,
      recipientPartyName: recipientParty?.name,
      type: offerType,
      lobbyBillKey: offerType === 'LOBBYING' ? lobbyBillKey : null,
      offeredCoins: (offerType === 'EXCHANGE' || offerType === 'LOBBYING') ? parseInt(offeredCoins) || 0 : 0,
      offeredMorale: (offerType === 'EXCHANGE' || offerType === 'LOBBYING') ? parseInt(offeredMorale) || 0 : 0,
      offeredMedia: offerType === 'LOBBYING' ? parseInt(offeredMedia) || 0 : 0,
      offeredSupport: offerType === 'EXCHANGE' ? parseInt(offeredSupport) || 0 : 0,
      offeredBuildingKeys: (offerType === 'EXCHANGE' || offerType === 'LOBBYING') ? offeredBuildingKeys : [],
      requestedCoins: offerType === 'EXCHANGE' ? parseInt(requestedCoins) || 0 : 0,
      requestedSupport: offerType === 'EXCHANGE' ? parseInt(requestedSupport) || 0 : 0,
      requestedMorale: offerType === 'EXCHANGE' ? parseInt(requestedMorale) || 0 : 0,
      // Pact duration / payments only apply to NON_AGGRESSION
      durationTurns: offerType === 'NON_AGGRESSION' ? parseInt(durationTurns) || 0 : 0,
      senderPaysPact: offerType === 'NON_AGGRESSION' ? includePayment && senderPaysPact : false,
      pactPaymentResource: offerType === 'NON_AGGRESSION' && includePayment ? pactPaymentResource : null,
      pactPaymentValue: offerType === 'NON_AGGRESSION' && includePayment && pactPaymentResource !== 'COMPLETED_BUILDING' ? parseInt(pactPaymentValue) || 0 : 0,
      pactPaymentBuildingKeys: offerType === 'NON_AGGRESSION' && includePayment && pactPaymentResource === 'COMPLETED_BUILDING' ? pactPaymentBuildingKeys : []
    };

    try {
      const updatedData = await createCooperationOffer(turnData.gameId, payload);
      onActionComplete(updatedData);
      
      const newOffers = updatedData.cooperationOffers || [];
      const created = newOffers[newOffers.length - 1];
      
      if (created && recipientParty?.controllerType === 'COMPUTER') {
        if (created.status === 'ACCEPTED') {
          setFeedback({
            status: 'SUCCESS',
            title: 'Proposal Accepted!',
            message: `✅ ${recipientParty.name} accepted your proposal! The transaction resources have been transferred.`
          });
        } else if (created.status === 'REJECTED') {
          setFeedback({
            status: 'REJECTED',
            title: 'Proposal Rejected',
            message: `❌ ${recipientParty.name} turned down your proposal.`
          });
        }
      } else {
        setFeedback({
          status: 'SUCCESS',
          title: 'Proposal Sent',
          message: `🤝 Your proposal has been sent to ${recipientParty?.name || 'the player'}.`
        });
      }
      
      // Reset fields
      setOfferedCoins(0);
      setOfferedMorale(0);
      setOfferedSupport(0);
      setOfferedMedia(0);
      setLobbyBillKey('');
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

  const handleBribe = async () => {
    if (!selectedFactionKey) {
      setErrorMsg('Please select a faction to target.');
      return;
    }
    if (bribeCoins <= 0) {
      setErrorMsg('Bribe amount must be greater than zero.');
      return;
    }
    if ((activeParty?.stats?.coins || 0) < bribeCoins) {
      setErrorMsg('You do not have enough coins.');
      return;
    }

    setLoading(true);
    setSuccessMsg('');
    setErrorMsg('');

    try {
      const updatedData = await bribeFaction(turnData.gameId, recipientId, selectedFactionKey, bribeCoins);
      onActionComplete(updatedData);

      const commentary = updatedData.lastRoundCommentary || [];
      const latestMsg = commentary[commentary.length - 1] || 'Bribe submitted.';
      
      const isSuccess = latestMsg.includes('Sabotage Successful');
      setFeedback({
        status: isSuccess ? 'BRIBE_SUCCESS' : 'BRIBE_SCANDAL',
        title: isSuccess ? 'Sabotage Successful! 🚨' : 'Bribe Scandal Exposed! 🚨',
        message: latestMsg
      });

      setBribeCoins(0);
      setSelectedFactionKey('');
    } catch (err) {
      setErrorMsg(err.message || 'Failed to submit bribe.');
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
    if (offer.type === 'LOBBYING') {
      const giveParts = [];
      if (offer.offeredCoins > 0) giveParts.push(`${offer.offeredCoins} Coins`);
      if (offer.offeredMorale > 0) giveParts.push(`${offer.offeredMorale} Morale`);
      if (offer.offeredMedia > 0) giveParts.push(`${offer.offeredMedia} Media Image`);
      if (offer.offeredBuildingKeys && offer.offeredBuildingKeys.length > 0) {
        const names = offer.offeredBuildingKeys.map(k => PROJECT_DEFS[k]?.name || k).join(', ');
        giveParts.push(`Buildings [${names}]`);
      }
      return `Lobbying: GIVES {${giveParts.join(', ') || 'Nothing'}} in exchange for Pledging to vote YES on Bill '${getBillName(offer.lobbyBillKey)}'`;
    }
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
      if (offer.offeredCoins > 0) giveParts.push(`${offer.offeredCoins} Coins`);
      if (offer.offeredMorale > 0) giveParts.push(`${offer.offeredMorale} Morale`);
      if (offer.offeredSupport > 0) giveParts.push(`${offer.offeredSupport}% Support`);
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
    <div style={{ display: 'flex', flexDirection: 'column', gap: '25px', color: '#0f172a' }}>
      
      {/* Custom Modal Feedback Banner */}
      {feedback && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(15, 23, 42, 0.75)',
          backdropFilter: 'blur(6px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 9999,
          padding: '20px'
        }}>
          <div style={{
            backgroundColor: '#ffffff',
            border: '1.5px solid var(--primary-border)',
            borderRadius: '16px',
            padding: '30px',
            maxWidth: '460px',
            width: '100%',
            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
            textAlign: 'center'
          }}>
            <div style={{ fontSize: '48px', marginBottom: '15px' }}>
              {(feedback.status === 'SUCCESS' || feedback.status === 'BRIBE_SUCCESS') ? '✅' : '❌'}
            </div>
            <h3 style={{ margin: '0 0 10px 0', color: 'var(--primary-dark)', fontSize: '20px', fontWeight: 'bold' }}>
              {feedback.title}
            </h3>
            <p style={{ margin: '0 0 25px 0', color: '#475569', fontSize: '14px', lineHeight: '1.6' }}>
              {feedback.message}
            </p>
            <button
              onClick={() => setFeedback(null)}
              style={{
                width: '100%',
                padding: '12px',
                background: 'var(--primary-dark)',
                color: '#fff',
                border: 'none',
                borderRadius: '8px',
                fontSize: '14px',
                fontWeight: 'bold',
                cursor: 'pointer',
                transition: 'all 0.15s'
              }}
            >
              Understood
            </button>
          </div>
        </div>
      )}

      {/* 1. Active Non-Aggression Treaties - Shown ONLY if there are active pacts */}
      {myPacts.length > 0 && (
        <div style={{ border: '1px solid var(--primary-border)', borderRadius: '12px', padding: '16px', background: '#ffffff', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05)' }}>
          <h4 style={{ margin: '0 0 12px 0', fontSize: '14px', color: 'var(--primary-dark)', display: 'flex', alignItems: 'center', gap: '6px', fontWeight: 'bold' }}>
            🕊️ Active Non-Aggression Treaties
          </h4>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {myPacts.map(p => {
              const partner = p.partyAId === activePartyId ? p.partyBName : p.partyAName;
              return (
                <div key={p.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'rgba(34,197,94,0.06)', border: '1px solid #22c55e', padding: '12px 16px', borderRadius: '8px', fontSize: '13px', fontWeight: 'bold', color: '#166534' }}>
                  <span>🤝 Treaty Pact with {partner}</span>
                  <span style={{ fontSize: '11px', background: '#22c55e', color: '#fff', padding: '3px 10px', borderRadius: '12px' }}>
                    ⏳ {p.turnsRemaining} Months Left
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* 2. Incoming Proposals - Shown ONLY if there are incoming offers */}
      {incomingOffers.length > 0 && (
        <div style={{ border: '1px solid var(--primary-border)', borderRadius: '12px', padding: '16px', background: '#ffffff', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05)' }}>
          <h4 style={{ margin: '0 0 12px 0', fontSize: '14px', color: 'var(--primary-dark)', display: 'flex', alignItems: 'center', gap: '6px', fontWeight: 'bold' }}>
            📥 Incoming Diplomatic Proposals
          </h4>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {incomingOffers.map(o => (
              <div key={o.id} style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '12px', background: 'rgba(0,0,0,0.015)' }}>
                <div style={{ fontSize: '11px', color: '#64748b', fontWeight: 'bold', textTransform: 'uppercase' }}>From: {o.senderPartyName}</div>
                <div style={{ fontSize: '13px', fontWeight: 'semibold', color: '#1e293b', marginTop: '6px', lineHeight: '1.4' }}>
                  {getResourceString(o)}
                </div>
                <div style={{ display: 'flex', gap: '10px', marginTop: '12px' }}>
                  <button
                    disabled={loading}
                    onClick={() => handleRespond(o.id, true)}
                    style={{ flex: 1, padding: '8px 16px', fontSize: '12px', fontWeight: 'bold', background: '#22c55e', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', transition: 'all 0.15s' }}
                  >
                    Accept Offer
                  </button>
                  <button
                    disabled={loading}
                    onClick={() => handleRespond(o.id, false)}
                    style={{ flex: 1, padding: '8px 16px', fontSize: '12px', fontWeight: 'bold', background: '#e11d48', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', transition: 'all 0.15s' }}
                  >
                    Reject Offer
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* 3. Accepted Lobbying Agreements - Shown ONLY if there are accepted lobby deals */}
      {acceptedLobbyAgreements.length > 0 && (
        <div style={{ border: '1px solid var(--primary-border)', borderRadius: '12px', padding: '16px', background: '#ffffff', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05)' }}>
          <h4 style={{ margin: '0 0 12px 0', fontSize: '14px', color: 'var(--primary-dark)', display: 'flex', alignItems: 'center', gap: '6px', fontWeight: 'bold' }}>
            🗳️ Accepted Lobbying Agreements
          </h4>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {acceptedLobbyAgreements.map(o => {
              const partner = o.senderPartyId === activePartyId ? o.recipientPartyName : o.senderPartyName;
              return (
                <div key={o.id} style={{ border: '1px solid #3b82f6', borderRadius: '8px', padding: '12px', background: 'rgba(59,130,246,0.04)', fontSize: '12.5px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontWeight: 'bold', color: '#1d4ed8' }}>
                    <span>🗳️ Bill Lobbying Pact</span>
                    <span>Active Pledge</span>
                  </div>
                  <div style={{ marginTop: '6px', color: '#334155' }}>
                    {o.senderPartyId === activePartyId ? (
                      <span>Lobbied <strong>{partner}</strong> to vote <strong>YES</strong> on Bill <strong>{getBillName(o.lobbyBillKey)}</strong>.</span>
                    ) : (
                      <span>We are lobbied by <strong>{partner}</strong> to vote <strong>YES</strong> on Bill <strong>{getBillName(o.lobbyBillKey)}</strong>.</span>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* 4. Treaty & Exchange Workshop Section */}
      <div style={{ border: '1px solid var(--primary-border)', borderRadius: '12px', padding: '20px', background: '#ffffff', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05)' }}>
        <h4 style={{ margin: '0 0 15px 0', fontSize: '16px', color: 'var(--primary-dark)', display: 'flex', alignItems: 'center', gap: '6px', fontWeight: 'bold' }}>
          🏛️ Treaty & Exchange Workshop
        </h4>

        {/* Step A: Choose Partner */}
        <div style={{ marginBottom: '20px' }}>
          <label htmlFor="partner-select" style={{ fontSize: '12px', fontWeight: 'bold', display: 'block', marginBottom: '6px', color: '#475569' }}>
            Select Partner:
          </label>
          <select
            id="partner-select"
            value={recipientId}
            onChange={(e) => setRecipientId(e.target.value)}
            style={{ width: '100%', padding: '10px 12px', fontSize: '14px', borderRadius: '8px', background: '#fff', color: '#0f172a', border: '1.5px solid var(--primary-border)', fontWeight: '500' }}
          >
            <option value="">-- Choose a Rival Party to Negotiate With --</option>
            {otherParties.map(p => (
              <option key={p.id} value={p.id}>{p.name} ({p.role})</option>
            ))}
          </select>
        </div>

        {/* Blank state block forcing user to select partner */}
        {!recipientId ? (
          <div style={{
            border: '2px dashed var(--primary-border)',
            borderRadius: '12px',
            padding: '40px 20px',
            textAlign: 'center',
            background: 'rgba(101,148,177,0.02)',
            color: '#64748b'
          }}>
            <span style={{ fontSize: '32px', display: 'block', marginBottom: '10px' }}>🏛️</span>
            <strong style={{ display: 'block', fontSize: '14px', color: 'var(--primary-dark)' }}>
              No negotiation partner selected
            </strong>
            <span style={{ fontSize: '13px' }}>
              Please select a rival party from the dropdown above to initiate negotiations.
            </span>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px', animation: 'fadeIn 0.25s ease-out' }}>
            
            {/* Step B: Type Selection Tabs */}
            <div>
              <span style={{ fontSize: '12px', fontWeight: 'bold', display: 'block', marginBottom: '8px', color: '#475569' }}>Proposal Category:</span>
              <div style={{ display: 'flex', gap: '8px' }}>
                <button
                  type="button"
                  onClick={() => setOfferType('EXCHANGE')}
                  style={{
                    flex: 1,
                    padding: '10px 14px',
                    fontSize: '13px',
                    fontWeight: 'bold',
                    borderRadius: '8px',
                    border: `1.5px solid ${offerType === 'EXCHANGE' ? 'var(--primary-dark)' : 'var(--primary-border)'}`,
                    background: offerType === 'EXCHANGE' ? 'rgba(33,60,81,0.08)' : '#ffffff',
                    color: offerType === 'EXCHANGE' ? 'var(--primary-dark)' : '#475569',
                    cursor: 'pointer',
                    transition: 'all 0.15s'
                  }}
                >
                  💱 Assets Exchange
                </button>
                <button
                  type="button"
                  onClick={() => setOfferType('LOBBYING')}
                  style={{
                    flex: 1,
                    padding: '10px 14px',
                    fontSize: '13px',
                    fontWeight: 'bold',
                    borderRadius: '8px',
                    border: `1.5px solid ${offerType === 'LOBBYING' ? 'var(--primary-dark)' : 'var(--primary-border)'}`,
                    background: offerType === 'LOBBYING' ? 'rgba(33,60,81,0.08)' : '#ffffff',
                    color: offerType === 'LOBBYING' ? 'var(--primary-dark)' : '#475569',
                    cursor: 'pointer',
                    transition: 'all 0.15s'
                  }}
                >
                  🗳️ Bill Lobbying
                </button>
                <button
                  type="button"
                  onClick={() => setOfferType('NON_AGGRESSION')}
                  style={{
                    flex: 1,
                    padding: '10px 14px',
                    fontSize: '13px',
                    fontWeight: 'bold',
                    borderRadius: '8px',
                    border: `1.5px solid ${offerType === 'NON_AGGRESSION' ? 'var(--primary-dark)' : 'var(--primary-border)'}`,
                    background: offerType === 'NON_AGGRESSION' ? 'rgba(33,60,81,0.08)' : '#ffffff',
                    color: offerType === 'NON_AGGRESSION' ? 'var(--primary-dark)' : '#475569',
                    cursor: 'pointer',
                    transition: 'all 0.15s'
                  }}
                >
                  🕊️ Non-Aggression Pact
                </button>
                <button
                  type="button"
                  onClick={() => setOfferType('SABOTAGE')}
                  style={{
                    flex: 1,
                    padding: '10px 14px',
                    fontSize: '13px',
                    fontWeight: 'bold',
                    borderRadius: '8px',
                    border: `1.5px solid ${offerType === 'SABOTAGE' ? 'var(--primary-dark)' : 'var(--primary-border)'}`,
                    background: offerType === 'SABOTAGE' ? 'rgba(33,60,81,0.08)' : '#ffffff',
                    color: offerType === 'SABOTAGE' ? 'var(--primary-dark)' : '#475569',
                    cursor: 'pointer',
                    transition: 'all 0.15s'
                  }}
                >
                  ⚡ Sabotage Faction
                </button>
              </div>
            </div>

            {/* Split layout Workshop Board */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '20px' }}>
              
              {/* EXCHANGE split columns */}
              {offerType === 'EXCHANGE' && (
                <>
                  {/* Left Column: Give */}
                  <div style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '16px', background: '#f8fafc' }}>
                    <h5 style={{ margin: '0 0 12px 0', fontSize: '13px', color: '#166534', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '4px' }}>
                      🎁 What You Offer (Give)
                    </h5>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                      <div style={{ display: 'flex', gap: '10px' }}>
                        <div style={{ flex: 1 }}>
                          <label htmlFor="give-coins" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: '#64748b' }}>Coins:</label>
                          <input id="give-coins" type="number" min="0" value={offeredCoins} onChange={(e) => setOfferedCoins(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '6px', fontSize: '13px', borderRadius: '6px', border: '1px solid var(--primary-border)' }} />
                        </div>
                        <div style={{ flex: 1 }}>
                          <label htmlFor="give-morale" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: '#64748b' }}>Morale:</label>
                          <input id="give-morale" type="number" min="0" value={offeredMorale} onChange={(e) => setOfferedMorale(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '6px', fontSize: '13px', borderRadius: '6px', border: '1px solid var(--primary-border)' }} />
                        </div>
                        <div style={{ flex: 1 }}>
                          <label htmlFor="give-support" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: '#64748b' }}>Support %:</label>
                          <input id="give-support" type="number" min="0" max="100" value={offeredSupport} onChange={(e) => setOfferedSupport(Math.min(100, Math.max(0, parseInt(e.target.value) || 0)))} style={{ width: '100%', padding: '6px', fontSize: '13px', borderRadius: '6px', border: '1px solid var(--primary-border)' }} />
                        </div>
                      </div>

                      {myCompletedProjects.length > 0 && (
                        <div style={{ marginTop: '5px' }}>
                          <span style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '4px', color: '#64748b' }}>Completed Buildings:</span>
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', maxHeight: '120px', overflowY: 'auto', padding: '8px', border: '1px solid var(--primary-border)', borderRadius: '6px', background: '#fff' }}>
                            {myCompletedProjects.map(proj => {
                              const pDef = PROJECT_DEFS[proj.projectKey] || {};
                              return (
                                <label key={proj.id} style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px', cursor: 'pointer' }}>
                                  <input type="checkbox" checked={offeredBuildingKeys.includes(proj.projectKey)} onChange={() => toggleBuildingSelection(proj.projectKey, 'OFFER')} />
                                  🏗️ {pDef.name || proj.projectKey}
                                </label>
                              );
                            })}
                          </div>
                        </div>
                      )}
                    </div>
                  </div>

                  {/* Right Column: Take */}
                  <div style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '16px', background: '#f8fafc' }}>
                    <h5 style={{ margin: '0 0 12px 0', fontSize: '13px', color: '#9f1239', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '4px' }}>
                      🤲 What You Request (Take)
                    </h5>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                      <div style={{ display: 'flex', gap: '10px' }}>
                        <div style={{ flex: 1 }}>
                          <label htmlFor="req-coins" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: '#64748b' }}>Coins:</label>
                          <input id="req-coins" type="number" min="0" value={requestedCoins} onChange={(e) => setRequestedCoins(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '6px', fontSize: '13px', borderRadius: '6px', border: '1px solid var(--primary-border)' }} />
                        </div>
                        <div style={{ flex: 1 }}>
                          <label htmlFor="req-morale" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: '#64748b' }}>Morale:</label>
                          <input id="req-morale" type="number" min="0" value={requestedMorale} onChange={(e) => setRequestedMorale(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '6px', fontSize: '13px', borderRadius: '6px', border: '1px solid var(--primary-border)' }} />
                        </div>
                        <div style={{ flex: 1 }}>
                          <label htmlFor="req-support" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: '#64748b' }}>Support %:</label>
                          <input id="req-support" type="number" min="0" max="100" value={requestedSupport} onChange={(e) => setRequestedSupport(Math.min(100, Math.max(0, parseInt(e.target.value) || 0)))} style={{ width: '100%', padding: '6px', fontSize: '13px', borderRadius: '6px', border: '1px solid var(--primary-border)' }} />
                        </div>
                      </div>
                      <p style={{ margin: 0, fontSize: '11px', color: '#64748b', fontStyle: 'italic', marginTop: '10px' }}>
                        * Note: Computer players will analyze the net resource value to accept/reject asset exchange proposals.
                      </p>
                    </div>
                  </div>
                </>
              )}

              {/* LOBBYING split columns */}
              {offerType === 'LOBBYING' && (
                <>
                  {/* Left Column: Select Bill & Offer */}
                  <div style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '16px', background: '#f8fafc' }}>
                    <h5 style={{ margin: '0 0 12px 0', fontSize: '13px', color: '#1d4ed8', fontWeight: 'bold' }}>
                      🗳️ Select Bill & Offered Compensation
                    </h5>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                      <div>
                        <label htmlFor="lobby-bill-select" style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '4px', color: '#64748b' }}>
                          Choose sponsored bill (Your Role: {myRole}, Bills: {targetBillRole}):
                        </label>
                        <select
                          id="lobby-bill-select"
                          value={lobbyBillKey}
                          onChange={(e) => setLobbyBillKey(e.target.value)}
                          style={{ width: '100%', padding: '8px', fontSize: '13px', borderRadius: '6px', background: '#fff', color: '#0f172a', border: '1px solid var(--primary-border)' }}
                        >
                          <option value="">-- Choose a Bill --</option>
                          {myRoleBills.map(b => (
                            <option key={b.billKey} value={b.billKey}>{b.name} ({b.billKey})</option>
                          ))}
                        </select>
                        {myRoleBills.length === 0 && (
                          <p style={{ margin: '4px 0 0 0', fontSize: '11px', color: '#e11d48' }}>
                            You have no bills of role type {targetBillRole} available to lobby for.
                          </p>
                        )}
                      </div>

                      <div style={{ display: 'flex', gap: '8px' }}>
                        <div style={{ flex: 1 }}>
                          <label htmlFor="lobby-coins" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: '#64748b' }}>Coins:</label>
                          <input id="lobby-coins" type="number" min="0" value={offeredCoins} onChange={(e) => setOfferedCoins(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '5px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }} />
                        </div>
                        <div style={{ flex: 1 }}>
                          <label htmlFor="lobby-morale" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: '#64748b' }}>Morale:</label>
                          <input id="lobby-morale" type="number" min="0" value={offeredMorale} onChange={(e) => setOfferedMorale(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '5px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }} />
                        </div>
                        <div style={{ flex: 1 }}>
                          <label htmlFor="lobby-media" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: '#64748b' }}>Media:</label>
                          <input id="lobby-media" type="number" min="0" value={offeredMedia} onChange={(e) => setOfferedMedia(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '5px', fontSize: '12px', borderRadius: '4px', border: '1px solid var(--primary-border)' }} />
                        </div>
                      </div>

                      {myCompletedProjects.length > 0 && (
                        <div>
                          <span style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '4px', color: '#64748b' }}>Buildings:</span>
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '5px', maxHeight: '100px', overflowY: 'auto', padding: '6px', border: '1px solid var(--primary-border)', borderRadius: '4px', background: '#fff' }}>
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
                  </div>

                  {/* Right Column: Vote Pledge Payout preview */}
                  <div style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '16px', background: '#f8fafc', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                    <div>
                      <h5 style={{ margin: '0 0 12px 0', fontSize: '13px', color: '#1d4ed8', fontWeight: 'bold' }}>
                        🤝 Binding Vote Agreement
                      </h5>
                      <p style={{ fontSize: '12.5px', color: '#334155', lineHeight: '1.5' }}>
                        In exchange for your offered assets, <strong>{recipientParty?.name}</strong> will commit to vote <strong>YES</strong> on this bill during the Legislative Session resolution.
                      </p>
                    </div>
                    <div style={{ background: '#eff6ff', border: '1px solid #bfdbfe', borderRadius: '8px', padding: '12px', marginTop: '12px' }}>
                      <span style={{ display: 'block', fontSize: '11px', color: '#1e3a8a', fontWeight: 'bold', textTransform: 'uppercase' }}>Vote Pledge Status:</span>
                      <strong style={{ fontSize: '14px', color: '#1d4ed8' }}>
                        {lobbyBillKey ? `Binding YES pledge for '${getBillName(lobbyBillKey)}'` : 'Please choose a bill'}
                      </strong>
                    </div>
                  </div>
                </>
              )}

              {/* NON_AGGRESSION split columns */}
              {offerType === 'NON_AGGRESSION' && (
                <>
                  {/* Left Column: Pact Duration */}
                  <div style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '16px', background: '#f8fafc' }}>
                    <h5 style={{ margin: '0 0 12px 0', fontSize: '13px', color: 'var(--primary-dark)', fontWeight: 'bold' }}>
                      🕊️ Pact Parameters
                    </h5>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                      <div>
                        <label htmlFor="duration-select" style={{ fontSize: '11px', display: 'block', marginBottom: '4px', color: '#64748b' }}>Pact Duration:</label>
                        <select id="duration-select" value={durationTurns} onChange={(e) => setDurationTurns(parseInt(e.target.value))} style={{ width: '100%', padding: '8px', fontSize: '13px', borderRadius: '6px', background: '#fff', color: '#000', border: '1px solid var(--primary-border)', fontWeight: '500' }}>
                          <option value={5}>5 Months (Short Treaty)</option>
                          <option value={10}>10 Months (Standard Treaty)</option>
                          <option value={15}>15 Months (Long-Term Pact)</option>
                        </select>
                      </div>
                      <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '12px', fontWeight: 'bold', cursor: 'pointer', marginTop: '5px' }}>
                        <input type="checkbox" checked={includePayment} onChange={(e) => setIncludePayment(e.target.checked)} />
                        Include Payment / Compensation
                      </label>
                    </div>
                  </div>

                  {/* Right Column: Payments */}
                  <div style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '16px', background: '#f8fafc' }}>
                    <h5 style={{ margin: '0 0 12px 0', fontSize: '13px', color: 'var(--primary-dark)', fontWeight: 'bold' }}>
                      💸 Compensation Details
                    </h5>
                    {!includePayment ? (
                      <p style={{ margin: 0, fontSize: '12px', color: '#64748b', fontStyle: 'italic' }}>
                        No financial payments or trades are tied to this Non-Aggression treaty.
                      </p>
                    ) : (
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', animation: 'fadeIn 0.2s' }}>
                        <div>
                          <span style={{ fontSize: '11px', display: 'block', marginBottom: '4px', color: '#64748b' }}>Payment Direction:</span>
                          <div style={{ display: 'flex', gap: '15px' }}>
                            <label style={{ fontSize: '12.5px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer' }}>
                              <input type="radio" checked={senderPaysPact} onChange={() => setSenderPaysPact(true)} />
                              We Pay Them
                            </label>
                            <label style={{ fontSize: '12.5px', display: 'flex', alignItems: 'center', gap: '4px', cursor: 'pointer' }}>
                              <input type="radio" checked={!senderPaysPact} onChange={() => setSenderPaysPact(false)} />
                              They Pay Us
                            </label>
                          </div>
                        </div>

                        <div>
                          <label htmlFor="payment-asset" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: '#64748b' }}>Asset Type:</label>
                          <select id="payment-asset" value={pactPaymentResource} onChange={(e) => setPactPaymentResource(e.target.value)} style={{ width: '100%', padding: '6px', fontSize: '12.5px', borderRadius: '6px', background: '#fff', color: '#000', border: '1px solid var(--primary-border)' }}>
                            <option value="COINS">Coins</option>
                            <option value="MORALE">Morale</option>
                            <option value="SUPPORT">Public Support %</option>
                            <option value="COMPLETED_BUILDING">Completed Buildings</option>
                          </select>
                        </div>

                        {pactPaymentResource !== 'COMPLETED_BUILDING' ? (
                          <div>
                            <label htmlFor="payment-val" style={{ fontSize: '11px', display: 'block', marginBottom: '2px', color: '#64748b' }}>Amount:</label>
                            <input id="payment-val" type="number" min="0" value={pactPaymentValue} onChange={(e) => setPactPaymentValue(Math.max(0, parseInt(e.target.value) || 0))} style={{ width: '100%', padding: '6px', fontSize: '13px', borderRadius: '6px', border: '1px solid var(--primary-border)' }} />
                          </div>
                        ) : (
                          <div>
                            <span style={{ fontSize: '11px', display: 'block', marginBottom: '4px', color: '#64748b' }}>Choose Completed Buildings:</span>
                            {senderPaysPact ? (
                              myCompletedProjects.length === 0 ? (
                                <p style={{ margin: 0, fontSize: '11px', color: '#e11d48', fontStyle: 'italic' }}>You own no completed buildings.</p>
                              ) : (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: '5px', maxHeight: '100px', overflowY: 'auto', padding: '6px', border: '1px solid var(--primary-border)', borderRadius: '6px', background: '#fff' }}>
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
                              targetCompletedProjects.length === 0 ? (
                                <p style={{ margin: 0, fontSize: '11px', color: '#e11d48', fontStyle: 'italic' }}>{recipientParty?.name} owns no completed buildings.</p>
                              ) : (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: '5px', maxHeight: '100px', overflowY: 'auto', padding: '6px', border: '1px solid var(--primary-border)', borderRadius: '6px', background: '#fff' }}>
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
                  </>
              )}

              {/* SABOTAGE split columns */}
              {offerType === 'SABOTAGE' && (() => {
                const selectedFaction = targetFactions.find(f => f.key === selectedFactionKey);
                const targetFactionProjects = (recipientParty?.projects || []).filter(
                  p => p.progressPercent === 100 && p.managingFactionKey === selectedFactionKey
                );

                return (
                  <>
                    {/* Left Column: Select & Info */}
                    <div style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '16px', background: '#f8fafc' }}>
                      <h5 style={{ margin: '0 0 12px 0', fontSize: '13px', color: '#9f1239', fontWeight: 'bold' }}>
                        ⚡ Target Faction Details
                      </h5>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                        <div>
                          <label htmlFor="faction-target-select" style={{ fontSize: '11px', display: 'block', marginBottom: '4px', color: '#64748b' }}>Select Target Faction:</label>
                          <select
                            id="faction-target-select"
                            value={selectedFactionKey}
                            onChange={(e) => setSelectedFactionKey(e.target.value)}
                            style={{ width: '100%', padding: '8px', fontSize: '13px', borderRadius: '6px', background: '#fff', color: '#000', border: '1px solid var(--primary-border)', fontWeight: '500' }}
                          >
                            <option value="">-- Select Faction --</option>
                            {targetFactions.map(f => (
                              <option key={f.key} value={f.key}>{f.name} (Loyalty: {f.loyalty}% | Power: {f.influence}%)</option>
                            ))}
                          </select>
                        </div>

                        {selectedFaction && (
                          <div style={{ background: '#fff', border: '1px solid var(--primary-border)', borderRadius: '6px', padding: '10px', fontSize: '12px', color: '#334155' }}>
                            <div style={{ marginBottom: '6px' }}><strong>Loyalty:</strong> {selectedFaction.loyalty}%</div>
                            <div style={{ marginBottom: '6px' }}><strong>Power (Influence):</strong> {selectedFaction.influence}%</div>
                            <div style={{ marginBottom: '6px' }}>
                              <strong>Assigned Posts:</strong> {selectedFaction.post && selectedFaction.post.length > 0 ? selectedFaction.post.map(p => {
                                const remainingTurns = selectedFaction.frozenPosts && selectedFaction.frozenPosts[p];
                                return remainingTurns > 0 ? `${p} (❄️ Frozen: ${remainingTurns}t)` : p;
                              }).join(', ') : 'None'}
                            </div>
                            <div style={{ marginBottom: '6px' }}>
                              <strong>Patronage Points:</strong> {selectedFaction.patronage || 0}
                              {selectedFaction.frozenPatronageTurns && selectedFaction.frozenPatronageTurns.length > 0 && (
                                <span style={{ color: '#ef4444', fontWeight: 'bold' }}> (❄️ {selectedFaction.frozenPatronageTurns.length} Frozen)</span>
                              )}
                            </div>
                            <div>
                              <strong>Allocated Projects:</strong> {targetFactionProjects.length > 0 ? targetFactionProjects.map(p => {
                                return p.frozenTurnsRemaining > 0 ? `${p.name || p.projectKey} (❄️ Frozen: ${p.frozenTurnsRemaining}t)` : (p.name || p.projectKey);
                              }).join(', ') : 'None'}
                            </div>
                          </div>
                        )}
                      </div>
                    </div>

                    {/* Right Column: Bribe Input */}
                    <div style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '16px', background: '#f8fafc' }}>
                      <h5 style={{ margin: '0 0 12px 0', fontSize: '13px', color: '#1d4ed8', fontWeight: 'bold' }}>
                        💰 Bribe Sabotage Fund
                      </h5>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                        <p style={{ margin: 0, fontSize: '12px', color: '#64748b', lineHeight: '1.4' }}>
                          Offer a cash bribe to convince this faction to work against their party leadership. 
                          If successful, their loyalty will drop significantly and all their assets (posts, projects, and patronage points) will be <strong>FROZEN for 10 rounds</strong>, denying them recurring passive yields.
                        </p>
                        <div>
                          <label htmlFor="bribe-fund-input" style={{ fontSize: '11px', display: 'block', marginBottom: '4px', color: '#64748b' }}>Bribe Coins:</label>
                          <input
                            id="bribe-fund-input"
                            type="number"
                            min="0"
                            value={bribeCoins}
                            onChange={(e) => setBribeCoins(Math.max(0, parseInt(e.target.value) || 0))}
                            style={{ width: '100%', padding: '8px', fontSize: '13px', borderRadius: '6px', border: '1px solid var(--primary-border)' }}
                          />
                          <span style={{ fontSize: '11px', color: '#64748b', marginTop: '4px', display: 'block' }}>
                            Your Coins Reserves: <strong>{activeParty?.stats?.coins || 0}</strong> | Target Party Coins: <strong>{recipientParty?.stats?.coins || 0}</strong>
                          </span>
                        </div>
                      </div>
                    </div>
                  </>
                );
              })()}
            </div>

            {/* Error alerts inside Workshop container */}
            {errorMsg && (
              <div style={{ background: 'rgba(225,29,72,0.08)', color: '#9f1239', border: '1.5px solid #e11d48', padding: '10px 15px', borderRadius: '8px', fontSize: '12.5px', fontWeight: 'bold' }}>
                ⚠️ {errorMsg}
              </div>
            )}

            {/* Proposal submit button */}
            <button
              type="button"
              onClick={offerType === 'SABOTAGE' ? handleBribe : handlePropose}
              disabled={loading || !recipientId || (offerType === 'LOBBYING' && !lobbyBillKey) || (offerType === 'SABOTAGE' && (!selectedFactionKey || bribeCoins <= 0))}
              style={{
                width: '100%',
                padding: '12px 24px',
                fontSize: '14px',
                fontWeight: 'bold',
                background: offerType === 'SABOTAGE' ? '#e11d48' : 'var(--primary-dark)',
                color: '#ffffff',
                border: 'none',
                borderRadius: '8px',
                cursor: 'pointer',
                opacity: (loading || !recipientId || (offerType === 'LOBBYING' && !lobbyBillKey) || (offerType === 'SABOTAGE' && (!selectedFactionKey || bribeCoins <= 0))) ? 0.6 : 1,
                boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)',
                transition: 'all 0.15s'
              }}
            >
              {loading ? '⏳ Processing...' : offerType === 'SABOTAGE' ? '⚡ Submit Sabotage / Bribe' : '🤝 Submit Diplomatic Proposal'}
            </button>

          </div>
        )}
      </div>
    </div>
  );
}
