import React from 'react';

// Core component to load transparent PNG party symbols from locally extracted assets
export const PartySymbolImage = ({ symbolName, size = 24, style = {}, color = '' }) => {
  const iconUrls = {
    bjp: '/symbols/bjp.png',
    inc: '/symbols/inc.png',
    cpim: '/symbols/cpim.png',
    ydp: 'https://cdn-icons-png.flaticon.com/512/2614/2614742.png',
    tiger: 'https://cdn-icons-png.flaticon.com/512/3069/3069172.png',
    elephant: '/symbols/bsp.png',
    peacock: 'https://cdn-icons-png.flaticon.com/512/2620/2620581.png',
    tdp: '/symbols/tdp.png',
    sp: '/symbols/sp.png',
    arrow: '/symbols/jdu.png',
    lantern: '/symbols/rjd.png',
    flower: '/symbols/tmc.png',
    bow: '/symbols/shivsena.png',
    fan: 'https://cdn-icons-png.flaticon.com/512/924/924619.png',
    leaves: '/symbols/aiadmk.png',
    sun: '/symbols/dmk.png',
    flag: 'https://cdn-icons-png.flaticon.com/512/206/206124.png',
    star: 'https://cdn-icons-png.flaticon.com/512/1828/1828884.png'
  };

  const name = (symbolName || '').toLowerCase().trim();
  let key = 'flag';
  if (name.includes('lotus') || name === 'bjp') key = 'bjp';
  else if (name.includes('hand') || name === 'inc' || name === 'congress') key = 'inc';
  else if (name.includes('hammer') || name.includes('sickle') || name === 'cpi' || name === 'ldf' || name.includes('left')) key = 'cpim';
  else if (name.includes('fist') || name === 'ydp' || name.includes('youth')) key = 'ydp';
  else if (name.includes('tiger') || name.includes('front')) key = 'tiger';
  else if (name.includes('elephant') || name === 'bsp') key = 'elephant';
  else if (name.includes('peacock')) key = 'peacock';
  else if (name.includes('bicycle') || name === 'tdp' || name === 'sp') {
    key = (name.includes('sp') || name.includes('samajwadi')) ? 'sp' : 'tdp';
  }
  else if (name.includes('arrow') || name === 'jdu' || name.includes('jd-u')) key = 'arrow';
  else if (name.includes('lantern') || name.includes('lamp') || name === 'rjd') key = 'lantern';
  else if (name.includes('flower') || name === 'tmc' || name.includes('twin')) key = 'flower';
  else if (name.includes('bow') || name.includes('shiv') || name === 'sena') key = 'bow';
  else if (name.includes('fan') || name.includes('ysr')) key = 'fan';
  else if (name.includes('leaf') || name.includes('leaves') || name === 'aiadmk') key = 'leaves';
  else if (name.includes('sun') || name === 'dmk') key = 'sun';
  else if (name.includes('star')) key = 'star';

  const src = iconUrls[key];

  return (
    <img 
      src={src} 
      alt={symbolName} 
      width={size} 
      height={size} 
      style={{ 
        objectFit: 'contain',
        display: 'inline-block',
        verticalAlign: 'middle',
        ...style 
      }} 
    />
  );
};

// Mathematically perfect Ashoka Chakra inline SVG component
export const AshokaChakraIcon = ({ color = '#000080', size = 24, style = {} }) => {
  // Generate 24 spokes at 15-degree intervals (360 / 24 = 15)
  const spokes = [];
  for (let i = 0; i < 24; i++) {
    const angle = i * 15;
    spokes.push(
      <line
        key={i}
        x1="50"
        y1="50"
        x2={50 + 38 * Math.cos((angle * Math.PI) / 180)}
        y2={50 + 38 * Math.sin((angle * Math.PI) / 180)}
        stroke={color}
        strokeWidth="2"
      />
    );
  }

  return (
    <svg viewBox="0 0 100 100" width={size} height={size} style={style}>
      {/* Outer Ring */}
      <circle cx="50" cy="50" r="40" stroke={color} strokeWidth="4.5" fill="none" />
      {/* Inner Hub */}
      <circle cx="50" cy="50" r="7" fill={color} />
      {/* 24 Spokes */}
      {spokes}
      {/* Outer spoke connection points (24 tiny decorative dots) */}
      {Array.from({ length: 24 }).map((_, i) => {
        const angle = i * 15 + 7.5; // Offset by 7.5 degrees to place between spokes
        return (
          <circle
            key={i}
            cx={50 + 40 * Math.cos((angle * Math.PI) / 180)}
            cy={50 + 40 * Math.sin((angle * Math.PI) / 180)}
            r="1.5"
            fill={color}
          />
        );
      })}
    </svg>
  );
};

