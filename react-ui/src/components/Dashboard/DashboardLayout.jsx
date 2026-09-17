import React, { useState } from 'react';
import { useGameStore } from '../../store/gameStore';
import { isAndroidApp } from '../../utils/platform';
import { generateTurnHints } from '../../utils/hintsEngine';

const ADMIN_USERNAME = 'AdminUserFoo';

export default function DashboardLayout({ children }) {
  const { user, logout, currentScreen, setScreen, turnData, activeGameId, timeLeft, activeGameView, setActiveGameView } = useGameStore();
  const isAdmin = user?.name === ADMIN_USERNAME;
  const isAndroid = isAndroidApp();
  const formatTime = (secs) => `${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, '0')}`;
  const hintsCount = turnData ? generateTurnHints(turnData).length : 0;

  return (
    <div className="dashboard-container">
      
      {/* Top Navigation Bar — All in 1 Single Line */}
      <div className="dashboard-top-nav" style={{ 
        display: 'flex', 
        flexDirection: 'row', 
        alignItems: 'center', 
        justifyContent: 'space-between', 
        gap: '8px', 
        marginBottom: '16px',
        width: '100%',
        flexWrap: 'nowrap'
      }}>
        
        {/* Item 1: Logo + Title (Title hidden if name is long) */}
        <div className="top-nav-left" style={{ display: 'flex', alignItems: 'center', gap: '8px', flexShrink: 0 }}>
          <img src="/app-logo.png" alt="Statecraft Logo" className="top-nav-logo" style={{ width: '34px', height: '34px', objectFit: 'contain', borderRadius: '8px', boxShadow: '0 2px 6px rgba(0,0,0,0.15)', flexShrink: 0 }} />
          {((user?.name || '').length <= 10) && (
            <div className="top-nav-brand-text" style={{ display: 'flex', flexDirection: 'column' }}>
              <span className="top-nav-title" style={{ fontSize: '16px', fontWeight: 900, color: 'var(--primary-dark)', lineHeight: 1.1 }}>
                Statecraft
              </span>
              <span className="nav-subtitle" style={{ fontSize: '9px', color: 'var(--text-secondary)', textTransform: 'uppercase', fontWeight: 700, letterSpacing: '0.04em' }}>
                Governance
              </span>
            </div>
          )}
        </div>

        {/* Item 2: User Welcome (middle element, truncates smoothly if long) */}
        <div className="top-nav-welcome" style={{ 
          flex: '1 1 auto', 
          minWidth: 0, 
          textAlign: 'center', 
          fontSize: '13px', 
          fontWeight: 700, 
          color: 'var(--primary-dark)',
          whiteSpace: 'nowrap',
          overflow: 'hidden',
          textOverflow: 'ellipsis',
          padding: '0 4px'
        }}>
          👋 <b style={{ fontWeight: 800 }}>{user?.name || 'Player'}</b>
        </div>

        {/* Item 3: Buttons & Logout Symbol */}
        <div className="dashboard-top-nav-buttons" style={{ display: 'flex', alignItems: 'center', gap: '6px', margin: 0, flexShrink: 0 }}>
          {turnData?.isMultiplayer && timeLeft !== null && (
            <button disabled style={{
              backgroundColor: timeLeft <= 30 ? '#dc2626' : '#be123c',
              borderColor: timeLeft <= 30 ? '#dc2626' : '#be123c',
              color: '#fff', padding: '4px 8px', borderRadius: '6px',
              fontWeight: 'bold', boxShadow: '0 2px 6px rgba(0,0,0,0.2)',
              fontSize: '11px', cursor: 'default',
              minWidth: '60px',
              animation: timeLeft <= 30 ? 'pulse-soft 1s infinite' : 'none',
            }}>
              ⏱️ {formatTime(timeLeft)}
            </button>
          )}
          {isAdmin && currentScreen !== 'ADMIN' && (
            <button onClick={() => setScreen('ADMIN')} title="Admin Console" style={{ backgroundColor: 'var(--card-bg)', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)', padding: '4px 8px', fontSize: '11px', borderRadius: '6px' }}>
              🛠️
            </button>
          )}
          {currentScreen === 'HOME' && (
            <button 
              onClick={logout} 
              title="Logout"
              aria-label="Logout"
              className="logout-symbol-btn"
              style={{ 
                backgroundColor: '#be123c', 
                border: 'none', 
                color: '#ffffff',
                width: '32px', 
                height: '32px', 
                borderRadius: '8px',
                display: 'inline-flex',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: 'pointer',
                boxShadow: '0 2px 6px rgba(190,18,60,0.25)',
                fontSize: '15px',
                flexShrink: 0
              }}
            >
              🚪
            </button>
          )}
        </div>
      </div>

      {/* Main Content Area */}
      <main>
        {children}
      </main>

      {/* ── Android Bottom Tab Bar (mobile only via CSS) ── */}
      <nav className="android-bottom-nav" role="navigation" aria-label="Main navigation">
        <button
          className={`android-bottom-nav-item ${currentScreen === 'HOME' ? 'active' : ''}`}
          onClick={() => setScreen('HOME')}
        >
          <span className="nav-icon">🏠</span>
          Home
        </button>
        {(activeGameId || turnData) && (
          <button
            className={`android-bottom-nav-item ${currentScreen === 'GAME' && activeGameView !== 'HINTS' ? 'active' : ''}`}
            onClick={() => {
              setScreen('GAME');
              if (activeGameView === 'HINTS') setActiveGameView('ACTION');
            }}
          >
            <span className="nav-icon">🎮</span>
            Campaign
          </button>
        )}
        <button
          className={`android-bottom-nav-item ${currentScreen === 'HOW_TO_PLAY' ? 'active' : ''}`}
          onClick={() => setScreen('HOW_TO_PLAY')}
        >
          <span className="nav-icon">📖</span>
          Rules
        </button>
        {isAdmin && (
          <button
            className={`android-bottom-nav-item ${currentScreen === 'ADMIN' ? 'active' : ''}`}
            onClick={() => setScreen('ADMIN')}
          >
            <span className="nav-icon">🛠️</span>
            Admin
          </button>
        )}
        <button
          className={`android-bottom-nav-item ${currentScreen === 'GAME' && activeGameView === 'HINTS' ? 'active' : ''}`}
          onClick={() => {
            if (activeGameId || turnData) {
              setScreen('GAME');
            }
            setActiveGameView('HINTS');
          }}
          style={{ position: 'relative' }}
        >
          <span className="nav-icon" style={{ position: 'relative', display: 'inline-block' }}>
            💡
            {hintsCount > 0 && (
              <span style={{
                position: 'absolute',
                top: '-4px',
                right: '-10px',
                backgroundColor: '#ef4444',
                color: '#ffffff',
                fontSize: '10px',
                fontWeight: '900',
                padding: '1px 5px',
                borderRadius: '8px',
                lineHeight: '1.2',
                boxShadow: '0 2px 4px rgba(0,0,0,0.3)'
              }}>
                {hintsCount}
              </span>
            )}
          </span>
          Hints {hintsCount > 0 ? `(${hintsCount})` : ''}
        </button>
      </nav>
      
    </div>
  );
}
