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
    delete_game,
)

# Import Gameplay steps
from gameplay_steps import render_turn_view

# Import Admin views
from admin_views import render_admin, west_bengal_2000_defaults
from ui_components import inject_game_css
import urllib.parse
import base64
import json

def render_login_page():
    st.markdown(
        """<div style="background: #6594B1; padding: 50px; border-radius: 16px; border: 2px solid #213C51; margin-top: 100px; text-align: center; box-shadow: 0 10px 30px rgba(33,60,81,0.05); font-family: 'Montserrat', sans-serif; max-width: 600px; margin-left: auto; margin-right: auto;">
<span style="font-size: 14px; color: #ffffff !important; text-transform: uppercase; font-weight: 800; letter-spacing: 0.15em; display: block; margin-bottom: 10px; opacity: 0.9;">GRAND ELECTION STRATEGY</span>
<h1 style="font-size: 36px; font-weight: 900; color: #ffffff !important; margin: 0; letter-spacing: -0.02em;">Indian Politics Simulation</h1>
<p style="font-size: 15px; color: #ffffff !important; opacity: 0.95; margin-top: 12px; margin-bottom: 30px; line-height: 1.5;">Sign in or register to govern state campaigns, design coalition policies, and maintain election sessions.</p>
</div>""",
        unsafe_allow_html=True
    )
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        st.write("")
        tab1, tab2 = st.tabs(["Login", "Register"])
        
        with tab1:
            with st.container(border=True):
                st.markdown("<h4 style='margin: 0 0 15px 0; color: #213C51 !important; text-align: center;'>Sign In</h4>", unsafe_allow_html=True)
                login_email = st.text_input("Email", key="login_email")
                login_password = st.text_input("Password", type="password", key="login_password")
                if st.button("Login", type="primary", use_container_width=True, key="login_btn"):
                    if login_email and login_password:
                        normalized_email = login_email.strip().lower()
                        st.session_state["user"] = {
                            "email": normalized_email,
                            "name": normalized_email.split("@")[0].capitalize(),
                            "picture": None
                        }
                        st.session_state["write_cache"] = True
                        st.rerun()
                    else:
                        st.error("Please enter both email and password.")

        with tab2:
            with st.container(border=True):
                st.markdown("<h4 style='margin: 0 0 15px 0; color: #213C51 !important; text-align: center;'>Create Account</h4>", unsafe_allow_html=True)
                reg_name = st.text_input("Full Name", key="reg_name")
                reg_email = st.text_input("Email", key="reg_email")
                reg_password = st.text_input("Password", type="password", key="reg_password")
                if st.button("Register", type="primary", use_container_width=True, key="reg_btn"):
                    if reg_name and reg_email and reg_password:
                        normalized_email = reg_email.strip().lower()
                        st.session_state["user"] = {
                            "email": normalized_email,
                            "name": reg_name.strip(),
                            "picture": None
                        }
                        st.session_state["write_cache"] = True
                        st.rerun()
                    else:
                        st.error("Please fill out all fields to register.")



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
            st.session_state["news_definitions"] = {(news.get("newsKey") or news.get("issueKey")): news for news in news_list}
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
    col_empty, col_user_info, col_admin_btn, col_logout_btn = st.columns([2.5, 1.7, 1.2, 0.8])
    with col_user_info:
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; gap: 8px; font-family: 'Montserrat', sans-serif; padding-top: 6px;">
                <span style="font-size: 14px; color: #213C51 !important; text-overflow: ellipsis; overflow: hidden; white-space: nowrap;">👋 Welcome, <b style="font-weight: 800; color: #213C51 !important;">{user['name'] if user else 'Unknown'}</b>!</span>
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
        f"""<div style="background: #6594B1; padding: 30px; border-radius: 16px; border: 2px solid #213C51; margin-bottom: 25px; text-align: center; box-shadow: 0 10px 30px rgba(33,60,81,0.1); font-family: 'Montserrat', sans-serif;">
<span style="font-size: 12px; color: #ffffff !important; text-transform: uppercase; font-weight: 800; letter-spacing: 0.15em; display: block; margin-bottom: 5px; opacity: 0.9;">GRAND CAMPAIGN BOARD</span>
<h1 style="font-size: 40px; font-weight: 900; color: #ffffff !important; margin: 0; letter-spacing: -0.02em;">Indian Politics Simulation</h1>
<p style="font-size: 15px; color: #ffffff !important; margin-top: 8px; opacity: 0.95;">Command campaign strategies, form coalitions, and win state elections across the Indian union.</p>
<div style="display: inline-block; background-color: #213C51; border: 1px solid #213C51; padding: 6px 18px; border-radius: 20px; color: #ffffff !important; font-weight: 800; font-size: 14px; margin-top: 15px; text-transform: uppercase; letter-spacing: 0.05em;">
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
                badge = '<span style="background-color: #22c55e; color: #ffffff !important; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">🏆 WON</span>'
            elif status == "IN_PROGRESS":
                badge = '<span style="background-color: #213C51; color: #ffffff !important; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">🔥 IN PROGRESS</span>'
            elif status == "LOCKED":
                badge = '<span style="background-color: rgba(33, 60, 81, 0.1); color: #213C51 !important; border: 1px solid rgba(33, 60, 81, 0.3); padding: 3px 7px; border-radius: 4px; font-weight: bold; font-size: 11px;">🔒 LOCKED</span>'
            else:
                badge = '<span style="background-color: #DDAED3; color: #000000 !important; border: 1px solid #213C51; padding: 3px 7px; border-radius: 4px; font-weight: bold; font-size: 11px;">🔓 AVAILABLE</span>'

            table_rows += (
                f'<tr style="border-bottom: 1px solid rgba(33, 60, 81, 0.2);">'
                f'<td style="padding: 14px 10px; font-weight: bold; color: #000000;">📍 {name}</td>'
                f'<td style="padding: 14px 10px; color: #000000; font-size: 13px;">{display_name}</td>'
                f'<td style="padding: 14px 10px; text-align: right;">{badge}</td>'
                f'</tr>'
            )

        table_html = (
            f'<table style="width: 100%; border-collapse: collapse; font-family: \'Montserrat\', sans-serif; background-color: #ffffff; border-radius: 12px; overflow: hidden; border: 2px solid #213C51;">'
            f'<thead>'
            f'<tr style="background-color: #6594B1; border-bottom: 2px solid #213C51; text-align: left;">'
            f'<th style="padding: 14px 10px; color: #ffffff; font-size: 12px; text-transform: uppercase; font-weight: 800;">Campaign</th>'
            f'<th style="padding: 14px 10px; color: #ffffff; font-size: 12px; text-transform: uppercase; font-weight: 800;">Key</th>'
            f'<th style="padding: 14px 10px; color: #ffffff; font-size: 12px; text-transform: uppercase; font-weight: 800; text-align: right;">Status</th>'
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

                    retain_inst = False
                    if selected_scenario.get("scenarioKey", "").endswith("_2006"):
                        retain_inst = st.checkbox("Carry forward completed public institutions from previous campaign", value=False, key="retain_inst_checkbox")

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
                                        "retainInstitutions": retain_inst,
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

                selected_load = st.selectbox("Select Campaign", list(options.keys()))
                game_to_act = options[selected_load]
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📂 Load Selected Game", use_container_width=True):
                        st.session_state["game_id"] = game_to_act
                        st.session_state.pop("confirm_delete_game_id", None)
                        st.rerun()
                with col2:
                    if st.button("🗑️ Delete Selected Game", use_container_width=True):
                        st.session_state["confirm_delete_game_id"] = game_to_act
                
                if st.session_state.get("confirm_delete_game_id") == game_to_act:
                    st.warning("⚠️ Are you sure you want to delete this campaign? This action is permanent and cannot be undone.")
                    confirm_col1, confirm_col2 = st.columns(2)
                    with confirm_col1:
                        if st.button("Yes, Delete Campaign", use_container_width=True, type="primary"):
                            try:
                                delete_game(game_to_act)
                                st.success("Campaign deleted successfully!")
                                st.session_state.pop("confirm_delete_game_id", None)
                                st.rerun()
                            except Exception as e:
                                st.error(f"Failed to delete campaign: {e}")
                    with confirm_col2:
                        if st.button("Cancel", use_container_width=True):
                            st.session_state.pop("confirm_delete_game_id", None)
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
inject_game_css()

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



if "user" not in st.session_state:
    st.markdown(
        """
        <img src="does-not-exist" onerror="
            try {
                const dataStr = localStorage.getItem('political_sim_user_cache');
                if (dataStr) {
                    const cache = JSON.parse(dataStr);
                    if (cache && cache.user && cache.expiresAt) {
                        const now = new Date().getTime();
                        if (now < cache.expiresAt) {
                            const userParam = encodeURIComponent(JSON.stringify(cache.user));
                            window.location.href = window.location.origin + window.location.pathname + '?cache_user=' + userParam;
                        } else {
                            localStorage.removeItem('political_sim_user_cache');
                        }
                    }
                }
            } catch (e) {
                console.error('Failed to read localStorage:', e);
            }
        " style="display:none;"/>
        """,
        unsafe_allow_html=True
    )
    render_login_page()
else:
    import time

    if st.session_state.get("clear_cache"):
        st.markdown(
            """
            <img src="does-not-exist" onerror="
                try {
                    localStorage.removeItem('political_sim_user_cache');
                    window.location.href = window.location.origin + window.location.pathname;
                } catch (e) {
                    console.error('Failed to clear localStorage:', e);
                }
            " style="display:none;"/>
            """,
            unsafe_allow_html=True
        )
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
        cache_b64 = base64.b64encode(cache_json.encode("utf-8")).decode("utf-8")
        st.markdown(
            f"""
            <img src="does-not-exist" onerror="
                try {{
                    localStorage.setItem('political_sim_user_cache', atob('{cache_b64}'));
                }} catch (e) {{
                    console.error('Failed to write to localStorage:', e);
                }}
            " style="display:none;"/>
            """,
            unsafe_allow_html=True
        )
        st.session_state.pop("write_cache", None)

    game_page = st.Page(game_main, title="Indian Politics Simulation", url_path="game", default=True)
    admin_page = st.Page(admin_main, title="Admin Console", url_path="admin")

    pg = st.navigation([game_page, admin_page], position="hidden")
    pg.run()


