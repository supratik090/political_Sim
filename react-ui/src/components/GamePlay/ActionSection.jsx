import React from 'react';

export default function ActionSection({ num, title, isCompleted, isOptional, activeAccordion, setActiveAccordion, children }) {
  const isExpanded = activeAccordion === num;
  return (
    <div style={{
      border: '2px solid var(--primary-border)',
      borderLeft: '5px solid var(--party-primary-color, var(--primary-dark))',
      borderRadius: '12px',
      marginBottom: '16px',
      background: '#ffffff',
      color: '#000000',
      overflow: 'hidden',
      boxShadow: '0 4px 14px rgba(33,60,81,0.06)'
    }}>
      <div 
        onClick={() => setActiveAccordion(isExpanded ? 0 : num)}
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          padding: '16px 18px',
          minHeight: '52px',
          background: isExpanded ? 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.10)' : 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.03)',
          cursor: 'pointer',
          borderBottom: isExpanded ? '2px solid var(--party-primary-color, var(--primary-border))' : 'none',
          userSelect: 'none',
          WebkitTapHighlightColor: 'transparent',
          touchAction: 'manipulation'
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <h4 style={{ margin: 0, textTransform: 'uppercase', fontSize: '14px', letterSpacing: '0.04em', color: 'var(--primary-dark)', fontWeight: 900 }}>
            {title}
          </h4>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{
            fontSize: '12px',
            fontWeight: '700',
            padding: '5px 10px',
            borderRadius: '12px',
            background: isCompleted ? 'rgba(22, 163, 74, 0.15)' : (isOptional ? 'rgba(101, 148, 177, 0.15)' : 'rgba(210, 63, 49, 0.15)'),
            color: isCompleted ? '#16A34A' : (isOptional ? 'var(--primary-dark)' : '#d23f31'),
            whiteSpace: 'nowrap'
          }}>
            {isCompleted ? '✅ READY' : (isOptional ? 'ℹ️ OPTIONAL' : '⏳ PENDING')}
          </span>
          <span style={{ fontSize: '16px', transform: isExpanded ? 'rotate(90deg)' : 'rotate(0deg)', transition: 'transform 0.2s', display: 'inline-block', color: 'var(--primary-dark)' }}>
            ▶
          </span>
        </div>
      </div>
      {isExpanded && (
        <div style={{ padding: '18px 16px' }}>
          {children}
        </div>
      )}
    </div>
  );
}
