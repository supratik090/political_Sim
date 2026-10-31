import React, { useState, useEffect } from 'react';
import { useGameStore } from '../../store/gameStore';
import {
  loginUser,
  registerUser,
  getSecretQuestion,
  resetPasswordWithSecretQuestion,
  fetchScenarios,
  getApiBaseUrl
} from '../../api/apiClient';
import { isAndroidApp } from '../../utils/platform';

const PRESET_SECURITY_QUESTIONS = [
  'What was the name of your first school?',
  'What is your favorite book or movie?',
  'What city were you born in?',
  "What is your mother's maiden name?",
  'What was your childhood nickname?'
];

export default function AuthScreen() {
  const [authMode, setAuthMode] = useState('LOGIN'); // 'LOGIN', 'REGISTER', 'FORGOT_STEP_1', 'FORGOT_STEP_2'
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [showPassword, setShowPassword] = useState(false);

  // Security question state
  const [selectedQuestion, setSelectedQuestion] = useState(PRESET_SECURITY_QUESTIONS[0]);
  const [secretAnswer, setSecretAnswer] = useState('');
  const [retrievedQuestion, setRetrievedQuestion] = useState('');

  // Password reset state
  const [newPassword, setNewPassword] = useState('');
  const [showNewPassword, setShowNewPassword] = useState(false);
  const [successMsg, setSuccessMsg] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const isAndroid = isAndroidApp();
  const [serverStatus, setServerStatus] = useState(isAndroid ? 'ONLINE' : 'CHECKING');
  const [currentApiUrl, setCurrentApiUrl] = useState(getApiBaseUrl());
  const [showUrlModal, setShowUrlModal] = useState(false);
  const [customUrlInput, setCustomUrlInput] = useState(currentApiUrl);
  const login = useGameStore((state) => state.login);

  const checkConnection = () => {
    if (isAndroid) {
      setServerStatus('ONLINE');
      return;
    }
    setServerStatus('CHECKING');
    fetchScenarios()
      .then(() => {
        setServerStatus('ONLINE');
        setCurrentApiUrl(getApiBaseUrl());
      })
      .catch((err) => {
        console.warn('Background server warmup call failed:', err);
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

  const handleAuthSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccessMsg('');

    if (!email || !password || (authMode === 'REGISTER' && (!name || !secretAnswer))) {
      setError('Please fill out all fields.');
      return;
    }

    const normalizedEmail = email.trim().toLowerCase();
    setLoading(true);

    try {
      let userData;
      if (authMode === 'LOGIN') {
        userData = await loginUser({ email: normalizedEmail, password });
      } else {
        userData = await registerUser({
          name: name.trim(),
          email: normalizedEmail,
          password,
          secretQuestion: selectedQuestion,
          secretAnswer: secretAnswer.trim()
        });
      }
      login(userData);
    } catch (err) {
      console.error('Authentication error:', err);
      setError(err.message || 'Authentication failed. Please check your credentials.');
    } finally {
      setLoading(false);
    }
  };

  const handleFetchSecretQuestion = async (e) => {
    e.preventDefault();
    setError('');
    setSuccessMsg('');

    if (!email) {
      setError('Please enter your email address or user ID.');
      return;
    }

    const normalizedEmail = email.trim().toLowerCase();
    setLoading(true);

    try {
      const res = await getSecretQuestion({ email: normalizedEmail });
      setRetrievedQuestion(res.secretQuestion || PRESET_SECURITY_QUESTIONS[0]);
      setAuthMode('FORGOT_STEP_2');
    } catch (err) {
      console.error('Get secret question error:', err);
      setError(err.message || 'No account found with this user ID or email.');
    } finally {
      setLoading(false);
    }
  };

  const handleResetPassword = async (e) => {
    e.preventDefault();
    setError('');
    setSuccessMsg('');

    if (!secretAnswer || !newPassword) {
      setError('Please provide your secret answer and new password.');
      return;
    }

    const normalizedEmail = email.trim().toLowerCase();
    setLoading(true);

    try {
      const res = await resetPasswordWithSecretQuestion({
        email: normalizedEmail,
        secretAnswer: secretAnswer.trim(),
        newPassword: newPassword
      });
      setSuccessMsg(res.message || '✅ Password reset successfully! You can now log in.');
      setPassword('');
      setSecretAnswer('');
      setNewPassword('');
      setAuthMode('LOGIN');
    } catch (err) {
      console.error('Reset password error:', err);
      setError(err.message || 'Failed to reset password. Incorrect secret answer.');
    } finally {
      setLoading(false);
    }
  };

  const isLogin = authMode === 'LOGIN';
  const isRegister = authMode === 'REGISTER';

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '100vh', padding: '20px', background: 'linear-gradient(180deg, #FFE4C7 0%, #FFF8EC 48%, #DFF2DB 100%)' }}>
      
      {/* Banner */}
      <div style={{
        background: '#0B2A6F',
        padding: '28px 20px',
        borderRadius: '16px',
        textAlign: 'center',
        boxShadow: '0 12px 30px rgba(11,42,111,0.25)',
        maxWidth: '420px',
        width: '100%',
        marginBottom: '20px',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        position: 'relative',
        overflow: 'hidden'
      }}>
        {/* Subtle Ashoka Chakra watermark in background */}
        <svg style={{ position: 'absolute', right: '-25px', top: '-25px', width: '160px', height: '160px', opacity: 0.12, pointerEvents: 'none' }} viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="46" fill="none" stroke="#FFFFFF" strokeWidth="2.5" />
          <circle cx="50" cy="50" r="8" fill="none" stroke="#FFFFFF" strokeWidth="2" />
          {Array.from({ length: 24 }).map((_, i) => (
            <line
              key={i}
              x1="50"
              y1="50"
              x2={50 + 46 * Math.cos((i * 15 * Math.PI) / 180)}
              y2={50 + 46 * Math.sin((i * 15 * Math.PI) / 180)}
              stroke="#FFFFFF"
              strokeWidth="1.2"
            />
          ))}
        </svg>

        {/* Logo in rounded white square */}
        <div style={{
          backgroundColor: '#FFFFFF',
          padding: '8px',
          borderRadius: '14px',
          boxShadow: '0 4px 12px rgba(0,0,0,0.18)',
          display: 'inline-flex',
          alignItems: 'center',
          justifyContent: 'center',
          marginBottom: '10px'
        }}>
          <img src="/app-logo.png" alt="Statecraft Logo" style={{ width: '48px', height: '48px', objectFit: 'contain' }} />
        </div>

        <h1 style={{ fontSize: '26px', fontWeight: 900, color: '#ffffff', margin: 0, letterSpacing: '-0.02em', lineHeight: 1.2 }}>
          Statecraft
        </h1>

        {/* Tricolor accent stripe at bottom */}
        <div style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: '4px',
          background: 'linear-gradient(to right, #FF9933 0%, #FF9933 33.33%, #FFFFFF 33.33%, #FFFFFF 66.66%, #138808 66.66%, #138808 100%)'
        }} />
      </div>

      {/* Auth Form Container */}
      <div className="unified-card" style={{ maxWidth: '420px', width: '100%', backgroundColor: '#FFFDF8', border: '1.5px solid #CBD5E1', borderRadius: '16px', padding: '22px' }}>
        
        {/* Navigation Tabs for Sign In & Register */}
        {(isLogin || isRegister) && (
          <div style={{ display: 'flex', marginBottom: '20px', gap: '10px' }}>
            <button 
              type="button"
              onClick={() => { setAuthMode('LOGIN'); setError(''); setSuccessMsg(''); }} 
              style={{
                flex: 1,
                backgroundColor: isLogin ? '#0B2A6F' : '#FFFFFF',
                color: isLogin ? '#FFFFFF' : '#0B2A6F',
                border: isLogin ? '1.5px solid #0B2A6F' : '1.5px solid #CBD5E1',
                borderRadius: '8px',
                fontWeight: 700,
                fontSize: '14px',
                padding: '9px 12px',
                cursor: 'pointer'
              }}
            >
              Sign In
            </button>
            <button 
              type="button"
              onClick={() => { setAuthMode('REGISTER'); setError(''); setSuccessMsg(''); }} 
              style={{
                flex: 1,
                backgroundColor: isRegister ? '#0B2A6F' : '#FFFFFF',
                color: isRegister ? '#FFFFFF' : '#0B2A6F',
                border: isRegister ? '1.5px solid #0B2A6F' : '1.5px solid #CBD5E1',
                borderRadius: '8px',
                fontWeight: 700,
                fontSize: '14px',
                padding: '9px 12px',
                cursor: 'pointer'
              }}
            >
              Register
            </button>
          </div>
        )}

        <h3 style={{ textAlign: 'center', marginTop: 0, marginBottom: '20px', color: '#0B2A6F', fontSize: '20px', fontWeight: 800 }}>
          {isLogin && 'Welcome Back'}
          {isRegister && 'Create an Account'}
          {authMode === 'FORGOT_STEP_1' && '🔑 Reset Password (Step 1/2)'}
          {authMode === 'FORGOT_STEP_2' && '🔐 Answer Question & Set Password'}
        </h3>

        {/* Success Message Banner */}
        {successMsg && (
          <div style={{
            background: 'rgba(16, 185, 129, 0.1)',
            border: '1px solid #10b981',
            color: '#059669',
            padding: '10px 14px',
            borderRadius: '8px',
            marginBottom: '15px',
            fontSize: '13px',
            fontWeight: 700,
            textAlign: 'center',
            lineHeight: 1.4
          }}>
            {successMsg}
          </div>
        )}

        {/* Error Banner */}
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

        {/* LOGIN / REGISTER FORM */}
        {(isLogin || isRegister) && (
          <form onSubmit={handleAuthSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            {isRegister && (
              <div>
                <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: '#0B2A6F' }}>Full Name</label>
                <input 
                  type="text" 
                  placeholder="Player Name" 
                  value={name} 
                  onChange={(e) => setName(e.target.value)} 
                  style={{ width: '100%', backgroundColor: '#FFFFFF', color: '#0F1C28', border: '1.5px solid #CBD5E1', borderRadius: '8px' }}
                />
              </div>
            )}
            
            <div>
              <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: '#0B2A6F' }}>
                {isLogin ? 'Email Address or User ID' : 'User ID / Email'}
              </label>
              <input 
                type="text" 
                placeholder={isLogin ? 'Email or User ID' : 'player1 or you@example.com'} 
                value={email} 
                onChange={(e) => setEmail(e.target.value)} 
                style={{ width: '100%', backgroundColor: '#FFFFFF', color: '#0F1C28', border: '1.5px solid #CBD5E1', borderRadius: '8px' }}
              />
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                <label style={{ fontSize: '13px', fontWeight: 700, margin: 0, color: '#0B2A6F' }}>Password</label>
                {isLogin && (
                  <button
                    type="button"
                    onClick={() => { setAuthMode('FORGOT_STEP_1'); setError(''); setSuccessMsg(''); }}
                    style={{
                      background: 'none',
                      border: 'none',
                      color: '#0B2A6F',
                      fontSize: '12px',
                      fontWeight: 700,
                      cursor: 'pointer',
                      padding: 0,
                      textDecoration: 'underline'
                    }}
                  >
                    Forgot Password?
                  </button>
                )}
              </div>
              <div style={{ position: 'relative' }}>
                <input 
                  type={showPassword ? 'text' : 'password'} 
                  placeholder="••••••••" 
                  value={password} 
                  onChange={(e) => setPassword(e.target.value)} 
                  style={{ width: '100%', paddingRight: '42px', boxSizing: 'border-box', backgroundColor: '#FFFFFF', color: '#0F1C28', border: '1.5px solid #CBD5E1', borderRadius: '8px' }}
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  style={{
                    position: 'absolute',
                    right: '10px',
                    top: '50%',
                    transform: 'translateY(-50%)',
                    background: 'none',
                    border: 'none',
                    cursor: 'pointer',
                    fontSize: '16px',
                    padding: '4px',
                    lineHeight: 1
                  }}
                  title={showPassword ? 'Hide Password' : 'Show Password'}
                >
                  {showPassword ? '🙈' : '👁️'}
                </button>
              </div>
            </div>

            {/* Secret Question & Answer fields for Registration */}
            {isRegister && (
              <>
                <div>
                  <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: '#0B2A6F' }}>
                    Security Question (for password recovery)
                  </label>
                  <select
                    value={selectedQuestion}
                    onChange={(e) => setSelectedQuestion(e.target.value)}
                    style={{ width: '100%', padding: '8px 10px', fontSize: '13px', borderRadius: '8px', border: '1.5px solid #CBD5E1', backgroundColor: '#FFFFFF', color: '#0F1C28' }}
                  >
                    {PRESET_SECURITY_QUESTIONS.map((q, idx) => (
                      <option key={idx} value={q}>{q}</option>
                    ))}
                  </select>
                </div>

                <div>
                  <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: '#0B2A6F' }}>
                    Secret Answer
                  </label>
                  <input
                    type="text"
                    placeholder="Your secret answer"
                    value={secretAnswer}
                    onChange={(e) => setSecretAnswer(e.target.value)}
                    style={{ width: '100%', backgroundColor: '#FFFFFF', color: '#0F1C28', border: '1.5px solid #CBD5E1', borderRadius: '8px' }}
                  />
                </div>
              </>
            )}

            <button 
              type="submit" 
              disabled={loading} 
              style={{ 
                marginTop: '15px', 
                width: '100%', 
                minHeight: '46px', 
                fontSize: '15px', 
                fontWeight: '800', 
                borderRadius: '10px',
                backgroundColor: '#FF9933',
                color: '#FFFFFF',
                border: 'none',
                boxShadow: '0 4px 14px rgba(255, 153, 51, 0.4)',
                cursor: 'pointer'
              }}
            >
              {loading ? 'Please wait...' : (isLogin ? 'Login' : 'Register')}
            </button>
          </form>
        )}

        {/* FORGOT PASSWORD STEP 1 FORM (Find Account) */}
        {authMode === 'FORGOT_STEP_1' && (
          <form onSubmit={handleFetchSecretQuestion} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <p style={{ fontSize: '13px', color: 'var(--text-secondary)', margin: '0 0 10px 0', lineHeight: 1.4 }}>
              Enter your registered User ID or Email to answer your security question and reset your password.
            </p>
            <div>
              <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: 'var(--text-secondary)' }}>User ID or Email</label>
              <input 
                type="text" 
                placeholder="User ID or Email" 
                value={email} 
                onChange={(e) => setEmail(e.target.value)} 
              />
            </div>

            <button type="submit" disabled={loading} style={{ marginTop: '10px', width: '100%', minHeight: '42px', fontSize: '14px', fontWeight: '800', borderRadius: '8px' }}>
              {loading ? 'Finding account...' : 'Next → Answer Security Question'}
            </button>

            <button 
              type="button"
              onClick={() => { setAuthMode('LOGIN'); setError(''); setSuccessMsg(''); }}
              style={{ background: 'transparent', border: '1px solid var(--card-border)', color: 'var(--text-secondary)', padding: '8px', borderRadius: '8px', fontSize: '13px', fontWeight: 700, cursor: 'pointer' }}
            >
              ← Back to Sign In
            </button>
          </form>
        )}

        {/* FORGOT PASSWORD STEP 2 FORM (Answer Secret Question) */}
        {authMode === 'FORGOT_STEP_2' && (
          <form onSubmit={handleResetPassword} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <div style={{
              background: 'rgba(59, 130, 246, 0.1)',
              border: '1.5px solid #3b82f6',
              padding: '12px 14px',
              borderRadius: '10px',
              color: '#1d4ed8'
            }}>
              <span style={{ fontSize: '11px', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.04em', display: 'block', marginBottom: '4px' }}>
                Security Question:
              </span>
              <span style={{ fontSize: '14px', fontWeight: 700 }}>
                {retrievedQuestion || 'What is your security question?'}
              </span>
            </div>

            <div>
              <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: 'var(--text-secondary)' }}>Your Answer</label>
              <input 
                type="text" 
                placeholder="Enter your answer" 
                value={secretAnswer} 
                onChange={(e) => setSecretAnswer(e.target.value)} 
              />
            </div>

            <div>
              <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: 'var(--text-secondary)' }}>New Password</label>
              <div style={{ position: 'relative' }}>
                <input 
                  type={showNewPassword ? 'text' : 'password'} 
                  placeholder="Enter new password" 
                  value={newPassword} 
                  onChange={(e) => setNewPassword(e.target.value)} 
                  style={{ width: '100%', paddingRight: '42px', boxSizing: 'border-box' }}
                />
                <button
                  type="button"
                  onClick={() => setShowNewPassword(!showNewPassword)}
                  style={{
                    position: 'absolute',
                    right: '10px',
                    top: '50%',
                    transform: 'translateY(-50%)',
                    background: 'none',
                    border: 'none',
                    cursor: 'pointer',
                    fontSize: '16px',
                    padding: '4px',
                    lineHeight: 1
                  }}
                  title={showNewPassword ? 'Hide Password' : 'Show Password'}
                >
                  {showNewPassword ? '🙈' : '👁️'}
                </button>
              </div>
            </div>

            <button type="submit" disabled={loading} style={{ marginTop: '10px', width: '100%', minHeight: '42px', fontSize: '14px', fontWeight: '800', borderRadius: '8px' }}>
              {loading ? 'Resetting Password...' : 'Reset Password'}
            </button>

            <button 
              type="button"
              onClick={() => { setAuthMode('LOGIN'); setError(''); setSuccessMsg(''); }}
              style={{ background: 'transparent', border: '1px solid var(--card-border)', color: 'var(--text-secondary)', padding: '8px', borderRadius: '8px', fontSize: '13px', fontWeight: 700, cursor: 'pointer' }}
            >
              ← Back to Sign In
            </button>
          </form>
        )}
      </div>

      {/* URL Switcher Modal (Only in web browser dev mode) */}
      {!isAndroid && showUrlModal && (
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
                onClick={() => setCustomUrlInput('http://localhost:7810')}
                style={{ textAlign: 'left', padding: '8px 12px', fontSize: '12px', background: 'rgba(0,0,0,0.03)', border: '1px solid var(--card-border)', borderRadius: '8px', cursor: 'pointer' }}
              >
                💻 <strong>Localhost:</strong> http://localhost:7810
              </button>
              <button 
                type="button"
                onClick={() => setCustomUrlInput('https://political-sim-279311597920.asia-south1.run.app')}
                style={{ textAlign: 'left', padding: '8px 12px', fontSize: '12px', background: 'rgba(0,0,0,0.03)', border: '1px solid var(--card-border)', borderRadius: '8px', cursor: 'pointer' }}
              >
                ☁️ <strong>Cloud Run Server:</strong> https://political-sim-279311597920.asia-south1.run.app
              </button>
            </div>

            <input 
              type="text" 
              value={customUrlInput}
              onChange={(e) => setCustomUrlInput(e.target.value)}
              placeholder="http://localhost:7810"
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
