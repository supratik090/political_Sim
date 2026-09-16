import React from 'react';
import { generateTurnHints } from '../../utils/hintsEngine';

export default function HintsDrawer({
  isOpen,
  onClose,
  turnData,
  localDecisions = {},
  scenarioBills = [],
  scenarioEvents = [],
  onNavigateTab
}) {
  if (!isOpen) return null;

  const hints = generateTurnHints(turnData, localDecisions, scenarioBills, scenarioEvents);
  const turnNumber = turnData?.turnNumber || 1;

  const handleActionClick = (targetTab) => {
    if (onNavigateTab && targetTab) {
      onNavigateTab(targetTab);
    }
    onClose();
  };

  return (
    <div
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(15, 23, 42, 0.75)',
        backdropFilter: 'blur(6px)',
        zIndex: 9999,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'flex-end',
        alignItems: 'center',
        animation: 'fadeIn 0.2s ease-out'
      }}
      onClick={onClose}
    >
      <div
        style={{
          width: '100%',
          maxWidth: '540px',
          maxHeight: '85vh',
          backgroundColor: '#1e293b',
          color: '#f8fafc',
          borderTopLeftRadius: '24px',
          borderTopRightRadius: '24px',
          boxShadow: '0 -10px 40px rgba(0,0,0,0.5)',
          padding: '24px 20px 32px 20px',
          boxSizing: 'border-box',
          overflowY: 'auto',
          display: 'flex',
          flexDirection: 'column',
          gap: '16px',
          borderTop: '2px solid rgba(255,255,255,0.1)'
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Handle bar for bottom sheet feel */}
        <div
          style={{
            width: '40px',
            height: '4px',
            backgroundColor: '#475569',
            borderRadius: '2px',
            margin: '0 auto 8px auto'
          }}
        />

        {/* Drawer Header */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div>
            <h2 style={{ margin: 0, fontSize: '20px', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.02em' }}>
              Tactical Campaign Hints
            </h2>
            <p style={{ margin: '4px 0 0 0', fontSize: '12px', color: '#94a3b8' }}>
              Turn {turnNumber} • Situation-based guidance to lead your party to victory
            </p>
          </div>
          <button
            onClick={onClose}
            style={{
              background: '#334155',
              border: 'none',
              color: '#cbd5e1',
              width: '32px',
              height: '32px',
              borderRadius: '50%',
              fontSize: '16px',
              fontWeight: 'bold',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}
          >
            ✕
          </button>
        </div>

        {/* Hints List */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '8px' }}>
          {hints.map((hint, idx) => (
            <div
              key={hint.id || idx}
              style={{
                backgroundColor: '#0f172a',
                borderRadius: '14px',
                padding: '16px',
                border: '1px solid #334155',
                display: 'flex',
                flexDirection: 'column',
                gap: '10px',
                boxShadow: '0 4px 12px rgba(0,0,0,0.2)'
              }}
            >
              {/* Badge & Category */}
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                <span
                  style={{
                    backgroundColor: hint.badgeBg || '#3b82f6',
                    color: '#ffffff',
                    fontSize: '10px',
                    fontWeight: 800,
                    padding: '3px 8px',
                    borderRadius: '20px',
                    textTransform: 'uppercase',
                    letterSpacing: '0.05em'
                  }}
                >
                  {hint.badgeText || 'Hint'}
                </span>
                <span style={{ fontSize: '11px', color: '#64748b', fontWeight: 600 }}>
                  Hint {idx + 1} of {hints.length}
                </span>
              </div>

              {/* Title & Description */}
              <div>
                <h3 style={{ margin: '0 0 4px 0', fontSize: '15px', fontWeight: 700, color: '#f1f5f9' }}>
                  {hint.title}
                </h3>
                <p style={{ margin: 0, fontSize: '13px', color: '#cbd5e1', lineHeight: '1.45' }}>
                  {hint.description}
                </p>
              </div>

              {/* Action Button */}
              {hint.actionLabel && (
                <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '4px' }}>
                  <button
                    onClick={() => handleActionClick(hint.targetTab)}
                    style={{
                      backgroundColor: 'rgba(59, 130, 246, 0.15)',
                      color: '#60a5fa',
                      border: '1px solid rgba(59, 130, 246, 0.4)',
                      padding: '7px 14px',
                      borderRadius: '8px',
                      fontSize: '12px',
                      fontWeight: 700,
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '6px',
                      transition: 'all 0.15s ease'
                    }}
                  >
                    <span>{hint.actionLabel}</span>
                    <span>→</span>
                  </button>
                </div>
              )}
            </div>
          ))}
        </div>

        {/* Footer info */}
        <div style={{ textAlign: 'center', marginTop: '4px', fontSize: '11px', color: '#64748b' }}>
          Hints update dynamically at the beginning of each turn based on game conditions.
        </div>
      </div>
    </div>
  );
}
