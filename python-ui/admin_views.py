import json
import requests
from datetime import date
import streamlit as st

from constants import IDEOLOGIES
from api_client import api_get, api_post, api_put, api_delete


def parse_json_area(label, default_value, height=180):
    raw = st.text_area(label, json.dumps(default_value, indent=2), height=height)
    try:
        return json.loads(raw), None
    except json.JSONDecodeError as exc:
        return None, str(exc)


def west_bengal_2000_defaults():
    from constants import DEFAULT_AI_PROFILES
    return {
        "scenarioKey": "west_bengal_2000",
        "name": "West Bengal 2000",
        "description": "Fictionalized Indian state scenario inspired by long incumbency, organized cadre politics, rural unrest, and a rising opposition mood.",
        "stateName": "West Bengal",
        "startDate": "2000-10-01",
        "cycleLengthMonths": 60,
        "governmentPartyName": "Tiger Front",
        "oppositionPartyName": "Elephant Congress",
        "thirdPartyName": "Peacock Party",
        "governmentStartingStats": {
            "coins": 260,
            "partyMorale": 76,
            "corruptionScore": 38,
            "mediaImage": 58,
            "publicSupport": 46,
        },
        "oppositionStartingStats": {
            "coins": 145,
            "partyMorale": 52,
            "corruptionScore": 20,
            "mediaImage": 44,
            "publicSupport": 30,
        },
        "thirdPartyStartingStats": {
            "coins": 120,
            "partyMorale": 52,
            "corruptionScore": 16,
            "mediaImage": 42,
            "publicSupport": 15,
        },
        "politicalParties": [
            {
                "partyKey": "tiger_front",
                "name": "Tiger Front",
                "startingRole": "GOVERNMENT",
                "defaultControllerType": "COMPUTER",
                "color": "#d23f31",
                "symbol": "Tiger",
                "ideology": "DEVELOPMENT_FIRST",
                "aiProfile": DEFAULT_AI_PROFILES["GOVERNMENT"],
                "startingStats": {
                    "coins": 260,
                    "partyMorale": 76,
                    "corruptionScore": 38,
                    "mediaImage": 58,
                    "publicSupport": 46,
                },
            },
            {
                "partyKey": "elephant_congress",
                "name": "Elephant Congress",
                "startingRole": "OPPOSITION",
                "defaultControllerType": "HUMAN",
                "color": "#244f9e",
                "symbol": "Elephant",
                "ideology": "ANTI_CORRUPTION",
                "aiProfile": DEFAULT_AI_PROFILES["OPPOSITION"],
                "startingStats": {
                    "coins": 145,
                    "partyMorale": 52,
                    "corruptionScore": 20,
                    "mediaImage": 44,
                    "publicSupport": 30,
                },
            },
            {
                "partyKey": "peacock_party",
                "name": "Peacock Party",
                "startingRole": "THIRD_PARTY",
                "defaultControllerType": "COMPUTER",
                "color": "#1f8f5f",
                "symbol": "Peacock",
                "ideology": "REGIONAL_PRIDE",
                "aiProfile": DEFAULT_AI_PROFILES["THIRD_PARTY"],
                "startingStats": {
                    "coins": 120,
                    "partyMorale": 52,
                    "corruptionScore": 16,
                    "mediaImage": 42,
                    "publicSupport": 15,
                },
            },
        ],
        "publicState": {
            "undecidedSupport": 24,
            "mood": "Restless",
            "mainIssues": ["Jobs", "Rural distress", "Cadre dominance"],
            "memoryHint": "Voters remember long incumbency, but the opposition still needs credibility.",
        },
        "ruleWeights": {
            "antiIncumbencyGrowthPerTurn": 0.35,
            "scandalFatigueLimit": 5,
            "noConfidenceSupportThreshold": 30,
            "noConfidenceMoraleThreshold": 35,
            "electionCoinReductionPercent": 70,
            "publicMemoryDecayPerTurn": 0.1,
        },
        "active": True,
    }


