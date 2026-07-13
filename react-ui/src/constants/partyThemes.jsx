import React from 'react';

// Core component to load transparent PNG party symbols from locally extracted assets
export const PartySymbolImage = ({ symbolName, size = 24, style = {}, color = '' }) => {
  const name = (symbolName || '').toLowerCase().trim();
  let initials = 'PTY';
  
  if (name === 'bjp' || name.includes('lotus')) initials = 'BJP';
  else if (name === 'inc' || name.includes('hand') || name === 'congress') initials = 'INC';
  else if (name === 'cpim' || name === 'cpi' || name.includes('hammer') || name.includes('sickle') || name === 'ldf' || name.includes('left')) initials = 'CPM';
  else if (name === 'ydp' || name.includes('fist') || name.includes('youth')) initials = 'YDP';
  else if (name === 'tf' || name.includes('tiger') || name.includes('front')) initials = 'TF';
  else if (name === 'agp') initials = 'AGP';
  else if (name === 'bsp' || name.includes('elephant')) initials = 'BSP';
  else if (name === 'pp' || name.includes('peacock')) initials = 'PP';
  else if (name === 'sp' || (name.includes('bicycle') && name.includes('sp')) || (name.includes('bicycle') && name.includes('samajwadi'))) initials = 'SP';
  else if (name === 'tdp' || name.includes('bicycle')) initials = 'TDP';
  else if (name === 'jdu' || name.includes('arrow')) initials = 'JDU';
  else if (name === 'rjd' || name.includes('lantern')) initials = 'RJD';
  else if (name === 'tmc' || name.includes('flower') || name.includes('twin')) initials = 'TMC';
  else if (name === 'jmm') initials = 'JMM';
  else if (name === 'ss' || name.includes('bow') || name.includes('shiv') || name === 'sena') initials = 'SS';
  else if (name === 'ycp' || name.includes('fan') || name.includes('ysr') || name === 'ysrcp') initials = 'YCP';
  else if (name === 'admk' || name.includes('leaf') || name.includes('leaves') || name === 'aiadmk') initials = 'ADMK';
  else if (name === 'dmk' || name.includes('sun')) initials = 'DMK';
  else if (name === 'star' || name === 'mnf') initials = 'MNF';
  else if (name === 'flag') initials = 'FLG';
  else if (name === 'ashoka' || name.includes('chakra')) initials = 'IND';
  else if (name === 'broom' || name === 'aap') initials = 'AAP';
  else if (name === 'conch' || name === 'bjd') initials = 'BJD';
  else if (name === 'spectacles' || name === 'inld') initials = 'INLD';
  else if (name === 'lady farmer' || name === 'jds') initials = 'JDS';
  else if (name === 'plough' || name === 'nc') initials = 'NC';
  else if (name === 'globe' || name === 'ndpp') initials = 'NDP';
  else if (name === 'cock' || name === 'npf') initials = 'NPF';
  else if (name === 'book' || name === 'npp') initials = 'NPP';
  else if (name === 'maize' || name === 'ppa') initials = 'PPA';
  else if (name === 'umbrella' || name === 'sdf') initials = 'SDF';
  else if (name === 'table lamp' || name.includes('lamp') || name === 'skm') initials = 'SKM';
  else if (name === 'drum' || name === 'udp') initials = 'UDP';
  else if (name === 'kettle' || name === 'zpm') initials = 'ZPM';
  else if (name === 'car' || name === 'trs' || name === 'brs') initials = 'TRS';
  else if (name === 'scales' || name === 'sad') initials = 'SAD';
  else if (name.length <= 4) initials = name.toUpperCase();

  return (
    <div style={{
      width: `${size}px`,
      height: `${size}px`,
      borderRadius: '50%',
      backgroundColor: color || 'var(--party-primary-color, var(--primary-dark))',
      color: '#ffffff',
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontSize: `${Math.max(7, size * 0.38)}px`,
      fontWeight: '900',
      fontFamily: 'system-ui, -apple-system, sans-serif',
      letterSpacing: '-0.02em',
      verticalAlign: 'middle',
      boxShadow: '0 1px 3px rgba(0,0,0,0.12)',
      border: '1.5px solid rgba(255,255,255,0.25)',
      textShadow: '0 1px 2px rgba(0,0,0,0.2)',
      ...style
    }}>
      {initials}
    </div>
  );
};

