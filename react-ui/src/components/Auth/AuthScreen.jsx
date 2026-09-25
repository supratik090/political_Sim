import React, { useState, useEffect } from 'react';
import { useGameStore } from '../../store/gameStore';
import { loginUser, registerUser, requestForgotPasswordOtp, resetPasswordWithOtp, fetchScenarios, getApiBaseUrl } from '../../api/apiClient';

export default function AuthScreen() {
  const [authMode, setAuthMode] = useState('LOGIN'); // 'LOGIN', 'REGISTER', 'FORGOT_STEP_1', 'FORGOT_STEP_2'
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [showPassword, setShowPassword] = useState(false);

  // Forgot Password flow states
  const [otpCode, setOtpCode] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [showNewPassword, setShowNewPassword] = useState(false);
  const [generatedOtp, setGeneratedOtp] = useState('');
  const [successMsg, setSuccessMsg] = useState('');
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

  const handleAuthSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccessMsg('');
    
    if (!email || !password || (authMode === 'REGISTER' && !name)) {
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

  const handleSendOtp = async (e) => {
    e.preventDefault();
    setError('');
    setSuccessMsg('');

    if (!email) {
      setError('Please enter your email address.');
      return;
    }

    const normalizedEmail = email.trim().toLowerCase();
    setLoading(true);

    try {
      const res = await requestForgotPasswordOtp({ email: normalizedEmail });
      setGeneratedOtp(res.otp || '');
      setSuccessMsg(`📩 OTP Code generated and sent to ${normalizedEmail}!`);
      setAuthMode('FORGOT_STEP_2');
    } catch (err) {
      console.error('Forgot password OTP error:', err);
      setError(err.message || 'Failed to generate OTP. Please check email address.');
    } finally {
      setLoading(false);
    }
  };

  const handleResetPassword = async (e) => {
    e.preventDefault();
    setError('');
    setSuccessMsg('');

    if (!otpCode || !newPassword) {
      setError('Please enter both OTP code and your new password.');
      return;
    }

    const normalizedEmail = email.trim().toLowerCase();
    setLoading(true);

    try {
      const res = await resetPasswordWithOtp({
        email: normalizedEmail,
        otp: otpCode.trim(),
        newPassword: newPassword
      });
      setSuccessMsg(res.message || '✅ Password reset successfully! You can now log in.');
      setPassword('');
      setOtpCode('');
      setNewPassword('');
      setGeneratedOtp('');
      setAuthMode('LOGIN');
    } catch (err) {
      console.error('Reset password error:', err);
      setError(err.message || 'Failed to reset password. Please verify OTP code.');
    } finally {
      setLoading(false);
    }
  };

  const isLogin = authMode === 'LOGIN';
  const isRegister = authMode === 'REGISTER';

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
        <h1 style={{ fontSize: 'clamp(22px, 5vw, 36px)', fontWeight: 900, color: '#ffffff', margin: 0, letterSpacing: '-0.02em', lineHeight: 1.2 }}>
          Statecraft
        </h1>
      </div>

      {/* Auth Form Container */}
      <div className="unified-card" style={{ maxWidth: '400px', width: '100%' }}>
        
        {/* Navigation Tabs for Sign In & Register */}
        {(isLogin || isRegister) && (
          <div style={{ display: 'flex', marginBottom: '20px', gap: '10px' }}>
            <button 
              type="button"
              className={isLogin ? 'selected' : ''} 
              onClick={() => { setAuthMode('LOGIN'); setError(''); setSuccessMsg(''); }} 
              style={{ flex: 1 }}
            >
              Sign In
            </button>
            <button 
              type="button"
              className={isRegister ? 'selected' : ''} 
              onClick={() => { setAuthMode('REGISTER'); setError(''); setSuccessMsg(''); }} 
              style={{ flex: 1 }}
            >
              Register
            </button>
          </div>
        )}

        <h3 style={{ textAlign: 'center', marginTop: 0, marginBottom: '20px' }}>
          {isLogin && 'Welcome Back'}
          {isRegister && 'Create an Account'}
          {authMode === 'FORGOT_STEP_1' && '🔑 Reset Password (Step 1/2)'}
          {authMode === 'FORGOT_STEP_2' && '🔐 Enter OTP & New Password'}
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

        {/* OTP Email Dispatch Confirmation Banner (Step 2) */}
        {authMode === 'FORGOT_STEP_2' && (
          <div style={{
            background: 'rgba(59, 130, 246, 0.12)',
            border: '1.5px solid #3b82f6',
            color: '#1d4ed8',
            padding: '12px 14px',
            borderRadius: '10px',
            marginBottom: '16px',
            textAlign: 'center',
            fontSize: '13px',
            fontWeight: 700,
            lineHeight: 1.4
          }}>
            📩 A 6-digit OTP code has been sent to your email:
            <span style={{ display: 'block', fontSize: '14px', fontWeight: 900, color: '#1e40af', marginTop: '3px' }}>
              {email}
            </span>
            <span style={{ display: 'block', fontSize: '11px', fontWeight: 500, color: 'var(--text-secondary)', marginTop: '4px' }}>
              Please check your inbox (and spam folder) and enter the code below.
            </span>
          </div>
        )}

        {/* LOGIN / REGISTER FORM */}
        {(isLogin || isRegister) && (
          <form onSubmit={handleAuthSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            {isRegister && (
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
              <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: 'var(--text-secondary)' }}>
                {isLogin ? 'Email Address or User ID' : 'Email'}
              </label>
              <input 
                type={isLogin ? 'text' : 'email'} 
                placeholder={isLogin ? 'Email, User ID, or Name' : 'you@example.com'} 
                value={email} 
                onChange={(e) => setEmail(e.target.value)} 
              />
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                <label style={{ fontSize: '13px', fontWeight: 700, margin: 0, color: 'var(--text-secondary)' }}>Password</label>
                {isLogin && (
                  <button
                    type="button"
                    onClick={() => { setAuthMode('FORGOT_STEP_1'); setError(''); setSuccessMsg(''); }}
                    style={{
                      background: 'none',
                      border: 'none',
                      color: 'var(--primary-dark)',
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
                  style={{ width: '100%', paddingRight: '42px', boxSizing: 'border-box' }}
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

            <button type="submit" disabled={loading} style={{ marginTop: '10px', width: '100%', minHeight: '42px', fontSize: '14px', fontWeight: '800', borderRadius: '8px' }}>
              {loading ? 'Please wait...' : (isLogin ? 'Login' : 'Register')}
            </button>
          </form>
        )}

        {/* FORGOT PASSWORD STEP 1 FORM */}
        {authMode === 'FORGOT_STEP_1' && (
          <form onSubmit={handleSendOtp} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <p style={{ fontSize: '13px', color: 'var(--text-secondary)', margin: '0 0 10px 0', lineHeight: 1.4 }}>
              Enter your registered email address. We will generate and send a 6-digit OTP code to reset your password.
            </p>
            <div>
              <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: 'var(--text-secondary)' }}>Registered Email</label>
              <input 
                type="email" 
                placeholder="you@example.com" 
                value={email} 
                onChange={(e) => setEmail(e.target.value)} 
              />
            </div>

            <button type="submit" disabled={loading} style={{ marginTop: '10px', width: '100%', minHeight: '42px', fontSize: '14px', fontWeight: '800', borderRadius: '8px' }}>
              {loading ? 'Sending OTP...' : 'Send OTP Code'}
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

        {/* FORGOT PASSWORD STEP 2 FORM */}
        {authMode === 'FORGOT_STEP_2' && (
          <form onSubmit={handleResetPassword} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            <div>
              <label style={{ fontSize: '13px', fontWeight: 700, marginBottom: '6px', display: 'block', color: 'var(--text-secondary)' }}>6-Digit OTP Code</label>
              <input 
                type="text" 
                placeholder="123456" 
                maxLength={6}
                value={otpCode} 
                onChange={(e) => setOtpCode(e.target.value)} 
                style={{ letterSpacing: '4px', fontWeight: 900, textAlign: 'center', fontSize: '16px' }}
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
