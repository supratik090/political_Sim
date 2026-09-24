import React, { useState, useEffect } from 'react';
import { createCooperationOffer, respondToCooperationOffer, bribeFaction, fetchBillsForGameplay } from '../../../api/apiClient';

/**
 * WR_Action7_Cooperation — Diplomatic Cooperation (War Room Aesthetic)
 * Plays with playing-card style party buttons, counter chips, and dark tactical styling.
 */
export default function WR_Action7_Cooperation({ turnData, projectDefs: PROJECT_DEFS = {}, onActionComplete }) {
  const activePartyId = turnData?.activeHumanPartyId;
  const activeParty = turnData?.parties?.find(p => p.id === activePartyId);
  const otherParties = (turnData?.parties || []).filter(p => p.id !== activePartyId);

  // Form State
  const [recipientId, setRecipientId] = useState('');
  const [offerType, setOfferType] = useState('EXCHANGE');

  // Lobbying
  const [scenarioBills, setScenarioBills] = useState([]);
  const [lobbyBillKey, setLobbyBillKey] = useState('');
  const [offeredMedia, setOfferedMedia] = useState(0);

  useEffect(() => {
    if (turnData?.scenarioKey) {
      fetchBillsForGameplay(turnData.scenarioKey)
        .then(data => setScenarioBills(data || []))
        .catch(err => console.error("Failed to load scenario bills:", err));
    }
  }, [turnData?.scenarioKey]);

  // Exchange
  const [offeredCoins, setOfferedCoins] = useState(0);
  const [offeredMorale, setOfferedMorale] = useState(0);
  const [offeredSupport, setOfferedSupport] = useState(0);
  const [offeredBuildingKeys, setOfferedBuildingKeys] = useState([]);

  const [requestedCoins, setRequestedCoins] = useState(0);
  const [requestedSupport, setRequestedSupport] = useState(0);
  const [requestedMorale, setRequestedMorale] = useState(0);

  // Non-Aggression
  const [durationTurns, setDurationTurns] = useState(10);
  const [includePayment, setIncludePayment] = useState(false);
  const [senderPaysPact, setSenderPaysPact] = useState(true);
  const [pactPaymentResource, setPactPaymentResource] = useState('COINS');
  const [pactPaymentValue, setPactPaymentValue] = useState(0);
  const [pactPaymentBuildingKeys, setPactPaymentBuildingKeys] = useState([]);

  // Sabotage / Bribe
  const [selectedFactionKey, setSelectedFactionKey] = useState('');
  const [bribeCoins, setBribeCoins] = useState(0);

  // Status & Modals
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');
  const [feedback, setFeedback] = useState(null);
  const [showPartnerModal, setShowPartnerModal] = useState(false);

  const recipientParty = turnData?.parties?.find(p => p.id === recipientId);
  const targetFactions = recipientParty?.factions || [];

  const myPacts = turnData?.activePacts ? turnData.activePacts.filter(p => p.partyAId === activePartyId || p.partyBId === activePartyId) : [];
  const existingPactWithRecipient = myPacts.find(p => 
    ((p.partyAId === activePartyId && p.partyBId === recipientId) || 
     (p.partyAId === recipientId && p.partyBId === activePartyId)) && p.turnsRemaining > 0
  );

  const myCompletedProjects = activeParty?.projects?.filter(p => p.progressPercent >= 100) || [];
  const targetCompletedProjects = recipientParty?.projects?.filter(p => p.progressPercent >= 100) || [];

  useEffect(() => {
    setOfferedBuildingKeys([]);
    setPactPaymentBuildingKeys([]);
    setErrorMsg('');
  }, [recipientId, offerType, includePayment, senderPaysPact]);

  const incomingOffers = turnData?.cooperationOffers ? turnData.cooperationOffers.filter(o => o.recipientPartyId === activePartyId && o.status === 'PENDING') : [];
  const acceptedLobbyAgreements = turnData?.cooperationOffers ? turnData.cooperationOffers.filter(o => o.type === 'LOBBYING' && o.status === 'ACCEPTED' && (o.senderPartyId === activePartyId || o.recipientPartyId === activePartyId)) : [];

  const myRole = activeParty?.role;
  const targetBillRole = myRole === 'GOVERNMENT' ? 'GOVERNMENT' : 'OPPOSITION';
  const myRoleBills = (scenarioBills || []).filter(b => b.proposingRole === targetBillRole);

  const getBillName = (billKey) => {
    const bill = (scenarioBills || []).find(b => b.billKey === billKey);
    return bill ? bill.name : billKey;
  };

  const handleRespond = async (offerId, accept) => {
    setLoading(true);
    setErrorMsg('');
    try {
      const updatedData = await respondToCooperationOffer(turnData.gameId, offerId, accept);
      onActionComplete(updatedData);
      setFeedback({
        status: accept ? 'SUCCESS' : 'REJECTED',
        title: accept ? 'DEAL ACCEPTED' : 'DEAL REJECTED',
        message: `Diplomatic proposal has been ${accept ? 'accepted' : 'rejected'}.`
      });
    } catch (err) {
      setErrorMsg(err.message || 'Failed to respond to offer.');
    } finally {
      setLoading(false);
    }
  };

  const handlePropose = async () => {
    if (offerType === 'NON_AGGRESSION' && existingPactWithRecipient) {
      const msg = `An active Non-Aggression Pact already exists with ${recipientParty?.name || 'this party'} (${existingPactWithRecipient.turnsRemaining} turns remaining).`;
      setErrorMsg(msg);
      setFeedback({
        status: 'REJECTED',
        title: 'PACT ALREADY ACTIVE',
        message: `⚠️ ${msg}`
      });
      return;
    }

    setLoading(true);
    setErrorMsg('');

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
            title: 'PROPOSAL ACCEPTED',
            message: `✅ ${recipientParty.name} accepted your diplomatic terms!`
          });
        } else {
          setFeedback({
            status: 'REJECTED',
            title: 'PROPOSAL REJECTED',
            message: `❌ ${recipientParty.name} declined the proposal.`
          });
        }
      } else {
        setFeedback({
          status: 'SUCCESS',
          title: 'PROPOSAL DISPATCHED',
          message: `🤝 Proposal sent to ${recipientParty?.name || 'rival party'}.`
        });
      }

      setOfferedCoins(0); setOfferedMorale(0); setOfferedSupport(0); setOfferedMedia(0);
      setLobbyBillKey(''); setOfferedBuildingKeys([]); setRequestedCoins(0); setRequestedSupport(0); setRequestedMorale(0);
      setIncludePayment(false); setPactPaymentValue(0); setPactPaymentBuildingKeys([]);
    } catch (err) {
      const msg = err.message || 'Failed to submit proposal.';
      setErrorMsg(msg);
      setFeedback({
        status: 'REJECTED',
        title: 'PROPOSAL FAILED',
        message: `⚠️ ${msg}`
      });
    } finally {
      setLoading(false);
    }
  };

  const handleBribe = async () => {
    if (!selectedFactionKey) return setErrorMsg('Select a target faction.');
    if (bribeCoins <= 0) return setErrorMsg('Enter a valid bribe amount.');
    if ((activeParty?.stats?.coins || 0) < bribeCoins) return setErrorMsg('Insufficient coins.');

    setLoading(true);
    setErrorMsg('');

    try {
      const updatedData = await bribeFaction(turnData.gameId, recipientId, selectedFactionKey, bribeCoins);
      onActionComplete(updatedData);

      const commentary = updatedData.lastRoundCommentary || [];
      const latestMsg = commentary[commentary.length - 1] || 'Bribe processed.';
      const isSuccess = latestMsg.includes('Sabotage Successful');

      setFeedback({
        status: isSuccess ? 'BRIBE_SUCCESS' : 'BRIBE_SCANDAL',
        title: isSuccess ? 'SABOTAGE SUCCESSFUL 🚨' : 'SCANDAL EXPOSED 🚨',
        message: latestMsg
      });

      setBribeCoins(0);
      setSelectedFactionKey('');
    } catch (err) {
      setErrorMsg(err.message || 'Failed to execute bribe.');
    } finally {
      setLoading(false);
    }
  };

  const toggleBuildingSelection = (key, type) => {
    if (type === 'OFFER') {
      setOfferedBuildingKeys(prev => prev.includes(key) ? prev.filter(k => k !== key) : [...prev, key]);
    } else {
      setPactPaymentBuildingKeys(prev => prev.includes(key) ? prev.filter(k => k !== key) : [...prev, key]);
    }
  };

  // Helper for Stepper controls (+ / - buttons)
  const renderCounterControl = (label, value, setter, min = 0, max = 100, step = 5) => (
    <div style={{
      background: 'rgba(255,255,255,0.03)',
      border: '1px solid rgba(255,255,255,0.08)',
      borderRadius: '10px',
      padding: '8px 10px',
      display: 'flex',
      flexDirection: 'column',
      gap: '6px'
    }}>
      <span style={{ fontSize: '11px', color: '#7D8590', fontWeight: 700, textTransform: 'uppercase' }}>{label}</span>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '6px' }}>
        <button
          type="button"
          onClick={() => setter(Math.max(min, value - step))}
          style={{
            width: '32px', height: '32px', borderRadius: '6px',
            background: 'rgba(255,255,255,0.08)', border: '1px solid rgba(255,255,255,0.15)',
            color: '#E6EDF3', fontSize: '14px', fontWeight: 900, cursor: 'pointer',
            touchAction: 'manipulation'
          }}
        >-</button>
        <span style={{ fontSize: '15px', fontWeight: 900, color: '#38BDF8', minWidth: '36px', textAlign: 'center' }}>
          {value}
        </span>
        <button
          type="button"
          onClick={() => setter(Math.min(max, value + step))}
          style={{
            width: '32px', height: '32px', borderRadius: '6px',
            background: 'rgba(255,255,255,0.08)', border: '1px solid rgba(255,255,255,0.15)',
            color: '#E6EDF3', fontSize: '14px', fontWeight: 900, cursor: 'pointer',
            touchAction: 'manipulation'
          }}
        >+</button>
      </div>
    </div>
  );

  useEffect(() => {
    if (feedback) {
      const timer = setTimeout(() => setFeedback(null), 6000);
      return () => clearTimeout(timer);
    }
  }, [feedback]);

  return (
    <div style={{
      padding: '14px 16px',
      color: '#E6EDF3',
      fontFamily: 'Montserrat, system-ui, -apple-system, sans-serif'
    }}>
      {/* Toast Notification Banner (Floating top-right) */}
      {feedback && (
        <div style={{
          position: 'fixed', top: '20px', right: '20px', zIndex: 99999,
          maxWidth: '400px', width: 'calc(100vw - 40px)',
          background: 'linear-gradient(145deg, #1e293b, #0f172a)',
          border: `2px solid ${(feedback.status === 'SUCCESS' || feedback.status === 'BRIBE_SUCCESS') ? '#22c55e' : '#ef4444'}`,
          borderRadius: '16px', padding: '16px 20px',
          boxShadow: `0 16px 36px rgba(0,0,0,0.6), 0 0 20px ${(feedback.status === 'SUCCESS' || feedback.status === 'BRIBE_SUCCESS') ? 'rgba(34,197,94,0.3)' : 'rgba(239,68,68,0.3)'}`,
          display: 'flex', flexDirection: 'column', gap: '10px'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '12px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <span style={{ fontSize: '24px' }}>
                {(feedback.status === 'SUCCESS' || feedback.status === 'BRIBE_SUCCESS') ? '✅' : '❌'}
              </span>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 900, color: '#ffffff', letterSpacing: '0.02em' }}>
                {feedback.title}
              </h3>
            </div>
            <button
              onClick={() => setFeedback(null)}
              style={{
                background: 'rgba(255,255,255,0.1)', border: 'none', color: '#94a3b8',
                width: '26px', height: '26px', borderRadius: '50%', fontSize: '14px',
                fontWeight: 900, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center'
              }}
            >
              ✕
            </button>
          </div>
          <p style={{ margin: 0, fontSize: '13px', color: '#94a3b8', lineHeight: 1.4, paddingLeft: '34px' }}>
            {feedback.message}
          </p>
          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '4px' }}>
            <button
              onClick={() => setFeedback(null)}
              style={{
                padding: '8px 16px', background: '#38BDF8', color: '#0f172a',
                border: 'none', borderRadius: '8px', fontSize: '12px', fontWeight: 900,
                cursor: 'pointer', touchAction: 'manipulation'
              }}
            >
              UNDERSTOOD
            </button>
          </div>
        </div>
      )}

      {/* Header */}
      <div style={{ marginBottom: '16px' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#34D399', display: 'flex', alignItems: 'center', gap: '8px' }}>
          🤝 DIPLOMATIC COOPERATION
        </div>
        <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>
          Form treaties, trade assets, lobby legislation, or bribe rival factions.
        </div>
      </div>

      {/* Active Non-Aggression Treaties */}
      {myPacts.length > 0 && (
        <div style={{ marginBottom: '16px', background: 'rgba(34,197,94,0.06)', border: '1px solid rgba(34,197,94,0.3)', borderRadius: '12px', padding: '14px' }}>
          <div style={{ fontSize: '12px', fontWeight: 800, color: '#4ADE80', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '8px' }}>
            🕊️ ACTIVE TREATIES & PACTS
          </div>
          {myPacts.map(p => {
            const partner = p.partyAId === activePartyId ? p.partyBName : p.partyAName;
            return (
              <div key={p.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 12px', background: 'rgba(0,0,0,0.3)', borderRadius: '8px', fontSize: '12px', fontWeight: 700 }}>
                <span>🤝 Non-Aggression Pact with <strong style={{ color: '#fff' }}>{partner}</strong></span>
                <span style={{ background: '#16a34a', color: '#fff', padding: '2px 8px', borderRadius: '12px', fontSize: '10px' }}>
                  ⏳ {p.turnsRemaining} turns left
                </span>
              </div>
            );
          })}
        </div>
      )}

      {/* Incoming Proposals */}
      {incomingOffers.length > 0 && (
        <div style={{ marginBottom: '16px', background: 'rgba(56,189,248,0.06)', border: '1px solid rgba(56,189,248,0.3)', borderRadius: '12px', padding: '14px' }}>
          <div style={{ fontSize: '12px', fontWeight: 800, color: '#38BDF8', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '8px' }}>
            📥 INCOMING DIPLOMATIC PROPOSALS
          </div>
          {incomingOffers.map(o => (
            <div key={o.id} style={{ background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '10px', padding: '12px', marginBottom: '8px' }}>
              <div style={{ fontSize: '10px', color: '#38BDF8', fontWeight: 800, textTransform: 'uppercase' }}>FROM: {o.senderPartyName}</div>
              <div style={{ fontSize: '12px', color: '#E6EDF3', margin: '6px 0 10px 0', lineHeight: 1.4 }}>
                {o.type === 'NON_AGGRESSION' ? `${o.durationTurns}-Turn Non-Aggression Treaty` : o.type === 'LOBBYING' ? `Lobbying pact for Bill ${o.lobbyBillKey}` : 'Asset Exchange Proposal'}
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px' }}>
                <button disabled={loading} onClick={() => handleRespond(o.id, true)} style={{ background: '#16a34a', color: '#fff', border: 'none', padding: '8px', borderRadius: '6px', fontSize: '12px', fontWeight: 800, cursor: 'pointer', touchAction: 'manipulation' }}>
                  ACCEPT
                </button>
                <button disabled={loading} onClick={() => handleRespond(o.id, false)} style={{ background: '#dc2626', color: '#fff', border: 'none', padding: '8px', borderRadius: '6px', fontSize: '12px', fontWeight: 800, cursor: 'pointer', touchAction: 'manipulation' }}>
                  DECLINE
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* STEP 1: PARTY SELECTOR — PLAYING CARDS AESTHETIC */}
      <div style={{ marginBottom: '16px' }}>
        <div style={{ fontSize: '11px', fontWeight: 800, color: '#7D8590', textTransform: 'uppercase', letterSpacing: '0.06em', marginBottom: '8px' }}>
          1. CHOOSE RIVAL PARTY (PLAYING CARDS)
        </div>

        {/* Playing Card Row */}
        <div style={{
          display: 'flex',
          gap: '10px',
          overflowX: 'auto',
          paddingBottom: '8px',
          WebkitOverflowScrolling: 'touch'
        }}>
          {otherParties.map(p => {
            const isSelected = p.id === recipientId;
            const pColor = p.color || '#38BDF8';
            const roleTag = p.role === 'GOVERNMENT' ? 'GOV' : p.role === 'OPPOSITION' ? 'OPP' : '3RD';
            return (
              <button
                key={p.id}
                type="button"
                onClick={() => setRecipientId(p.id)}
                style={{
                  minWidth: '120px',
                  maxWidth: '145px',
                  flex: '0 0 auto',
                  padding: '12px 10px',
                  borderRadius: '14px',
                  background: isSelected
                    ? `linear-gradient(145deg, ${pColor}25, rgba(15,23,42,0.9))`
                    : 'linear-gradient(145deg, rgba(30,41,59,0.6), rgba(15,23,42,0.8))',
                  border: isSelected ? `2px solid ${pColor}` : '1.5px solid rgba(255,255,255,0.12)',
                  boxShadow: isSelected ? `0 0 16px ${pColor}55` : '0 4px 10px rgba(0,0,0,0.3)',
                  cursor: 'pointer',
                  textAlign: 'left',
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between',
                  touchAction: 'manipulation',
                  transition: 'all 0.15s ease'
                }}
              >
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                    <span style={{ fontSize: '9px', fontWeight: 800, padding: '2px 6px', borderRadius: '4px', background: `${pColor}33`, color: pColor, border: `1px solid ${pColor}55` }}>
                      {roleTag}
                    </span>
                  </div>
                  <div style={{ fontSize: '13px', fontWeight: 900, color: '#ffffff', lineHeight: 1.2, marginBottom: '4px' }}>
                    {p.name}
                  </div>
                </div>

                <div style={{ fontSize: '10px', color: '#94A3B8', borderTop: '1px solid rgba(255,255,255,0.08)', paddingTop: '6px', marginTop: '6px' }}>
                  🏛️ {p.stats?.seats || 0} Seats • {p.stats?.publicSupport || 0}%
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* STEP 2: PROPOSAL CATEGORY CARDS */}
      {recipientId && (
        <div style={{ marginBottom: '16px' }}>
          <div style={{ fontSize: '11px', fontWeight: 800, color: '#7D8590', textTransform: 'uppercase', letterSpacing: '0.06em', marginBottom: '8px' }}>
            2. SELECT PROPOSAL ACTION
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '8px' }}>
            {[
              { id: 'EXCHANGE', label: '💱 Assets Exchange', desc: 'Trade Coins, Morale, Support' },
              { id: 'NON_AGGRESSION', label: '🕊️ Non-Aggression', desc: 'Form Multi-turn Treaty' },
              { id: 'LOBBYING', label: '🗳️ Bill Lobbying', desc: 'Pledge Legislation Votes' },
              { id: 'SABOTAGE', label: '⚡ Sabotage Faction', desc: 'Bribe & Freeze Assets' },
            ].map(cat => {
              const isCatSelected = offerType === cat.id;
              return (
                <button
                  key={cat.id}
                  type="button"
                  onClick={() => setOfferType(cat.id)}
                  style={{
                    padding: '10px 12px',
                    borderRadius: '10px',
                    textAlign: 'left',
                    background: isCatSelected ? 'rgba(56,189,248,0.12)' : 'rgba(255,255,255,0.03)',
                    border: isCatSelected ? '1.5px solid #38BDF8' : '1px solid rgba(255,255,255,0.08)',
                    color: isCatSelected ? '#38BDF8' : '#C9D1D9',
                    cursor: 'pointer',
                    touchAction: 'manipulation',
                    transition: 'all 0.15s ease'
                  }}
                >
                  <div style={{ fontSize: '13px', fontWeight: 900 }}>{cat.label}</div>
                  <div style={{ fontSize: '10px', color: '#7D8590', marginTop: '2px' }}>{cat.desc}</div>
                </button>
              );
            })}
          </div>
        </div>
      )}

      {/* STEP 3: WORKSHOP FORM */}
      {recipientId && (
        <div style={{
          background: 'linear-gradient(145deg, #1e293b, #0f172a)',
          border: '1px solid rgba(255,255,255,0.12)',
          borderRadius: '14px',
          padding: '16px',
          marginBottom: '16px'
        }}>
          {/* EXCHANGE */}
          {offerType === 'EXCHANGE' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              <div>
                <div style={{ fontSize: '12px', fontWeight: 800, color: '#4ADE80', textTransform: 'uppercase', marginBottom: '8px' }}>
                  🎁 WHAT YOU OFFER (GIVE)
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px' }}>
                  {renderCounterControl('Coins', offeredCoins, setOfferedCoins, 0, activeParty?.stats?.coins || 999, 10)}
                  {renderCounterControl('Morale', offeredMorale, setOfferedMorale, 0, 100, 5)}
                  {renderCounterControl('Support %', offeredSupport, setOfferedSupport, 0, 100, 5)}
                </div>
              </div>

              <div>
                <div style={{ fontSize: '12px', fontWeight: 800, color: '#F87171', textTransform: 'uppercase', marginBottom: '8px' }}>
                  🤲 WHAT YOU REQUEST (TAKE)
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px' }}>
                  {renderCounterControl('Coins', requestedCoins, setRequestedCoins, 0, recipientParty?.stats?.coins || 999, 10)}
                  {renderCounterControl('Morale', requestedMorale, setRequestedMorale, 0, 100, 5)}
                  {renderCounterControl('Support %', requestedSupport, setRequestedSupport, 0, 100, 5)}
                </div>
              </div>
            </div>
          )}

          {/* NON-AGGRESSION */}
          {offerType === 'NON_AGGRESSION' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              {existingPactWithRecipient && (
                <div style={{
                  padding: '12px 14px',
                  background: 'rgba(239, 68, 68, 0.12)',
                  border: '1px solid #EF4444',
                  borderRadius: '10px',
                  color: '#F87171',
                  fontSize: '12.5px',
                  fontWeight: 700,
                  lineHeight: 1.4
                }}>
                  ⚠️ Active Non-Aggression Treaty already in effect with {recipientParty?.name} ({existingPactWithRecipient.turnsRemaining} turns remaining). New pacts cannot be entered until the current one expires.
                </div>
              )}
              <div>
                <div style={{ fontSize: '12px', fontWeight: 800, color: '#38BDF8', textTransform: 'uppercase', marginBottom: '8px' }}>
                  🕊️ TREATY DURATION
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px' }}>
                  {[5, 10, 15].map(t => (
                    <button
                      key={t}
                      type="button"
                      onClick={() => setDurationTurns(t)}
                      style={{
                        padding: '10px', borderRadius: '8px',
                        background: durationTurns === t ? '#38BDF8' : 'rgba(255,255,255,0.05)',
                        border: durationTurns === t ? 'none' : '1px solid rgba(255,255,255,0.1)',
                        color: durationTurns === t ? '#0f172a' : '#E6EDF3',
                        fontSize: '12px', fontWeight: 900, cursor: 'pointer', touchAction: 'manipulation'
                      }}
                    >
                      {t} Turns
                    </button>
                  ))}
                </div>
              </div>

              {/* Include Payment Toggle */}
              <div style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '10px', padding: '12px' }}>
                <label style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '12.5px', fontWeight: 800, cursor: 'pointer', color: '#E6EDF3' }}>
                  <input
                    type="checkbox"
                    checked={includePayment}
                    onChange={(e) => setIncludePayment(e.target.checked)}
                    style={{ width: '18px', height: '18px', accentColor: '#38BDF8', cursor: 'pointer' }}
                  />
                  <span>Include Compensation / Financial Payment</span>
                </label>

                {includePayment && (
                  <div style={{ marginTop: '14px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
                    {/* Payment Direction: We Pay Them vs They Pay Us */}
                    <div>
                      <span style={{ fontSize: '11px', color: '#7D8590', fontWeight: 800, textTransform: 'uppercase', display: 'block', marginBottom: '6px' }}>
                        Payment Direction:
                      </span>
                      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px' }}>
                        <button
                          type="button"
                          onClick={() => setSenderPaysPact(true)}
                          style={{
                            padding: '9px 12px', borderRadius: '8px', fontSize: '12px', fontWeight: 900,
                            background: senderPaysPact ? '#16A34A' : 'rgba(255,255,255,0.05)',
                            border: senderPaysPact ? 'none' : '1px solid rgba(255,255,255,0.1)',
                            color: '#ffffff', cursor: 'pointer', touchAction: 'manipulation'
                          }}
                        >
                          📤 We Pay {recipientParty?.name}
                        </button>
                        <button
                          type="button"
                          onClick={() => setSenderPaysPact(false)}
                          style={{
                            padding: '9px 12px', borderRadius: '8px', fontSize: '12px', fontWeight: 900,
                            background: !senderPaysPact ? '#2563EB' : 'rgba(255,255,255,0.05)',
                            border: !senderPaysPact ? 'none' : '1px solid rgba(255,255,255,0.1)',
                            color: '#ffffff', cursor: 'pointer', touchAction: 'manipulation'
                          }}
                        >
                          📥 They Pay Us
                        </button>
                      </div>
                    </div>

                    {/* Asset Type Selector */}
                    <div>
                      <span style={{ fontSize: '11px', color: '#7D8590', fontWeight: 800, textTransform: 'uppercase', display: 'block', marginBottom: '6px' }}>
                        Payment Asset:
                      </span>
                      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '6px' }}>
                        {[
                          { key: 'COINS', label: '💰 Coins' },
                          { key: 'MORALE', label: '⭐ Morale' },
                          { key: 'SUPPORT', label: '📊 Support' },
                          { key: 'COMPLETED_BUILDING', label: '🏗️ Building' }
                        ].map(asset => (
                          <button
                            key={asset.key}
                            type="button"
                            onClick={() => setPactPaymentResource(asset.key)}
                            style={{
                              padding: '8px 4px', borderRadius: '6px', fontSize: '11px', fontWeight: 800,
                              background: pactPaymentResource === asset.key ? '#38BDF8' : 'rgba(255,255,255,0.05)',
                              border: pactPaymentResource === asset.key ? 'none' : '1px solid rgba(255,255,255,0.1)',
                              color: pactPaymentResource === asset.key ? '#0f172a' : '#E6EDF3',
                              cursor: 'pointer', touchAction: 'manipulation'
                            }}
                          >
                            {asset.label}
                          </button>
                        ))}
                      </div>
                    </div>

                    {/* Amount Value Counter or Building Selection */}
                    {pactPaymentResource !== 'COMPLETED_BUILDING' ? (
                      renderCounterControl(
                        `${pactPaymentResource} Amount (${senderPaysPact ? 'We Pay' : 'They Pay'})`,
                        pactPaymentValue,
                        setPactPaymentValue,
                        0,
                        senderPaysPact ? (activeParty?.stats?.coins || 999) : (recipientParty?.stats?.coins || 999),
                        10
                      )
                    ) : (
                      <div>
                        <span style={{ fontSize: '11px', color: '#7D8590', fontWeight: 800, display: 'block', marginBottom: '6px' }}>
                          Select Completed Buildings ({senderPaysPact ? 'We Transfer' : 'They Transfer'}):
                        </span>
                        {(senderPaysPact ? myCompletedProjects : targetCompletedProjects).length === 0 ? (
                          <div style={{ fontSize: '11px', color: '#F87171', fontStyle: 'italic' }}>
                            No completed buildings available to transfer.
                          </div>
                        ) : (
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', maxHeight: '120px', overflowY: 'auto' }}>
                            {(senderPaysPact ? myCompletedProjects : targetCompletedProjects).map(proj => {
                              const pDef = PROJECT_DEFS[proj.projectKey] || {};
                              const isChecked = pactPaymentBuildingKeys.includes(proj.projectKey);
                              return (
                                <label
                                  key={proj.id}
                                  style={{
                                    display: 'flex', alignItems: 'center', gap: '8px', padding: '8px 10px',
                                    borderRadius: '6px', background: isChecked ? 'rgba(56,189,248,0.15)' : 'rgba(255,255,255,0.04)',
                                    border: `1px solid ${isChecked ? '#38BDF8' : 'rgba(255,255,255,0.08)'}`,
                                    fontSize: '12px', cursor: 'pointer'
                                  }}
                                >
                                  <input
                                    type="checkbox"
                                    checked={isChecked}
                                    onChange={() => toggleBuildingSelection(proj.projectKey, 'PACT')}
                                    style={{ accentColor: '#38BDF8' }}
                                  />
                                  <span>🏗️ {pDef.name || proj.projectKey}</span>
                                </label>
                              );
                            })}
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                )}
              </div>
            </div>
          )}

          {/* LOBBYING */}
          {offerType === 'LOBBYING' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              <div>
                <div style={{ fontSize: '12px', fontWeight: 800, color: '#F59E0B', textTransform: 'uppercase', marginBottom: '8px' }}>
                  🗳️ SELECT BILL TO LOBBY
                </div>
                {myRoleBills.length === 0 ? (
                  <div style={{ fontSize: '12px', color: '#EF4444' }}>No bills available for role {targetBillRole}.</div>
                ) : (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', maxHeight: '140px', overflowY: 'auto' }}>
                    {myRoleBills.map(b => {
                      const isSelected = lobbyBillKey === b.billKey;
                      return (
                        <button
                          key={b.billKey}
                          type="button"
                          onClick={() => setLobbyBillKey(b.billKey)}
                          style={{
                            padding: '10px 12px', borderRadius: '8px', textAlign: 'left',
                            background: isSelected ? 'rgba(245,158,11,0.15)' : 'rgba(255,255,255,0.04)',
                            border: `1.5px solid ${isSelected ? '#F59E0B' : 'rgba(255,255,255,0.08)'}`,
                            color: isSelected ? '#FCD34D' : '#E6EDF3',
                            fontSize: '12px', fontWeight: isSelected ? 800 : 500, cursor: 'pointer', touchAction: 'manipulation'
                          }}
                        >
                          📜 {b.name} ({b.billKey})
                        </button>
                      );
                    })}
                  </div>
                )}
              </div>

              {/* Lobby Compensation / Asset Offers */}
              <div>
                <div style={{ fontSize: '12px', fontWeight: 800, color: '#4ADE80', textTransform: 'uppercase', marginBottom: '8px' }}>
                  🎁 COMPENSATION OFFERED FOR VOTE PLEDGE
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px' }}>
                  {renderCounterControl('Coins Offered', offeredCoins, setOfferedCoins, 0, activeParty?.stats?.coins || 999, 10)}
                  {renderCounterControl('Morale Offered', offeredMorale, setOfferedMorale, 0, 100, 5)}
                  {renderCounterControl('Media Offered', offeredMedia, setOfferedMedia, 0, 100, 5)}
                </div>

                {/* Optional Completed Buildings offered for Lobbying */}
                {myCompletedProjects.length > 0 && (
                  <div style={{ marginTop: '10px' }}>
                    <span style={{ fontSize: '11px', color: '#7D8590', fontWeight: 800, display: 'block', marginBottom: '6px' }}>
                      Offer Completed Buildings for Vote Pledge:
                    </span>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', maxHeight: '100px', overflowY: 'auto' }}>
                      {myCompletedProjects.map(proj => {
                        const pDef = PROJECT_DEFS[proj.projectKey] || {};
                        const isChecked = offeredBuildingKeys.includes(proj.projectKey);
                        return (
                          <label
                            key={proj.id}
                            style={{
                              display: 'flex', alignItems: 'center', gap: '8px', padding: '6px 10px',
                              borderRadius: '6px', background: isChecked ? 'rgba(74,222,128,0.15)' : 'rgba(255,255,255,0.04)',
                              border: `1px solid ${isChecked ? '#4ADE80' : 'rgba(255,255,255,0.08)'}`,
                              fontSize: '12px', cursor: 'pointer'
                            }}
                          >
                            <input
                              type="checkbox"
                              checked={isChecked}
                              onChange={() => toggleBuildingSelection(proj.projectKey, 'OFFER')}
                              style={{ accentColor: '#4ADE80' }}
                            />
                            <span>🏗️ {pDef.name || proj.projectKey}</span>
                          </label>
                        );
                      })}
                    </div>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* SABOTAGE */}
          {offerType === 'SABOTAGE' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <div style={{ fontSize: '12px', fontWeight: 800, color: '#EF4444', textTransform: 'uppercase' }}>
                ⚡ SELECT FACTION TO BRIBE
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                {targetFactions.map(f => {
                  const isSelected = selectedFactionKey === f.key;
                  return (
                    <button
                      key={f.key}
                      type="button"
                      onClick={() => setSelectedFactionKey(f.key)}
                      style={{
                        padding: '10px 12px', borderRadius: '8px', textAlign: 'left',
                        background: isSelected ? 'rgba(239,68,68,0.15)' : 'rgba(255,255,255,0.04)',
                        border: `1.5px solid ${isSelected ? '#EF4444' : 'rgba(255,255,255,0.08)'}`,
                        color: isSelected ? '#F87171' : '#E6EDF3',
                        fontSize: '12px', cursor: 'pointer', touchAction: 'manipulation'
                      }}
                    >
                      <div style={{ fontWeight: 900 }}>{f.name}</div>
                      <div style={{ fontSize: '10px', color: '#94A3B8' }}>Loyalty: {f.loyalty}% | Power: {f.influence}%</div>
                    </button>
                  );
                })}
              </div>

              {renderCounterControl('Bribe Coins (Cost)', bribeCoins, setBribeCoins, 0, activeParty?.stats?.coins || 999, 25)}
            </div>
          )}

          {/* Error Message */}
          {errorMsg && (
            <div style={{ marginTop: '10px', color: '#F87171', fontSize: '12px', fontWeight: 700 }}>
              ⚠️ {errorMsg}
            </div>
          )}

          {/* SUBMIT BUTTON */}
          <button
            type="button"
            onClick={offerType === 'SABOTAGE' ? handleBribe : handlePropose}
            disabled={loading || !recipientId || (offerType === 'NON_AGGRESSION' && !!existingPactWithRecipient)}
            style={{
              marginTop: '16px', width: '100%', minHeight: '48px',
              borderRadius: '10px', border: 'none',
              background: (offerType === 'NON_AGGRESSION' && !!existingPactWithRecipient)
                ? '#475569'
                : offerType === 'SABOTAGE' ? 'linear-gradient(135deg, #dc2626, #991b1b)' : 'linear-gradient(135deg, #2563eb, #1d4ed8)',
              color: '#ffffff', fontSize: '14px', fontWeight: 900,
              letterSpacing: '0.04em', textTransform: 'uppercase',
              boxShadow: '0 4px 14px rgba(0,0,0,0.4)', cursor: (offerType === 'NON_AGGRESSION' && !!existingPactWithRecipient) ? 'not-allowed' : 'pointer',
              touchAction: 'manipulation', opacity: (loading || !recipientId || (offerType === 'NON_AGGRESSION' && !!existingPactWithRecipient)) ? 0.6 : 1
            }}
          >
            {loading ? '⏳ PROCESSING...' : (offerType === 'NON_AGGRESSION' && !!existingPactWithRecipient) ? '🚫 PACT ALREADY ACTIVE' : offerType === 'SABOTAGE' ? '⚡ EXECUTE SABOTAGE' : '🤝 DISPATCH DIPLOMATIC TERMS'}
          </button>
        </div>
      )}
    </div>
  );
}
