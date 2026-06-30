import React, { useState } from 'react';

export default function LandingPage({ onPlayNow }) {
  const [activeSlide, setActiveSlide] = useState(0);

  const screenshots = [
    {
      url: '/stats_initial.png',
      title: 'Campaign Command Center',
      desc: 'Analyze live state maps, track your core metrics (Coins, Morale, Support), and manage long-term infrastructure building projects like Mega Rallies and IT Cells.'
    },
    {
      url: '/actions_tab.png',
      title: 'Action Strategy & News',
      desc: 'React to monthly state-wide news events and regional crises. Select your stance wisely—every choice shapes public opinion and risks surprise backlashes.'
    },
    {
      url: '/actions_expanded.png',
      title: 'Bilateral Diplomacy Hub & Bids',
      desc: 'Form coalition alliances, negotiate Non-Aggression Pacts, and trade assets (Coins, Morale, Support, or buildings) with other human or computer-controlled parties.'
    }
  ];

  const features = [
    {
      icon: '⚡',
      title: 'Dynamic Turn Resolution',
      desc: 'An advance turn resolution cycle that applies strategic cards, evaluates project yields, normalizes voter shares, and reports tactical strategic commentaries.'
    },
    {
      icon: '🛡️',
      title: 'Smart AI Competitors',
      desc: 'Play against responsive computer-controlled parties driven by unique strategic profiles (like Aggressive Populists) that hold grudges and retaliate dynamically.'
    },
    {
      icon: '📈',
      title: 'Incremental Infrastructure',
      desc: 'Fund long-term projects step-by-step. Achieve 100% completion to unlock persistent per-turn resource yields that pay back initial capital expenses.'
    },
    {
      icon: '⚖️',
      title: 'Bidding and Resource Bids',
      desc: 'Submit blind bids using your party\'s reserves to win high-impact 5-turn cycle rewards, while managing safety limits to avoid bankruptcy.'
    }
  ];

  return (
    <div style={{
      backgroundColor: '#0a0f1d',
      color: '#f8fafc',
      fontFamily: "'Outfit', 'Montserrat', sans-serif",
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      overflowX: 'hidden'
    }}>
      {/* Navbar */}
      <header style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '20px 40px',
        borderBottom: '1px solid rgba(101, 148, 177, 0.1)',
        backdropFilter: 'blur(10px)',
        position: 'sticky',
        top: 0,
        zIndex: 100,
        backgroundColor: 'rgba(10, 15, 29, 0.9)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <img src="/politics.svg" alt="Bharat Rajneeti Logo" style={{ width: '40px', height: '40px', borderRadius: '8px' }} />
          <span style={{ fontSize: '20px', fontWeight: 800, letterSpacing: '-0.02em', background: 'linear-gradient(90deg, #38bdf8, #818cf8)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
            BHARAT RAJNEETI
          </span>
        </div>
        <button 
          onClick={onPlayNow}
          style={{
            background: 'linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%)',
            border: 'none',
            color: '#ffffff',
            padding: '10px 24px',
            fontSize: '14px',
            fontWeight: 700,
            borderRadius: '9999px',
            boxShadow: '0 4px 15px rgba(99, 102, 241, 0.4)',
            transition: 'transform 0.2s, box-shadow 0.2s'
          }}
          onMouseOver={(e) => {
            e.currentTarget.style.transform = 'translateY(-2px)';
            e.currentTarget.style.boxShadow = '0 6px 20px rgba(99, 102, 241, 0.6)';
          }}
          onMouseOut={(e) => {
            e.currentTarget.style.transform = 'none';
            e.currentTarget.style.boxShadow = '0 4px 15px rgba(99, 102, 241, 0.4)';
          }}
        >
          Play Now
        </button>
      </header>

      {/* Hero Section */}
      <section style={{
        padding: '100px 20px 80px',
        textAlign: 'center',
        background: 'radial-gradient(circle at center, rgba(99, 102, 241, 0.15) 0%, rgba(10, 15, 29, 0) 70%)',
        position: 'relative'
      }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <span style={{
            fontSize: '12px',
            fontWeight: 800,
            color: '#38bdf8',
            textTransform: 'uppercase',
            letterSpacing: '0.2em',
            display: 'inline-block',
            marginBottom: '16px',
            background: 'rgba(56, 189, 248, 0.1)',
            padding: '6px 16px',
            borderRadius: '9999px'
          }}>
            Grand Strategy Election Simulator
          </span>
          <h1 style={{
            fontSize: '56px',
            fontWeight: 900,
            lineHeight: 1.1,
            letterSpacing: '-0.03em',
            margin: '0 0 24px',
            background: 'linear-gradient(135deg, #ffffff 40%, #94a3b8 100%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent'
          }}>
            Experience the High-Stakes World of Indian Elections
          </h1>
          <p style={{
            fontSize: '18px',
            color: '#94a3b8',
            lineHeight: 1.6,
            marginBottom: '40px',
            maxWidth: '650px',
            margin: '0 auto 40px'
          }}>
            Step into the boots of a campaign manager. Play strategy cards, govern news events, invest in mega-rallies, and sign diplomatic pacts to lead your party to power.
          </p>
          <button 
            onClick={onPlayNow}
            style={{
              background: 'linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%)',
              border: 'none',
              color: '#ffffff',
              padding: '16px 44px',
              fontSize: '16px',
              fontWeight: 800,
              borderRadius: '9999px',
              boxShadow: '0 8px 30px rgba(99, 102, 241, 0.4)',
              cursor: 'pointer',
              transition: 'transform 0.2s, box-shadow 0.2s'
            }}
            onMouseOver={(e) => {
              e.currentTarget.style.transform = 'translateY(-3px) scale(1.02)';
              e.currentTarget.style.boxShadow = '0 12px 35px rgba(99, 102, 241, 0.6)';
            }}
            onMouseOut={(e) => {
              e.currentTarget.style.transform = 'none';
              e.currentTarget.style.boxShadow = '0 8px 30px rgba(99, 102, 241, 0.4)';
            }}
          >
            Enter Campaign Board
          </button>
        </div>
      </section>

      {/* Showcase / Screenshot Carousel Section */}
      <section style={{
        padding: '20px 20px 80px',
        maxWidth: '1100px',
        margin: '0 auto',
        width: '100%'
      }}>
        <h2 style={{
          textAlign: 'center',
          fontSize: '32px',
          fontWeight: 800,
          marginBottom: '40px',
          letterSpacing: '-0.02em'
        }}>
          Interactive Gameplay Walkthrough
        </h2>

        <div style={{
          background: 'rgba(30, 41, 59, 0.4)',
          border: '1px solid rgba(101, 148, 177, 0.2)',
          borderRadius: '24px',
          padding: '24px',
          backdropFilter: 'blur(20px)',
          boxShadow: '0 20px 40px rgba(0,0,0,0.3)',
          display: 'flex',
          flexDirection: 'column',
          gap: '24px'
        }}>
          {/* Main Slide Image */}
          <div style={{
            position: 'relative',
            borderRadius: '16px',
            overflow: 'hidden',
            aspectRatio: '16/10',
            backgroundColor: '#070a13',
            border: '1px solid rgba(255, 255, 255, 0.05)',
            boxShadow: '0 10px 30px rgba(0,0,0,0.5)'
          }}>
            <img 
              src={screenshots[activeSlide].url} 
              alt={screenshots[activeSlide].title} 
              style={{
                width: '100%',
                height: '100%',
                objectFit: 'contain',
                transition: 'opacity 0.3s ease-in-out'
              }} 
            />
          </div>

          {/* Slide Navigation Tabs */}
          <div style={{
            display: 'grid',
            gridTemplateColumns: '1fr 1fr 1fr',
            gap: '16px'
          }}>
            {screenshots.map((shot, idx) => (
              <button
                key={idx}
                onClick={() => setActiveSlide(idx)}
                style={{
                  background: activeSlide === idx ? 'rgba(99, 102, 241, 0.15)' : 'transparent',
                  border: '1px solid ' + (activeSlide === idx ? 'rgba(99, 102, 241, 0.4)' : 'rgba(255,255,255,0.05)'),
                  borderRadius: '12px',
                  padding: '16px',
                  textAlign: 'left',
                  cursor: 'pointer',
                  transition: 'all 0.2s',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '6px',
                  boxShadow: 'none'
                }}
                onMouseOver={(e) => {
                  if (activeSlide !== idx) {
                    e.currentTarget.style.border = '1px solid rgba(255, 255, 255, 0.15)';
                    e.currentTarget.style.background = 'rgba(255, 255, 255, 0.02)';
                  }
                }}
                onMouseOut={(e) => {
                  if (activeSlide !== idx) {
                    e.currentTarget.style.border = '1px solid rgba(255,255,255,0.05)';
                    e.currentTarget.style.background = 'transparent';
                  }
                }}
              >
                <span style={{
                  fontSize: '15px',
                  fontWeight: 700,
                  color: activeSlide === idx ? '#38bdf8' : '#ffffff'
                }}>
                  {shot.title}
                </span>
                <span style={{
                  fontSize: '12px',
                  color: '#94a3b8',
                  lineHeight: 1.4,
                  fontWeight: 400
                }}>
                  {shot.desc}
                </span>
              </button>
            ))}
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section style={{
        backgroundColor: '#070a13',
        padding: '80px 20px',
        borderTop: '1px solid rgba(101, 148, 177, 0.1)',
        borderBottom: '1px solid rgba(101, 148, 177, 0.1)'
      }}>
        <div style={{ maxWidth: '1100px', margin: '0 auto' }}>
          <h2 style={{
            textAlign: 'center',
            fontSize: '32px',
            fontWeight: 800,
            marginBottom: '16px',
            letterSpacing: '-0.02em'
          }}>
            Sophisticated Game Mechanics
          </h2>
          <p style={{
            textAlign: 'center',
            color: '#94a3b8',
            maxWidth: '600px',
            margin: '0 auto 60px',
            fontSize: '16px',
            lineHeight: 1.5
          }}>
            Every turn represents one month in a 5-year election cycle. Out-think your rival parties by balancing quick gains with long-term investments.
          </p>

          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
            gap: '24px'
          }}>
            {features.map((feat, idx) => (
              <div 
                key={idx}
                style={{
                  background: 'rgba(30, 41, 59, 0.3)',
                  border: '1px solid rgba(255, 255, 255, 0.05)',
                  borderRadius: '16px',
                  padding: '24px',
                  transition: 'all 0.3s ease'
                }}
              >
                <div style={{
                  fontSize: '32px',
                  marginBottom: '16px',
                  background: 'rgba(99, 102, 241, 0.1)',
                  width: '56px',
                  height: '56px',
                  borderRadius: '12px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }}>
                  {feat.icon}
                </div>
                <h3 style={{
                  fontSize: '18px',
                  fontWeight: 700,
                  marginBottom: '8px',
                  color: '#ffffff'
                }}>
                  {feat.title}
                </h3>
                <p style={{
                  fontSize: '14px',
                  color: '#94a3b8',
                  lineHeight: 1.5,
                  margin: 0
                }}>
                  {feat.desc}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Step by Step Turn Sequence */}
      <section style={{
        padding: '80px 20px',
        maxWidth: '900px',
        margin: '0 auto',
        width: '100%'
      }}>
        <h2 style={{
          textAlign: 'center',
          fontSize: '32px',
          fontWeight: 800,
          marginBottom: '50px',
          letterSpacing: '-0.02em'
        }}>
          How to Play a Round
        </h2>

        <div style={{
          position: 'relative',
          display: 'flex',
          flexDirection: 'column',
          gap: '30px'
        }}>
          {/* Step 1 */}
          <div style={{ display: 'flex', gap: '20px', alignItems: 'flex-start' }}>
            <div style={{
              background: 'linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%)',
              color: '#ffffff',
              width: '40px',
              height: '40px',
              borderRadius: '50%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontWeight: 800,
              fontSize: '16px',
              flexShrink: 0,
              boxShadow: '0 4px 10px rgba(99, 102, 241, 0.3)'
            }}>
              1
            </div>
            <div>
              <h3 style={{ fontSize: '18px', fontWeight: 700, margin: '0 0 6px' }}>Select strategy cards</h3>
              <p style={{ color: '#94a3b8', margin: 0, fontSize: '15px', lineHeight: 1.5 }}>
                Choose a role-based political card to play. Spend coins to launch smears, media campaigns, or legal challenges against target rival parties.
              </p>
            </div>
          </div>

          {/* Step 2 */}
          <div style={{ display: 'flex', gap: '20px', alignItems: 'flex-start' }}>
            <div style={{
              background: 'linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%)',
              color: '#ffffff',
              width: '40px',
              height: '40px',
              borderRadius: '50%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontWeight: 800,
              fontSize: '16px',
              flexShrink: 0,
              boxShadow: '0 4px 10px rgba(99, 102, 241, 0.3)'
            }}>
              2
            </div>
            <div>
              <h3 style={{ fontSize: '18px', fontWeight: 700, margin: '0 0 6px' }}>React to state news</h3>
              <p style={{ color: '#94a3b8', margin: 0, fontSize: '15px', lineHeight: 1.5 }}>
                Read the monthly newspaper and make structural choices. Call audits, offer drought relief packages, or propose grassland reserves to boost support.
              </p>
            </div>
          </div>

          {/* Step 3 */}
          <div style={{ display: 'flex', gap: '20px', alignItems: 'flex-start' }}>
            <div style={{
              background: 'linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%)',
              color: '#ffffff',
              width: '40px',
              height: '40px',
              borderRadius: '50%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontWeight: 800,
              fontSize: '16px',
              flexShrink: 0,
              boxShadow: '0 4px 10px rgba(99, 102, 241, 0.3)'
            }}>
              3
            </div>
            <div>
              <h3 style={{ fontSize: '18px', fontWeight: 700, margin: '0 0 6px' }}>Negotiate pacts & Bids</h3>
              <p style={{ color: '#94a3b8', margin: 0, fontSize: '15px', lineHeight: 1.5 }}>
                Submit blind bids for cycle rewards. Propose non-aggression treaties or request asset trades with rival parties before advancing the turn.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Footer */}
      <footer style={{
        marginTop: 'auto',
        backgroundColor: '#070a13',
        padding: '60px 40px',
        borderTop: '1px solid rgba(101, 148, 177, 0.1)',
        textAlign: 'center'
      }}>
        <div style={{ maxWidth: '600px', margin: '0 auto' }}>
          <h2 style={{ fontSize: '28px', fontWeight: 800, marginBottom: '16px' }}>Ready to Run Your Campaign?</h2>
          <p style={{ color: '#94a3b8', fontSize: '15px', marginBottom: '30px' }}>
            Take command of active elections and see if you have the strategic mind to capture the assembly.
          </p>
          <button 
            onClick={onPlayNow}
            style={{
              background: 'linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%)',
              border: 'none',
              color: '#ffffff',
              padding: '14px 36px',
              fontSize: '15px',
              fontWeight: 800,
              borderRadius: '9999px',
              boxShadow: '0 4px 20px rgba(99, 102, 241, 0.4)'
            }}
          >
            Start Playing
          </button>
          <div style={{ marginTop: '40px', fontSize: '13px', color: '#475569' }}>
            © 2026 Bharat Rajneeti. Built using premium responsive Web Technologies.
          </div>
        </div>
      </footer>
    </div>
  );
}
