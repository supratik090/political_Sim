import React from 'react';

export default function SkipTurnConfirmationModal({
  isOpen,
  onConfirm,
  onCancel,
  partyColor = '#ef4444'
}) {
  if (!isOpen) return null;

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(9, 13, 22, 0.85)',
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      zIndex: 10000,
      padding: '15px',
      backdropFilter: 'blur(8px)',
      fontFamily: "'Inter', system-ui, sans-serif"
    }}>
      <div style={{
        backgroundColor: '#ffffff',
        width: '100%',
        maxWidth: '400px',
        borderRadius: '20px',
        overflow: 'hidden',
        boxShadow: '0 15px 40px rgba(0, 0, 0, 0.4)',
        border: `3px solid ${partyColor}`,
        animation: 'modalSlideIn 0.3s ease-out'
      }}>
        <style dangerouslySetInnerHTML={{__html: `
          @keyframes modalSlideIn {
            from { transform: translateY(30px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
          }
        `}} />

        {/* Modal Header */}
        <div style={{
          backgroundColor: partyColor,
          padding: '20px',
          color: '#ffffff',
          textAlign: 'center',
        }}>
          <h2 style={{ margin: 0, fontSize: '18px', fontWeight: '800', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            Confirm Skip Turn
          </h2>
        </div>

        {/* Modal Body */}
        <div style={{ padding: '25px 20px', display: 'flex', flexDirection: 'column', gap: '20px', textAlign: 'center' }}>
          <p style={{ margin: 0, fontSize: '15px', color: '#334155', lineHeight: '1.5' }}>
            Are you sure you want to skip this turn? 
          </p>
          <div style={{
            background: 'rgba(239, 68, 68, 0.1)',
            border: '1px solid rgba(239, 68, 68, 0.2)',
            borderRadius: '10px',
            padding: '12px',
            fontSize: '13px',
            color: '#b91c1c',
            fontWeight: '600'
          }}>
            Your party will pass its card play, place a 0 bid, and submit routine/default responses to news and issues. This might lead to unexpected passive support drop.
          </div>

          <div style={{ display: 'flex', gap: '10px', marginTop: '10px' }}>
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
    </div>
  );
}
