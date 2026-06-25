import React from 'react';
import { useGameStore } from '../../store/gameStore';

const ADMIN_USERNAME = 'AdminUserFoo';

export default function DashboardLayout({ children }) {
  const { user, logout, currentScreen, setScreen } = useGameStore();
  const isAdmin = user?.name === ADMIN_USERNAME;

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
