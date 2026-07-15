import json
import re

json_path = "/Users/supratikde/Desktop/DEV/Political party Sim/seed-data/startup/news.json"

print("Reading news.json...")
with open(json_path, 'r', encoding='utf-8') as f:
    news_data = json.load(f)

print(f"Loaded {len(news_data)} news items.")

# 1. Regex patterns for date suffix removal
suffix_patterns = [
    (re.compile(r',\s*addressing the \d{4}[-\s_]?\d{2} issues\.?', re.IGNORECASE), "."),
    (re.compile(r',\s*criticizing the handling of the \d{4}[-\s_]?\d{2} developments\.?', re.IGNORECASE), "."),
    (re.compile(r',\s*seeking a consensus on the \d{4}[-\s_]?\d{2} situation\.?', re.IGNORECASE), "."),
    (re.compile(r',\s*citing the sensitivity of the \d{4}[-\s_]?\d{2} context\.?', re.IGNORECASE), "."),
    (re.compile(r'\b(?:in relation to|regarding the) \d{4}[-\s_]?\d{2}\.?', re.IGNORECASE), ""),
    (re.compile(r'\b(?:in the) \d{4}[-\s_]?\d{2} (?:joint efforts)\.?', re.IGNORECASE), "")
]

# 2. Generalizing party names
party_replacements = [
    (r'\bMamata Banerjee leads a TMC delegation\b', 'Lead a high-level party delegation'),
    (r'\bMamata Banerjee\b', 'Our party leadership'),
    (r'\bBiman Bose\b', 'The party leadership'),
    (r'\bSusanta Ghosh\b', 'The former minister'),
    (r'\bNaveen Patnaik\b', 'The Chief Minister'),
    (r'\bNaveen\b', 'the Chief Minister'),
    (r'\bRabri Devi\b', 'The Chief Minister'),
    (r'\bLaloo Prasad\b', 'The party president'),
    (r'\bLalu Prasad\b', 'The party president'),
    (r'\bLalu\b', 'the party president'),
    (r'\bPaswan\b', 'rival leadership'),
    (r'\bParkash Singh Badal\b', 'The Chief Minister'),
    (r'\bBadal\b', 'the Chief Minister'),
    (r'\bAmarinder Singh\b', 'The Chief Minister'),
    (r'\bTarun Gogoi\b', 'The Chief Minister'),
    (r'\bGogoi\b', 'the Chief Minister'),
    (r'\bBabu Marandi\b', 'The Chief Minister'),
    (r'\bBabulal Marandi\b', 'The Chief Minister'),
    (r'\bArjun Munda\b', 'The Chief Minister'),
    (r'\bMunda\b', 'the Chief Minister'),
    (r'\bShibu Soren\b', 'The party leader'),
    (r'\bSoren\b', 'the party leader'),
    (r'\bOpposition BJP leaders\b', 'Opposition leaders'),
    (r'\bOpposition Congress leaders\b', 'Opposition leaders'),
    (r'\bOpposition RJD leaders\b', 'Opposition leaders'),
    (r'\bOpposition CPI\(M\) leaders\b', 'Opposition leaders'),
    (r'\bOpposition SAD leaders\b', 'Opposition leaders'),
    (r'\bOpposition BJD leaders\b', 'Opposition leaders'),
    (r'\bOpposition TMC leaders\b', 'Opposition leaders'),
    (r'\bTMC poll agents\b', 'Our poll agents'),
    (r'\bTMC-Congress pact\b', 'opposition alliance'),
    (r'\bLeft Front headquarters\b', 'Our headquarters'),
    (r'\bLeft Front\b', 'our coalition'),
    (r'\bBJD-BJP alliance\b', 'the ruling coalition'),
    (r'\bBJD-BJP coalition\b', 'the ruling coalition'),
    (r'\bBJP-BJD alliance\b', 'the ruling coalition'),
    (r'\bBJP-SAD alliance\b', 'the ruling coalition'),
    (r'\bSAD-BJP alliance\b', 'the ruling coalition'),
    (r'\bCongress-TMC alliance\b', 'the opposition coalition'),
    (r'\bTMC-Congress alliance\b', 'the opposition coalition'),
    (r'\bCongress-TMC pact\b', 'opposition pact'),
    (r'\bTMC-Congress pact\b', 'opposition pact'),
    (r'\bTrinamool Congress\b', 'our party'),
    (r'\bTrinamool\b', 'our party'),
    (r'\bTMC delegation\b', 'party delegation'),
    (r'\bTMC cadres\b', 'party cadres'),
    (r'\bTMC\b', 'our party'),
    (r'\bBJD cadres\b', 'party cadres'),
    (r'\bBJD\b', 'ruling party'),
    (r'\bBJP cadres\b', 'opposition cadres'),
    (r'\bBJP\b', 'opposition'),
    (r'\bRJD regime\b', 'ruling regime'),
    (r'\bRJD leaders\b', 'ruling party leaders'),
    (r'\bRJD\b', 'ruling party'),
    (r'\bCongress leaders\b', 'opposition leaders'),
    (r'\bCongress\b', 'opposition'),
    (r'\bCPI\(M\) cadres\b', 'rival cadres'),
    (r'\bCPI\(M\) leaders\b', 'opposition leaders'),
    (r'\bCPI\(M\) state secretary\b', 'the opposition state secretary'),
    (r'\bCPI\(M\) state unit\b', 'opposition state unit'),
    (r'\bCPI\(M\)\b', 'opposition'),
    (r'\bAkali Dal\b', 'ruling party'),
    (r'\bSAD cadres\b', 'party cadres'),
    (r'\bSAD\b', 'ruling party'),
]

