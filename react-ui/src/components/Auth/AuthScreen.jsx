import React, { useState, useEffect } from 'react';
import { useGameStore } from '../../store/gameStore';
import { loginUser, registerUser, fetchScenarios, getApiBaseUrl } from '../../api/apiClient';

export default function AuthScreen() {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [serverStatus, setServerStatus] = useState('CHECKING'); // 'ONLINE', 'OFFLINE', 'CHECKING'
  const [currentApiUrl, setCurrentApiUrl] = useState(getApiBaseUrl());
  const [showUrlModal, setShowUrlModal] = useState(false);
  const [customUrlInput, setCustomUrlInput] = useState(currentApiUrl);
  const login = useGameStore((state) => state.login);

  const checkConnection = () => {
    setServerStatus('CHECKING');
    fetchScenarios()
      .then(() => {
        setServerStatus('ONLINE');
        setCurrentApiUrl(getApiBaseUrl());
      })
      .catch(err => {
        console.warn("Background server warmup call failed:", err);
        setServerStatus('OFFLINE');
        setCurrentApiUrl(getApiBaseUrl());
      });
  };

  useEffect(() => {
    checkConnection();
  }, [currentApiUrl]);

  const handleSaveCustomUrl = (newUrl) => {
    let formatted = (newUrl || '').trim();
    if (formatted) {
      if (!formatted.startsWith('http://') && !formatted.startsWith('https://')) {
        formatted = 'http://' + formatted;
      }
      localStorage.setItem('CUSTOM_API_URL', formatted);
    } else {
      localStorage.removeItem('CUSTOM_API_URL');
    }
    const updated = getApiBaseUrl();
    setCurrentApiUrl(updated);
    setShowUrlModal(false);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    if (!email || !password || (!isLogin && !name)) {
      setError('Please fill out all fields.');
      return;
    }
    
    const normalizedEmail = email.trim().toLowerCase();
    setLoading(true);

    try {
      let userData;
      if (isLogin) {
        userData = await loginUser({ email: normalizedEmail, password });
      } else {
        userData = await registerUser({ name: name.trim(), email: normalizedEmail, password });
      }
      login(userData);
    } catch (err) {
      console.error('Authentication error:', err);
      setError(err.message || 'Authentication failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', padding: '20px' }}>
      
      {/* Banner */}
      <div style={{
        background: 'var(--primary-border)',
        padding: 'clamp(24px, 5vw, 40px) clamp(20px, 6vw, 50px)',
        borderRadius: '16px',
        border: '2px solid var(--primary-dark)',
        textAlign: 'center',
        boxShadow: '0 10px 30px rgba(26,52,72,0.05)',
        maxWidth: '600px',
        width: '100%',
        marginBottom: '28px',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center'
      }}>
        <img src="/app-logo.png" alt="Statecraft Logo" style={{ width: '80px', height: '80px', marginBottom: '18px', borderRadius: '16px', boxShadow: '0 8px 25px rgba(0,0,0,0.3)' }} />
        <span style={{ fontSize: '13px', color: '#ffffff', textTransform: 'uppercase', fontWeight: 800, letterSpacing: '0.15em', display: 'block', marginBottom: '10px', opacity: 0.9 }}>
          RULES OF STATECRAFT
        </span>
        <h1 style={{ fontSize: 'clamp(22px, 5vw, 36px)', fontWeight: 900, color: '#ffffff', margin: 0, letterSpacing: '-0.02em', lineHeight: 1.2 }}>
          Statecraft
        </h1>
      </div>

      {/* Auth Form Container */}
      <div className="unified-card" style={{ maxWidth: '400px', width: '100%' }}>
        <div style={{ display: 'flex', marginBottom: '20px', gap: '10px' }}>
          <button 
            className={isLogin ? 'selected' : ''} 
            onClick={() => setIsLogin(true)} 
            style={{ flex: 1 }}
          >
            Sign In
          </button>
          <button 
            className={!isLogin ? 'selected' : ''} 
            onClick={() => setIsLogin(false)} 
            style={{ flex: 1 }}
          >
            Register
          </button>
        </div>

        <h3 style={{ textAlign: 'center', marginTop: 0, marginBottom: '20px' }}>
          {isLogin ? 'Welcome Back' : 'Create an Account'}
        </h3>

        {error && (
          <div style={{
            background: 'rgba(210, 63, 49, 0.1)',
            border: '1px solid #d23f31',
            color: '#d23f31',
            padding: '10px',
            borderRadius: '8px',
            marginBottom: '15px',
            fontSize: '13px',
            fontWeight: 700,
            textAlign: 'center',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '6px'
          }}>
            <span>⚠️</span> {error}
          </div>
        )}

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
          {!isLogin && (
            <div>
              <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: 'var(--text-secondary)' }}>Full Name</label>
              <input 
                type="text" 
                placeholder="Name" 
                value={name} 
                onChange={(e) => setName(e.target.value)} 
              />
            </div>
          )}
          
          <div>
            <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: 'var(--text-secondary)' }}>Email</label>
            <input 
              type="email" 
              placeholder="you@example.com" 
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
            />
          </div>

          <div>
            <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: 'var(--text-secondary)' }}>Password</label>
            <input 
              type="password" 
              placeholder="••••••••" 
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
            />
          </div>

          <button type="submit" disabled={loading} style={{ marginTop: '16px', width: '100%', minHeight: '52px', fontSize: '16px', fontWeight: '800', borderRadius: '12px' }}>
            {loading ? 'Please wait...' : (isLogin ? 'Login' : 'Register')}
          </button>
        </form>

        {/* Backend Connection Bar */}
        <div style={{ marginTop: '24px', paddingTop: '16px', borderTop: '1px dashed var(--card-border)', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '8px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '12px', fontWeight: 700 }}>
            <span style={{
              display: 'inline-block', width: '9px', height: '9px', borderRadius: '50%',
              backgroundColor: serverStatus === 'ONLINE' ? '#16A34A' : serverStatus === 'OFFLINE' ? '#DC2626' : '#F59E0B',
              boxShadow: serverStatus === 'ONLINE' ? '0 0 6px #16A34A' : 'none'
            }} />
            <span style={{ color: serverStatus === 'ONLINE' ? '#16A34A' : serverStatus === 'OFFLINE' ? '#DC2626' : '#F59E0B' }}>
              {serverStatus === 'ONLINE' ? 'Backend Connected' : serverStatus === 'OFFLINE' ? 'Backend Disconnected' : 'Checking Connection...'}
            </span>
          </div>

          <div style={{ fontSize: '11px', color: 'var(--text-secondary)', textAlign: 'center', wordBreak: 'break-all' }}>
            Target: <code style={{ background: 'rgba(0,0,0,0.05)', padding: '2px 6px', borderRadius: '4px' }}>{currentApiUrl}</code>
          </div>

          <div style={{ display: 'flex', gap: '8px', marginTop: '4px' }}>
            <button 
              type="button"
              onClick={checkConnection}
              style={{ background: 'transparent', border: '1px solid var(--card-border)', color: 'var(--text-secondary)', fontSize: '11px', padding: '4px 10px', borderRadius: '6px', cursor: 'pointer' }}
            >
              🔄 Retry
            </button>
            <button 
              type="button"
              onClick={() => { setCustomUrlInput(currentApiUrl); setShowUrlModal(true); }}
              style={{ background: 'transparent', border: '1px solid var(--card-border)', color: 'var(--text-primary)', fontSize: '11px', fontWeight: 700, padding: '4px 10px', borderRadius: '6px', cursor: 'pointer' }}
            >
              ⚙️ Change Server IP
            </button>
          </div>
        </div>
      </div>

      {/* URL Switcher Modal */}
      {showUrlModal && (
        <div style={{
          position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
          background: 'rgba(0,0,0,0.6)', backdropFilter: 'blur(4px)',
          display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '20px'
        }}>
          <div style={{ background: '#ffffff', borderRadius: '16px', padding: '24px', maxWidth: '420px', width: '100%', boxShadow: '0 20px 40px rgba(0,0,0,0.3)' }}>
            <h3 style={{ margin: '0 0 8px 0', fontSize: '18px', fontWeight: 900, color: 'var(--primary-dark)' }}>⚙️ Change Backend Server URL</h3>
            <p style={{ fontSize: '13px', color: 'var(--text-secondary)', margin: '0 0 16px 0', lineHeight: 1.5 }}>
              Enter the backend server address (e.g. your local Wi-Fi IP, Emulator IP, or Cloud URL):
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginBottom: '16px' }}>
              <button 
                type="button"
                onClick={() => setCustomUrlInput('http://192.168.29.219:7810')}
                style={{ textAlign: 'left', padding: '8px 12px', fontSize: '12px', background: 'rgba(0,0,0,0.03)', border: '1px solid var(--card-border)', borderRadius: '8px', cursor: 'pointer' }}
              >
                📡 <strong>Local Wi-Fi IP:</strong> http://192.168.29.219:7810
              </button>
              <button 
                type="button"
                onClick={() => setCustomUrlInput('http://10.0.2.2:7810')}
                style={{ textAlign: 'left', padding: '8px 12px', fontSize: '12px', background: 'rgba(0,0,0,0.03)', border: '1px solid var(--card-border)', borderRadius: '8px', cursor: 'pointer' }}
              >
                🤖 <strong>Android Emulator IP:</strong> http://10.0.2.2:7810
              </button>
              <button 
                type="button"
                onClick={() => setCustomUrlInput('https://political-sim.onrender.com')}
                style={{ textAlign: 'left', padding: '8px 12px', fontSize: '12px', background: 'rgba(0,0,0,0.03)', border: '1px solid var(--card-border)', borderRadius: '8px', cursor: 'pointer' }}
              >
                ☁️ <strong>Render Cloud Server:</strong> https://political-sim.onrender.com
              </button>
            </div>

            <input 
              type="text" 
              value={customUrlInput}
              onChange={(e) => setCustomUrlInput(e.target.value)}
              placeholder="http://192.168.29.219:7810"
              style={{ width: '100%', padding: '10px 12px', fontSize: '13px', borderRadius: '8px', border: '1.5px solid var(--card-border)', marginBottom: '20px' }}
            />

            <div style={{ display: 'flex', gap: '10px', justifyContent: 'flex-end' }}>
              <button 
                type="button" 
                onClick={() => setShowUrlModal(false)}
                style={{ background: 'transparent', border: '1px solid var(--card-border)', padding: '8px 16px', borderRadius: '8px', fontSize: '13px', cursor: 'pointer' }}
              >
                Cancel
              </button>
              <button 
                type="button" 
                onClick={() => handleSaveCustomUrl(customUrlInput)}
                style={{ background: 'var(--primary-dark)', color: '#ffffff', border: 'none', padding: '8px 18px', borderRadius: '8px', fontSize: '13px', fontWeight: 700, cursor: 'pointer' }}
              >
                Save &amp; Connect
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}
