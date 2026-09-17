import React from 'react';

export default function SkipTurnConfirmationModal({
  isOpen,
  onConfirm,
  onCancel,
  partyColor = '#ef4444'
}) {
  if (!isOpen) return null;

  return (
    <div
      className="modal-overlay"
      style={{
        fontFamily: "'Inter', system-ui, sans-serif",
        zIndex: 10000,
        backgroundColor: 'rgba(9, 13, 22, 0.85)',
        backdropFilter: 'blur(8px)',
      }}
    >
      <style dangerouslySetInnerHTML={{__html: `
        @keyframes modalSlideIn {
          from { transform: translateY(30px); opacity: 0; }
          to { transform: translateY(0); opacity: 1; }
        }
      `}} />

      <div
        className="modal-card"
        style={{
          backgroundColor: '#ffffff',
          maxWidth: '400px',
          boxShadow: '0 15px 40px rgba(0, 0, 0, 0.4)',
          border: `3px solid ${partyColor}`,
          animation: 'modalSlideIn 0.3s ease-out'
        }}
      >
        {/* Modal Header */}
        <div
          className="modal-header"
          style={{
            backgroundColor: partyColor,
            padding: '16px 20px',
            color: '#ffffff',
            textAlign: 'center',
            position: 'relative',
          }}
        >
          <h2 style={{ margin: 0, fontSize: '16px', fontWeight: '800', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            Confirm Skip Turn
          </h2>
          <button
            className="modal-close-btn"
            onClick={onCancel}
            style={{
              position: 'absolute',
              top: '10px',
              right: '10px',
              background: 'rgba(255,255,255,0.2)',
              border: 'none',
              color: '#ffffff',
              borderRadius: '50%',
              width: '34px',
              height: '34px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              cursor: 'pointer',
              fontSize: '16px',
              flexShrink: 0,
            }}
            aria-label="Cancel"
          >
            ✕
          </button>
        </div>

        {/* Scrollable Modal Body */}
        <div className="modal-body" style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '16px', textAlign: 'center' }}>
          <p style={{ margin: 0, fontSize: '14px', color: '#334155', lineHeight: '1.5' }}>
            Are you sure you want to skip this turn?
          </p>
          <div style={{
            background: 'rgba(239, 68, 68, 0.1)',
            border: '1px solid rgba(239, 68, 68, 0.2)',
            borderRadius: '10px',
            padding: '12px',
            fontSize: '12px',
            color: '#b91c1c',
            fontWeight: '600'
          }}>
            Your party will pass its card play, place a 0 bid, and submit routine/default responses to news and issues. This might lead to unexpected passive support drop.
          </div>
        </div>

        {/* Sticky Footer */}
        <div className="modal-footer" style={{ padding: '12px 20px', borderTop: '1px solid #e2e8f0', display: 'flex', gap: '10px' }}>
          <button
            onClick={onCancel}
            style={{
              flex: 1,
              backgroundColor: '#f1f5f9',
              color: '#475569',
              border: '1px solid #cbd5e1',
              padding: '12px',
              borderRadius: '10px',
              fontWeight: 'bold',
              fontSize: '14px',
              cursor: 'pointer',
              transition: 'background 0.2s'
            }}
            onMouseOver={e => e.target.style.backgroundColor = '#e2e8f0'}
            onMouseOut={e => e.target.style.backgroundColor = '#f1f5f9'}
          >
            Cancel
          </button>
          <button
            onClick={onConfirm}
            style={{
              flex: 1,
              backgroundColor: partyColor,
              color: '#ffffff',
              border: 'none',
              padding: '12px',
              borderRadius: '10px',
              fontWeight: 'bold',
              fontSize: '14px',
              cursor: 'pointer',
              boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
              transition: 'opacity 0.2s'
            }}
            onMouseOver={e => e.target.style.opacity = '0.9'}
            onMouseOut={e => e.target.style.opacity = '1'}
          >
            Skip Turn
          </button>
        </div>

      </div>
    </div>
  );
}
