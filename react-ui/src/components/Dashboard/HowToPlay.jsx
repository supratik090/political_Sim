import React from 'react';

export default function HowToPlay() {
  const actions = [
    {
      id: 1,
      title: 'Action 1: Political Card Selection (Required)',
      description: 'Play a campaign strategy card from a role-specific deck. Standard cards can be played at most 2 times per game to avoid repetitive play. Cards cost Coins or Morale. If the card requires a target, select a rival party. Use offensive cards to expose rival corruption or defensive cards to boost your own media image.',
      imagePlaceholder: '/action1_screenshot.png'
    },
    {
      id: 2,
      title: 'Action 2: State News Reaction (Required)',
      description: 'React to the monthly state-wide news event, presented as a newspaper (The State Chronicle). Select one of four responses. Your choice shapes public opinion and affects your core stats. Be careful—extreme choices carry risk rolls that might backfire.',
      imagePlaceholder: '/action2_screenshot.png'
    },
    {
      id: 3,
      title: 'Action 3: Party News Reaction (Required)',
      description: 'Resolve an internal policy decision, monthly governance issue, or local crisis, presented as an urgent TV Breaking News alert. This focuses on managing internal morale, corruption, and immediate crisis management.',
      imagePlaceholder: '/action3_screenshot.png'
    },
    {
      id: 4,
      title: 'Action 4: Bid for Reward (Required)',
      description: 'Place a blind resource bid (using Coins, Morale, or Support) against rival parties for the upcoming 5-turn cycle reward. The highest bidder wins a powerful inventory booster that can turn the tide of the campaign.',
      imagePlaceholder: '/action4_screenshot.png'
    },
    {
      id: 5,
      title: 'Action 5: Play Reward (Optional)',
      description: 'Deploy any inventory booster rewards (e.g., Grassroots Boost) you have won during previous bidding cycles. This action allows you to apply powerful effects exactly when you need them most.',
      imagePlaceholder: '/action5_screenshot.png'
    },
    {
      id: 6,
      title: 'Action 6: Party Building Activity (Optional)',
      description: 'Allocate funds step-by-step or fully toward long-term infrastructure building projects (e.g., Mega Rally, Prime Leader Visit, IT Cell, Media Smear). Once a project reaches 100% completion, it provides persistent per-turn yields that quickly pay back their construction costs.',
      imagePlaceholder: '/action6_screenshot.png'
    },
    {
      id: 7,
      title: 'Action 7: Diplomatic Cooperation (Optional)',
      description: 'Propose or respond to diplomatic proposals with other human or computer-controlled parties. You can form Non-Aggression Pacts or trade assets like Coins, Morale, Support, or completed buildings. Betraying a pact by playing a hostile card will result in severe Morale penalties.',
      imagePlaceholder: '/action7_screenshot.png'
    }
  ];

  return (
    <div style={{ maxWidth: '900px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '25px', paddingBottom: '40px' }}>
      <div className="unified-card">
        <h2 style={{ marginTop: 0, borderBottom: '1px solid var(--primary-border)', paddingBottom: '10px' }}>
          📖 How to Play Guide
        </h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: '15px', lineHeight: 1.6 }}>
          Welcome to the Political Sim! Your goal is to navigate a 60-turn campaign representing a dynamic election cycle. 
          Manage your core metrics—<strong>Coins</strong>, <strong>Morale</strong>, <strong>Corruption</strong>, and <strong>Media Image</strong>—to win the majority of <strong>Public Support</strong>.
          Every turn, you will complete a series of required and optional actions before advancing to the next month.
        </p>
      </div>

      <h3 style={{ margin: '10px 0 0 0', color: 'var(--primary-dark)', borderLeft: '4px solid var(--selected-highlight)', paddingLeft: '10px' }}>
        The 7 Campaign Actions
      </h3>

      {actions.map(action => (
        <div key={action.id} className="unified-card" style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
          <h4 style={{ margin: 0, fontSize: '18px', color: 'var(--primary-dark)' }}>
            {action.title}
          </h4>
          <p style={{ margin: 0, color: 'var(--text-secondary)', fontSize: '14.5px', lineHeight: 1.6 }}>
            {action.description}
          </p>
          <div style={{ 
            width: '100%', 
            height: '300px', 
            backgroundColor: '#070a13', 
            borderRadius: '8px', 
            border: '1px dashed rgba(101, 148, 177, 0.4)',
            display: 'flex', 
            alignItems: 'center', 
            justifyContent: 'center',
            position: 'relative',
            overflow: 'hidden'
          }}>
            {/* The user will provide real screenshots to replace these placeholders */}
            <img 
              src={action.imagePlaceholder} 
              alt={action.title}
              onError={(e) => { 
                e.target.style.display = 'none'; 
                e.target.nextSibling.style.display = 'flex'; 
              }}
              style={{ width: '100%', height: '100%', objectFit: 'contain' }}
            />
            <div style={{ display: 'none', flexDirection: 'column', alignItems: 'center', color: '#94a3b8' }}>
              <span style={{ fontSize: '24px', marginBottom: '10px' }}>📸</span>
              <span>Screenshot Placeholder for {action.title}</span>
            </div>
          </div>
        </div>
      ))}

      <h3 style={{ margin: '20px 0 0 0', color: 'var(--primary-dark)', borderLeft: '4px solid #d23f31', paddingLeft: '10px' }}>
        Win and Defeat Scenarios
      </h3>

      <div className="unified-card" style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        
        <div style={{ padding: '15px', backgroundColor: 'rgba(210, 63, 49, 0.05)', borderRadius: '8px', borderLeft: '4px solid #d23f31' }}>
          <h4 style={{ margin: '0 0 10px 0', color: '#d23f31', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span>💀</span> Campaign Defeat (Elimination)
          </h4>
          <p style={{ margin: 0, color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.6 }}>
            Your party will instantly collapse and be eliminated from the scenario if you hit any of the following critical thresholds:
          </p>
          <ul style={{ color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.6, marginTop: '10px', marginBottom: 0 }}>
            <li><strong>Bankruptcy:</strong> Coins drop to 0 or below.</li>
            <li><strong>Cadre Collapse:</strong> Party Morale drops below 10.</li>
            <li><strong>Total Loss of Faith:</strong> Public Support drops below 10%.</li>
          </ul>
        </div>

        <div style={{ padding: '15px', backgroundColor: 'rgba(21, 128, 61, 0.05)', borderRadius: '8px', borderLeft: '4px solid #15803d' }}>
          <h4 style={{ margin: '0 0 10px 0', color: '#15803d', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span>🏆</span> Campaign Victory
          </h4>
          <p style={{ margin: 0, color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.6 }}>
            You can secure victory through two primary paths:
          </p>
          <ul style={{ color: 'var(--text-secondary)', fontSize: '14px', lineHeight: 1.6, marginTop: '10px', marginBottom: 0 }}>
            <li><strong>Election Day Victory:</strong> Survive all 60 turns. On Turn 60, elections are held automatically, and the party with the highest Public Support forms the government and wins the campaign.</li>
            <li><strong>Sole Survivor:</strong> If all rival parties collapse due to bankruptcy or morale failure before Turn 60, you win by default as the only remaining viable party.</li>
          </ul>
        </div>

      </div>

    </div>
  );
}
