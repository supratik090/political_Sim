import React, { useState } from 'react';

export default function LandingPage({ onPlayNow }) {
  const [districts, setDistricts] = useState([
    { name: 'Northeast Assembly (District A)', player: 42, rival: 45, status: '⚠️ Swing District', color: '#ea580c' },
    { name: 'Central Valley (District B)', player: 51, rival: 38, status: '✅ Safe Zone', color: '#16a34a' },
    { name: 'Southern Metropolis (District C)', player: 35, rival: 55, status: '🚨 Stronghold Opp', color: '#dc2626' }
  ]);
  const [partyCoins, setPartyCoins] = useState(300);
  const [selectedStrategy, setSelectedStrategy] = useState('SMEAR');
  const [selectedDistrict, setSelectedDistrict] = useState(0);
  const [campaignReport, setCampaignReport] = useState('Welcome, Campaign Manager. Select a strategy and target district below, then deploy your order.');

  const handleSimulatePlay = () => {
    let cost = 50;
    if (selectedStrategy === 'SMEAR') cost = 60;
    else if (selectedStrategy === 'COALITION_BRIBE') cost = 100;
    else if (selectedStrategy === 'GRASSROOTS') cost = 70;

    if (partyCoins < cost) {
      setCampaignReport(`❌ Bankruptcy Warning: Deploying this strategy costs ${cost} Coins. Your reserves only have ${partyCoins} Coins!`);
      return;
    }

    const updated = districts.map((d, idx) => {
      if (idx !== parseInt(selectedDistrict)) return d;
      let p = d.player;
      let r = d.rival;

      if (selectedStrategy === 'SMEAR') {
        const drop = Math.min(r, 8);
        r -= drop;
        p += Math.round(drop * 0.5);
      } else if (selectedStrategy === 'COALITION_BRIBE') {
        r = Math.max(0, r - 12);
        p += 8;
      } else if (selectedStrategy === 'GRASSROOTS') {
        p = Math.min(100, p + 10);
        r = Math.max(0, 100 - p - 10);
      }

      // bound checks
      if (p + r > 100) {
        const diff = (p + r) - 100;
        r = Math.max(0, r - diff);
      }

      let status = '⚠️ Swing District';
      let color = '#ea580c';
      if (p > r + 5) {
        status = '✅ Safe Zone';
        color = '#16a34a';
      } else if (p > r) {
        status = '💛 Leaning Player';
        color = '#eab308';
      } else if (r > p + 5) {
        status = '🚨 Stronghold Opp';
        color = '#dc2626';
      }

      return { ...d, player: p, rival: r, status, color };
    });

    let strategyLabel = selectedStrategy === 'SMEAR' ? 'Smear Campaign' : selectedStrategy === 'COALITION_BRIBE' ? 'Faction Bribe' : 'IT Cell Outreach';
    let targetName = districts[selectedDistrict].name.split(' ')[0];

    setDistricts(updated);
    setPartyCoins(partyCoins - cost);
    setCampaignReport(`📰 News Ticker: Deployed ${strategyLabel} in ${targetName}. Cost: ${cost} Coins. Faction shifts resolved! Player support now at ${updated[selectedDistrict].player}%.`);
  };

  const handleResetSim = () => {
    setDistricts([
      { name: 'Northeast Assembly (District A)', player: 42, rival: 45, status: '⚠️ Swing District', color: '#ea580c' },
      { name: 'Central Valley (District B)', player: 51, rival: 38, status: '✅ Safe Zone', color: '#16a34a' },
      { name: 'Southern Metropolis (District C)', player: 35, rival: 55, status: '🚨 Stronghold Opp', color: '#dc2626' }
    ]);
    setPartyCoins(300);
    setCampaignReport('Campaign playbook reset. Ready to run orders.');
  };

  const features = [
    {
      icon: '🗺️',
      title: 'Pan-Indian States (2001 - 2021)',
      desc: 'Take command of assembly campaigns in any Indian state (Kerala, Bihar, etc.) across crucial election scenarios spanning from the historical 2001 era to the modern 2021 cycle.'
    },
    {
      icon: '👥',
      title: 'Party Factions & Cabinet Allocations',
      desc: 'Assign critical leadership posts like Fund Manager and Party Secretary, allocate patronage points to satisfy faction loyalty metrics, and avoid severe party split crises.'
    },
    {
      icon: '🤝',
      title: 'Cooperative Diplomacy',
      desc: 'Form bilateral Non-Aggression Pacts, negotiate asset transfers (Coins, Morale, Support), or conduct strategic faction sabotages with rival coalitions.'
    },
    {
      icon: '⚡',
      title: 'Dynamic Turn Resolution',
      desc: 'An advanced turn resolution cycle that resolves strategy card actions, computes complex project yields, handles faction power shares, and posts detailed logs.'
    },
    {
      icon: '🛡️',
      title: 'Vindictive AI Competitors',
      desc: 'Compete against adaptive AI opponents built with distinct playstyles (Aggressive Attacker, Late Striker) that dynamically retaliate when attacked.'
    },
    {
      icon: '📈',
      title: 'Infrastructure Projects',
      desc: 'Fund and construct regional infrastructure (e.g. Mega Rally, IT Cell). Once completed, they reward your party with persistent turn-by-turn yield boosts.'
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
            maxWidth: '750px',
            margin: '0 auto 40px'
          }}>
            Step into the boots of a campaign manager. Run election campaigns in any Indian state across historical scenarios from the years 2001 to 2021. Play strategy cards, govern regional news, assign posts, manage faction loyalties, and negotiate diplomatic pacts to lead your party to power.
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
              <h3 style={{ fontSize: '18px', fontWeight: 700, margin: '0 0 6px' }}>Draft Strategy & Play Cards</h3>
              <p style={{ color: '#94a3b8', margin: 0, fontSize: '15px', lineHeight: 1.5 }}>
                Choose a role-based political strategy card to play. Spend coins or morale to deploy campaign campaigns, smearing attacks, or voter outreach.
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
              <h3 style={{ fontSize: '18px', fontWeight: 700, margin: '0 0 6px' }}>Govern State-wide News Reactions</h3>
              <p style={{ color: '#94a3b8', margin: 0, fontSize: '15px', lineHeight: 1.5 }}>
                Read the monthly region chronicle and select your policy response. Navigate risks to align public support while avoiding backlashes.
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
              <h3 style={{ fontSize: '18px', fontWeight: 700, margin: '0 0 6px' }}>Manage Faction Loyalties</h3>
              <p style={{ color: '#94a3b8', margin: 0, fontSize: '15px', lineHeight: 1.5 }}>
                Keep your core party factions satisfied. Assign leadership roles (e.g. Fund Manager, Party Secretary) and distribute patronage points to maximize resource yields.
              </p>
            </div>
          </div>

          {/* Step 4 */}
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
              4
            </div>
            <div>
              <h3 style={{ fontSize: '18px', fontWeight: 700, margin: '0 0 6px' }}>Bid in Bidding Cycles</h3>
              <p style={{ color: '#94a3b8', margin: 0, fontSize: '15px', lineHeight: 1.5 }}>
                Submit secret bids using coins, morale, or support to secure powerful inventory reward cards that boost campaigns.
              </p>
            </div>
          </div>

          {/* Step 5 */}
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
              5
            </div>
            <div>
              <h3 style={{ fontSize: '18px', fontWeight: 700, margin: '0 0 6px' }}>Deploy Infrastructure & Diplomacy</h3>
              <p style={{ color: '#94a3b8', margin: 0, fontSize: '15px', lineHeight: 1.5 }}>
                Build projects like Mega Rallies or state offices, and negotiate pacts or trade assets under the Bilateral Diplomacy workspace.
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
