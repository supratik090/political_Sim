const fs = require('fs');

const data = JSON.parse(fs.readFileSync('seed-data/national/national_configs/2001.json', 'utf8'));

console.log('--- Current Party Summary ---');
let totalLokSabhaSeats = 0;
data.parties.forEach(p => {
  console.log(`${p.shortName} (${p.partyKey}): ${p.initialSeats} seats, power: ${p.power}%`);
  totalLokSabhaSeats += (p.initialSeats || 0);
});
console.log(`Total Party Seats: ${totalLokSabhaSeats}`);

console.log('\n--- State Matrix Total ---');
let stateMatrixSeats = 0;
data.stateMatrix.forEach(sm => {
  let sTotal = 0;
  Object.entries(sm.partySeats).forEach(([k, v]) => {
    sTotal += v;
  });
  stateMatrixSeats += sTotal;
});
console.log(`Total State Matrix Seats: ${stateMatrixSeats}`);
