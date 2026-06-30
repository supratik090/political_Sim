import React, { useState, useEffect } from 'react';
import { Joyride, STATUS } from 'react-joyride';

export default function GameTutorial() {
  const [run, setRun] = useState(false);

  useEffect(() => {
    // Check if the user has already seen the tutorial
    const hasSeenTutorial = localStorage.getItem('hasSeenTutorial');
    if (!hasSeenTutorial) {
      setRun(true);
    }
  }, []);

  const handleJoyrideCallback = (data) => {
    const { status } = data;
    const finishedStatuses = [STATUS.FINISHED, STATUS.SKIPPED];

    if (finishedStatuses.includes(status)) {
      setRun(false);
      localStorage.setItem('hasSeenTutorial', 'true');
    }
  };

  const steps = [
    {
      target: '.game-title-banner',
      content: 'Welcome to your first Campaign! Your goal is to survive 60 months and win the most Public Support.',
      disableBeacon: true,
    },
    {
      target: '.view-toggle-bar',
      content: 'You can toggle between your Campaign Stats and your Turn Actions here.',
    },
    {
      target: '.floating-nav-arrow',
      content: 'When you are done reviewing your Stats, click here to go to the Actions tab and start making your decisions.',
    }
  ];

  return (
    <Joyride
      steps={steps}
      run={run}
      continuous={true}
      showProgress={true}
      showSkipButton={true}
      callback={handleJoyrideCallback}
      styles={{
        options: {
          zIndex: 10000,
          primaryColor: '#0ea5e9',
          textColor: '#0f172a',
          backgroundColor: '#ffffff',
          overlayColor: 'rgba(0, 0, 0, 0.7)',
        },
      }}
    />
  );
}
