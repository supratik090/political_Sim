import React from 'react';
// Wraps the existing Action3PartyDecision in a War Room shell.
// The complex faction logic lives in the original component — we don't duplicate it.
import Action3PartyDecision from '../Action3PartyDecision';

/**
 * WR_Action3_Governance — Party Management (Governance tab)
 * Wraps the existing Action3PartyDecision in a War Room–styled shell.
 */
export default function WR_Action3_Governance(props) {
  const {
    turnData,
    selectedIssueOptionKey,
    setSelectedIssueOptionKey,
    activeParty,
    selectedEventOptionKey,
    setSelectedEventOptionKey,
    scenarioEvents,
    projectDefs,
  } = props;

  return (
    <div style={{ padding: '14px 16px 0' }}>
      {/* Section header */}
      <div style={{ marginBottom: '14px' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#34D399' }}>
          ⚖️ Party Management
        </div>
        <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>
          Manage factions, allocate resources & respond to issues
        </div>
      </div>

      {/* War Room skin wrapper — dark surface */}
      <div style={{
        background: 'rgba(16,185,129,0.04)',
        border: '1px solid rgba(16,185,129,0.15)',
        borderRadius: '14px',
        padding: '14px',
        // Override the existing component's inner white backgrounds so they blend
      }}>
        <style>{`
          /* Scoped overrides for Action3 inside War Room */
          .wr-root .action3-inner-card,
          .wr-root .unified-card {
            background: rgba(255,255,255,0.04) !important;
            border-color: rgba(255,255,255,0.10) !important;
            color: #E6EDF3 !important;
          }
          .wr-root input[type="range"] {
            accent-color: #10B981;
          }
        `}</style>
        <Action3PartyDecision
          turnData={turnData}
          selectedIssueOptionKey={selectedIssueOptionKey}
          setSelectedIssueOptionKey={setSelectedIssueOptionKey}
          activeParty={activeParty}
          selectedEventOptionKey={selectedEventOptionKey}
          setSelectedEventOptionKey={setSelectedEventOptionKey}
          scenarioEvents={scenarioEvents}
          projectDefs={projectDefs}
        />
      </div>
    </div>
  );
}