def sample_card_defaults():
    return {
        "scenarioKey": "west_bengal_2000",
        "cardKey": "cleanliness_drive",
        "name": "Cleanliness Drive",
        "category": "positive_service",
        "roleAllowed": ["OPPOSITION", "GOVERNMENT"],
        "cost": 8,
        "maxUsesPerCycle": 2,
        "target": {"selfParty": True, "opponentParty": False, "public": True},
        "visibleEffects": {
            "scheduled": [
                {
                    "label": "civic_response",
                    "timing": {"minTurns": 1, "maxTurns": 3},
                    "effects": {
                        "selfParty": {"coins": -8, "partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
                        "opponentParty": {"coins": 0, "partyMorale": 0, "corruptionScore": 0, "mediaImage": 0, "publicSupport": 0},
                    },
                }
            ]
        },
        "hiddenEffects": {
            "scheduled": [
                {
                    "label": "service_memory",
                    "timing": {"minTurns": 2, "maxTurns": 5},
                    "effects": {"publicMemory": {"civicService": 4, "trustInParty": 2, "protestFatigue": -1}},
                }
            ]
        },
        "riskRoll": {
            "chance": 15,
            "badOutcome": "Seen as a photo-op.",
            "effects": {"selfParty": {"mediaImage": -2, "publicSupport": -1}},
        },
        "ideologyTags": {"strongFit": ["DEVELOPMENT_FIRST", "WELFARE_POPULIST"], "weakFit": ["IDENTITY_POLITICS"]},
        "timing": {"minTurns": 1, "maxTurns": 3},
        "weights": {
            "basePlayWeight": 1.0,
            "aiPriorityWeight": 0.8,
            "publicImpactWeight": 1.0,
            "riskWeight": 0.4,
        },
        "active": True,
    }


def sample_news_defaults():
    return {
        "scenarioKey": "west_bengal_2000",
        "newsKey": "new_government_formed",
        "type": "internal",
        "title": "New Government Formed By Tiger Front",
        "description": "Tiger Front begins another term. Voters are watching whether stability turns into delivery or fatigue.",
        "monthTags": ["october"],
        "issueTags": ["governance", "incumbency"],
        "reactionOptions": [
            {
                "reactionKey": "promise_stable_governance",
                "text": "Promise stable and responsible governance.",
                "roleAllowed": ["GOVERNMENT"],
                "effects": {"playerParty": {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1}},
                "hiddenEffects": {"publicMemory": {"governanceExpectation": 2}},
                "risk": {"chance": 10, "badOutcome": "Message feels routine.", "effects": {"playerParty": {"mediaImage": -1}}},
                "weight": 1,
            },
            {
                "reactionKey": "constructive_opposition",
                "text": "Accept the mandate and promise constructive opposition.",
                "roleAllowed": ["OPPOSITION"],
                "effects": {"playerParty": {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 1}},
                "hiddenEffects": {"publicMemory": {"oppositionMaturity": 2}},
                "risk": {"chance": 10, "badOutcome": "Cadre sees it as too soft.", "effects": {"playerParty": {"partyMorale": -2}}},
                "weight": 1,
            },
            {
                "reactionKey": "warn_on_delivery",
                "text": "Warn that voters will judge delivery, not speeches.",
                "roleAllowed": ["OPPOSITION"],
                "effects": {"playerParty": {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1}},
                "hiddenEffects": {"publicMemory": {"accountabilityNarrative": 1}},
                "risk": {},
                "weight": 1,
            },
            {
                "reactionKey": "thank_workers",
                "text": "Thank voters and party workers.",
                "roleAllowed": ["GOVERNMENT", "OPPOSITION"],
                "effects": {"playerParty": {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 0}},
                "hiddenEffects": {},
                "risk": {},
                "weight": 1,
            },
        ],
        "weights": {"baseSelectionWeight": 1, "cycleStartOnly": True},
        "active": True,
    }


def render_json_maintenance(items, resource_name, path):
    st.subheader(f"Existing {resource_name}")
    if not items:
        st.write(f"No {resource_name.lower()} found.")
        return

    for item in items:
        label = item.get("name") or item.get("title") or item.get("scenarioKey") or item.get("id")
        with st.expander(f"{label} | {item.get('id')}"):
            edited, error = parse_json_area(
                f"Edit JSON for {label}",
                item,
                height=320,
            )
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Save", key=f"save-{path}-{item.get('id')}"):
                    if error:
                        st.error(error)
                    else:
                        try:
                            api_put(f"{path}/{item['id']}", edited)
                            st.success("Saved.")
                            st.rerun()
                        except requests.RequestException as exc:
                            st.error(f"Save failed: {exc}")
            with col2:
                if st.button("Delete", key=f"delete-{path}-{item.get('id')}"):
                    try:
                        api_delete(f"{path}/{item['id']}")
                        st.success("Deleted.")
                        st.rerun()
                    except requests.RequestException as exc:
                        st.error(f"Delete failed: {exc}")


def render_quick_delete(items, resource_name, path, key_prefix):
    if not items:
        return

    options = {
        f"{item.get('name') or item.get('title') or item.get('scenarioKey')} | {item.get('id')}": item.get("id")
        for item in items
    }
    with st.expander(f"Quick Delete {resource_name}"):
        selected = st.selectbox(f"Select {resource_name[:-1]} To Delete", list(options.keys()), key=f"{key_prefix}-delete-select")
        st.warning("Delete is permanent once confirmed.")
        if st.button(f"Delete Selected {resource_name[:-1]}", key=f"{key_prefix}-delete-button"):
            try:
                api_delete(f"{path}/{options[selected]}")
                st.success("Deleted.")
                st.rerun()
            except requests.RequestException as exc:
                st.error(f"Delete failed: {exc}")


def render_scenario_admin():
    from constants import DEFAULT_AI_PROFILES
    st.header("Scenario Admin")
    st.caption("Create and maintain scenario-level starting state, rules, and weights.")

    defaults = west_bengal_2000_defaults()
    with st.form("create-scenario"):
        st.subheader("Create Scenario")
        scenario_key = st.text_input("Scenario Key", defaults["scenarioKey"])
        name = st.text_input("Name", defaults["name"])
        description = st.text_area("Description", defaults["description"])
        state_name = st.text_input("State Name", defaults["stateName"])
        start_date = st.date_input("Start Date", date(2000, 1, 1))
        cycle_length = st.number_input("Cycle Length Months", min_value=1, max_value=120, value=60)
        st.markdown("#### Political Parties")
        st.caption("MVP scenarios support exactly three political parties: government, opposition, and third party.")

        p1, p2, p3 = st.columns(3)
        with p1:
            government_party_name = st.text_input("Party 1 Name", defaults["governmentPartyName"])
            government_party_key = st.text_input("Party 1 Key", defaults["politicalParties"][0]["partyKey"])
            government_ideology_label = st.selectbox(
                "Party 1 Ideology",
                list(IDEOLOGIES.keys()),
                index=list(IDEOLOGIES.values()).index(defaults["politicalParties"][0]["ideology"]),
                key="scenario-gov-ideology",
            )
        with p2:
            opposition_party_name = st.text_input("Party 2 Name", defaults["oppositionPartyName"])
            opposition_party_key = st.text_input("Party 2 Key", defaults["politicalParties"][1]["partyKey"])
            opposition_ideology_label = st.selectbox(
                "Party 2 Ideology",
                list(IDEOLOGIES.keys()),
                index=list(IDEOLOGIES.values()).index(defaults["politicalParties"][1]["ideology"]),
                key="scenario-opp-ideology",
            )
        with p3:
            third_party_name = st.text_input("Party 3 Name", defaults["thirdPartyName"])
            third_party_key = st.text_input("Party 3 Key", defaults["politicalParties"][2]["partyKey"])
            third_ideology_label = st.selectbox(
                "Party 3 Ideology",
                list(IDEOLOGIES.keys()),
                index=list(IDEOLOGIES.values()).index(defaults["politicalParties"][2]["ideology"]),
                key="scenario-third-ideology",
            )

        left, middle, right = st.columns(3)
        with left:
            govt_stats, govt_error = parse_json_area("Party 1 Starting Stats", defaults["governmentStartingStats"])
            govt_ai_profile, govt_ai_error = parse_json_area("Party 1 AI Profile", defaults["politicalParties"][0]["aiProfile"])
        with middle:
            opp_stats, opp_error = parse_json_area("Party 2 Starting Stats", defaults["oppositionStartingStats"])
            opp_ai_profile, opp_ai_error = parse_json_area("Party 2 AI Profile", defaults["politicalParties"][1]["aiProfile"])
        with right:
            third_stats, third_error = parse_json_area("Party 3 Starting Stats", defaults["thirdPartyStartingStats"])
            third_ai_profile, third_ai_error = parse_json_area("Party 3 AI Profile", defaults["politicalParties"][2]["aiProfile"])

        public_state, public_error = parse_json_area("Public State", defaults["publicState"])
        rule_weights, weights_error = parse_json_area("Rule Weights", defaults["ruleWeights"])
        active = st.checkbox("Active", value=True)
        submitted = st.form_submit_button("Create Scenario", type="primary")

    if submitted:
        errors = [
            err
            for err in [
                govt_error,
                opp_error,
                third_error,
                govt_ai_error,
                opp_ai_error,
                third_ai_error,
                public_error,
                weights_error,
            ]
            if err
        ]
        if errors:
            st.error("; ".join(errors))
        else:
            payload = {
                "scenarioKey": scenario_key,
                "name": name,
                "description": description,
                "stateName": state_name,
                "startDate": start_date.isoformat(),
                "cycleLengthMonths": int(cycle_length),
                "governmentPartyName": government_party_name,
                "oppositionPartyName": opposition_party_name,
                "thirdPartyName": third_party_name,
                "governmentStartingStats": govt_stats,
                "oppositionStartingStats": opp_stats,
                "thirdPartyStartingStats": third_stats,
                "politicalParties": [
                    {
                        "partyKey": government_party_key,
                        "name": government_party_name,
                        "startingRole": "GOVERNMENT",
                        "defaultControllerType": "COMPUTER",
                        "ideology": IDEOLOGIES[government_ideology_label],
                        "aiProfile": govt_ai_profile,
                        "startingStats": govt_stats,
                    },
                    {
                        "partyKey": opposition_party_key,
                        "name": opposition_party_name,
                        "startingRole": "OPPOSITION",
                        "defaultControllerType": "HUMAN",
                        "ideology": IDEOLOGIES[opposition_ideology_label],
                        "aiProfile": opp_ai_profile,
                        "startingStats": opp_stats,
                    },
                    {
                        "partyKey": third_party_key,
                        "name": third_party_name,
                        "startingRole": "THIRD_PARTY",
                        "defaultControllerType": "COMPUTER",
                        "ideology": IDEOLOGIES[third_ideology_label],
                        "aiProfile": third_ai_profile,
                        "startingStats": third_stats,
                    },
                ],
                "publicState": public_state,
                "ruleWeights": rule_weights,
                "active": active,
            }
            try:
                api_post("/api/admin/scenarios", payload)
                st.success("Scenario created.")
                st.rerun()
            except requests.RequestException as exc:
                st.error(f"Create failed: {exc}")

    try:
        scenarios = api_get("/api/admin/scenarios")
        render_json_maintenance(scenarios, "Scenarios", "/api/admin/scenarios")
    except requests.RequestException as exc:
        st.error(f"Could not load scenarios: {exc}")


def render_card_admin():
    defaults = sample_card_defaults()
    with st.form("create-card"):
        st.subheader("Create Card")
        scenario_key = st.text_input("Scenario Key", defaults["scenarioKey"], key="card-scenario-key")
        card_key = st.text_input("Card Key", defaults["cardKey"])
        name = st.text_input("Name", defaults["name"], key="card-name")
        category = st.text_input("Category", defaults["category"])
        role_allowed = st.multiselect("Role Allowed", ["GOVERNMENT", "OPPOSITION", "THIRD_PARTY"], defaults["roleAllowed"])
        cost = st.number_input("Cost", min_value=0, max_value=9999, value=defaults["cost"])
        max_uses_per_cycle = st.number_input(
            "Max Uses Per Cycle",
            min_value=1,
            max_value=10,
            value=defaults["maxUsesPerCycle"],
        )
        target, target_error = parse_json_area("Target JSON", defaults["target"])
        visible_effects, visible_error = parse_json_area("Visible Effects JSON", defaults["visibleEffects"], height=260)
        hidden_effects, hidden_error = parse_json_area("Hidden Effects JSON", defaults["hiddenEffects"], height=220)
        risk_roll, risk_error = parse_json_area("Risk Roll JSON", defaults["riskRoll"])
        ideology_tags, ideology_error = parse_json_area("Ideology Tags JSON", defaults["ideologyTags"])
        timing, timing_error = parse_json_area("Timing JSON", defaults["timing"])
        weights, weights_error = parse_json_area("Card Weights JSON", defaults["weights"])
        active = st.checkbox("Active", value=True, key="card-active")
        submitted = st.form_submit_button("Create Card", type="primary")

    if submitted:
        errors = [err for err in [target_error, visible_error, hidden_error, risk_error, ideology_error, timing_error, weights_error] if err]
        if errors:
            st.error("; ".join(errors))
        else:
            payload = {
                "scenarioKey": scenario_key,
                "cardKey": card_key,
                "name": name,
                "category": category,
                "roleAllowed": role_allowed,
                "cost": int(cost),
                "maxUsesPerCycle": int(max_uses_per_cycle),
                "target": target,
                "visibleEffects": visible_effects,
                "hiddenEffects": hidden_effects,
                "riskRoll": risk_roll,
                "ideologyTags": ideology_tags,
                "timing": timing,
                "weights": weights,
                "active": active,
            }
            try:
                api_post("/api/admin/cards", payload)
                st.success("Card created.")
                st.rerun()
            except requests.RequestException as exc:
                st.error(f"Create failed: {exc}")

    filter_key = st.text_input("Filter Cards By Scenario Key", "west_bengal_2000")
    try:
        cards = api_get("/api/admin/cards", params={"scenarioKey": filter_key})
        render_quick_delete(cards, "Cards", "/api/admin/cards", "cards")
        render_json_maintenance(cards, "Cards", "/api/admin/cards")
    except requests.RequestException as exc:
        st.error(f"Could not load cards: {exc}")


def render_news_admin():
    defaults = sample_news_defaults()
    with st.form("create-news"):
        st.subheader("Create News Item")
        scenario_key = st.text_input("Scenario Key", defaults["scenarioKey"], key="news-scenario-key")
        news_key = st.text_input("News Key", defaults["newsKey"])
        news_type = st.selectbox("Type", ["external", "internal"], index=1)
        title = st.text_input("Title", defaults["title"])
        description = st.text_area("Description", defaults["description"])
        month_tags_raw = st.text_input("Month Tags comma-separated", ", ".join(defaults["monthTags"]))
        issue_tags_raw = st.text_input("Issue Tags comma-separated", ", ".join(defaults["issueTags"]))
        base_selection_weight = st.number_input(
            "News Base Selection Weight",
            min_value=0.0,
            max_value=100.0,
            value=float(defaults["weights"]["baseSelectionWeight"]),
            step=0.1,
        )
        reaction_options, reactions_error = parse_json_area("Reaction Options JSON", defaults["reactionOptions"], height=420)
        default_news_weights = {**defaults["weights"], "baseSelectionWeight": base_selection_weight}
        weights, weights_error = parse_json_area("News Weights JSON", default_news_weights)
        active = st.checkbox("Active", value=True, key="news-active")
        submitted = st.form_submit_button("Create News", type="primary")

    if submitted:
        errors = [err for err in [reactions_error, weights_error] if err]
        if errors:
            st.error("; ".join(errors))
        else:
            payload = {
                "scenarioKey": scenario_key,
                "newsKey": news_key,
                "type": news_type,
                "title": title,
                "description": description,
                "monthTags": [tag.strip() for tag in month_tags_raw.split(",") if tag.strip()],
                "issueTags": [tag.strip() for tag in issue_tags_raw.split(",") if tag.strip()],
                "reactionOptions": reaction_options,
                "weights": weights,
                "active": active,
            }
            try:
                api_post("/api/admin/news", payload)
                st.success("News item created.")
                st.rerun()
            except requests.RequestException as exc:
                st.error(f"Create failed: {exc}")

    filter_key = st.text_input("Filter News By Scenario Key", "west_bengal_2000")
    try:
        news_items = api_get("/api/admin/news", params={"scenarioKey": filter_key})
        render_quick_delete(news_items, "News Items", "/api/admin/news", "news")
        render_json_maintenance(news_items, "News Items", "/api/admin/news")
    except requests.RequestException as exc:
        st.error(f"Could not load news items: {exc}")


def render_issue_admin():
    st.header("Issue Admin")
    st.caption("Maintain role-specific monthly governance and party issues in MongoDB.")
    filter_key = st.text_input("Filter Issues By Scenario Key", "west_bengal_2000")
    try:
        issues = api_get("/api/admin/issues", params={"scenarioKey": filter_key})
        render_quick_delete(issues, "Issues", "/api/admin/issues", "issues")
        render_json_maintenance(issues, "Issues", "/api/admin/issues")
    except requests.RequestException as exc:
        st.error(f"Could not load issues: {exc}")


def render_admin():
    st.title("Admin Rule Editor")
    st.write("Maintain scenario rules, cards, news, and monthly issues in MongoDB through the Spring Boot backend.")
    tab1, tab2, tab3, tab4 = st.tabs(["Scenarios", "Cards", "News", "Issues"])
    with tab1:
        render_scenario_admin()
    with tab2:
        render_card_admin()
    with tab3:
        render_news_admin()
    with tab4:
        render_issue_admin()
