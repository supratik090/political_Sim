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
    <div style={{ maxWidth: '1000px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '30px', padding: '10px 20px 50px 20px' }}>
      
      {/* Banner Card */}
      <div style={{
        background: 'linear-gradient(135deg, #0f172a 0%, #1e293b 100%)',
        borderRadius: '16px',
        padding: '35px 30px',
        color: '#ffffff',
        boxShadow: '0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)',
        textAlign: 'center'
      }}>
        <span style={{ fontSize: '40px', display: 'block', marginBottom: '10px' }}>📖</span>
        <h1 style={{ marginTop: 0, fontSize: '32px', fontWeight: '900', letterSpacing: '-0.025em', color: '#ffffff' }}>
          How to Play Guide
        </h1>
        <p style={{ color: '#cbd5e1', fontSize: '16px', lineHeight: 1.6, maxWidth: '750px', margin: '15px auto 0 auto' }}>
          Welcome to the Political Sim! Navigate a 60-turn campaign representing a dynamic election cycle. 
          Manage your core metrics—<strong>Coins</strong>, <strong>Morale</strong>, <strong>Corruption</strong>, and <strong>Media Image</strong>—to win the majority of <strong>Public Support</strong>.
        </p>
      </div>

      {/* Grid Layout of the 7 actions */}
      <div>
        <h2 style={{ margin: '10px 0 25px 0', fontSize: '22px', color: 'var(--primary-dark)', display: 'flex', alignItems: 'center', gap: '10px', fontWeight: '800' }}>
          🎯 The 7 Campaign Actions
        </h2>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '25px' }}>
          {actions.map(action => (
            <div 
              key={action.id} 
              style={{
                background: '#ffffff',
                border: '1px solid var(--primary-border)',
                borderRadius: '16px',
                padding: '24px',
                boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)',
                display: 'flex',
                flexDirection: 'column',
                gap: '20px'
              }}
            >
              {/* Card Header Info */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '10px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                  <div style={{
                    width: '42px',
                    height: '42px',
                    borderRadius: '10px',
                    backgroundColor: `${action.color}15`,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontSize: '20px',
                    border: `1.5px solid ${action.color}`
                  }}>
                    {action.icon}
                  </div>
                  <div>
                    <span style={{ fontSize: '11px', fontWeight: '800', color: '#64748b', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Action 0{action.id}</span>
                    <h3 style={{ margin: 0, fontSize: '18px', color: 'var(--primary-dark)', fontWeight: 'bold' }}>{action.title}</h3>
                  </div>
                </div>

                <span style={{
                  fontSize: '11px',
                  fontWeight: '800',
                  padding: '5px 10px',
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
              <p style={{ margin: 0, color: 'var(--text-secondary)', fontSize: '14.5px', lineHeight: 1.6 }}>
                {action.description}
              </p>

              {/* Light Blue Screenshot Placeholder */}
              <div style={{ 
                width: '100%', 
                height: '240px', 
                background: 'linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%)', 
                borderRadius: '12px', 
                border: '2px dashed #0284c7',
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'center',
                position: 'relative',
                overflow: 'hidden',
                boxShadow: 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)'
              }}>
                <img 
                  src={action.imagePlaceholder} 
                  alt={action.title}
                  onError={(e) => { 
                    e.target.style.display = 'none'; 
                    e.target.nextSibling.style.display = 'flex'; 
                  }}
                  style={{ width: '100%', height: '100%', objectFit: 'contain' }}
                />
                <div style={{ display: 'none', flexDirection: 'column', alignItems: 'center', color: '#0369a1', gap: '8px' }}>
                  <span style={{ fontSize: '32px' }}>📸</span>
                  <span style={{ fontSize: '13px', fontWeight: 'bold' }}>Screenshot Placeholder</span>
                  <span style={{ fontSize: '11px', opacity: 0.8 }}>{action.title} Interface Mockup</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Rules and Win/Defeat Scenarios */}
      <h2 style={{ margin: '20px 0 10px 0', fontSize: '22px', color: 'var(--primary-dark)', display: 'flex', alignItems: 'center', gap: '10px', fontWeight: '800' }}>
        ⚙️ Victory and Defeat Scenarios
      </h2>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '25px' }}>
        
        <div style={{ 
          background: '#ffffff',
          border: '1px solid var(--primary-border)',
          borderRadius: '16px',
          padding: '24px',
          boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)',
          borderTop: '5px solid #d9534f'
        }}>
          <h4 style={{ margin: '0 0 15px 0', color: '#d9534f', fontSize: '16px', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span>💀</span> Campaign Defeat (Elimination)
          </h4>
          <p style={{ margin: '0 0 15px 0', color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.6 }}>
            Your party will instantly collapse and be eliminated from the scenario if you hit any of the following critical thresholds:
          </p>
          <ul style={{ color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.8, paddingLeft: '20px', margin: 0 }}>
            <li><strong>Bankruptcy:</strong> Coins drop to 0 or below.</li>
            <li><strong>Cadre Collapse:</strong> Party Morale drops below 10.</li>
            <li><strong>Total Loss of Faith:</strong> Public Support drops below 10%.</li>
          </ul>
        </div>

        <div style={{ 
          background: '#ffffff',
          border: '1px solid var(--primary-border)',
          borderRadius: '16px',
          padding: '24px',
          boxShadow: '0 4px 6px -1px rgba(0,0,0,0.05)',
          borderTop: '5px solid #16a34a'
        }}>
          <h4 style={{ margin: '0 0 15px 0', color: '#16a34a', fontSize: '16px', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span>🏆</span> Campaign Victory
          </h4>
          <p style={{ margin: '0 0 15px 0', color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.6 }}>
            You can secure victory through two primary paths:
          </p>
          <ul style={{ color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.8, paddingLeft: '20px', margin: 0 }}>
            <li><strong>Election Day Victory:</strong> Survive all 60 turns. On Turn 60, elections are held automatically. The party with the highest support forms government and wins.</li>
            <li><strong>Sole Survivor:</strong> If all rival parties collapse due to bankruptcy or morale failure before Turn 60, you win by default.</li>
          </ul>
        </div>

      </div>

    </div>
  );
}
