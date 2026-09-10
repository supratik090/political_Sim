import React from 'react';

export default function ActionSection({ num, title, isCompleted, isOptional, activeAccordion, setActiveAccordion, children }) {
  const isExpanded = activeAccordion === num;
  return (
    <div style={{
      border: '1px solid var(--primary-border)',
      borderRadius: '12px',
      marginBottom: '15px',
      background: '#ffffff',
      color: '#000000',
      overflow: 'hidden',
      boxShadow: '0 4px 12px rgba(33,60,81,0.03)'
    }}>
      <div 
        onClick={() => setActiveAccordion(isExpanded ? 0 : num)}
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          padding: '16px 18px',
          minHeight: '52px',
          background: isExpanded ? 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.08)' : 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.02)',
          cursor: 'pointer',
          borderBottom: isExpanded ? '1px solid var(--party-primary-color, var(--primary-border))' : 'none',
          userSelect: 'none',
          WebkitTapHighlightColor: 'transparent',
          touchAction: 'manipulation'
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <span style={{
            background: 'var(--party-primary-color, var(--primary-dark))',
            color: '#ffffff',
            width: '30px',
            height: '30px',
            borderRadius: '50%',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '14px',
            fontWeight: 'bold',
            flexShrink: 0
          }}>
            {num}
          </span>
          <h4 style={{ margin: 0, textTransform: 'uppercase', fontSize: '14px', letterSpacing: '0.04em', color: 'var(--primary-dark)', fontWeight: 'bold' }}>
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