// Fallback wrappers
export const LotusIcon = (props) => <PartySymbolImage {...props} symbolName="Lotus" />;
export const HandIcon = (props) => <PartySymbolImage {...props} symbolName="Hand" />;
export const HammerIcon = (props) => <PartySymbolImage {...props} symbolName="Hammer" />;
export const ClosedFistIcon = (props) => <PartySymbolImage {...props} symbolName="Closed Fist" />;
export const TigerIcon = (props) => <PartySymbolImage {...props} symbolName="Tiger" />;
export const ElephantIcon = (props) => <PartySymbolImage {...props} symbolName="Elephant" />;
export const PeacockIcon = (props) => <PartySymbolImage {...props} symbolName="Peacock" />;
export const BicycleIcon = (props) => <PartySymbolImage {...props} symbolName="Bicycle" />;
export const ArrowIcon = (props) => <PartySymbolImage {...props} symbolName="Arrow" />;
export const LanternIcon = (props) => <PartySymbolImage {...props} symbolName="Lantern" />;
export const TwinFlowersIcon = (props) => <PartySymbolImage {...props} symbolName="Twin Flowers" />;
export const BowArrowIcon = (props) => <PartySymbolImage {...props} symbolName="Bow & Arrow" />;
export const CeilingFanIcon = (props) => <PartySymbolImage {...props} symbolName="Ceiling Fan" />;
export const TwoLeavesIcon = (props) => <PartySymbolImage {...props} symbolName="Two Leaves" />;
export const RisingSunIcon = (props) => <PartySymbolImage {...props} symbolName="Rising Sun" />;
export const FlagIcon = (props) => <PartySymbolImage {...props} symbolName="Flag" />;
export const StarIcon = (props) => <PartySymbolImage {...props} symbolName="Star" />;

// Helper function to resolve symbol SVG component by name
export const getSymbolIconComponent = (symbolName) => {
  const normalized = (symbolName || '').toLowerCase().trim();
  if (normalized.includes('lotus') || normalized === 'bjp') return LotusIcon;
  if (normalized.includes('hand') || normalized === 'inc' || normalized === 'congress') return HandIcon;
  if (normalized.includes('hammer') || normalized.includes('sickle') || normalized === 'cpi' || normalized === 'ldf' || normalized.includes('left')) return HammerIcon;
  if (normalized.includes('fist')) return ClosedFistIcon;
  if (normalized === 'ydp' || normalized.includes('youth')) return AshokaChakraIcon;
  if (normalized.includes('tiger') || normalized.includes('front')) return TigerIcon;
  if (normalized.includes('elephant') || normalized === 'bsp') return ElephantIcon;
  if (normalized.includes('peacock')) return PeacockIcon;
  if (normalized.includes('bicycle') || normalized === 'tdp' || normalized === 'sp') return BicycleIcon;
  if (normalized.includes('arrow') || normalized === 'jdu' || normalized.includes('jd-u')) return ArrowIcon;
  if (normalized.includes('lantern') || normalized.includes('lamp') || normalized === 'rjd') return LanternIcon;
  if (normalized.includes('flower') || normalized === 'tmc' || normalized.includes('twin')) return TwinFlowersIcon;
  if (normalized.includes('bow') || normalized.includes('shiv') || normalized.includes('sena')) return BowArrowIcon;
  if (normalized.includes('fan') || normalized.includes('ysr')) return CeilingFanIcon;
  if (normalized.includes('leaf') || normalized.includes('leaves') || normalized === 'aiadmk') return TwoLeavesIcon;
  if (normalized.includes('sun') || normalized === 'dmk') return RisingSunIcon;
  if (normalized.includes('star')) return StarIcon;
  return AshokaChakraIcon; // default fallback
};