# 3. Third-person government verbs to active player actions
govt_active_replacements = [
    (r'^The state government defends the audit as', 'Defend the audit as'),
    (r'^The state government defends the policy as', 'Defend the policy as'),
    (r'^The state government defends the decision as', 'Defend the decision as'),
    (r'^The state government defends', 'Defend'),
    (r'^The state administration coordinates', 'Coordinate'),
    (r'^The state administration deploys', 'Deploy'),
    (r'^The state administration sets up', 'Set up'),
    (r'^The Finance Minister announces', 'Announce'),
    (r'^The Finance Minister promises', 'Promise'),
    (r'^The Finance Department implements', 'Implement'),
    (r'^The CM initiates negotiations', 'Initiate negotiations'),
    (r'^The CM welcomes the new', 'Welcome the new'),
    (r'^The CM\'s office declines', 'Decline'),
    (r'^The CM decides', 'Decide'),
    (r'^The Education Department defends', 'Defend'),
    (r'^The Education Director declines', 'Decline'),
    (r'^The Forest Department strengthens', 'Strengthen'),
    (r'^The Chief Conservator of Forests declines', 'Decline'),
    (r'^The Commercial Tax Department conducts', 'Conduct'),
    (r'^The Finance Minister declines', 'Decline'),
    (r'^The Municipal Corporation launches', 'Launch'),
    (r'^The Municipal Corporation coordinates', 'Coordinate'),
    (r'^The Municipal Corporation deploys', 'Deploy'),
    (r'^The Municipal Corporation orders', 'Order'),
    (r'^The Agriculture Department releases', 'Release'),
    (r'^The Agriculture Department sets up', 'Set up'),
    (r'^The Land Department launches', 'Launch'),
    (r'^The land acquisition officer sets up', 'Set up'),
    (r'^The Mining Department launches', 'Launch'),
    (r'^The Mining Secretary declines', 'Decline'),
    (r'^The Fisheries Department initiates', 'Initiate'),
    (r'^The Fisheries Director declines', 'Decline'),
    (r'^The Vigilance Director welcomes', 'Direct the vigilance bureau to'),
    (r'^The Vigilance Bureau spokesperson declines', 'Decline'),
    (r'^The Health Department deploys', 'Deploy'),
    (r'^The Health Directorate declines', 'Decline'),
    (r'^The Infrastructure Department announces', 'Announce'),
    (r'^The Infrastructure Minister declines', 'Decline'),
    (r'^The Home Department coordinates', 'Coordinate'),
    (r'^The Home Department deploys', 'Deploy'),
    (r'^The Cooperative Department suspends', 'Suspend'),
    (r'^The Cooperative Registrar declines', 'Decline'),
    (r'^The Urban Development Department fast-tracks', 'Fast-track'),
    (r'^The state relief director declines', 'Decline'),
    (r'^The state election commissioner declines', 'Decline'),
    (r'^The state treasury declines', 'Decline'),
    (r'^The state cabinet spokesperson declines', 'Decline'),
    (r'^The Industry Minister declines', 'Decline'),
    (r'^The state election coordinators decline', 'Decline'),
    (r'^The Governor\'s office declines', 'Decline'),
    (r'^The Water Minister declines', 'Decline'),
    (r'^The Water Department suspends', 'Suspend'),
    (r'^The Mining Department declines', 'Decline'),
    (r'^The Jajpur Development Commissioner declines', 'Decline'),
    (r'^The Mining Minister declines', 'Decline'),
    (r'^The DGP office declines', 'Decline'),
    (r'^The Cooperative Minister declines', 'Decline'),
    (r'^The Public Health Engineering Department releases', 'Release emergency funds'),
    (r'^The Public Health Engineering Minister declines', 'Decline'),
    (r'^Tata Motors\' Bengal office declines', 'Decline'),
    (r'^Tata Motors declines', 'Decline'),
    
    # Generic "The state government" or "The government"
    (r'^The state government fast-tracks', 'Fast-track'),
    (r'^The state government announces', 'Announce'),
    (r'^The state government appoints', 'Appoint'),
    (r'^The state government files', 'File'),
    (r'^The state government releases', 'Release'),
    (r'^The state government deploys', 'Deploy'),
    (r'^The state government sets up', 'Set up'),
    (r'^The state government invokes', 'Invoke'),
    (r'^The state government welcomes', 'Welcome'),
    (r'^The state government initiates', 'Initiate'),
    
    (r'^The government fast-tracks', 'Fast-track'),
    (r'^The government announces', 'Announce'),
    (r'^The government appoints', 'Appoint'),
    (r'^The government files', 'File'),
    (r'^The government releases', 'Release'),
    (r'^The government deploys', 'Deploy'),
    (r'^The government sets up', 'Set up'),
    (r'^The government invokes', 'Invoke'),
    (r'^The government welcomes', 'Welcome'),
    (r'^The government initiates', 'Initiate'),
    
    # Opposition / Generic Third-person actions
    (r'^Opposition leaders stage', 'Stage'),
    (r'^Opposition leaders lead', 'Lead'),
    (r'^Opposition leaders demand', 'Demand'),
    (r'^Opposition leaders claim', 'Claim'),
    (r'^Opposition leaders organize', 'Organize'),
    (r'^Opposition leaders visit', 'Visit'),
    (r'^Opposition leaders support', 'Support'),
    (r'^Opposition leaders state', 'State'),
    (r'^Opposition leaders join', 'Join'),
    (r'^Opposition leaders call', 'Call'),
    (r'^Opposition leaders stage', 'Stage'),
    (r'^Opposition leaders accuse', 'Accuse'),
    (r'^Opposition leaders reject', 'Reject'),
    
    # "All parties" or "Both parties" active choices
    (r'^Both parties agree to', 'Agree to'),
    (r'^All parties issue a joint statement appreciating', 'Issue a joint statement appreciating'),
    (r'^All parties issue a joint statement', 'Issue a joint statement'),
    (r'^All parties agree to', 'Agree to'),
]

