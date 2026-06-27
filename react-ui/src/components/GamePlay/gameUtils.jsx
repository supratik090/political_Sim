import React from 'react';
import { getPartyThemeByName } from '../../constants/partyThemes';

export const getPartyColor = (party) => {
  if (!party) return '#6594B1';
  const theme = getPartyThemeByName(party.name || '');
  if (theme && theme.symbolName !== 'Flag') {
    return theme.color;
  }
  if (party.color && party.color !== '#ffffff' && party.color !== '#fff' && party.color !== '') {
    return party.color;
  }
  const role = party.role || '';
  if (role === 'GOVERNMENT') return '#E15554'; // Coral Red
  if (role === 'OPPOSITION') return '#3F88C5'; // Steel Blue
  return '#17B890'; // Mint Green (Third Party)
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
