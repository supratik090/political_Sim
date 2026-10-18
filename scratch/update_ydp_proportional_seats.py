import json

file_path = 'seed-data/national/national_configs/2001.json'

with open(file_path, 'r') as f:
    data = json.load(f)

matrix = data['stateMatrix']
print(f"Total states: {len(matrix)}")

# Let's inspect total seats per state
total_ls_seats = 0
for sm in matrix:
    st_seats = sum(sm['partySeats'].values())
    total_ls_seats += st_seats
    print(f"{sm['stateName']}: {st_seats} seats")

print(f"Total Lok Sabha seats across all states: {total_ls_seats}")

# Distribution of 54 YDP seats proportionally based on state seat count:
# Larger states get 2-4 seats, medium get 1-2, smaller get 1 or 0 so it sums to exactly 54.
# Let's calculate target YDP seats per state:
ydp_target_total = 54
# Proportion of state_seats / 543 * 54
state_ydp = {}
assigned_ydp = 0

for sm in matrix:
    st_seats = sum(sm['partySeats'].values())
    # calculate float share
    share = (st_seats / 543.0) * 54.0
    val = int(round(share))
    if st_seats == 1 and val == 0:
        val = 0 # 1 seat states like Sikkim/Nagaland/Mizoram can stay 0 or get 0
    state_ydp[sm['stateName']] = val
    assigned_ydp += val

diff = ydp_target_total - assigned_ydp
print(f"Raw assigned YDP seats: {assigned_ydp}, diff needed: {diff}")

# Adjust diff on largest states
large_states = sorted(matrix, key=lambda s: sum(s['partySeats'].values()), reverse=True)
for i in range(abs(diff)):
    st_name = large_states[i]['stateName']
    if diff > 0:
        state_ydp[st_name] += 1
    else:
        state_ydp[st_name] -= 1

total_ydp_check = sum(state_ydp.values())
print(f"Adjusted YDP Total Seats: {total_ydp_check}")

# Apply YDP seats to matrix by deducting from the party with highest seats in each state
for sm in matrix:
    st_name = sm['stateName']
    ydp_seats = state_ydp[st_name]
    if ydp_seats > 0:
        # Find party with most seats in this state (excluding YDP)
        sorted_parties = sorted(
            [(k, v) for k, v in sm['partySeats'].items() if k != 'ydp' and v >= ydp_seats],
            key=lambda x: x[1],
            reverse=True
        )
        if not sorted_parties:
            # fallback if no single party has >= ydp_seats
            sorted_parties = sorted(
                [(k, v) for k, v in sm['partySeats'].items() if k != 'ydp' and v > 0],
                key=lambda x: x[1],
                reverse=True
            )
        
        needed = ydp_seats
        for p_key, p_seats in sorted_parties:
            deduct = min(needed, p_seats)
            sm['partySeats'][p_key] -= deduct
            needed -= deduct
            if needed == 0:
                break
        
        sm['partySeats']['ydp'] = sm['partySeats'].get('ydp', 0) + ydp_seats
    else:
        sm['partySeats']['ydp'] = 0

# Recalculate all party seat totals
party_seat_totals = {}
for sm in matrix:
    for k, v in sm['partySeats'].items():
        party_seat_totals[k] = party_seat_totals.get(k, 0) + v

print("\n--- Recalculated Party Seat Totals ---")
total_check = 0
for p_key, seats in sorted(party_seat_totals.items(), key=lambda x: x[1], reverse=True):
    print(f"{p_key}: {seats} seats")
    total_check += seats

print(f"\nTotal seats across all parties & states: {total_check}")

# Update parties array in data
for p in data['parties']:
    p_key = p['partyKey']
    seats = party_seat_totals.get(p_key, 0)
    p['initialSeats'] = seats
    p['power'] = int(round((seats / 543.0) * 100))
    if p_key == 'ydp':
        p['initialSeats'] = 54
        p['power'] = 10
        p['initialContent'] = 80
        p['description'] = "New upstart youth development party"
        p['activeInAllStates'] = True
        p['activeStates'] = [sm['stateName'] for sm in matrix if sm['partySeats'].get('ydp', 0) > 0]

# Write back to 2001.json
with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)

print("\nSuccessfully updated 2001.json with YDP ~54 seats (10% vote share, 4th largest party)!")
