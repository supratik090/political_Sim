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
      <div className="dashboard-top-nav" style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginBottom: '16px' }}>
        
        {/* Top Header Row */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%', gap: '10px' }}>
          
          {/* Top Left: Logo + App Title + Logout */}
          <div className="top-nav-left" style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
            <img src="/app-logo.png" alt="Statecraft Logo" className="top-nav-logo" style={{ width: '38px', height: '38px', objectFit: 'contain', borderRadius: '10px', boxShadow: '0 2px 8px rgba(0,0,0,0.15)', flexShrink: 0 }} />
            <div style={{ display: 'flex', flexDirection: 'column', marginRight: '4px' }}>
              <span className="top-nav-title" style={{ fontSize: '18px', fontWeight: 900, color: 'var(--primary-dark)', lineHeight: 1.1 }}>
                Statecraft
              </span>
              <span className="nav-subtitle" style={{ fontSize: '10px', color: 'var(--text-secondary)', textTransform: 'uppercase', fontWeight: 700, letterSpacing: '0.05em' }}>
                Grand Strategy &amp; Governance
              </span>
            </div>

            {/* Logout button situated on Top Left */}
            {currentScreen === 'HOME' && (
              <button 
                onClick={logout} 
                style={{ 
                  backgroundColor: '#be123c', 
                  borderColor: '#be123c', 
                  color: '#ffffff',
                  padding: '5px 12px', 
                  fontSize: '12px', 
                  fontWeight: 800, 
                  borderRadius: '6px',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '4px',
                  cursor: 'pointer',
                  boxShadow: '0 2px 6px rgba(190,18,60,0.25)',
                  margin: 0
                }}
              >
                🚪 Logout
              </button>
            )}
          </div>

          {/* Top Right: Buttons (Timer & Admin) */}
          <div className="dashboard-top-nav-buttons" style={{ display: 'flex', alignItems: 'center', gap: '8px', margin: 0 }}>
            {turnData?.isMultiplayer && timeLeft !== null && (
              <button disabled style={{
                backgroundColor: timeLeft <= 30 ? '#dc2626' : '#be123c',
                borderColor: timeLeft <= 30 ? '#dc2626' : '#be123c',
                color: '#fff', padding: '5px 10px', borderRadius: '6px',
                fontWeight: 'bold', boxShadow: '0 4px 10px rgba(0,0,0,0.2)',
                fontSize: '12px', cursor: 'default',
                minWidth: '75px',
                animation: timeLeft <= 30 ? 'pulse-soft 1s infinite' : 'none',
              }}>
                ⏱️ {formatTime(timeLeft)}
              </button>
            )}
            {isAdmin && currentScreen !== 'ADMIN' && (
              <button onClick={() => setScreen('ADMIN')} style={{ backgroundColor: 'var(--card-bg)', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)', padding: '5px 10px', fontSize: '12px', borderRadius: '6px' }}>
                🛠️ Admin Console
              </button>
            )}
          </div>
        </div>

        {/* 2nd Line: Welcome message (supports long names without pushing Logout) */}
        <div className="top-nav-welcome" style={{ fontSize: '13px', color: 'var(--text-secondary)', fontWeight: 600, wordBreak: 'break-word', marginTop: '2px' }}>
          👋 Welcome, <b style={{ fontWeight: 800, color: 'var(--primary-dark)' }}>{user?.name || 'Unknown'}</b>!
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
