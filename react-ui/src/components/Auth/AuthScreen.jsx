import React, { useState, useEffect } from 'react';
import { useGameStore } from '../../store/gameStore';
import { loginUser, registerUser, fetchScenarios } from '../../api/apiClient';

export default function AuthScreen() {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const login = useGameStore((state) => state.login);

  useEffect(() => {
    // Wake up the backend server on mount to reduce initial user waiting time
    fetchScenarios().catch(err => {
      console.warn("Background server warmup call pending/failed:", err);
    });
  }, []);

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
        padding: '40px 50px',
        borderRadius: '16px',
        border: '2px solid var(--primary-dark)',
        textAlign: 'center',
        boxShadow: '0 10px 30px rgba(33,60,81,0.05)',
        maxWidth: '600px',
        width: '100%',
        marginBottom: '30px',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center'
      }}>
        <img src="/politics.svg" alt="Political Sim Logo" style={{ width: '80px', height: '80px', marginBottom: '20px', borderRadius: '12px', boxShadow: '0 4px 15px rgba(0,0,0,0.2)' }} />
        <span style={{ fontSize: '14px', color: '#ffffff', textTransform: 'uppercase', fontWeight: 800, letterSpacing: '0.15em', display: 'block', marginBottom: '10px', opacity: 0.9 }}>
          GRAND ELECTION STRATEGY
        </span>
        <h1 style={{ fontSize: '36px', fontWeight: 900, color: '#ffffff', margin: 0, letterSpacing: '-0.02em' }}>
          Indian Politics Simulation
        </h1>
        <p style={{ fontSize: '15px', color: '#ffffff', opacity: 0.95, marginTop: '12px', marginBottom: 0, lineHeight: 1.5 }}>
          Sign in or register to govern state campaigns, design coalition policies, and maintain election sessions.
        </p>
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
              <label style={{ fontSize: '12px', fontWeight: 700, marginBottom: '5px', display: 'block' }}>Full Name</label>
              <input 
                type="text" 
                placeholder="Name" 
                value={name} 
                onChange={(e) => setName(e.target.value)} 
              />
            </div>
          )}
          
          <div>
            <label style={{ fontSize: '12px', fontWeight: 700, marginBottom: '5px', display: 'block' }}>Email</label>
            <input 
              type="email" 
              placeholder="you@example.com" 
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
            />
          </div>

          <div>
            <label style={{ fontSize: '12px', fontWeight: 700, marginBottom: '5px', display: 'block' }}>Password</label>
            <input 
              type="password" 
              placeholder="••••••••" 
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
            />
          </div>

          <button type="submit" disabled={loading} style={{ marginTop: '10px', width: '100%' }}>
            {loading ? 'Please wait...' : (isLogin ? 'Login' : 'Register')}
          </button>
        </form>
      </div>

    </div>
  );
}
