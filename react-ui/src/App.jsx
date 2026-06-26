import React, { useState } from 'react';
import { useGameStore } from './store/gameStore';
import AuthScreen from './components/Auth/AuthScreen';
import LandingPage from './components/LandingPage';
import DashboardLayout from './components/Dashboard/DashboardLayout';
import DashboardHome from './components/Dashboard/DashboardHome';
import GamePlayBoard from './components/GamePlay/GamePlayBoard';
import AdminConsole from './components/Admin/AdminConsole';

const ADMIN_USERNAME = 'AdminUserFoo';

function App() {
  const { user, currentScreen, activeGameId } = useGameStore();
  const [isPlayClicked, setIsPlayClicked] = useState(false);
  const isAdmin = user?.name === ADMIN_USERNAME;

  if (!user) {
    if (!isPlayClicked) {
      return <LandingPage onPlayNow={() => setIsPlayClicked(true)} />;
    }
    return (
      <div style={{ position: 'relative' }}>
        {/* Simple floating back button */}
        <button 
          onClick={() => setIsPlayClicked(false)}
          style={{
            position: 'absolute',
            top: '20px',
            left: '20px',
            background: 'rgba(255, 255, 255, 0.05)',
            border: '1px solid rgba(255, 255, 255, 0.1)',
            color: '#94a3b8',
            fontSize: '12px',
            padding: '6px 12px',
            borderRadius: '9999px',
            cursor: 'pointer',
            zIndex: 10
          }}
        >
          ← Back to Info
        </button>
        <AuthScreen />
      </div>
    );
  }

  return (
    <DashboardLayout>
      <div style={{ display: currentScreen === 'HOME' ? 'block' : 'none' }}>
        <DashboardHome />
      </div>
      {isAdmin && (
        <div style={{ display: currentScreen === 'ADMIN' ? 'block' : 'none' }}>
          <AdminConsole />
        </div>
      )}
      {activeGameId && (
        <div style={{ display: currentScreen === 'GAME' ? 'block' : 'none' }}>
          <GamePlayBoard />
        </div>
      )}
    </DashboardLayout>
  );
}

export default App;
