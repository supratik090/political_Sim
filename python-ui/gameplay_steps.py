import requests
import streamlit as st

from api_client import advance_turn
from constants import SYMBOL_ART, CATEGORY_LABELS, CATEGORY_COLORS
from ui_components import (
    inject_game_css,
    render_party_banner,
    render_selected_card_panel,
    render_party_panel,
    render_last_decisions_panel,
    render_playable_card,
    card_requires_target,
)


def summarize_reaction_effects(reaction):
    effects = reaction.get("effects", {}).get("selfParty", {})
    if not effects:
        effects = reaction.get("effects", {}).get("playerParty", {})
    if not effects:
        return "No immediate effect"
    labels = {
        "coins": "Coins",
        "partyMorale": "Morale",
        "corruptionScore": "Corruption",
        "mediaImage": "Media",
        "publicSupport": "Support",
    }
    parts = []
    for key in ["coins", "partyMorale", "corruptionScore", "mediaImage", "publicSupport"]:
        if key in effects and effects[key] != 0:
            value = effects[key]
            sign = "+" if value > 0 else ""
            parts.append(f"{labels[key]} {sign}{value}")
    return ", ".join(parts) if parts else "No immediate effect"


def summarize_issue_option_effects(option):
    effects = option.get("effects", {}).get("selfParty", {})
    if not effects:
        return "No immediate effect"
    labels = {
        "coins": "Coins",
        "partyMorale": "Morale",
        "corruptionScore": "Corruption",
        "mediaImage": "Media",
        "publicSupport": "Support",
    }
    parts = []
    for key in ["coins", "partyMorale", "corruptionScore", "mediaImage", "publicSupport"]:
        if key in effects and effects[key] != 0:
            value = effects[key]
            sign = "+" if value > 0 else ""
            parts.append(f"{labels[key]} {sign}{value}")
    return ", ".join(parts) if parts else "No immediate effect"


def summarize_delayed_effect(effect):
    effects = effect.get("effects", {}).get("selfParty", {})
    if not effects:
        opponent_effects = effect.get("effects", {}).get("opponentParty", {})
        if opponent_effects:
            effects = opponent_effects
    if not effects:
        return "No delayed effect"
    labels = {
        "coins": "Coins",
        "partyMorale": "Morale",
        "corruptionScore": "Corruption",
        "mediaImage": "Media",
        "publicSupport": "Support",
    }
    parts = []
    for key in ["coins", "partyMorale", "corruptionScore", "mediaImage", "publicSupport"]:
        if key in effects and effects[key] != 0:
            value = effects[key]
            sign = "+" if value > 0 else ""
            parts.append(f"{labels[key]} {sign}{value}")
    return ", ".join(parts) if parts else "No delayed effect"


def render_kbc_options(options, current_selection, key_prefix):
    labels = ["A", "B", "C", "D", "E", "F", "G", "H"]
    clicked_key = None
    
    # Render options in a 2x2 grid
    num_cols = 2
    rows = (len(options) + num_cols - 1) // num_cols
    
    for row in range(rows):
        cols = st.columns(num_cols)
        for col_idx in range(num_cols):
            opt_idx = row * num_cols + col_idx
            if opt_idx < len(options):
                opt = options[opt_idx]
                letter = labels[opt_idx] if opt_idx < len(labels) else str(opt_idx + 1)
                
                is_selected = (opt["key"] == current_selection)
                label_text = f"♦ {letter}: {opt['text']} ♦"
                if is_selected:
                    label_text = f"🔥 {letter}: {opt['text']} (SELECTED) 🔥"
                
                btn_type = "primary" if is_selected else "secondary"
                with cols[col_idx]:
                    if st.button(label_text, key=f"{key_prefix}-{opt['key']}", use_container_width=True, type=btn_type):
                        clicked_key = opt["key"]
    return clicked_key


