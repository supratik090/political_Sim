import React from 'react';

export default function HowToPlay() {
  const actions = [
    {
      id: 1,
      title: 'Political Card Selection',
      type: 'REQUIRED',
      description: 'Play a campaign strategy card from your role-specific deck. Standard cards can be played at most 2 times per game to avoid repetitive play. Cards cost Coins or Morale. Target rival parties to expose their corruption, or play defensive cards to boost your own media image.',
      icon: '🎴',
      color: '#0284c7',
      imagePlaceholder: '/action1_screenshot.png'
    },
    {
      id: 2,
      title: 'State News Reaction',
      type: 'REQUIRED',
      description: 'React to the monthly state-wide news event, presented as a newspaper (The State Chronicle). Select one of four responses. Your choice shapes public opinion and affects your core stats. Be careful—extreme choices carry risk rolls that might backfire.',
      icon: '📰',
      color: '#ea580c',
      imagePlaceholder: '/action2_screenshot.png'
    },
    {
      id: 3,
      title: 'Factions Management',
      type: 'OPTIONAL',
      description: 'Manage the loyalty and influence of your party\'s 5 factions (Loyalists, Youth Wing, Trade Unions, etc.). Allocate Patronage points, Funding posts, and Media attention to keep loyalty high and generate positive turn-by-turn yields. Unloyal factions reduce project yields and increase corruption.',
      icon: '👥',
      color: '#16a34a',
      imagePlaceholder: '/action3_screenshot.png'
    },
    {
      id: 4,
      title: 'Bid for Reward',
      type: 'REQUIRED',
      description: 'Place a blind resource bid (using Coins, Morale, or Support) against rival parties for the upcoming 5-turn cycle reward. The highest bidder wins a powerful inventory booster that can turn the tide of the campaign.',
      icon: '⚖️',
      color: '#8b5cf6',
      imagePlaceholder: '/action4_screenshot.png'
    },
    {
      id: 5,
      title: 'Play Reward Booster',
      type: 'OPTIONAL',
      description: 'Deploy any inventory booster rewards (e.g., Grassroots Boost) you have won during previous bidding cycles. This action allows you to apply powerful effects exactly when you need them most.',
      icon: '🎁',
      color: '#ec4899',
      imagePlaceholder: '/action5_screenshot.png'
    },
    {
      id: 6,
      title: 'Party Building Activity',
      type: 'OPTIONAL',
      description: 'Allocate funds step-by-step or fully toward long-term infrastructure building projects (e.g., Mega Rally, Prime Leader Visit, IT Cell, Media Smear). Once a project reaches 100% completion, it provides persistent per-turn yields that quickly pay back their construction costs.',
      icon: '🏗️',
      color: '#eab308',
      imagePlaceholder: '/action6_screenshot.png'
    },
    {
      id: 7,
      title: 'Diplomatic Cooperation',
      type: 'OPTIONAL',
      description: 'Propose or respond to diplomatic proposals with other human or computer-controlled parties. You can form Non-Aggression Pacts or trade assets like Coins, Morale, Support, or completed buildings. Betraying a pact by playing a hostile card will result in severe Morale penalties.',
      icon: '🤝',
      color: '#0d9488',
      imagePlaceholder: '/action7_screenshot.png'
    }
  ];

  return (
    <div className="rules-container">
      <style dangerouslySetInnerHTML={{__html: `
        .rules-container {
          max-width: 1000px;
          margin: 0 auto;
          display: flex;
          flex-direction: column;
          gap: 25px;
          padding: 15px 20px 80px 20px;
          font-family: 'Inter', system-ui, sans-serif;
        }

        .rules-banner-card {
          background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
          border-radius: 16px;
          padding: 30px 24px;
          color: #ffffff;
          box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
          text-align: center;
        }

        .rules-banner-icon {
          font-size: 36px;
          display: block;
          margin-bottom: 8px;
        }

        .rules-banner-title {
          margin: 0;
          font-size: 26px;
          font-weight: 900;
          letter-spacing: -0.02em;
          color: #ffffff;
        }

        .rules-banner-desc {
          color: #cbd5e1;
          font-size: 14.5px;
          line-height: 1.5;
          max-width: 750px;
          margin: 12px auto 0 auto;
        }

        .rules-section-title {
          margin: 10px 0 15px 0;
          font-size: 20px;
          color: var(--primary-dark);
          display: flex;
          align-items: center;
          gap: 8px;
          font-weight: 800;
        }

        .rules-action-card {
          background: #ffffff;
          border: 1px solid var(--primary-border);
          border-radius: 14px;
          padding: 20px;
          box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04);
          display: flex;
          flex-direction: column;
          gap: 16px;
        }

        .rules-action-title {
          margin: 0;
          font-size: 17px;
          color: var(--primary-dark);
          font-weight: bold;
        }

        .rules-action-desc {
          margin: 0;
          color: var(--text-secondary);
          font-size: 14px;
          line-height: 1.55;
        }

        .rules-screenshot-box {
          width: 100%;
          height: 200px;
          background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
          border-radius: 10px;
          border: 2px dashed #0284c7;
          display: flex;
          align-items: center;
          justify-content: center;
          position: relative;
          overflow: hidden;
        }

        .rules-outcomes-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
          gap: 20px;
        }

        .rules-outcome-card {
          background: #ffffff;
          border: 1px solid var(--primary-border);
          border-radius: 14px;
          padding: 20px;
          box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04);
        }

        /* Mobile / Android Responsive Adjustments */
        @media (max-width: 640px) {
          .rules-container {
            padding: 8px 10px 85px 10px;
            gap: 14px;
          }
          .rules-banner-card {
            padding: 16px 12px;
            border-radius: 12px;
          }
          .rules-banner-icon {
            font-size: 26px;
            margin-bottom: 4px;
          }
          .rules-banner-title {
            font-size: 18px;
          }
          .rules-banner-desc {
            font-size: 12px;
            line-height: 1.4;
            margin-top: 6px;
          }
          .rules-section-title {
            font-size: 15px;
            margin: 4px 0 8px 0;
          }
          .rules-action-card {
            padding: 12px;
            border-radius: 10px;
            gap: 10px;
          }
          .rules-action-title {
            font-size: 14px;
          }
          .rules-action-desc {
            font-size: 11.5px;
            line-height: 1.4;
          }
          .rules-screenshot-box {
            height: 110px;
            border-radius: 8px;
          }
          .rules-outcomes-grid {
            grid-template-columns: 1fr;
            gap: 12px;
          }
          .rules-outcome-card {
            padding: 12px;
            border-radius: 10px;
          }
        }
      `}} />

      {/* Banner Card */}
      <div className="rules-banner-card">
        <span className="rules-banner-icon">📖</span>
        <h1 className="rules-banner-title">
          Statecraft Guide
        </h1>
        <p className="rules-banner-desc">
          Welcome to Statecraft! Navigate a 60-turn campaign representing a dynamic election cycle. 
          Manage your core metrics—<strong>Coins</strong>, <strong>Morale</strong>, <strong>Corruption</strong>, and <strong>Media Image</strong>—to win the battle for the assembly.
        </p>
      </div>

      {/* Grid Layout of the 7 actions */}
      <div>
        <h2 className="rules-section-title">
          🎯 The 7 Campaign Actions
        </h2>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {actions.map(action => (
            <div key={action.id} className="rules-action-card">
              {/* Card Header Info */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '8px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <div style={{
                    width: '36px',
                    height: '36px',
                    borderRadius: '8px',
                    backgroundColor: `${action.color}15`,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontSize: '18px',
                    border: `1.5px solid ${action.color}`,
                    flexShrink: 0
                  }}>
                    {action.icon}
                  </div>
                  <div>
                    <span style={{ fontSize: '10px', fontWeight: '800', color: '#64748b', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Action 0{action.id}</span>
                    <h3 className="rules-action-title">{action.title}</h3>
                  </div>
                </div>

                <span style={{
                  fontSize: '10px',
                  fontWeight: '800',
                  padding: '3px 8px',
                  borderRadius: '20px',
                  letterSpacing: '0.05em',
                  backgroundColor: action.type === 'REQUIRED' ? '#fee2e2' : '#dcfce7',
                  color: action.type === 'REQUIRED' ? '#b91c1c' : '#15803d',
                  border: `1px solid ${action.type === 'REQUIRED' ? '#fecaca' : '#bbf7d0'}`
                }}>
                  {action.type}
                </span>
              </div>

              {/* Description */}
              <p className="rules-action-desc">
                {action.description}
              </p>

              {/* Screenshot Placeholder */}
              <div className="rules-screenshot-box">
                <img 
                  src={action.imagePlaceholder} 
                  alt={action.title}
                  onError={(e) => { 
                    e.target.style.display = 'none'; 
                    e.target.nextSibling.style.display = 'flex'; 
                  }}
                  style={{ width: '100%', height: '100%', objectFit: 'contain' }}
                />
                <div style={{ display: 'none', flexDirection: 'column', alignItems: 'center', color: '#0369a1', gap: '4px' }}>
                  <span style={{ fontSize: '24px' }}>📸</span>
                  <span style={{ fontSize: '11px', fontWeight: 'bold' }}>Screenshot Placeholder</span>
                  <span style={{ fontSize: '10px', opacity: 0.8 }}>{action.title} Interface Mockup</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Rules and Win/Defeat Scenarios */}
      <h2 className="rules-section-title">
        ⚙️ Victory and Defeat Scenarios
      </h2>

      <div className="rules-outcomes-grid">
        
        <div className="rules-outcome-card" style={{ borderTop: '4px solid #d9534f' }}>
          <h4 style={{ margin: '0 0 10px 0', color: '#d9534f', fontSize: '15px', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span>💀</span> Campaign Defeat (Elimination)
          </h4>
          <p style={{ margin: '0 0 10px 0', color: 'var(--text-secondary)', fontSize: '12.5px', lineHeight: 1.45 }}>
            Your party will instantly collapse and be eliminated from the scenario if you hit any of the following critical thresholds:
          </p>
          <ul style={{ color: 'var(--text-secondary)', fontSize: '12px', lineHeight: 1.6, paddingLeft: '18px', margin: 0 }}>
            <li><strong>Bankruptcy:</strong> Coins drop to 0 or below.</li>
            <li><strong>Cadre Collapse:</strong> Party Morale drops below 10.</li>
            <li><strong>Total Loss of Faith:</strong> Public Support drops below 10%.</li>
          </ul>
        </div>

        <div className="rules-outcome-card" style={{ borderTop: '4px solid #16a34a' }}>
          <h4 style={{ margin: '0 0 10px 0', color: '#16a34a', fontSize: '15px', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span>🏆</span> Campaign Victory
          </h4>
          <p style={{ margin: '0 0 10px 0', color: 'var(--text-secondary)', fontSize: '12.5px', lineHeight: 1.45 }}>
            You can secure victory through two primary paths:
          </p>
          <ul style={{ color: 'var(--text-secondary)', fontSize: '12px', lineHeight: 1.6, paddingLeft: '18px', margin: 0 }}>
            <li><strong>Election Day Victory:</strong> Survive all 60 turns. On Turn 60, elections are held automatically. The party with the highest support forms government and wins.</li>
            <li><strong>Sole Survivor:</strong> If all rival parties collapse due to bankruptcy or morale failure before Turn 60, you win by default.</li>
          </ul>
        </div>

      </div>

    </div>
  );
}
