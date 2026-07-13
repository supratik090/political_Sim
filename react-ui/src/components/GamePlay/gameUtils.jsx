import React from 'react';
import { getPartyThemeByName } from '../../constants/partyThemes';
import { useGameStore } from '../../store/gameStore';

export const getPartyColor = (party, allParties = null) => {
  if (!party) return '#6594B1';

  // 1. Resolve allParties: if not passed, try to fetch it from the store
  let partiesList = allParties;
  if (!partiesList) {
    const storeState = useGameStore.getState();
    partiesList = storeState.turnData?.parties || null;
  }

  // 2. Define a list of distinct fallback colors to assign in case of a clash
  const distinctColors = [
    '#E15554', // Coral Red
    '#3F88C5', // Steel Blue
    '#17B890', // Mint Green
    '#FF9933', // Saffron/Orange
    '#8B5CF6', // Purple
    '#EC4899', // Pink
    '#EAB308'  // Gold/Yellow
  ];

  // Helper function to resolve the base color for any party
  const getBaseColor = (p) => {
    if (!p) return '#6594B1';
    const theme = getPartyThemeByName(p.name || '');
    if (theme && theme.symbolName !== 'Ashoka Chakra' && theme.color !== '#000080') {
      return theme.color;
    }
    if (p.color && p.color !== '#ffffff' && p.color !== '#fff' && p.color !== '') {
      return p.color;
    }
    const role = p.role || p.startingRole || '';
    if (role === 'GOVERNMENT') return '#E15554';
    if (role === 'OPPOSITION') return '#3F88C5';
    return '#17B890';
  };

  const myBaseColor = getBaseColor(party);

  // If there are no other parties to compare with, return the base color directly
  if (!partiesList || partiesList.length <= 1) {
    return myBaseColor;
  }

  // Find my index in the current session's party list
  const myIndex = partiesList.findIndex(p => p.id === party.id || p.name === party.name || p.partyKey === party.partyKey);
  if (myIndex === -1) {
    return myBaseColor;
  }

  // Gather colors claimed by parties appearing *before* me in the list
  const claimedColors = [];
  for (let i = 0; i < myIndex; i++) {
    claimedColors.push(getBaseColor(partiesList[i]));
  }

  // If my base color conflicts with any previously claimed colors, assign an alternative
  if (claimedColors.includes(myBaseColor)) {
    // Find the first distinct fallback color that isn't claimed by *any* party in the game
    const allClaimedColors = partiesList.map(p => getBaseColor(p));
    const uniqueFallback = distinctColors.find(c => !allClaimedColors.includes(c) && !claimedColors.includes(c));
    if (uniqueFallback) {
      return uniqueFallback;
    }
    // Deep fallback: pick a distinct color based on index
    return distinctColors[myIndex % distinctColors.length];
  }

  return myBaseColor;
};

export const cardRequiresTarget = (card) => {
  if (!card || !card.target) return false;
  return !!card.target.opponentParty || (card.visibleEffects && Object.keys(card.visibleEffects.opponentParty || {}).length > 0);
};

export const getMetricSymbol = (key) => {
  switch (key) {
    case 'coins': return '💰';
    case 'partyMorale': return '✊';
    case 'corruptionScore': return '⚖️';
    case 'mediaImage': return '📢';
    case 'publicSupport': return '📈';
    default: return key;
  }
};

export const formatEffectValue = (key, val) => {
  const symbol = getMetricSymbol(key);
  const sign = val > 0 ? '+' : '';
  const percent = (key === 'publicSupport' || key === 'corruptionScore') ? '%' : '';
  return `${symbol} ${sign}${val}${percent}`;
};

export const getProgressCost = (projectDef, progress) => {
  return {
    coins: Math.ceil((projectDef.costCoins * progress) / 100),
    morale: Math.ceil((projectDef.costMorale * progress) / 100),
    corruption: Math.ceil((projectDef.costCorruption * progress) / 100),
    media: Math.ceil(((projectDef.costMedia || 0) * progress) / 100),
    support: Math.ceil(((projectDef.costSupport || 0) * progress) / 100)
  };
};

export const canAffordCost = (cost, stats) => {
  return (stats.coins || 0) >= cost.coins && 
         (stats.partyMorale || 0) >= cost.morale &&
         (stats.mediaImage || 0) >= cost.media &&
         (stats.publicSupport || 0) >= cost.support;
};

export const checkDefeatWarnings = (party) => {
  const warnings = [];
  const stats = party.stats || {};
  if (stats.coins <= 15) {
    warnings.push(`Coins are critically low (${stats.coins}). Party will face defeat at 0!`);
  }
  if (stats.partyMorale <= 15) {
    warnings.push(`Morale is critically low (${stats.partyMorale}). Party will face defeat below 10!`);
  }
  if (stats.corruptionScore >= 80) {
    warnings.push(`Corruption is critically high (${stats.corruptionScore}%). Party will face defeat above 95%!`);
  }
  if (stats.publicSupport <= 8) {
    warnings.push(`Public support is critically low (${stats.publicSupport}%). Party will face defeat below 5%!`);
  }
  return warnings;
};