// Mathematically perfect Ashoka Chakra inline SVG component replaced with Initials Badge
export const AshokaChakraIcon = ({ color = '#000080', size = 24, style = {} }) => {
  return (
    <div style={{
      width: `${size}px`,
      height: `${size}px`,
      borderRadius: '50%',
      backgroundColor: color,
      color: '#ffffff',
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontSize: `${Math.max(7, size * 0.38)}px`,
      fontWeight: '900',
      fontFamily: 'system-ui, -apple-system, sans-serif',
      letterSpacing: '-0.02em',
      verticalAlign: 'middle',
      boxShadow: '0 1px 3px rgba(0,0,0,0.12)',
      border: '1.5px solid rgba(255,255,255,0.25)',
      textShadow: '0 1px 2px rgba(0,0,0,0.2)',
      ...style
    }}>
      IND
    </div>
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
export const YdpIcon = (props) => <PartySymbolImage {...props} symbolName="YDP" />;

// Helper function to resolve symbol SVG component by name
export const getSymbolIconComponent = (symbolName) => {
  const normalized = (symbolName || '').toLowerCase().trim();
  if (normalized.includes('lotus') || normalized === 'bjp') return LotusIcon;
  if (normalized.includes('hand') || normalized === 'inc' || normalized === 'congress') return HandIcon;
  if (normalized.includes('hammer') || normalized.includes('sickle') || normalized === 'cpi' || normalized === 'ldf' || normalized.includes('left')) return HammerIcon;
  if (normalized.includes('fist')) return ClosedFistIcon;
  if (normalized === 'ydp' || normalized.includes('youth') || normalized.includes('ashoka') || normalized.includes('chakra')) return YdpIcon;
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
      color: '#E65100',
      rgb: '230, 81, 0',
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
      color: '#4CAF50',
      rgb: '76, 175, 80',
      symbolName: 'SP',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="SP" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="SP" style={{ opacity: 0.1, filter: 'grayscale(100%)' }} />
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
      color: '#D8B4FE',
      rgb: '216, 180, 254',
      symbolName: 'YDP',
      SymbolIcon: YdpIcon,
      WatermarkIcon: (props) => <YdpIcon {...props} style={{ opacity: 0.1 }} />
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

  // 16. AAP (Aam Aadmi Party)
  if (name.includes('aap') || name.includes('broom')) {
    return {
      color: '#0054A6',
      rgb: '0, 84, 166',
      symbolName: 'Broom',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Broom" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Broom" style={{ opacity: 0.1 }} />
    };
  }

  // 17. BJD (Biju Janata Dal)
  if (name.includes('bjd') || name.includes('conch')) {
    return {
      color: '#006400',
      rgb: '0, 100, 0',
      symbolName: 'Conch',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Conch" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Conch" style={{ opacity: 0.1 }} />
    };
  }

  // 18. JMM (Jharkhand Mukti Morcha)
  if (name.includes('jmm')) {
    return {
      color: '#556B2F',
      rgb: '85, 107, 47',
      symbolName: 'Bow & Arrow',
      SymbolIcon: BowArrowIcon,
      WatermarkIcon: (props) => <BowArrowIcon {...props} style={{ opacity: 0.1 }} />
    };
  }

  // 19. TRS (Telangana Rashtra Samithi) / BRS / Car
  if (name.includes('trs') || name.includes('brs') || name.includes('car')) {
    return {
      color: '#FF69B4',
      rgb: '255, 105, 180',
      symbolName: 'Car',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Car" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Car" style={{ opacity: 0.1 }} />
    };
  }

  // 20. SAD (Shiromani Akali Dal)
  if (name.includes('sad') || name.includes('akali') || name.includes('scales')) {
    return {
      color: '#0F4C81',
      rgb: '15, 76, 129',
      symbolName: 'Scales',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Scales" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Scales" style={{ opacity: 0.1 }} />
    };
  }

  // 21. NC (National Conference)
  if (name.includes('nc') || name.includes('conference') || name.includes('plough')) {
    return {
      color: '#D21F3C',
      rgb: '210, 31, 60',
      symbolName: 'Plough',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Plough" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Plough" style={{ opacity: 0.1 }} />
    };
  }

  // 22. MNF (Mizo National Front)
  if (name.includes('mnf')) {
    return {
      color: '#0038A8',
      rgb: '0, 56, 168',
      symbolName: 'Star',
      SymbolIcon: StarIcon,
      WatermarkIcon: (props) => <StarIcon {...props} style={{ opacity: 0.1 }} />
    };
  }

  // 23. AGP (Asom Gana Parishad)
  if (name.includes('agp')) {
    return {
      color: '#84CC16',
      rgb: '132, 204, 22',
      symbolName: 'Elephant',
      SymbolIcon: ElephantIcon,
      WatermarkIcon: (props) => <ElephantIcon {...props} style={{ opacity: 0.1 }} />
    };
  }

  // 24. INLD (Indian National Lok Dal)
  if (name.includes('inld') || name.includes('spectacles')) {
    return {
      color: '#2E8B57',
      rgb: '46, 139, 87',
      symbolName: 'Spectacles',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Spectacles" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Spectacles" style={{ opacity: 0.1 }} />
    };
  }

  // 25. JD(S)
  if (name.includes('jd(s)') || name.includes('jds')) {
    return {
      color: '#228B22',
      rgb: '34, 139, 34',
      symbolName: 'Lady Farmer',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Lady Farmer" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Lady Farmer" style={{ opacity: 0.1 }} />
    };
  }

  // 26. NDPP
  if (name.includes('ndpp') || name.includes('globe')) {
    return {
      color: '#E61A22',
      rgb: '230, 26, 34',
      symbolName: 'Globe',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Globe" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Globe" style={{ opacity: 0.1 }} />
    };
  }

  // 27. NPF
  if (name.includes('npf') || name.includes('cock')) {
    return {
      color: '#0000FF',
      rgb: '0, 0, 255',
      symbolName: 'Cock',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Cock" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Cock" style={{ opacity: 0.1 }} />
    };
  }

  // 28. NPP
  if (name.includes('npp') || name.includes('book')) {
    return {
      color: '#000080',
      rgb: '0, 0, 128',
      symbolName: 'Book',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Book" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Book" style={{ opacity: 0.1 }} />
    };
  }

  // 29. PPA
  if (name.includes('ppa') || name.includes('maize')) {
    return {
      color: '#FFCC00',
      rgb: '255, 204, 0',
      symbolName: 'Maize',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Maize" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Maize" style={{ opacity: 0.1 }} />
    };
  }

  // 30. SDF
  if (name.includes('sdf') || name.includes('umbrella')) {
    return {
      color: '#0ea5e9',
      rgb: '14, 165, 233',
      symbolName: 'Umbrella',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Umbrella" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Umbrella" style={{ opacity: 0.1 }} />
    };
  }

  // 31. SKM
  if (name.includes('skm') || name.includes('lamp')) {
    return {
      color: '#FF3333',
      rgb: '255, 51, 51',
      symbolName: 'Table Lamp',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Table Lamp" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Table Lamp" style={{ opacity: 0.1 }} />
    };
  }

  // 32. UDP
  if (name.includes('udp') || name.includes('drum')) {
    return {
      color: '#FFCC00',
      rgb: '255, 204, 0',
      symbolName: 'Drum',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Drum" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Drum" style={{ opacity: 0.1 }} />
    };
  }

  // 33. ZPM
  if (name.includes('zpm') || name.includes('kettle')) {
    return {
      color: '#004D40',
      rgb: '0, 77, 64',
      symbolName: 'Kettle',
      SymbolIcon: (props) => <PartySymbolImage {...props} symbolName="Kettle" />,
      WatermarkIcon: (props) => <PartySymbolImage {...props} symbolName="Kettle" style={{ opacity: 0.1 }} />
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