@st.dialog("Campaign Successful! 🏆")
def show_victory_dialog(state_name, last_results):
    st.balloons()
    st.markdown(
        f"""
        <div style='text-align: center; font-family: "Montserrat", sans-serif;'>
            <div style='font-size: 60px;'>👑</div>
            <h2 style='color: #22c55e; font-weight: 800; margin-top: 10px;'>CONGRATULATIONS!</h2>
            <p style='font-size: 15px; margin-bottom: 20px;'>
                You have successfully led your party to victory in <b>{state_name}</b> and formed the government!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("**Final Election Results:**")
    for r in last_results:
        st.write(f"- {r}")
    if st.button("Continue to Dashboard", type="primary", use_container_width=True):
        st.rerun()


@st.dialog("Campaign Failed ❌")
def show_defeat_dialog(state_name, last_results):
    st.markdown(
        f"""
        <div style='text-align: center; font-family: "Montserrat", sans-serif;'>
            <div style='font-size: 60px;'>💀</div>
            <h2 style='color: #ef4444; font-weight: 800; margin-top: 10px;'>DEFEAT</h2>
            <p style='font-size: 15px; margin-bottom: 20px;'>
                Your campaign in <b>{state_name}</b> was unsuccessful.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("**Final Election Results:**")
    for r in last_results:
        st.write(f"- {r}")
    if st.button("Return to Start Screen", type="primary", use_container_width=True):
        st.rerun()


def render_turn_view(turn_view):
    inject_game_css()
    
    if st.session_state.get("scroll_to_top"):
        st.markdown(
            """
            <img src="does-not-exist" onerror="
              const scrollTarget = (el) => {
                if (el) {
                  try { el.scrollTo({top: 0, behavior: 'smooth'}); } catch(e) {}
                  el.scrollTop = 0;
                }
              };
              try {
                window.scrollTo({top: 0, behavior: 'smooth'});
                window.scrollTop = 0;
                scrollTarget(document.querySelector('section.main'));
                scrollTarget(document.querySelector('.stApp'));
                scrollTarget(document.documentElement);
                scrollTarget(document.body);
              } catch(e) {}
              try {
                if (window.parent && window.parent !== window) {
                  window.parent.scrollTo({top: 0, behavior: 'smooth'});
                  if (window.parent.document) {
                    scrollTarget(window.parent.document.querySelector('section.main'));
                    scrollTarget(window.parent.document.querySelector('.stApp'));
                    scrollTarget(window.parent.document.documentElement);
                    scrollTarget(window.parent.document.body);
                  }
                }
              } catch(e) {}
            " style="display:none;"/>
            """,
            unsafe_allow_html=True
        )
        st.session_state["scroll_to_top"] = False

    if st.session_state.get("scroll_to_stats"):
        st.markdown(
            """
            <img src="does-not-exist" onerror="
              const scrollToStats = (el) => {
                if (el) {
                  try { el.scrollIntoView({behavior: 'smooth', block: 'start'}); } catch(e) {}
                }
              };
              try {
                const el = document.getElementById('stats-focus') || (window.parent && window.parent.document && window.parent.document.getElementById('stats-focus'));
                scrollToStats(el);
              } catch(e) {}
            " style="display:none;"/>
            """,
            unsafe_allow_html=True
        )
        st.session_state["scroll_to_stats"] = False

    col_title, col_menu = st.columns([3, 1])
    with col_title:
        st.title("Political Strategy Sim")
    with col_menu:
        menu_option = st.selectbox(
            "⚙️ Campaign Menu",
            ["Select Action...", "Return to Start Screen", "Forfeit & End Campaign"],
            key="campaign_menu_select"
        )
        if menu_option == "Return to Start Screen":
            st.session_state["game_id"] = None
            st.rerun()
        elif menu_option == "Forfeit & End Campaign":
            try:
                from api_client import forfeit_game
                forfeit_game(turn_view["id"])
                st.session_state["game_id"] = None
                st.success("Campaign forfeited.")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")
    
    turn_number = turn_view.get("turnNumber", 1)
    progress_pct = min(100, max(0, (turn_number / 60.0) * 100.0))
    state_name = turn_view.get("stateName", "West Bengal")
    current_date = turn_view.get("currentDate", "2001-01-01")
    parts = current_date.split("-")
    formatted_date = f"{parts[0]} {parts[1]}" if len(parts) >= 2 else current_date
    election_in = turn_view.get("monthsUntilMandatoryElection", 60)
    status_label = turn_view.get("status", "ACTIVE")

    st.markdown(
        f"""<div style="background: linear-gradient(135deg, #6594B1 0%, #4a7692 100%); padding: 16px 20px; border-radius: 12px; border: 2px solid #213C51; margin-bottom: 25px; box-shadow: 0 4px 20px rgba(33,60,81,0.1); font-family: 'Montserrat', sans-serif;">
<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
<!-- Left Section: Location and Date -->
<div>
<span style="font-size: 10px; color: #ffffff !important; opacity: 0.9; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; display: block;">State and Date</span>
<div style="font-size: 16px; font-weight: 800; color: #ffffff !important; display: flex; align-items: center; gap: 6px; margin-top: 2px;">
<span style="color: #ffffff !important;">📍</span> <span style="color: #ffffff !important;">{state_name}</span> <span style="color: #213C51 !important; font-weight: 400;">|</span> 📅 <span style="color: #ffffff !important;">{formatted_date}</span>
</div>
</div>
<!-- Middle Section: Election Countdown -->
<div>
<span style="font-size: 10px; color: #ffffff !important; opacity: 0.9; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; display: block;">Election Countdown</span>
<div style="font-size: 15px; font-weight: 800; color: #ffffff !important; display: flex; align-items: center; gap: 6px; margin-top: 2px;">
<span style="color: #ffffff !important;">🗳️</span> <span style="color: #DDAED3 !important;">{election_in} months left</span> <span style="background-color: #22c55e !important; color: #ffffff !important; font-size: 9px; font-weight: 900; padding: 2px 6px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.05em; margin-left: 8px;">{status_label}</span>
</div>
</div>
<!-- Right Section: Progress Tracker -->
<div style="min-width: 220px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
<span style="font-size: 10px; color: #ffffff !important; opacity: 0.9; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em;">60-Month Cycle Progress</span>
<span style="font-size: 11px; font-weight: 800; color: #ffffff !important;">Month <span style="color: #DDAED3 !important;">{turn_number}</span>/60</span>
</div>
<!-- Progress Bar: Lavender (done) and transparent white (left) -->
<div style="width: 100%; height: 8px; background-color: rgba(255, 255, 255, 0.2); border-radius: 4px; overflow: hidden; display: flex; box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);">
<div style="width: {progress_pct}%; height: 100%; background-color: #22c55e !important; border-radius: 4px 0 0 4px;"></div>
</div>
</div>
</div>
</div>""",
        unsafe_allow_html=True
    )
    
    status_label = turn_view.get("status", "ACTIVE")
    is_game_over = status_label in ("GAME_OVER", "VICTORY", "DEFEAT")
    if status_label == "VICTORY":
        human_won = True
    elif status_label == "DEFEAT":
        human_won = False
    else:
        gov_party = turn_view.get("governmentParty")
        active_human_party_id = turn_view.get("activeHumanPartyId")
        human_won = bool(gov_party and active_human_party_id and gov_party.get("id") == active_human_party_id)

    if is_game_over:
        if human_won:
            if not st.session_state.get("victory_dialog_shown"):
                st.session_state["victory_dialog_shown"] = True
                show_victory_dialog(state_name, turn_view.get("lastResults", []))
        else:
            if not st.session_state.get("defeat_dialog_shown"):
                st.session_state["defeat_dialog_shown"] = True
                show_defeat_dialog(state_name, turn_view.get("lastResults", []))

        # Show final results banner
        if human_won:
            st.markdown(
                f"""
                <div style="background: linear-gradient(135deg, #15803d 0%, #166534 100%); padding: 25px; border-radius: 12px; border: 2px solid #22c55e; margin-bottom: 25px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.3); font-family: 'Montserrat', sans-serif;">
                    <div style="font-size: 50px; margin-bottom: 10px;">🏆</div>
                    <h2 style="color: #ffffff; font-weight: 800; margin: 0;">CAMPAIGN SUCCESSFUL!</h2>
                    <p style="font-size: 14px; color: #f0fdf4; margin-top: 8px; margin-bottom: 15px;">
                        Congratulations! You have successfully won the campaign and formed the government in {state_name}.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="background: linear-gradient(135deg, #991b1b 0%, #7f1d1d 100%); padding: 25px; border-radius: 12px; border: 2px solid #ef4444; margin-bottom: 25px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.3); font-family: 'Montserrat', sans-serif;">
                    <div style="font-size: 50px; margin-bottom: 10px;">❌</div>
                    <h2 style="color: #ffffff; font-weight: 800; margin: 0;">CAMPAIGN FAILED</h2>
                    <p style="font-size: 14px; color: #fef2f2; margin-top: 8px; margin-bottom: 15px;">
                        You were unable to win the election in {state_name}.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        st.subheader("Final Party Standings")
        party_columns = st.columns(3)
        for index, party in enumerate(turn_view.get("parties", [])):
            with party_columns[index % 3]:
                render_party_panel(
                    party["role"].replace("_", " ").title(),
                    party,
                    turn_view.get("lastMetricDeltas", {}).get(party["id"], {}),
                )
                
        st.write("")
        with st.expander("Final Logs & Verdict", expanded=True):
            st.write("**Final Election/Motion Results:**")
            for result in turn_view.get("lastResults", []):
                st.write(f"- {result}")
            st.write("**Campaign Commentary Log:**")
            for line in turn_view.get("lastRoundCommentary", []):
                st.write(f"- {line}")
                
        st.write("")
        if st.button("Return to Start Screen", key="game_over_return_btn", type="primary", use_container_width=True):
            st.session_state["game_id"] = None
            st.session_state.pop("victory_dialog_shown", None)
            st.session_state.pop("defeat_dialog_shown", None)
            st.rerun()
            
        return

    human_parties = [party for party in turn_view.get("parties", []) if party["playerControlled"]]
    active_party = next(
        (party for party in turn_view.get("parties", []) if party["id"] == turn_view.get("activeHumanPartyId")),
        human_parties[0] if human_parties else turn_view["parties"][0],
    )
    active_party_id = active_party["id"]

    # ----------------------------------------------------
    # Unified TBS Grid (Left: Status Panel, Right: Actions Panel)
    # ----------------------------------------------------
    col_left, col_right = st.columns([1.5, 2.2], gap="large")
    
    with col_left:
        # Active Player Medallion banner
        render_party_banner(active_party)
        
        st.markdown('<div id="stats-focus"></div>', unsafe_allow_html=True)
        st.markdown('<div class="standing-columns-marker"></div>', unsafe_allow_html=True)
        st.subheader("Current Standings")
        
        # Render the standings panels vertically
        for index, party in enumerate(turn_view.get("parties", [])):
            render_party_panel(
                party["role"].replace("_", " ").title(),
                party,
                turn_view.get("lastMetricDeltas", {}).get(party["id"], {}),
            )
            
        # Last Played (Last Turn Details) placed vertically below current standings
        last_submissions = turn_view.get("lastRoundSubmissions", [])
        if last_submissions:
            st.write("")
            st.subheader("Last Turn Decisions")
            
            # Check for revealed cycle reward in the last round's commentary
            cycle_reward_line = None
            for line in turn_view.get("lastRoundCommentary", []):
                if "🏆 CYCLE REWARD" in line:
                    cycle_reward_line = line
                    break
                    
            if cycle_reward_line:
                clean_msg = cycle_reward_line.replace("🏆 CYCLE REWARD AWARDED: ", "").replace("🏆 CYCLE REWARD: ", "")
                st.markdown(
                    f"""<div style="background: linear-gradient(135deg, #1e1b4b 0%, #311042 100%); border: 2px solid #8b5cf6; border-radius: 12px; padding: 12px 16px; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(139, 92, 246, 0.25); font-family: 'Montserrat', sans-serif;">
<div style="font-size: 10px; color: #a78bfa; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; display: flex; align-items: center; gap: 4px;">
<span>🏆</span> Revealed Cycle Reward
</div>
<div style="font-size: 14px; font-weight: 800; color: #ffffff; margin-top: 4px;">
{clean_msg}
</div>
</div>""",
                    unsafe_allow_html=True
                )
            
            last_by_party = {sub["partyId"]: sub for sub in last_submissions}
            for index, party in enumerate(turn_view.get("parties", [])):
                render_last_decisions_panel(
                    party,
                    last_by_party.get(party["id"]),
                    turn_view.get("lastRoundBiddingMetric"),
                    turn_view.get("lastRoundWinnerPartyId")
                )

            
        # Bidding Station has been moved to the right column below Party Decisions

    with col_right:
        # Calculate checklist requirements
        card_ready = bool(st.session_state.get("selected_card"))
        target_required = card_requires_target(st.session_state["selected_card"]) if card_ready else False
        target_ready = not target_required or bool(st.session_state.get("target_party_id"))
        
        news_items = turn_view.get("currentNews", [])
        selected_news = st.session_state.setdefault("selected_news_reactions", {})
        news_ready = all((news.get("newsKey") or news.get("issueKey")) in selected_news for news in news_items)
        
        issue_ready = not turn_view.get("currentIssue") or bool(st.session_state.get("selected_issue_option_key"))
        
        # 1. Card Selection / Drafted Card Block
        st.subheader("🃏 Select Card")
        if card_ready:
            card = st.session_state["selected_card"]
            render_selected_card_panel(card)
            
            # Inline target selection if required
            if target_required:
                st.markdown("#### 🎯 Select Target Opponent")
                target_parties = [p for p in turn_view.get("parties", []) if p["id"] != active_party_id]
                target_options = ["Select Target..."] + [p["name"] for p in target_parties]
                
                current_target_id = st.session_state.get("target_party_id")
                current_target_name = "Select Target..."
                if current_target_id:
                    t_party = next((p for p in target_parties if p["id"] == current_target_id), None)
                    if t_party:
                        current_target_name = t_party["name"]
                        
                selected_t_name = st.selectbox(
                    "Choose an opponent party to target:",
                    target_options,
                    index=target_options.index(current_target_name),
                    key="inline_card_target_select"
                )
                if selected_t_name == "Select Target...":
                    st.session_state["target_party_id"] = None
                else:
                    selected_t_party = next((p for p in target_parties if p["name"] == selected_t_name), None)
                    if selected_t_party:
                        st.session_state["target_party_id"] = selected_t_party["id"]
                        
            st.write("")
            if st.button("Change Campaign Move (Deselect)", type="secondary", use_container_width=True, key="cancel_drafted_card_btn"):
                st.session_state.pop("selected_card", None)
                st.session_state["target_party_id"] = None
                st.rerun()
        else:
            available_cards = turn_view.get("availableCards", [])
            
            deduped = {}
            for card in available_cards:
                deduped[card.get("cardKey", card["name"])] = card
            filtered_cards = list(deduped.values())
                
            if not filtered_cards:
                st.info("No cards available.")
            else:
                grouped = {}
                for card in filtered_cards:
                    grouped.setdefault(card.get("category", "other"), []).append(card)
                
                tab_names = []
                tab_keys = []
                for cat in sorted(grouped.keys()):
                    label = CATEGORY_LABELS.get(cat, cat.replace("_", " ").title())
                    tab_names.append(label)
                    tab_keys.append(cat)
                    
                if tab_names:
                    selected_category_label = st.selectbox(
                        "📁 Filter Cards by Category:",
                        tab_names,
                        key="card_category_filter_select"
                    )
                    selected_idx = tab_names.index(selected_category_label)
                    cat = tab_keys[selected_idx]
                    
                    cat_cards = sorted(grouped[cat], key=lambda item: item["name"])
                    for row_start in range(0, len(cat_cards), 2):
                        r_cols = st.columns(2)
                        for col, card in zip(r_cols, cat_cards[row_start:row_start + 2]):
                            with col:
                                render_playable_card(card, turn_view)

        # 2. News Reactions (inline form)
        if news_items:
            st.write("")
            with st.container(border=True):
                st.markdown("<div class='news-reactions-marker'></div>", unsafe_allow_html=True)
                st.markdown("### 📣 News Reactions")
                for news in news_items:
                    st.write(f"**{news['title']}**")
                    st.caption(news.get("description", ""))
                    
                    options = []
                    reaction_list = news.get("reactionOptions") or news.get("options") or []
                    for reaction in reaction_list:
                        effects_desc = summarize_reaction_effects(reaction)
                        reaction_key = reaction.get("reactionKey") or reaction.get("optionKey")
                        options.append({
                            "key": reaction_key,
                            "text": f"{reaction['text']} ({effects_desc})"
                        })
                        
                    news_key = news.get("newsKey") or news.get("issueKey")
                    current_selection = selected_news.get(news_key)
                    clicked_key = render_kbc_options(options, current_selection, f"news-react-{news_key}")
                    if clicked_key:
                        selected_news[news_key] = clicked_key
                        st.session_state["selected_news_reactions"] = selected_news
                        st.rerun()

        # 3. Party Decisions (inline form)
        issue = turn_view.get("currentIssue")
        if issue:
            st.write("")
            with st.container(border=True):
                st.markdown("<div class='party-decisions-marker'></div>", unsafe_allow_html=True)
                st.markdown("### 🏛️ Party Decisions")
                st.write(f"**{issue['title']}**")
                st.write(issue.get("description", ""))
                
                options = []
                for opt in issue.get("options", []):
                    effects_desc = summarize_issue_option_effects(opt)
                    options.append({
                        "key": opt["optionKey"],
                        "text": f"{opt['text']} ({effects_desc})"
                    })
                    
                current_selection = st.session_state.get("selected_issue_option_key")
                clicked_key = render_kbc_options(options, current_selection, f"issue-select-{issue['issueKey']}")
                if clicked_key:
                    st.session_state["selected_issue_option_key"] = clicked_key
                    st.rerun()

        # 4. Bidding Station (inline form)
        bid_metric = turn_view.get("biddingMetric", "COINS")
        cycle_turn = ((turn_view["turnNumber"] - 1) % 5) + 1
        
        stats = active_party.get("stats", {})
        metric_key_map = {
            "COINS": "coins",
            "CORRUPTION": "corruptionScore",
            "MORALE": "partyMorale",
            "MEDIA": "mediaImage",
            "PUBLIC_SUPPORT": "publicSupport"
        }
        metric_key = metric_key_map.get(bid_metric.upper(), "coins")
        max_bid = stats.get(metric_key, 0)
        
        st.write("")
        with st.container(border=True):
            # Inject CSS marker for background styling
            st.markdown("<div class='bidding-station-marker'></div>", unsafe_allow_html=True)
            st.markdown(f"### 🗳️ Bidding Station (Round {cycle_turn}/5)")
            st.write("")
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.markdown(
                    f"""
                    <div style="font-size: 9px; text-transform: uppercase; color: #cbd5e1; font-weight: 700; letter-spacing: 0.05em;">Bidding Metric</div>
                    <div style="font-size: 14px; font-weight: 800; color: #ffffff; margin-top: 2px;">⚡ {bid_metric.replace('_', ' ').upper()}</div>
                    """,
                    unsafe_allow_html=True
                )
            with col_m2:
                st.markdown(
                    f"""
                    <div style="font-size: 9px; text-transform: uppercase; color: #cbd5e1; font-weight: 700; letter-spacing: 0.05em;">Your Value</div>
                    <div style="font-size: 14px; font-weight: 800; color: #ffffff; margin-top: 2px;">💎 {max_bid}</div>
                    """,
                    unsafe_allow_html=True
                )
            
            wins_str = ', '.join([f"{p['name']}: {turn_view.get('partyRoundWins', {}).get(p['id'], 0)}" for p in turn_view.get('parties', [])])
            st.markdown(
                f"""
                <div style="margin-top: 10px; font-size: 11px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px; color: #cbd5e1;">
                    <b>Cycle Wins:</b> {wins_str}
                </div>
                """,
                unsafe_allow_html=True
            )
            
            if max_bid > 0:
                bid_val = st.slider("Select your BID", min_value=0, max_value=max_bid, value=st.session_state.get("bid_amount", 0), key="bidding_station_slider")
                st.session_state["bid_amount"] = bid_val
            else:
                st.info("Your value for this metric is 0 (Cannot place bid).")
                st.session_state["bid_amount"] = 0

        # 4. Held Rewards in its own block colored with DDAED3
        st.write("")
        with st.container(border=True):
            st.markdown("<div class='held-rewards-marker'></div>", unsafe_allow_html=True)
            st.markdown("### 🎒 Your Held Rewards")
            
            held = turn_view.get("activePlayerHeldRewards", [])
            if not held:
                st.markdown("<div style='font-size: 11px; color: #213C51; font-style: italic;'>No rewards currently held. Win bidding rounds to earn rewards!</div>", unsafe_allow_html=True)
            else:
                for r in held:
                    st.markdown(
                        f"<div style='background: rgba(255, 255, 255, 0.4); padding: 10px; border-radius: 8px; margin-bottom: 8px; border-left: 4px solid #213C51;'>"
                        f"<div style='font-size: 12px; font-weight: 700; color: #000000;'>🎁 {r['name']}</div>"
                        f"<div style='font-size: 11px; color: #213C51; margin-top: 2px;'>{r['description']}</div>"
                        f"<div style='font-size: 10px; color: #be123c; font-weight: bold; margin-top: 4px;'>⏳ Expires in {r['turnsLeft']} turn(s)</div>"
                        f"</div>",
                        unsafe_allow_html=True
                    )


        # 4. Play Reward (inline form if rewards present)
        held_rewards = turn_view.get("activePlayerHeldRewards", [])
        if held_rewards:
            st.write("")
            with st.container(border=True):
                st.markdown("<div class='play-reward-marker'></div>", unsafe_allow_html=True)
                st.markdown("### 🎒 Play Inventory Reward (Optional)")
                reward_options = ["None (Skip Reward)"] + [f"🎁 {r['name']} (Turns left: {r.get('turnsLeft', 1)})" for r in held_rewards]
                
                current_reward_key = st.session_state.get("selected_reward_key")
                current_idx = 0
                if current_reward_key:
                    for idx, r in enumerate(held_rewards):
                        if r["rewardKey"] == current_reward_key:
                            current_idx = idx + 1
                            break
                            
                selected_reward_label = st.selectbox(
                    "Select a reward card to play this turn:",
                    reward_options,
                    index=current_idx,
                    key="inline_reward_select_dropdown"
                )
                
                if selected_reward_label == "None (Skip Reward)":
                    st.session_state["selected_reward_key"] = None
                    st.session_state["reward_target_party_id"] = None
                else:
                    reward_idx = reward_options.index(selected_reward_label) - 1
                    selected_reward = held_rewards[reward_idx]
                    st.session_state["selected_reward_key"] = selected_reward["rewardKey"]
                    
                    if selected_reward.get("requiresTarget"):
                        target_parties = [p for p in turn_view.get("parties", []) if p["id"] != active_party_id]
                        target_party_names = [p["name"] for p in target_parties]
                        
                        current_reward_target = st.session_state.get("reward_target_party_id")
                        current_t_idx = 0
                        if current_reward_target:
                            for idx, p in enumerate(target_parties):
                                if p["id"] == current_reward_target:
                                    current_t_idx = idx
                                    break
                                    
                        chosen_t_name = st.selectbox(
                            "Select target party for reward:",
                            target_party_names,
                            index=current_t_idx,
                            key="inline_reward_target_select"
                        )
                        chosen_t_party = next((p for p in target_parties if p["name"] == chosen_t_name), None)
                        if chosen_t_party:
                            st.session_state["reward_target_party_id"] = chosen_t_party["id"]

        # 5. End Turn Submission Block
        st.write("")
        all_ready = card_ready and target_ready and news_ready and issue_ready
        
        if all_ready:
            st.success("🎉 All decisions locked! Ready to proceed.")
        else:
            st.warning("⚠️ Complete all required checklist items to advance turn.")
            
        if st.button("End Turn (Submit Decisions)", disabled=not all_ready, type="primary", use_container_width=True, key="tbs_end_turn_button"):
            try:
                advance_turn(
                    turn_view["gameId"],
                    {
                        "selectedCardKey": st.session_state["selected_card"]["cardKey"],
                        "targetPartyId": st.session_state.get("target_party_id"),
                        "selectedNewsReactions": st.session_state.get("selected_news_reactions", {}),
                        "selectedIssueOptionKey": st.session_state.get("selected_issue_option_key"),
                        "bid": st.session_state.get("bid_amount", 0),
                        "selectedRewardKey": st.session_state.get("selected_reward_key"),
                        "rewardTargetPartyId": st.session_state.get("reward_target_party_id"),
                    },
                )
                st.session_state.pop("selected_card", None)
                st.session_state["target_party_id"] = None
                st.session_state["selected_news_reactions"] = {}
                st.session_state["selected_issue_option_key"] = None
                st.session_state["selected_reward_key"] = None
                st.session_state["reward_target_party_id"] = None
                st.session_state["bid_amount"] = 0
                st.session_state["scroll_to_stats"] = True
                st.success("Turn advanced successfully!")
                st.rerun()
            except requests.RequestException as exc:
                st.error(f"Could not advance turn: {exc}")

    st.divider()

    
    # Combined Log expander containing party tabs, collapsing by default
    with st.expander("Logs & Round Summary", expanded=False):
        parties = turn_view.get("parties", [])
        active_party_id = turn_view.get("activeHumanPartyId")
        active_party = next((p for p in parties if p["id"] == active_party_id), None)
        
        other_parties = [p for p in parties if p["id"] != active_party_id]
        tab_parties = [active_party] + other_parties if active_party else other_parties
        tab_names = [p["name"] for p in tab_parties] + ["All Parties"]
        
        tabs = st.tabs(tab_names)
        
        for idx, tab in enumerate(tabs):
            with tab:
                if idx < len(tab_parties):
                    filter_party_name = tab_parties[idx]["name"]
                    filter_party_id = tab_parties[idx]["id"]
                else:
                    filter_party_name = "All Parties"
                    filter_party_id = None
                
                # 1. Commentary
                commentary = turn_view.get("lastRoundCommentary", [])
                if filter_party_name != "All Parties":
                    commentary = [line for line in commentary if filter_party_name.lower() in line.lower()]
                st.write("**Commentary:**")
                if commentary:
                    for line in commentary:
                        st.write(f"- {line}")
                else:
                    st.caption("No commentary matching this party.")
                    
                # 2. Locked Submissions
                submissions = turn_view.get("currentRoundSubmissions", [])
                if filter_party_id:
                    submissions = [s for s in submissions if s["partyId"] == filter_party_id]
                st.write("**Locked Moves This Month:**")
                if submissions:
                    for submission in submissions:
                        st.write(f"- {submission['partyName']} locked `{submission['cardName']}`")
                else:
                    st.caption("No locked moves matching this party.")
                    
                # 3. Pending / Delayed Results
                delayed_effects = turn_view.get("delayedEffects", [])
                pending_results_list = turn_view.get("pendingResults", [])
                if filter_party_name != "All Parties":
                    delayed_effects = [
                        eff for eff in delayed_effects
                        if (eff.get("targetPartyName") and filter_party_name.lower() == eff.get("targetPartyName", "").lower()) or
                           (eff.get("sourceName") and filter_party_name.lower() in eff.get("sourceName", "").lower())
                    ]
                    pending_results_list = [
                        res for res in pending_results_list
                        if filter_party_name.lower() in res.lower()
                    ]
                    
                st.write("**Pending / Delayed Results:**")
                if delayed_effects:
                    for effect in delayed_effects:
                        st.write(
                            f"- Turn {effect['dueTurnNumber']}: {effect['sourceName']} -> "
                            f"{effect['targetPartyName']} | {summarize_delayed_effect(effect)} | Chance {effect.get('chance', 100)}%"
                        )
                elif pending_results_list:
                    for result in pending_results_list:
                        st.write(f"- {result}")
                else:
                    st.caption("No pending results matching this party.")