export const renderStatDelta = (value, isPercentage = false, inverse = false) => {
  if (!value || value === 0) return null;
  const isGood = inverse ? value < 0 : value > 0;
  const color = isGood ? '#22c55e' : '#d23f31';
  const arrow = value > 0 ? '▲' : '▼';
  const sign = value > 0 ? '+' : '';
  const unit = isPercentage ? '%' : '';
  
  return (
    <span style={{ color, marginLeft: '6px', fontSize: '11px', fontWeight: '800' }}>
      {arrow} {sign}{value}{unit}
    </span>
  );
};

export const getFactionDisplayName = (partyName, factionKey) => {
  const pName = (partyName || '').toLowerCase().trim();
  const fKey = (factionKey || '').toLowerCase().trim();

  // YDP
  if (pName.includes('ydp') || pName.includes('youth development')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Progressives';
    if (fKey === 'youth') return 'Insta Gang';
    if (fKey === 'trade_union' || fKey === 'trade') return 'Labour Wing';
  }

  // 1. BJP
  if (pName.includes('bjp') || pName.includes('nda')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Sangh Parivar';
    if (fKey === 'trade_union' || fKey === 'trade') return 'BMS (Mazdoor Sangh)';
    if (fKey === 'youth') return 'BJYM (Youth Wing)';
  }
  // 2. INC
  if (pName.includes('inc') || pName.includes('congress') || pName.includes('udf')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Working Committee';
    if (fKey === 'trade_union' || fKey === 'trade') return 'INTUC (Trade Union)';
    if (fKey === 'youth') return 'IYC (Youth Congress)';
  }
  // 3. CPM / CPI-M / Left Front / LDF
  if (pName.includes('cpi') || pName.includes('cpim') || pName.includes('ldf') || pName.includes('left')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Politburo Core';
    if (fKey === 'trade_union' || fKey === 'trade') return 'CITU (Trade Union)';
    if (fKey === 'youth') return 'SFI / DYFI (Youth)';
  }
  // 4. TMC
  if (pName.includes('tmc') || pName.includes('trinamool')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Trinamool Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'INTTUC (Labour Wing)';
    if (fKey === 'youth') return 'TMCP (Youth Front)';
  }
  // 5. DMK
  if (pName.includes('dmk') && !pName.includes('aiadmk')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Dravidian Ideologues';
    if (fKey === 'trade_union' || fKey === 'trade') return 'LPF (Labour Federation)';
    if (fKey === 'youth') return 'DMK Youth Wing';
  }
  // 6. AIADMK
  if (pName.includes('aiadmk')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Amma Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'ATP (Anna Sangam)';
    if (fKey === 'youth') return 'Youth Ani';
  }
  // 7. SP
  if (pName.includes('sp') || pName.includes('samajwadi')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Socialist Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'Samajwadi Shramik Sabha';
    if (fKey === 'youth') return 'Yuvjan Sabha';
  }
  // 8. BSP
  if (pName.includes('bsp')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Bahujan Cadres';
    if (fKey === 'trade_union' || fKey === 'trade') return 'BAMCEF Union';
    if (fKey === 'youth') return 'BSP Youth Wing';
  }
  // 9. TDP
  if (pName.includes('tdp') || pName.includes('telugu')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'NTR Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'TNTUC (Trade Union)';
    if (fKey === 'youth') return 'TNSF (Youth)';
  }
  // 10. RJD
  if (pName.includes('rjd')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'MY Alliance Core';
    if (fKey === 'trade_union' || fKey === 'trade') return 'RJD Shramik Sabha';
    if (fKey === 'youth') return 'Yuva RJD';
  }
  // 11. AAP
  if (pName.includes('aap')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Founding Volunteers';
    if (fKey === 'trade_union' || fKey === 'trade') return 'Shramik Sangathan';
    if (fKey === 'youth') return 'CYSS (Youth Wing)';
  }
  // 12. Shiv Sena
  if (pName.includes('shiv') || pName.includes('sena')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Balasaheb Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'Kamgar Sena';
    if (fKey === 'youth') return 'Yuva Sena';
  }
  // 13. JD(U) / JDU
  if (pName.includes('jd-u') || pName.includes('jdu') || pName.includes('jd(u)')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Janata Core Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'JD-U Shramik Cell';
    if (fKey === 'youth') return 'Chhatra JD-U';
  }
  // 14. JMM
  if (pName.includes('jmm')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Soren Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'Jharkhand Mazdoor Morcha';
    if (fKey === 'youth') return 'JMM Chhatra Morcha';
  }
  // 15. YSRCP / YSR
  if (pName.includes('ysr') || pName.includes('ysrcp')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'YSR Family Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'YSR Trade Union Congress';
    if (fKey === 'youth') return 'YSRCP Youth Wing';
  }
  // 16. SAD (Akali Dal)
  if (pName.includes('sad') || pName.includes('akali')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Akali Panthic Advisory';
    if (fKey === 'trade_union' || fKey === 'trade') return 'Akali Mazdoor Wing';
    if (fKey === 'youth') return 'SOI (Youth Wing)';
  }
  // 17. NC (National Conference)
  if (pName.includes('nc') || pName.includes('conference')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Abdullah Core Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'JKN Labour Cell';
    if (fKey === 'youth') return 'JKN Youth Front';
  }
  // 18. MNF
  if (pName.includes('mnf')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Mizo Nationalist Core';
    if (fKey === 'trade_union' || fKey === 'trade') return 'Mizo Labour Union';
    if (fKey === 'youth') return 'MNF Youth Front';
  }
  // 19. AGP
  if (pName.includes('agp')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Assam Movement Veterans';
    if (fKey === 'trade_union' || fKey === 'trade') return 'Asom Shramik Parishad';
    if (fKey === 'youth') return 'Asom Chhatra Parishad';
  }
  // 20. INLD
  if (pName.includes('inld')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Chautala Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'INLD Kamgar Wing';
    if (fKey === 'youth') return 'INSO (Youth Wing)';
  }
  // 21. JD(S)
  if (pName.includes('jd(s)') || pName.includes('jds')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Deve Gowda Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'JD(S) Labour Cell';
    if (fKey === 'youth') return 'JD(S) Youth Wing';
  }
  // 22. NDPP
  if (pName.includes('ndpp')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Rio Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'NDPP Labour Wing';
    if (fKey === 'youth') return 'NDPP Youth Front';
  }
  // 23. NPF
  if (pName.includes('npf')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Naga Peoples Advisory';
    if (fKey === 'trade_union' || fKey === 'trade') return 'NPF Trade Union';
    if (fKey === 'youth') return 'NPF Youth Association';
  }
  // 24. NPP
  if (pName.includes('npp')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Sangma Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'NPP Labour Front';
    if (fKey === 'youth') return 'NYF (Youth Front)';
  }
  // 25. PPA
  if (pName.includes('ppa')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Arunachal Tribal Core';
    if (fKey === 'trade_union' || fKey === 'trade') return 'PPA Shramik Union';
    if (fKey === 'youth') return 'PPA Youth Wing';
  }
  // 26. SDF
  if (pName.includes('sdf')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Chamling Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'Sikkim Shramik Union';
    if (fKey === 'youth') return 'SDF Youth Front';
  }
  // 27. SKM
  if (pName.includes('skm')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Golay Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'SKM Shramik Wing';
    if (fKey === 'youth') return 'SKM Youth Front';
  }
  // 28. UDP
  if (pName.includes('udp')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Khasi-Jaintia Advisory';
    if (fKey === 'trade_union' || fKey === 'trade') return 'UDP Labour Wing';
    if (fKey === 'youth') return 'UDP Youth Front';
  }
  // 29. ZPM
  if (pName.includes('zpm')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Zoram Reforms Council';
    if (fKey === 'trade_union' || fKey === 'trade') return 'ZPM Labour Front';
    if (fKey === 'youth') return 'ZPM Youth Front';
  }
  // 30. BJD
  if (pName.includes('bjd')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Patnaik Loyalists';
    if (fKey === 'trade_union' || fKey === 'trade') return 'Biju Shramik Samukhya';
    if (fKey === 'youth') return 'Biju Chhatra Janata Dal';
  }
  // 31. TRS / BRS
  if (pName.includes('trs') || pName.includes('brs')) {
    if (fKey === 'loyalist' || fKey === 'veteran') return 'Telangana Ideologues';
    if (fKey === 'trade_union' || fKey === 'trade') return 'TRS Labour Wing';
    if (fKey === 'youth') return 'TRSV (Youth Wing)';
  }

  // Fallbacks
  if (fKey === 'loyalist' || fKey === 'veteran') return 'Party Loyalists';
  if (fKey === 'trade_union' || fKey === 'trade') return 'Trade Unions';
  if (fKey === 'youth') return 'Youth Wing';

  // Fallbacks
  if (fKey === 'loyalist' || fKey === 'veteran') return 'Party Loyalists';
  if (fKey === 'trade_union' || fKey === 'trade') return 'Trade Unions';
  if (fKey === 'youth') return 'Youth Wing';

  // Capitalize word otherwise
  return factionKey.split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
};
