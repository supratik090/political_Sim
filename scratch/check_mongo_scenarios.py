import json

with open('/Users/supratikde/Desktop/DEV/Political party Sim/seed-data/startup/scenarios.json', 'r') as f:
    scenarios = json.load(f)

scenarios_2001 = [s for s in scenarios if s.get('scenarioKey', '').endswith('_2001')]

print(f"Total 2001 scenarios found in mongo seed: {len(scenarios_2001)}")
for s in scenarios_2001:
    parties = [p['partyKey'] for p in s.get('politicalParties', [])]
    gov = s.get('governmentPartyName')
    opp = s.get('oppositionPartyName')
    third = s.get('thirdPartyName')
    gov_sup = s.get('governmentStartingStats', {}).get('publicSupport')
    opp_sup = s.get('oppositionStartingStats', {}).get('publicSupport')
    third_sup = s.get('thirdPartyStartingStats', {}).get('publicSupport')
    print(f"State: {s.get('stateName')}, Key: {s.get('scenarioKey')}")
    print(f"  Gov: {gov} ({gov_sup}%), Opp: {opp} ({opp_sup}%), 3rd: {third} ({third_sup}%)")
    print(f"  Parties: {parties}")
