import React from 'react';
import { useGameStore } from '../../store/gameStore';

export default function DashboardLayout({ children }) {
  const { user, logout, currentScreen, setScreen } = useGameStore();

  return (
    <div className="dashboard-container">
      
      {/* Top Navigation Bar */}
      <div className="dashboard-top-nav">
        <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
          <div style={{ fontSize: '14px', color: 'var(--primary-dark)' }}>
            👋 Welcome, <b style={{ fontWeight: 800 }}>{user?.name || 'Unknown'}</b>!
          </div>
          <div style={{ fontSize: '12px', color: 'var(--text-secondary)', fontStyle: 'italic' }} className="nav-subtitle">
            Command campaign strategies, build party, and win state elections.
          </div>
        </div>
        
        <div className="dashboard-top-nav-buttons">
          {currentScreen !== 'HOME' && (
            <button onClick={() => setScreen('HOME')} style={{ backgroundColor: 'var(--card-bg)', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)' }}>
              🏠 Home
            </button>
          )}
          {currentScreen !== 'ADMIN' && (
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
