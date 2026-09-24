import React, { useState } from 'react';
import { generateTurnHints } from '../../utils/hintsEngine';

export default function HintsView({
  turnData,
  localDecisions = {},
  scenarioBills = [],
  scenarioEvents = [],
  onNavigateToAction
}) {
  const [filterCategory, setFilterCategory] = useState('ALL');

  const hints = generateTurnHints(turnData, localDecisions, scenarioBills, scenarioEvents);
  const turnNumber = turnData?.turnNumber || 1;
  const myParty = turnData?.myParty || turnData?.parties?.[0] || {};

  // Filter hints based on selected tab
  const filteredHints = hints.filter(h => {
    if (filterCategory === 'ALL') return true;
    if (filterCategory === 'CRITICAL') return h.urgency === 'CRITICAL';
    if (filterCategory === 'CARDS') return h.category === 'CARDS';
    if (filterCategory === 'RESOURCES') return h.category === 'RESOURCES';
    if (filterCategory === 'OPERATIONS') return h.category === 'OPERATIONS' || h.category === 'PARTY_BUILDING' || h.category === 'CARDS';
    if (filterCategory === 'LEGISLATION') return h.category === 'LEGISLATION' || h.category === 'COOPERATION' || h.category === 'ASSEMBLY';
    return true;
  });

  const criticalCount = hints.filter(h => h.urgency === 'CRITICAL').length;
  const recommendedCount = hints.filter(h => h.urgency === 'RECOMMENDED').length;

  return (
    <div style={{
      width: '100%',
      maxWidth: '1000px',
      margin: '0 auto',
      padding: '16px',
      boxSizing: 'border-box',
      animation: 'fadeIn 0.2s ease-out'
    }}>
      {/* Main Container Card */}
      <div style={{
        background: 'linear-gradient(145deg, #1e293b 0%, #0f172a 100%)',
        borderRadius: '16px',
        border: '1px solid rgba(255,255,255,0.1)',
        boxShadow: '0 10px 30px rgba(0,0,0,0.3)',
        padding: '24px',
        color: '#f8fafc'
      }}>
        {/* Header Section */}
        <div style={{
          display: 'flex',
          flexDirection: 'row',
          justifyContent: 'space-between',
          alignItems: 'flex-start',
          flexWrap: 'wrap',
          gap: '12px',
          borderBottom: '1px solid rgba(255,255,255,0.1)',
          paddingBottom: '16px',
          marginBottom: '20px'
        }}>
          <div>
            <h2 style={{
              margin: 0,
              fontSize: '22px',
              fontWeight: 800,
              color: '#ffffff',
              display: 'flex',
              alignItems: 'center',
              gap: '8px'
            }}>
              💡 Tactical Campaign Hints
            </h2>
            <p style={{ margin: '6px 0 0 0', fontSize: '13px', color: '#94a3b8', lineHeight: '1.4' }}>
              Turn {turnNumber} • Real-time strategic guidance customized to your party's political standing
            </p>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{
              background: 'rgba(59, 130, 246, 0.15)',
              border: '1px solid rgba(59, 130, 246, 0.3)',
              color: '#60a5fa',
              padding: '6px 12px',
              borderRadius: '20px',
              fontSize: '12px',
              fontWeight: 700
            }}>
              📊 {hints.length} Total Advice
            </span>
            {criticalCount > 0 && (
              <span style={{
                background: 'rgba(239, 68, 68, 0.15)',
                border: '1px solid rgba(239, 68, 68, 0.4)',
                color: '#f87171',
                padding: '6px 12px',
                borderRadius: '20px',
                fontSize: '12px',
                fontWeight: 800,
                animation: 'pulse-soft 1.5s infinite'
              }}>
                🚨 {criticalCount} Critical
              </span>
            )}
          </div>
        </div>

        {/* Category Filter Bar */}
        <div style={{
          display: 'flex',
          gap: '8px',
          flexWrap: 'wrap',
          marginBottom: '20px'
        }}>
          {[
            { id: 'ALL', label: `All Hints (${hints.length})` },
            { id: 'CRITICAL', label: `🚨 Critical (${criticalCount})` },
            { id: 'CARDS', label: `🃏 Cards & Strategy` },
            { id: 'RESOURCES', label: `💰 Resources` },
            { id: 'OPERATIONS', label: `⚡ Operations` },
            { id: 'LEGISLATION', label: `📜 Assembly & Diplomacy` }
          ].map(tab => {
            const isActive = filterCategory === tab.id;
            return (
              <button
                key={tab.id}
                type="button"
                onClick={() => setFilterCategory(tab.id)}
                style={{
                  padding: '8px 14px',
                  borderRadius: '10px',
                  fontSize: '12px',
                  fontWeight: 'bold',
                  border: isActive ? '1.5px solid #38bdf8' : '1px solid rgba(255,255,255,0.12)',
                  background: isActive ? '#0284c7' : 'rgba(255,255,255,0.05)',
                  color: isActive ? '#ffffff' : '#94a3b8',
                  cursor: 'pointer',
                  transition: 'all 0.15s ease'
                }}
              >
                {tab.label}
              </button>
            );
          })}
        </div>

        {/* Hints List */}
        {filteredHints.length === 0 ? (
          <div style={{
            padding: '40px 20px',
            textAlign: 'center',
            background: 'rgba(255,255,255,0.02)',
            borderRadius: '12px',
            border: '1px dashed rgba(255,255,255,0.1)',
            color: '#94a3b8'
          }}>
            <span style={{ fontSize: '28px', display: 'block', marginBottom: '8px' }}>✅</span>
            <strong style={{ display: 'block', fontSize: '15px', color: '#f8fafc' }}>No Hints Found in this Category</strong>
            <span style={{ fontSize: '12px' }}>Your party is operating on solid ground for this area.</span>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '14px' }}>
            {filteredHints.map((hint, idx) => {
              const isCritical = hint.urgency === 'CRITICAL';
              return (
                <div
                  key={hint.id || idx}
                  style={{
                    backgroundColor: '#0f172a',
                    borderRadius: '14px',
                    padding: '18px',
                    border: isCritical ? '1.5px solid rgba(239, 68, 68, 0.5)' : '1px solid rgba(255,255,255,0.1)',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'space-between',
                    gap: '12px',
                    boxShadow: isCritical ? '0 4px 20px rgba(239, 68, 68, 0.15)' : '0 4px 12px rgba(0,0,0,0.2)',
                    transition: 'transform 0.15s ease, box-shadow 0.15s ease'
                  }}
                >
                  <div>
                    {/* Badge & Counter */}
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px' }}>
                      <span
                        style={{
                          backgroundColor: hint.badgeBg || (isCritical ? '#ef4444' : '#3b82f6'),
                          color: '#ffffff',
                          fontSize: '10px',
                          fontWeight: 800,
                          padding: '3px 9px',
                          borderRadius: '20px',
                          textTransform: 'uppercase',
                          letterSpacing: '0.05em'
                        }}
                      >
                        {hint.badgeText || (isCritical ? 'Critical' : 'Hint')}
                      </span>
                      <span style={{ fontSize: '11px', color: '#64748b', fontWeight: 600 }}>
                        #{idx + 1}
                      </span>
                    </div>

                    {/* Title & Description */}
                    <h3 style={{ margin: '0 0 6px 0', fontSize: '15px', fontWeight: 700, color: '#f1f5f9', lineHeight: '1.3' }}>
                      {hint.title}
                    </h3>
                    <p style={{ margin: 0, fontSize: '13px', color: '#cbd5e1', lineHeight: '1.45' }}>
                      {hint.description}
                    </p>
                  </div>

                  {/* Action Button */}
                  {hint.actionLabel && (
                    <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '6px' }}>
                      <button
                        type="button"
                        onClick={() => {
                          if (onNavigateToAction) {
                            onNavigateToAction(hint.targetTab, hint);
                          }
                        }}
                        style={{
                          backgroundColor: isCritical ? 'rgba(239, 68, 68, 0.18)' : 'rgba(59, 130, 246, 0.15)',
                          color: isCritical ? '#fca5a5' : '#60a5fa',
                          border: isCritical ? '1px solid rgba(239, 68, 68, 0.5)' : '1px solid rgba(59, 130, 246, 0.4)',
                          padding: '8px 16px',
                          borderRadius: '8px',
                          fontSize: '12.5px',
                          fontWeight: 700,
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '6px',
                          transition: 'all 0.15s ease'
                        }}
                      >
                        <span>{hint.actionLabel}</span>
                        <span>⚡</span>
                      </button>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        )}

        {/* Footer info */}
        <div style={{ textAlign: 'center', marginTop: '20px', fontSize: '11px', color: '#64748b' }}>
          💡 Hints update dynamically at the beginning of each turn based on active campaign metrics.
        </div>
      </div>
    </div>
  );
}
