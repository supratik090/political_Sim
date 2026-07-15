import json
import re

json_path = "/Users/supratikde/Desktop/DEV/Political party Sim/seed-data/startup/news.json"

with open(json_path, 'r', encoding='utf-8') as f:
    news_data = json.load(f)

print(f"Total news items: {len(news_data)}")

date_pattern = re.compile(r'\b(200\d)[-\s_]?\d\d?\b')
party_pattern = re.compile(r'\b(BJP|Congress|BJD|INC|CPM|CPI|SAD|SDF|JMM|SP|BSP|RJD|DMK|AIADMK|TDP|TRS|AGP|ZPM)\b', re.IGNORECASE)
third_person_patterns = [
    re.compile(r'^(The (Excise Department|state|ruling|opposition|CM|minister|election commissioner|relief director|PHE|administration|government|BJP|Congress|BJD|INC|CPM|CPI|SAD|SDF|JMM|SP|BSP|RJD|DMK|AIADMK|TDP|TRS|AGP|ZPM|BJP leaders|Congress leaders|Opposition BJP leaders|ruling BJD))', re.IGNORECASE),
    re.compile(r'\b(declines to comment|declines to release|demands a rollback)\b', re.IGNORECASE)
]

date_issues = []
party_issues = []
third_person_issues = []

for idx, item in enumerate(news_data):
    news_key = item.get("newsKey", "unknown")
    scenario = item.get("scenarioKey", "unknown")
    
    # Check reactions
    reactions = item.get("reactionOptions", [])
    for r in reactions:
        text = r.get("text", "")
        key = r.get("reactionKey", "")
        role = r.get("roleAllowed", [])
        
        # 1. Date reference issues
        date_match = date_pattern.search(text)
        if date_match:
            date_issues.append((scenario, news_key, key, text, date_match.group(0)))
            
        # 2. Specific party names issues
        party_match = party_pattern.search(text)
        if party_match:
            party_issues.append((scenario, news_key, key, text, party_match.group(0)))
            
        # 3. Third person vs active player perspective
        is_third = False
        matched_pat = ""
        for pat in third_person_patterns:
            m = pat.search(text)
            if m:
                is_third = True
                matched_pat = m.group(0)
                break
        if is_third:
            third_person_issues.append((scenario, news_key, key, text, matched_pat))

print(f"Date reference issues: {len(date_issues)}")
print(f"Party name issues: {len(party_issues)}")
print(f"Third person/Department stance issues: {len(third_person_issues)}")

print("\n--- SAMPLE DATE ISSUES (First 15) ---")
for x in date_issues[:15]:
    print(f"Scenario: {x[0]} | Key: {x[2]}")
    print(f"Text: {x[3]}")
    print(f"Matched: {x[4]}\n")

print("\n--- SAMPLE PARTY ISSUES (First 15) ---")
for x in party_issues[:15]:
    print(f"Scenario: {x[0]} | Key: {x[2]}")
    print(f"Text: {x[3]}")
    print(f"Matched: {x[4]}\n")

print("\n--- SAMPLE THIRD PERSON/DEPARTMENT ISSUES (First 15) ---")
for x in third_person_issues[:15]:
    print(f"Scenario: {x[0]} | Key: {x[2]}")
    print(f"Text: {x[3]}")
    print(f"Matched: {x[4]}\n")
