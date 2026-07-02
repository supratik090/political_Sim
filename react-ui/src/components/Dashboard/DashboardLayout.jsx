import React from 'react';
import { useGameStore } from '../../store/gameStore';

const ADMIN_USERNAME = 'AdminUserFoo';

export default function DashboardLayout({ children }) {
  const { user, logout, currentScreen, setScreen, turnData, timeLeft } = useGameStore();
  const isAdmin = user?.name === ADMIN_USERNAME;
  const formatTime = (secs) => `${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, '0')}`;

  return (
    <div className="dashboard-container">
      
      {/* Top Navigation Bar */}
      <div className="dashboard-top-nav" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '15px' }}>
        
        {/* Left Side: Logo & App Title */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <img src="/politics.svg" alt="Political Sim Logo" style={{ width: '42px', height: '42px', borderRadius: '8px' }} />
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span style={{ fontSize: '18px', fontWeight: 900, color: 'var(--primary-dark)', letterSpacing: '-0.02em', lineHeight: 1.2 }}>
              Political Sim
            </span>
            <span style={{ fontSize: '10px', color: 'var(--text-secondary)', textTransform: 'uppercase', fontWeight: 700, letterSpacing: '0.05em' }}>
              Grand Campaign Simulation
            </span>
          </div>
        </div>

        {/* Center: Welcome message */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '2px', minWidth: '150px' }}>
          <div style={{ fontSize: '13px', color: 'var(--primary-dark)' }}>
            👋 Welcome, <b style={{ fontWeight: 800 }}>{user?.name || 'Unknown'}</b>!
          </div>
          <div style={{ fontSize: '11px', color: 'var(--text-secondary)', fontStyle: 'italic' }} className="nav-subtitle">
            Command campaigns & win elections.
          </div>
        </div>
        
        {/* Right Side: Buttons */}
        <div className="dashboard-top-nav-buttons" style={{ margin: 0 }}>
          {turnData?.isMultiplayer && timeLeft !== null && (
            <button disabled style={{
              backgroundColor: timeLeft <= 30 ? '#dc2626' : '#be123c',
              borderColor: timeLeft <= 30 ? '#dc2626' : '#be123c',
              color: '#fff', padding: '8px 12px', borderRadius: '4px',
              fontWeight: 'bold', boxShadow: '0 4px 10px rgba(0,0,0,0.2)',
              fontSize: '14px', cursor: 'default', order: 0, marginRight: '8px',
              minWidth: '90px',
              animation: timeLeft <= 30 ? 'pulse-soft 1s infinite' : 'none',
            }}>
              ⏱️ {formatTime(timeLeft)}
            </button>
          )}
          {currentScreen !== 'HOW_TO_PLAY' && (
            <button onClick={() => setScreen('HOW_TO_PLAY')} style={{ backgroundColor: 'var(--card-bg)', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)', order: 1 }}>
              📖 How to Play
            </button>
          )}
          {currentScreen !== 'HOME' && (
            <button onClick={() => setScreen('HOME')} style={{ backgroundColor: 'var(--card-bg)', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)' }}>
              🏠 Home
            </button>
          )}
          {isAdmin && currentScreen !== 'ADMIN' && (
            <button onClick={() => setScreen('ADMIN')} style={{ backgroundColor: 'var(--card-bg)', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)' }}>
              🛠️ Admin Console
            </button>
          )}
          <button onClick={logout} style={{ backgroundColor: '#be123c', borderColor: '#be123c' }}>
            🚪 Logout
          </button>
        </div>
      </div>

      {/* Main Content Area */}
      <main>
        {children}
      </main>
      
    </div>
  );
}
