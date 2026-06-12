import os
import requests
import streamlit as st
from datetime import date

# Import constants
from constants import (
    API_BASE_URL,
    IDEOLOGIES,
    PARTY_SYMBOLS,
    PARTY_COLORS,
    DEFAULT_AI_PROFILES,
    AI_PROFILE_PRESETS,
)

# Import API client
from api_client import (
    api_get,
    create_game,
    list_games,
    fetch_turn_view,
)

# Import Gameplay steps
from gameplay_steps import render_turn_view

# Import Admin views
from admin_views import render_admin, west_bengal_2000_defaults
import urllib.parse
import base64
import json

def handle_oauth_callback(code):
    client_id = os.environ.get("GOOGLE_CLIENT_ID")
    client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")
    redirect_uri = os.environ.get("GOOGLE_REDIRECT_URI", "http://localhost:8501/")
    
    if not client_id or not client_secret:
        return
        
    token_url = "https://oauth2.googleapis.com/token"
    payload = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }
    try:
        res = requests.post(token_url, data=payload, timeout=10)
        if res.status_code == 200:
            tokens = res.json()
            id_token = tokens.get("id_token")
            if id_token:
                parts = id_token.split(".")
                if len(parts) >= 2:
                    payload_b64 = parts[1]
                    payload_b64 += "=" * (4 - len(payload_b64) % 4)
                    user_info = json.loads(base64.b64decode(payload_b64).decode("utf-8"))
                    st.session_state["user"] = {
                        "email": user_info.get("email").strip().lower(),
                        "name": user_info.get("name"),
                        "picture": user_info.get("picture"),
                    }
                    st.session_state["write_cache"] = True
                    st.query_params.clear()
                    st.rerun()
    except Exception as e:
        st.error(f"Google authentication failed: {e}")