// Main theme matching function
export const getPartyThemeByName = (partyName) => {
  const name = (partyName || '').toLowerCase().trim();
  
  // 1. BJP / NDA / NDA (BJP+JD-U)
  if (name.includes('bjp') || name.includes('nda') || name.includes('lotus')) {
    return {
      color: '#FF9933',
      rgb: '255, 153, 51',
      symbolName: 'Lotus',
      SymbolIcon: LotusIcon,
      WatermarkIcon: (props) => <LotusIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 2. INC / Congress / INC-UDF / INC (YSR)
  if (name.includes('ysr')) {
    return {
      color: '#1E3A8A',
      rgb: '30, 58, 138',
      symbolName: 'Ceiling Fan',
      SymbolIcon: CeilingFanIcon,
      WatermarkIcon: (props) => <CeilingFanIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }
  if (name.includes('inc') || name.includes('congress') || name.includes('hand') || name.includes('udf')) {
    return {
      color: '#128807',
      rgb: '18, 136, 7',
      symbolName: 'Hand',
      SymbolIcon: HandIcon,
      WatermarkIcon: (props) => <HandIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 3. TMC (Trinamool Congress)
  if (name.includes('tmc') || name.includes('trinamool') || name.includes('flower')) {
    return {
      color: '#0095B6',
      rgb: '0, 149, 182',
      symbolName: 'Twin Flowers',
      SymbolIcon: TwinFlowersIcon,
      WatermarkIcon: (props) => <TwinFlowersIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 4. Shiv Sena
  if (name.includes('shiv') || name.includes('sena') || name.includes('bow')) {
    return {
      color: '#FF9933',
      rgb: '255, 153, 51',
      symbolName: 'Bow & Arrow',
      SymbolIcon: BowArrowIcon,
      WatermarkIcon: (props) => <BowArrowIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 5. CPI-M / LDF / Left Front / Communist
  if (name.includes('cpi-m') || name.includes('cpi(m)') || name.includes('ldf') || name.includes('hammer') || name.includes('communist') || name.includes('left front')) {
    return {
      color: '#D23F31',
      rgb: '210, 63, 49',
      symbolName: 'Hammer & Sickle',
      SymbolIcon: HammerIcon,
      WatermarkIcon: (props) => <HammerIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 6. RJD (Rashtriya Janata Dal)
  if (name.includes('rjd') || name.includes('lantern') || name.includes('lalten')) {
    return {
      color: '#1E824C',
      rgb: '30, 130, 76',
      symbolName: 'Lantern',
      SymbolIcon: LanternIcon,
      WatermarkIcon: (props) => <LanternIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 7. JD-U / JDU
  if (name.includes('jd-u') || name.includes('jdu') || name.includes('arrow')) {
    return {
      color: '#196F3D',
      rgb: '25, 111, 61',
      symbolName: 'Arrow',
      SymbolIcon: ArrowIcon,
      WatermarkIcon: (props) => <ArrowIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 8. TDP (Telugu Desam Party)
  if (name.includes('tdp') || name.includes('telugu') || name.includes('bicycle')) {
    return {
      color: '#FDD835',
      rgb: '253, 220, 53',
      symbolName: 'Bicycle',
      SymbolIcon: BicycleIcon,
      WatermarkIcon: (props) => <BicycleIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 9. Samajwadi Party (SP)
  if (name.includes('sp') || name.includes('samajwadi')) {
    return {
      color: '#1E824C',
      rgb: '30, 130, 76',
      symbolName: 'Bicycle',
      SymbolIcon: BicycleIcon,
      WatermarkIcon: (props) => <BicycleIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 10. BSP / Elephant Congress
  if (name.includes('bsp') || name.includes('elephant')) {
    return {
      color: '#1A5276',
      rgb: '26, 82, 118',
      symbolName: 'Elephant',
      SymbolIcon: ElephantIcon,
      WatermarkIcon: (props) => <ElephantIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 11. Youth Development Party (YDP)
  if (name.includes('youth') || name.includes('ydp')) {
    return {
      color: '#0ABAB5',
      rgb: '10, 186, 181',
      symbolName: 'Ashoka Chakra',
      SymbolIcon: AshokaChakraIcon,
      WatermarkIcon: (props) => <AshokaChakraIcon {...props} style={{ opacity: 0.1 }} />
    };
  }

  // 12. Tiger Front
  if (name.includes('tiger')) {
    return {
      color: '#E15554',
      rgb: '225, 85, 84',
      symbolName: 'Tiger',
      SymbolIcon: TigerIcon,
      WatermarkIcon: (props) => <TigerIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 13. Peacock Party
  if (name.includes('peacock')) {
    return {
      color: '#17B890',
      rgb: '23, 184, 144',
      symbolName: 'Peacock',
      SymbolIcon: PeacockIcon,
      WatermarkIcon: (props) => <PeacockIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 14. AIADMK
  if (name.includes('aiadmk') || name.includes('leaves') || name.includes('leaf')) {
    return {
      color: '#008000',
      rgb: '0, 128, 0',
      symbolName: 'Two Leaves',
      SymbolIcon: TwoLeavesIcon,
      WatermarkIcon: (props) => <TwoLeavesIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // 15. DMK
  if (name.includes('dmk') || name.includes('sun') || name.includes('rising')) {
    return {
      color: '#B22222',
      rgb: '178, 34, 34',
      symbolName: 'Rising Sun',
      SymbolIcon: RisingSunIcon,
      WatermarkIcon: (props) => <RisingSunIcon {...props} style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
    };
  }

  // Fallback defaults to Ashoka Chakra in Navy Blue
  return {
    color: '#000080',
    rgb: '0, 0, 128',
    symbolName: 'Ashoka Chakra',
    SymbolIcon: AshokaChakraIcon,
    WatermarkIcon: (props) => <AshokaChakraIcon {...props} style={{ opacity: 0.1 }} />
  };
};
