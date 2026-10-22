import React, { useState, useEffect, useCallback } from 'react';
import { Joyride, STATUS, EVENTS, ACTIONS } from 'react-joyride';

/**
 * WarRoomSpotlightGuide — Interactive onboarding tour for the Campaign War Room.
 * Spotlight walkthrough covering:
 *  1. Header & Turn goal
 *  2. 3 Strategy Tabs (Politics, Governance, Economy)
 *  3. Card Categories (Welfare, Agitation, Media, Scandal)
 *  4. Card Carousel (Costs, Party effects, Rival damage)
 *  5. Target Selection & News Reaction
 *  6. Hex Progress Tracker
 *  7. End Turn CTA
 *
 * Can auto-play on first campaign visit, or re-triggered anytime via the "🎯 Guide" button.
 */
export default function WarRoomSpotlightGuide({
  run,
  setRun,
  activeTab,
  setActiveTab,
}) {
  // Define the tour steps targeting guaranteed DOM elements
  const steps = [
    {
      target: '.wr-header-guide',
      title: '⚔️ Campaign War Room',
      content: (
        <div>
          <p style={{ margin: '0 0 8px' }}>
            Welcome to your <strong>War Room</strong>! Each turn represents <strong>1 month</strong> in your 60-month election campaign.
          </p>
          <p style={{ margin: 0, color: '#94A3B8', fontSize: '12px' }}>
            Your goal is to build <strong>Public Support</strong>, manage your Coins and Morale, and win the assembly election!
          </p>
        </div>
      ),
      disableBeacon: true,
      placement: 'bottom',
    },
    {
      target: '.wr-tab-bar-guide',
      title: '🗂️ Three Strategy Domains',
      content: (
        <div>
          <p style={{ margin: '0 0 8px' }}>
            Decisions are organized across three strategy tabs:
          </p>
          <ul style={{ margin: '0 0 6px', paddingLeft: '18px', lineHeight: '1.6' }}>
            <li><strong style={{ color: '#C084FC' }}>🗳️ Politics</strong>: Play campaign cards & react to breaking news.</li>
            <li><strong style={{ color: '#34D399' }}>🏛️ Governance</strong>: Media blitz & narrative strategy, party factions & alliances.</li>
            <li><strong style={{ color: '#FBBF24' }}>💰 Economy</strong>: Resource bidding & party infrastructure projects.</li>
          </ul>
          <p style={{ margin: 0, color: '#FCD34D', fontSize: '12px' }}>
            ⚡ Look for the yellow <strong>!</strong> badge for pending required moves!
          </p>
        </div>
      ),
      disableBeacon: true,
      placement: 'bottom',
    },
    {
      target: '#wr-section-1',
      title: '🃏 Play Your Monthly Card',
      content: (
        <div>
          <p style={{ margin: '0 0 8px' }}>
            This is your <strong>primary campaign action</strong> for the month:
          </p>
          <ul style={{ margin: '0 0 6px', paddingLeft: '18px', lineHeight: '1.6', fontSize: '12px' }}>
            <li><strong>Categories</strong>: Filter cards by Welfare, Agitation, Media, or Scandal.</li>
            <li><strong>Cost</strong>: Deducted from Coins or Morale.</li>
            <li><strong>Lock In</strong>: Tap any card (and target rival if offensive), then click Lock to commit.</li>
          </ul>
        </div>
      ),
      disableBeacon: true,
      placement: 'bottom',
    },
    {
      target: '#wr-section-2',
      title: '📰 Breaking News Reaction',
      content: (
        <div>
          <p style={{ margin: '0 0 8px' }}>
            State headlines break every month! Select your party's official stance.
          </p>
          <p style={{ margin: 0, color: '#94A3B8', fontSize: '12px' }}>
            Your response directly shapes your <strong>Media Image</strong>, <strong>Corruption Score</strong>, and voter trust.
          </p>
        </div>
      ),
      disableBeacon: true,
      placement: 'top',
    },
    {
      target: '.wr-end-turn-guide',
      title: '🚀 Submit & Advance Month',
      content: (
        <div>
          <p style={{ margin: '0 0 8px' }}>
            Once your required decisions (Card, News, and Monthly Bid) are set, this button lights up green.
          </p>
          <p style={{ margin: 0, color: '#4ADE80', fontSize: '12px', fontWeight: 700 }}>
            Tap END TURN to resolve the round and watch public support swing!
          </p>
        </div>
      ),
      disableBeacon: true,
      placement: 'top',
    },
  ];

  // Joyride event and step callbacks
  const handleJoyrideCallback = useCallback((data) => {
    const { status, type, action } = data;
    const finishedStatuses = [STATUS.FINISHED, STATUS.SKIPPED];

    if (finishedStatuses.includes(status) || action === ACTIONS.CLOSE || type === EVENTS.TOUR_END) {
      setRun(false);
      try {
        localStorage.setItem('hasSeenWarRoomGuide_v1', 'true');
      } catch (e) {
        // Ignore localStorage errors in private browsing
      }
    }
  }, [setRun]);

  return (
    <Joyride
      steps={steps}
      run={run}
      continuous={true}
      scrollToFirstStep={true}
      showProgress={true}
      showSkipButton={true}
      disableOverlayClose={false}
      callback={handleJoyrideCallback}
      locale={{
        back: '← Back',
        close: '✕',
        last: 'Got it! 🚀',
        next: 'Next →',
        open: 'Open',
        skip: 'Skip Tour',
      }}
      styles={{
        options: {
          zIndex: 100000,
          primaryColor: '#F59E0B',
          textColor: '#F1F5F9',
          backgroundColor: '#0F172A',
          arrowColor: '#0F172A',
          overlayColor: 'rgba(0, 0, 0, 0.78)',
        },
        tooltip: {
          borderRadius: '16px',
          padding: '18px 20px',
          backgroundColor: '#0F172A',
          border: '1.5px solid rgba(245, 158, 11, 0.5)',
          boxShadow: '0 20px 40px rgba(0, 0, 0, 0.8), 0 0 25px rgba(245, 158, 11, 0.25)',
          fontSize: '13px',
          fontFamily: 'Montserrat, system-ui, sans-serif',
          maxWidth: '380px',
          color: '#E2E8F0',
        },
        tooltipTitle: {
          fontSize: '16px',
          fontWeight: 900,
          color: '#F59E0B',
          letterSpacing: '0.04em',
          marginBottom: '8px',
        },
        tooltipContent: {
          padding: '6px 0 14px',
          lineHeight: '1.55',
          color: '#CBD5E1',
          fontSize: '13px',
        },
        buttonPrimary: {
          background: 'linear-gradient(135deg, #F59E0B, #D97706)',
          borderRadius: '10px',
          color: '#0F172A',
          fontWeight: 900,
          fontSize: '12px',
          padding: '8px 16px',
          border: 'none',
          boxShadow: '0 2px 10px rgba(245,158,11,0.4)',
          cursor: 'pointer',
        },
        buttonBack: {
          color: '#94A3B8',
          fontWeight: 700,
          fontSize: '12px',
          marginRight: '8px',
          cursor: 'pointer',
        },
        buttonSkip: {
          color: '#64748B',
          fontWeight: 700,
          fontSize: '12px',
          cursor: 'pointer',
        },
        buttonClose: {
          color: '#94A3B8',
          top: '12px',
          right: '12px',
        },
        spotlight: {
          borderRadius: '14px',
        },
      }}
    />
  );
}