def render_login_page():
    st.markdown(
        """<div style="background: linear-gradient(135deg, #0b0f19 0%, #111827 100%); padding: 50px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.08); margin-top: 100px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); font-family: 'Montserrat', sans-serif; max-width: 600px; margin-left: auto; margin-right: auto;">
<span style="font-size: 14px; color: #fbbf24; text-transform: uppercase; font-weight: 800; letter-spacing: 0.15em; display: block; margin-bottom: 10px;">GRAND ELECTION STRATEGY</span>
<h1 style="font-size: 36px; font-weight: 900; color: #ffffff; margin: 0; letter-spacing: -0.02em;">Indian Politics Simulation</h1>
<p style="font-size: 15px; color: #a1a1aa; margin-top: 12px; margin-bottom: 30px; line-height: 1.5;">Login with your Google account to govern state campaigns, design coalition policies, and maintain election sessions.</p>
</div>""",
        unsafe_allow_html=True
    )
    
    client_id = os.environ.get("GOOGLE_CLIENT_ID")
    client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")
    redirect_uri = os.environ.get("GOOGLE_REDIRECT_URI", "http://localhost:8501/")
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if client_id and client_secret:
            google_auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={client_id}&redirect_uri={urllib.parse.quote(redirect_uri)}&scope=openid%20email%20profile"
            st.markdown(
                f"""
                <div style="text-align: center; margin-top: 20px;">
                    <a href="{google_auth_url}" target="_self" style="display: inline-block; padding: 12px 24px; background-color: #ffffff; color: #757575; border-radius: 24px; font-weight: bold; border: 1px solid #dadce0; text-decoration: none; font-size: 16px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: background-color 0.2s;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" style="width: 18px; margin-right: 12px; vertical-align: middle;"/>
                        Sign in with Google
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.info("💡 Real Google Authentication is not configured. Set GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET to enable.")
            
        st.markdown(
            """
            <div style="text-align: center; margin-top: 30px; padding: 20px; border-radius: 12px; background-color: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05);">
                <h4 style="margin: 0 0 10px 0; color: #fbbf24; font-size: 14px; text-transform: uppercase;">🔑 Developer Bypass Login</h4>
            </div>
            """,
            unsafe_allow_html=True
        )
        mock_email = st.text_input("Enter developer email:", "player@example.com", key="mock_email_input")
        if st.button("Proceed with Mock User", type="primary", use_container_width=True):
            normalized_email = mock_email.strip().lower()
            st.session_state["user"] = {
                "email": normalized_email,
                "name": normalized_email.split("@")[0].capitalize(),
                "picture": None
            }
            st.session_state["write_cache"] = True
            st.rerun()


def list_scenarios_for_game():
    try:
        scenarios = [scenario for scenario in api_get("/api/admin/scenarios") if scenario.get("active", True)]
    except requests.RequestException:
        scenarios = []
    if scenarios:
        return scenarios
    return [west_bengal_2000_defaults()]


def scenario_party_defaults(scenario):
    parties = scenario.get("politicalParties") or west_bengal_2000_defaults()["politicalParties"]
    normalized = []
    for index, party in enumerate(parties[:3]):
        normalized.append(
            {
                "partyKey": party.get("partyKey", f"party_{index + 1}"),
                "partyName": party.get("name", f"Party {index + 1}"),
                "role": party.get("startingRole", ["GOVERNMENT", "OPPOSITION", "THIRD_PARTY"][index]),
                "controllerType": party.get("defaultControllerType", "COMPUTER"),
                "ideology": party.get("ideology", "DEVELOPMENT_FIRST"),
                "color": party.get("color") or PARTY_COLORS[index % len(PARTY_COLORS)],
                "symbol": party.get("symbol") or PARTY_SYMBOLS[index % len(PARTY_SYMBOLS)],
                "aiProfile": party.get("aiProfile") or DEFAULT_AI_PROFILES.get(
                    {
                        "GOVERNMENT": "STRENGTH_BUILDER",
                        "OPPOSITION": "AGGRESSIVE_ATTACKER",
                        "THIRD_PARTY": "BALANCED_STRATEGIST",
                    }.get(
                        party.get("startingRole", ["GOVERNMENT", "OPPOSITION", "THIRD_PARTY"][index]),
                        "BALANCED_STRATEGIST"
                    ),
                    DEFAULT_AI_PROFILES["BALANCED_STRATEGIST"]
                ),
                "startingStats": party.get("startingStats"),
            }
        )
    return normalized


def format_game_date(date_str):
    if not date_str:
        return "2001 01"
    parts = date_str.split("-")
    if len(parts) >= 2:
        return f"{parts[0]} {parts[1]}"
    return date_str


def game_main():
    if "card_definitions" not in st.session_state:
        try:
            cards_list = api_get("/api/admin/cards")
            st.session_state["card_definitions"] = {card["cardKey"]: card for card in cards_list}
        except Exception:
            st.session_state["card_definitions"] = {}

    if "news_definitions" not in st.session_state:
        try:
            news_list = api_get("/api/admin/news")
            st.session_state["news_definitions"] = {news["newsKey"]: news for news in news_list}
        except Exception:
            st.session_state["news_definitions"] = {}

    game_id = st.session_state.get("game_id")
    
    # Render active gameplay screen without sidebar
    if game_id:
        try:
            turn_view = fetch_turn_view(game_id)
            render_turn_view(turn_view)
        except requests.RequestException as exc:
            st.error(f"Could not load game `{game_id}`: {exc}")
        return

    user = st.session_state.get("user")
    user_id = user.get("email") if user else None

    # Start Screen Mode - Render clean main screen without sidebar
    try:
        games = list_games(user_id=user_id)
    except Exception:
        games = []

    try:
        progress = api_get("/api/scenarios/progress", {"userId": user_id} if user_id else None)
    except Exception:
        progress = {"currentEra": 2001, "scenarios": []}

    current_era = progress.get("currentEra", 2001)

    # Admin Console and Logout header
    col_empty, col_user_info, col_admin_btn, col_logout_btn = st.columns([3, 1.2, 1.2, 0.8])
    with col_user_info:
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; gap: 8px; font-family: 'Montserrat', sans-serif; padding-top: 6px;">
                <span style="font-size: 13px; font-weight: bold; color: #a1a1aa; text-overflow: ellipsis; overflow: hidden; white-space: nowrap;">👤 {user['name'] if user else 'Unknown'}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_admin_btn:
        if st.button("🛠️ Admin Console", key="go_to_admin_btn", use_container_width=True):
            st.switch_page(admin_page)
    with col_logout_btn:
        if st.button("🚪 Logout", key="logout_btn", use_container_width=True):
            st.session_state["clear_cache"] = True
            st.rerun()

    # Title Banner Card
    st.markdown(
        f"""<div style="background: linear-gradient(135deg, #0b0f19 0%, #111827 100%); padding: 30px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.08); margin-bottom: 25px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); font-family: 'Montserrat', sans-serif;">
<span style="font-size: 12px; color: #fbbf24; text-transform: uppercase; font-weight: 800; letter-spacing: 0.15em; display: block; margin-bottom: 5px;">GRAND CAMPAIGN BOARD</span>
<h1 style="font-size: 40px; font-weight: 900; color: #ffffff; margin: 0; letter-spacing: -0.02em;">Indian Politics Simulation</h1>
<p style="font-size: 15px; color: #a1a1aa; margin-top: 8px;">Command campaign strategies, form coalitions, and win state elections across the Indian union.</p>
<div style="display: inline-block; background-color: rgba(251, 191, 36, 0.15); border: 1px solid #fbbf24; padding: 6px 18px; border-radius: 20px; color: #fbbf24; font-weight: 800; font-size: 14px; margin-top: 15px; text-transform: uppercase; letter-spacing: 0.05em;">
📅 Campaign Era: {current_era}
</div>
</div>""",
        unsafe_allow_html=True
    )


    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### 📊 Campaigns Status Table")
        
        table_rows = ""
        for item in progress.get("scenarios", []):
            name = item.get("stateName", "Unknown")
            display_name = item.get("name", "Unknown")
            status = item.get("status", "LOCKED")
            
            if status == "WON":
                badge = '<span style="background-color: #10b981; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">🏆 WON</span>'
            elif status == "IN_PROGRESS":
                badge = '<span style="background-color: #3b82f6; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">🔵 IN PROGRESS</span>'
            elif status == "LOCKED":
                badge = '<span style="background-color: #374151; color: #9ca3af; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">🔒 LOCKED</span>'
            else:
                badge = '<span style="background-color: #d97706; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">🔓 AVAILABLE</span>'

            table_rows += (
                f'<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">'
                f'<td style="padding: 14px 10px; font-weight: bold; color: #ffffff;">📍 {name}</td>'
                f'<td style="padding: 14px 10px; color: #9ca3af; font-size: 13px;">{display_name}</td>'
                f'<td style="padding: 14px 10px; text-align: right;">{badge}</td>'
                f'</tr>'
            )

        table_html = (
            f'<table style="width: 100%; border-collapse: collapse; font-family: \'Montserrat\', sans-serif; background-color: #0b0f19; border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.08);">'
            f'<thead>'
            f'<tr style="background-color: #111827; border-bottom: 1px solid rgba(255,255,255,0.1); text-align: left;">'
            f'<th style="padding: 14px 10px; color: #fbbf24; font-size: 12px; text-transform: uppercase; font-weight: 800;">Campaign</th>'
            f'<th style="padding: 14px 10px; color: #fbbf24; font-size: 12px; text-transform: uppercase; font-weight: 800;">Key</th>'
            f'<th style="padding: 14px 10px; color: #fbbf24; font-size: 12px; text-transform: uppercase; font-weight: 800; text-align: right;">Status</th>'
            f'</tr>'
            f'</thead>'
            f'<tbody>'
            f'{table_rows}'
            f'</tbody>'
            f'</table>'
        )
        st.markdown(table_html, unsafe_allow_html=True)


    with col2:
        # Buttons layout for Create & Load
        btn_col1, btn_col2 = st.columns(2)
        active_action = st.session_state.get("menu_action", None)
        
        with btn_col1:
            if st.button("🎮 Create Campaign", use_container_width=True, type="primary" if active_action == "create" else "secondary"):
                st.session_state["menu_action"] = "create"
                st.rerun()
        with btn_col2:
            if st.button("📂 Load Saved Campaign", use_container_width=True, type="primary" if active_action == "load" else "secondary"):
                st.session_state["menu_action"] = "load"
                st.rerun()

        # Render options below buttons
        if active_action == "create":
            st.markdown("### Choose a Campaign")
            
            # Build options map from progress
            scenario_options = {}
            for item in progress.get("scenarios", []):
                s = item.get("scenarioDefinition")
                if not s:
                    continue
                name = s.get("name")
                status = item.get("status", "LOCKED")
                
                if status == "LOCKED":
                    label = f"🔒 {name} (Locked - Win West Bengal first)"
                elif status == "WON":
                    label = f"👑 {name} (Won!)"
                else:
                    label = f"🟢 {name}"
                scenario_options[label] = (s, status)

            if not scenario_options:
                st.info("No campaigns found for the current era.")
            else:
                selected_label = st.selectbox("Select Scenario", list(scenario_options.keys()))
                selected_scenario, selected_status = scenario_options[selected_label]
                
                if selected_status == "Locked":
                    st.warning("This campaign is locked. Win the West Bengal campaign first to unlock it.")
                else:
                    st.markdown(f"**State**: {selected_scenario.get('stateName')}")
                    st.caption(selected_scenario.get("description", "No description available."))
                    
                    controller_mix = st.selectbox("Multiplayer Setting", ["1 Human + 2 Computer", "2 Human + 1 Computer"])
                    
                    st.markdown("#### Configure Parties")
                    party_setups = scenario_party_defaults(selected_scenario)
                    human_count_target = 1 if controller_mix == "1 Human + 2 Computer" else 2
                    human_count = 0
                    
                    for index, party in enumerate(party_setups):
                        with st.expander(f"{party['symbol']} {party['partyName']} - {party['role'].replace('_', ' ').title()}", expanded=True):
                            party["partyName"] = st.text_input("Party Name", party["partyName"], key=f"start-name-{index}")
                            c1, c2 = st.columns(2)
                            with c1:
                                party["color"] = st.color_picker("Party Color", party["color"], key=f"start-color-{index}")
                                party["symbol"] = st.selectbox(
                                    "Symbol / Flag Emblem",
                                    PARTY_SYMBOLS,
                                    index=PARTY_SYMBOLS.index(party["symbol"]) if party["symbol"] in PARTY_SYMBOLS else 0,
                                    key=f"start-symbol-{index}",
                                )
                            with c2:
                                party["controllerType"] = st.selectbox(
                                    "Controller",
                                    ["HUMAN", "COMPUTER"],
                                    index=0 if party["controllerType"] == "HUMAN" else 1,
                                    key=f"start-controller-{index}",
                                )
                                ideology_values = list(IDEOLOGIES.values())
                                ideology_labels = list(IDEOLOGIES.keys())
                                party["ideology"] = IDEOLOGIES[
                                    st.selectbox(
                                        "Ideology",
                                        ideology_labels,
                                        index=ideology_values.index(party["ideology"]) if party["ideology"] in ideology_values else 0,
                                        key=f"start-ideology-{index}",
                                    )
                                ]
                            if party["controllerType"] == "HUMAN":
                                human_count += 1
                            else:
                                from constants import DEFAULT_AI_PROFILES
                                style = None
                                if party.get("aiProfile"):
                                    style = party["aiProfile"].get("style")
                                else:
                                    if party["role"] == "GOVERNMENT":
                                        style = "STRENGTH_BUILDER"
                                    elif party["role"] == "OPPOSITION":
                                        style = "AGGRESSIVE_ATTACKER"
                                    else:
                                        style = "BALANCED_STRATEGIST"

                                st.markdown("##### AI Strategy Profile")
                                preset_names = list(AI_PROFILE_PRESETS.keys())
                                default_preset = "Balanced Strategist ⚖️"
                                for preset_name, preset in AI_PROFILE_PRESETS.items():
                                    if preset and preset.get("style") == style:
                                        default_preset = preset_name
                                        break
                                selected_preset = st.selectbox(
                                    "AI Strategy Profile",
                                    preset_names,
                                    index=preset_names.index(default_preset),
                                    key=f"start-ai-profile-{index}",
                                )
                                party["aiProfile"] = AI_PROFILE_PRESETS[selected_preset]
                                
                    if human_count != human_count_target:
                        st.warning(f"This setup needs exactly {human_count_target} human-controlled party/parties. Current: {human_count}.")

                    if st.button("Start Campaign", type="primary", use_container_width=True):
                        if human_count != human_count_target:
                            st.error(f"Cannot start: select exactly {human_count_target} human-controlled party/parties.")
                        else:
                            human_index = 1
                            payload_parties = []
                            for p in party_setups:
                                setup = dict(p)
                                setup["humanPlayerLabel"] = None
                                if setup["controllerType"] == "HUMAN":
                                    setup["humanPlayerLabel"] = f"Player {human_index}"
                                    human_index += 1
                                payload_parties.append(setup)

                            try:
                                game = create_game(
                                    {
                                        "scenarioKey": selected_scenario.get("scenarioKey"),
                                        "stateName": selected_scenario.get("stateName"),
                                        "startDate": "2006-01-01" if current_era == 2006 else "2001-01-01",
                                        "partySetups": payload_parties,
                                        "userId": user_id,
                                    }
                                )
                                st.session_state["game_id"] = game["id"]
                                st.success("Campaign started successfully!")
                                st.rerun()
                            except Exception as exc:
                                err_msg = str(exc)
                                if hasattr(exc, "response") and exc.response is not None:
                                    try:
                                        err_msg = exc.response.json().get("error", err_msg)
                                    except Exception:
                                        pass
                                st.error(f"Could not create campaign: {err_msg}")
        
        elif active_action == "load":
            st.markdown("### Load an Active Campaign")
            active_games = [g for g in games if g.get("status") == "ACTIVE"]
            
            if not active_games:
                st.caption("No active saved campaigns found.")
            else:
                options = {}
                for g in active_games:
                    scenario = g.get("scenarioKey") or "unknown_scenario"
                    current_date = g.get("currentDate") or "2001-01-01"
                    formatted_date = format_game_date(current_date)
                    game_id = g.get("id")
                    label = f"📍 {g.get('stateName', scenario)} | 📅 {formatted_date} | ID: {game_id[:8]}"
                    options[label] = game_id

                selected_load = st.selectbox("Load Game", list(options.keys()))
                if st.button("Load Selected Game", use_container_width=True):
                    st.session_state["game_id"] = options[selected_load]
                    st.rerun()


def admin_main():
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; font-family: 'Montserrat', sans-serif;">
            <h2 style="margin: 0; color: #ffffff;">🛠️ Admin Console</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("🎮 Return to Game", key="return_to_game_btn"):
        st.switch_page(game_page)
        
    render_admin()


# Page configurations and routing registration
st.set_page_config(page_title="Indian Politics Simulation", layout="wide")

# Check for cache_user query parameter
cache_user = st.query_params.get("cache_user")
if cache_user and "user" not in st.session_state:
    try:
        user_info = json.loads(urllib.parse.unquote(cache_user))
        st.session_state["user"] = user_info
        st.query_params.clear()
        st.rerun()
    except Exception as e:
        pass

# Check for OAuth callback code
code = st.query_params.get("code")
if code and "user" not in st.session_state:
    handle_oauth_callback(code)

if "user" not in st.session_state:
    import streamlit.components.v1 as components
    components.html("""
        <script>
            try {
                const dataStr = window.parent.localStorage.getItem("political_sim_user_cache");
                if (dataStr) {
                    const cache = JSON.parse(dataStr);
                    if (cache && cache.user && cache.expiresAt) {
                        const now = new Date().getTime();
                        if (now < cache.expiresAt) {
                            const userParam = encodeURIComponent(JSON.stringify(cache.user));
                            window.parent.location.href = window.parent.location.origin + window.parent.location.pathname + "?cache_user=" + userParam;
                        } else {
                            window.parent.localStorage.removeItem("political_sim_user_cache");
                        }
                    }
                }
            } catch (e) {
                console.error("Failed to read localStorage:", e);
            }
        </script>
    """, height=0, width=0)
    render_login_page()
else:
    import streamlit.components.v1 as components
    import time

    if st.session_state.get("clear_cache"):
        components.html("""
            <script>
                try {
                    window.parent.localStorage.removeItem("political_sim_user_cache");
                    window.parent.location.href = window.parent.location.origin + window.parent.location.pathname;
                } catch (e) {
                    console.error("Failed to clear localStorage:", e);
                }
            </script>
        """, height=0, width=0)
        st.session_state.pop("clear_cache", None)
        st.session_state.pop("user", None)
        st.session_state.pop("game_id", None)
        st.rerun()

    if st.session_state.get("write_cache"):
        user_data = st.session_state["user"]
        expires_at = int(time.time() * 1000) + (5 * 24 * 60 * 60 * 1000)  # 5 days
        cache_payload = {
            "user": user_data,
            "expiresAt": expires_at
        }
        cache_json = json.dumps(cache_payload)
        components.html(f"""
            <script>
                try {{
                    window.parent.localStorage.setItem("political_sim_user_cache", `{cache_json}`);
                }} catch (e) {{
                    console.error("Failed to write to localStorage:", e);
                }}
            </script>
        """, height=0, width=0)
        st.session_state.pop("write_cache", None)

    game_page = st.Page(game_main, title="Indian Politics Simulation", url_path="game", default=True)
    admin_page = st.Page(admin_main, title="Admin Console", url_path="admin")

    pg = st.navigation([game_page, admin_page], position="hidden")
    pg.run()