# Generic match for "The [X Department / Official] declines to [verb]" -> "Decline to [verb]"
generic_decline_pattern = re.compile(
    r'^The (?:[a-zA-Z\'\s\-]{2,30}) (?:declines|refuses) to (comment|release|publish|give|share|name)\b', 
    re.IGNORECASE
)

# Helper function to apply changes to text fields
def clean_text(text):
    if not text:
        return text
        
    original = text
    
    # 1. Date Suffixes
    for pattern, repl in suffix_patterns:
        text = pattern.sub(repl, text)
        
    # Clean up double periods or spaces around the end of sentences
    text = text.replace("..", ".").strip()
    
    # 2. Party Name Replacements
    for pattern, repl in party_replacements:
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
        
    # 3. Third Person -> First Person / Active Actions
    for pattern, repl in govt_active_replacements:
        text = re.sub(pattern, repl, text)
        
    # 4. Generic declines rule
    text = generic_decline_pattern.sub(r'Decline to \1', text)
        
    # Make sure starting character is capitalized if we stripped prefix
    if len(text) > 0:
        text = text[0].upper() + text[1:]
        
    return text

print("Migrating reactions...")
modified_count = 0
for item in news_data:
    # 1. Clean reactionOptions
    reactions = item.get("reactionOptions", [])
    for r in reactions:
        orig = r.get("text", "")
        cleaned = clean_text(orig)
        if cleaned != orig:
            r["text"] = cleaned
            modified_count += 1
            
        # Clean badOutcome in risk if present
        risk = r.get("risk", {})
        if risk and "badOutcome" in risk:
            orig_risk = risk["badOutcome"]
            cleaned_risk = clean_text(orig_risk)
            if cleaned_risk != orig_risk:
                risk["badOutcome"] = cleaned_risk
                modified_count += 1
                
    # 2. Clean options
    opts = item.get("options", [])
    for o in opts:
        orig = o.get("text", "")
        cleaned = clean_text(orig)
        if cleaned != orig:
            o["text"] = cleaned
            modified_count += 1
            
        risk = o.get("risk", {})
        if risk and "badOutcome" in risk:
            orig_risk = risk["badOutcome"]
            cleaned_risk = clean_text(orig_risk)
            if cleaned_risk != orig_risk:
                risk["badOutcome"] = cleaned_risk
                modified_count += 1

print(f"Applied {modified_count} text updates.")

print("Saving news.json...")
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(news_data, f, indent=2, ensure_ascii=False)

print("Migration completed successfully!")
