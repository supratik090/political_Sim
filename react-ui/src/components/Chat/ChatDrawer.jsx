import React, { useRef, useEffect, useState } from 'react';

/**
 * ChatDrawer – premium styled chat panel that matches the game UX.
 * Uses the game's design tokens: --primary-dark, --primary-border, --primary-background,
 * Montserrat font, and playerPartyColor for own message bubbles.
 *
 * Props:
 *  - isOpen: boolean
 *  - onClose: () => void
 *  - messages: [{ senderId, senderName, text, timestamp }]
 *  - sendMessage: (text) => void
 *  - chatInput: string
 *  - setChatInput: (value) => void
 *  - user: object
 *  - partyColor: string (hex) – the player's party color used for own message bubbles
 */
const ChatDrawer = ({
  isOpen,
  onClose,
  messages,
  sendMessage,
  chatInput,
  setChatInput,
  user,
  partyColor = '#213C51',
}) => {
  const scrollRef = useRef(null);
  const [vibrate, setVibrate] = useState(false);
  const prevMsgCount = useRef(messages.length);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, isOpen]);

  // Vibrate the panel when a new message arrives (even if drawer is closed)
  useEffect(() => {
    if (messages.length > prevMsgCount.current) {
      setVibrate(true);
      const t = setTimeout(() => setVibrate(false), 620);
      prevMsgCount.current = messages.length;
      return () => clearTimeout(t);
    }
    prevMsgCount.current = messages.length;
  }, [messages.length]);

  if (!isOpen) return null;

  const handleKey = (e) => {
    if (e.key === 'Enter' && chatInput.trim()) {
      sendMessage(chatInput.trim());
      setChatInput('');
    }
  };

  const handleSend = () => {
    if (chatInput.trim()) {
      sendMessage(chatInput.trim());
      setChatInput('');
    }
  };

  return (
    <div
      className={vibrate ? 'chat-panel-vibrate' : ''}
      style={{
        position: 'fixed',
        bottom: '90px',           // above the floating chat button
        right: '24px',
        width: '340px',
        height: '480px',
        borderRadius: '16px',
        boxShadow: '0 20px 50px rgba(33,60,81,0.35)',
        display: 'flex',
        flexDirection: 'column',
        zIndex: 1090,
        overflow: 'hidden',
        border: '2px solid var(--primary-border)',
        fontFamily: "'Montserrat', sans-serif",
        animation: 'chatSlideUp 0.22s cubic-bezier(0.4,0,0.2,1)',
      }}
    >
      <style>{`
        @keyframes chatSlideUp {
          from { opacity: 0; transform: translateY(20px); }
          to   { opacity: 1; transform: translateY(0); }
        }
        @keyframes chatVibrate {
          0%   { transform: translateX(0); }
          15%  { transform: translateX(-6px); }
          30%  { transform: translateX(6px); }
          45%  { transform: translateX(-5px); }
          60%  { transform: translateX(5px); }
          75%  { transform: translateX(-3px); }
          90%  { transform: translateX(3px); }
          100% { transform: translateX(0); }
        }
        .chat-panel-vibrate {
          animation: chatVibrate 0.55s ease;
        }
        .chat-msg-bubble {
          transition: transform 0.15s ease;
        }
        .chat-msg-bubble:hover {
          transform: scale(1.01);
        }
        .chat-input-field {
          background-color: var(--primary-dark) !important;
          color: #ffffff !important;
          border: 1.5px solid var(--primary-border) !important;
          border-radius: 8px !important;
          padding: 10px 12px !important;
          font-family: 'Montserrat', sans-serif !important;
          font-size: 13px !important;
          flex: 1;
          outline: none;
        }
        .chat-input-field:focus {
          border-color: var(--selected-highlight) !important;
        }
        .chat-input-field::placeholder {
          color: rgba(255,255,255,0.45) !important;
        }
        .chat-send-btn {
          background-color: var(--party-chat-color, #213C51);
          border: none;
          border-radius: 8px;
          color: #fff;
          font-family: 'Montserrat', sans-serif;
          font-weight: 700;
          font-size: 13px;
          padding: 10px 16px;
          cursor: pointer;
          transition: opacity 0.2s, transform 0.15s;
          box-shadow: none;
        }
        .chat-send-btn:hover:not(:disabled) {
          opacity: 0.85;
          transform: translateY(-1px);
          box-shadow: none;
          background-color: var(--party-chat-color, #213C51);
        }
      `}</style>

      {/* ── Header ── */}
      <div
        style={{
          padding: '12px 16px',
          background: 'var(--primary-dark)',
          color: '#fff',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{
            width: '10px', height: '10px',
            borderRadius: '50%',
            backgroundColor: partyColor,
            display: 'inline-block',
            border: '2px solid rgba(255,255,255,0.5)',
          }} />
          <span style={{ fontWeight: 800, fontSize: '14px', letterSpacing: '0.04em' }}>
            Chat
          </span>
          <span style={{
            fontSize: '10px', fontWeight: 600,
            background: 'rgba(255,255,255,0.12)',
            padding: '2px 7px', borderRadius: '999px',
            color: 'rgba(255,255,255,0.7)',
          }}>
            {messages.length} msg{messages.length !== 1 ? 's' : ''}
          </span>
        </div>
        <button
          onClick={onClose}
          style={{
            background: 'rgba(255,255,255,0.1)',
            border: '1px solid rgba(255,255,255,0.2)',
            color: '#fff',
            fontSize: '16px',
            width: '28px',
            height: '28px',
            borderRadius: '50%',
            cursor: 'pointer',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            padding: 0,
            lineHeight: 1,
            boxShadow: 'none',
          }}
          title="Close chat"
        >
          ×
        </button>
      </div>

      {/* ── Message List ── */}
      <div
        ref={scrollRef}
        style={{
          flex: 1,
          overflowY: 'auto',
          padding: '14px 14px 8px',
          background: 'var(--primary-background)',
          display: 'flex',
          flexDirection: 'column',
          gap: '10px',
        }}
      >
        {messages.length === 0 && (
          <div style={{
            flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center',
            flexDirection: 'column', gap: '8px',
            color: 'var(--text-secondary)', fontSize: '13px', textAlign: 'center',
            padding: '20px',
          }}>
            <span style={{ fontSize: '28px' }}>💬</span>
            <span>No messages yet.<br />Say hello to start the campaign chat!</span>
          </div>
        )}
        {messages.map((m, idx) => {
          const isMe = m.senderId === (user?.id || user?.email);
          return (
            <div
              key={idx}
              style={{
                alignSelf: isMe ? 'flex-end' : 'flex-start',
                maxWidth: '82%',
              }}
            >
              <div
                style={{
                  fontSize: '10px',
                  fontWeight: 700,
                  color: isMe ? partyColor : 'var(--text-secondary)',
                  marginBottom: '3px',
                  textAlign: isMe ? 'right' : 'left',
                  letterSpacing: '0.04em',
                  textTransform: 'uppercase',
                }}
              >
                {isMe ? 'You' : m.senderName}
              </div>
              <div
                className="chat-msg-bubble"
                style={{
                  padding: '9px 13px',
                  borderRadius: isMe ? '14px 14px 4px 14px' : '14px 14px 14px 4px',
                  backgroundColor: isMe ? partyColor : '#ffffff',
                  color: isMe ? '#fff' : 'var(--primary-dark)',
                  fontSize: '13px',
                  fontWeight: 500,
                  boxShadow: isMe
                    ? `0 3px 10px rgba(0,0,0,0.18)`
                    : '0 2px 6px rgba(33,60,81,0.1)',
                  border: isMe ? 'none' : '1px solid var(--primary-border)',
                  lineHeight: 1.5,
                  wordBreak: 'break-word',
                }}
              >
                {m.text}
              </div>
            </div>
          );
        })}
      </div>

      {/* ── Input Bar ── */}
      <div
        style={{
          padding: '10px 12px',
          background: 'var(--primary-dark)',
          borderTop: '1px solid rgba(255,255,255,0.1)',
          display: 'flex',
          gap: '8px',
          alignItems: 'center',
        }}
      >
        <input
          type="text"
          value={chatInput}
          onChange={(e) => setChatInput(e.target.value)}
          onKeyDown={handleKey}
          placeholder="Type a message..."
          className="chat-input-field"
          style={{ '--party-chat-color': partyColor }}
        />
        <button
          onClick={handleSend}
          disabled={!chatInput.trim()}
          className="chat-send-btn"
          style={{ '--party-chat-color': partyColor }}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatDrawer;
