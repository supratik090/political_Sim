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
      
      {/* Top Navigation Bar */}
      <div className="dashboard-top-nav">
        
        {/* Left Side: Logo & App Title */}
        <div className="top-nav-left">
          <img src="/app-logo.png" alt="Statecraft Logo" className="top-nav-logo" style={{ width: '42px', height: '42px', objectFit: 'contain', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.15)', flexShrink: 0 }} />
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span className="top-nav-title">
              Statecraft
            </span>
            <span className="nav-subtitle" style={{ fontSize: '10px', color: 'var(--text-secondary)', textTransform: 'uppercase', fontWeight: 700, letterSpacing: '0.05em' }}>
              Grand Strategy &amp; Governance
            </span>
          </div>
        </div>

        {/* Center: Welcome message */}
        <div className="top-nav-welcome">
          👋 Welcome, <b style={{ fontWeight: 800 }}>{user?.name || 'Unknown'}</b>!
        </div>
        
        {/* Right Side: Buttons */}
        <div className="dashboard-top-nav-buttons" style={{ margin: 0 }}>
          {turnData?.isMultiplayer && timeLeft !== null && (
            <button disabled style={{
              backgroundColor: timeLeft <= 30 ? '#dc2626' : '#be123c',
              borderColor: timeLeft <= 30 ? '#dc2626' : '#be123c',
              color: '#fff', padding: '6px 10px', borderRadius: '4px',
              fontWeight: 'bold', boxShadow: '0 4px 10px rgba(0,0,0,0.2)',
              fontSize: '13px', cursor: 'default', order: 0, marginRight: '6px',
              minWidth: '80px',
              animation: timeLeft <= 30 ? 'pulse-soft 1s infinite' : 'none',
            }}>
              ⏱️ {formatTime(timeLeft)}
            </button>
          )}
          {isAdmin && currentScreen !== 'ADMIN' && (
            <button onClick={() => setScreen('ADMIN')} style={{ backgroundColor: 'var(--card-bg)', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)' }}>
              🛠️ Admin Console
            </button>
          )}
          {currentScreen === 'HOME' && (
            <button onClick={logout} style={{ backgroundColor: '#be123c', borderColor: '#be123c' }}>
              🚪 Logout
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
