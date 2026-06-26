import React from 'react';

export default function ActionSection({ num, title, isCompleted, isOptional, activeAccordion, setActiveAccordion, children }) {
  const isExpanded = activeAccordion === num;
  return (
    <div style={{
      border: '1.5px solid var(--card-border)',
      borderRadius: '12px',
      marginBottom: '15px',
      background: 'var(--card-bg)',
      color: 'var(--text-primary)',
      overflow: 'hidden',
      boxShadow: '0 4px 20px rgba(0,0,0,0.2)'
    }}>
      <div 
        onClick={() => setActiveAccordion(isExpanded ? 0 : num)}
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          padding: '15px 20px',
          background: isExpanded ? 'rgba(99, 102, 241, 0.15)' : 'transparent',
          cursor: 'pointer',
          borderBottom: isExpanded ? '1px solid var(--primary-border)' : 'none',
          userSelect: 'none'
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <span style={{
            background: 'var(--button-bg)',
            color: '#ffffff',
            width: '24px',
            height: '24px',
            borderRadius: '50%',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '12px',
            fontWeight: 'bold'
          }}>
            {num}
          </span>
          <h4 style={{ margin: 0, textTransform: 'uppercase', fontSize: '13px', letterSpacing: '0.05em', color: 'var(--text-primary)', fontWeight: 'bold' }}>
            {title}
          </h4>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{
            fontSize: '11px',
            fontWeight: 'bold',
            padding: '3px 8px',
            borderRadius: '12px',
            background: isCompleted ? 'rgba(34, 197, 94, 0.15)' : (isOptional ? 'rgba(99, 102, 241, 0.15)' : 'rgba(239, 68, 68, 0.15)'),
            color: isCompleted ? '#22c55e' : (isOptional ? 'var(--text-secondary)' : '#ef4444')
          }}>
            {isCompleted ? '✅ READY' : (isOptional ? 'ℹ️ OPTIONAL' : '⏳ PENDING')}
          </span>
          <span style={{ fontSize: '12px', transform: isExpanded ? 'rotate(90deg)' : 'rotate(0deg)', transition: 'transform 0.2s', display: 'inline-block', color: 'var(--text-secondary)' }}>
            ▶
          </span>
        </div>
      </div>
      {isExpanded && (
        <div style={{ padding: '20px' }}>
          {children}
        </div>
      )}
    </div>
  );
}
