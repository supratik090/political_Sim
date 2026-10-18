import json

with open('seed-data/national/national_configs/2001.json', 'r') as f:
    data = json.load(f)

print("Title:", data.get("title"))
print("Era:", data.get("era"))

# Let's inspect current party totals
parties = data["parties"]
print("\nParties before edit:")
for p in parties:
    print(f"{p['shortName']} ({p['partyKey']}): {p.get('initialSeats', 0)} seats")

# Let's check state matrix
state_matrix = data["stateMatrix"]
print(f"\nTotal states in matrix: {len(state_matrix)}")
