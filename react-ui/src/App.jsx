import React from 'react';
import { useGameStore } from './store/gameStore';
import AuthScreen from './components/Auth/AuthScreen';
import DashboardLayout from './components/Dashboard/DashboardLayout';
import DashboardHome from './components/Dashboard/DashboardHome';
import GamePlayBoard from './components/GamePlay/GamePlayBoard';
import AdminConsole from './components/Admin/AdminConsole';

const ADMIN_USERNAME = 'AdminUserFoo';

function App() {
  const { user, currentScreen, activeGameId } = useGameStore();
  const isAdmin = user?.name === ADMIN_USERNAME;

  if (!user) {
    return <AuthScreen />;
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
