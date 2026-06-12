import requests
import streamlit as st

from api_client import advance_turn
from constants import SYMBOL_ART, CATEGORY_LABELS
from ui_components import (
    inject_game_css,
    render_party_banner,
    render_selected_card_panel,
    render_party_panel,
    render_last_decisions_panel,
    render_playable_card,
    card_requires_target,
    render_sidebar_inventory,
)



def render_card_deck(cards, turn_view):
    st.caption("Expand any card to view details and select it for your turn.")
    
    # Add Card Search bar
    search_query = st.text_input("🔍 Search Cards by Name", "").strip().lower()
    
    if st.session_state.get("selected_card"):
        st.info(f"Selected card: {st.session_state['selected_card']['name']}")
        if st.button("Cancel Card Selection", use_container_width=True):
            st.session_state.pop("selected_card", None)
            st.session_state["target_party_id"] = None
            st.rerun()
            
    if not cards:
        st.info("No cards available.")
        return

    deduped = {}
    for card in cards:
        deduped[card.get("cardKey", card["name"])] = card

    filtered_cards = list(deduped.values())
    if search_query:
        filtered_cards = [c for c in filtered_cards if search_query in c["name"].lower()]

    if not filtered_cards:
        st.warning("No cards match your search.")
        return

    grouped = {}
    for card in filtered_cards:
        grouped.setdefault(card.get("category", "other"), []).append(card)

    for category in sorted(grouped.keys()):
        label = CATEGORY_LABELS.get(category, category.replace("_", " ").title())
        st.markdown(f"### {label}")
        category_cards = sorted(grouped[category], key=lambda item: item["name"])
        for row_start in range(0, len(category_cards), 3):
            st.markdown('<div class="card-columns-marker"></div>', unsafe_allow_html=True)
            cols = st.columns(3)
            for col, card in zip(cols, category_cards[row_start:row_start + 3]):
                with col:
                    render_playable_card(card, turn_view)


def summarize_reaction_effects(reaction):
    effects = reaction.get("effects", {}).get("playerParty", {})
    parts = []
    labels = {
        "partyMorale": "Morale",
        "corruptionScore": "Corruption",
        "mediaImage": "Media",
        "publicSupport": "Support",
    }
    for key in ["partyMorale", "corruptionScore", "mediaImage", "publicSupport"]:
        value = effects.get(key, 0)
        if value:
            sign = "+" if value > 0 else ""
            parts.append(f"{labels[key]} {sign}{value}")
    return ", ".join(parts) if parts else "No visible effect"


def summarize_issue_option_effects(option):
    effects = option.get("effects", {}).get("selfParty", {})
    parts = []
    labels = {
        "coins": "Coins",
        "partyMorale": "Morale",
        "corruptionScore": "Corruption",
        "mediaImage": "Media",
        "publicSupport": "Support",
    }
    for key in ["coins", "partyMorale", "corruptionScore", "mediaImage", "publicSupport"]:
        value = effects.get(key, 0)
        if value:
            sign = "+" if value > 0 else ""
            parts.append(f"{labels[key]} {sign}{value}")
    delayed = option.get("delayedEffects", [])
    if delayed:
        parts.append(f"Delayed x{len(delayed)}")
    risk = option.get("risk", {})
    if risk and risk.get("chance"):
        parts.append(f"Risk {risk.get('chance')}%")
    return ", ".join(parts) if parts else "No visible effect"


def summarize_delayed_effect(effect):
    effects = effect.get("effects", {})
    labels = {
        "coins": "Coins",
        "partyMorale": "Morale",
        "corruptionScore": "Corruption",
        "mediaImage": "Media",
        "publicSupport": "Support",
    }
    parts = []
    for key in ["coins", "partyMorale", "corruptionScore", "mediaImage", "publicSupport"]:
        value = effects.get(key, 0)
        if value:
            sign = "+" if value > 0 else ""
            parts.append(f"{labels[key]} {sign}{value}")
    return ", ".join(parts) if parts else "No visible stat effect"


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
                
                with cols[col_idx]:
                    if st.button(label_text, key=f"{key_prefix}-{opt['key']}", use_container_width=True):
                        clicked_key = opt["key"]
    return clicked_key


def render_kbc_target_selection(turn_view):
    st.markdown("<div class='kbc-question-title'>Target Selection</div>", unsafe_allow_html=True)
    st.write("The selected card requires you to target an opponent party. Select one opponent party:")
    
    active_party_id = turn_view.get("activeHumanPartyId")
    opponents = [
        party for party in turn_view.get("parties", [])
        if party["id"] != active_party_id
    ]
    
    options = []
    for opponent in opponents:
        options.append({
            "key": opponent["id"],
            "text": f"{opponent.get('symbol', '')} {opponent['name']} ({opponent['role'].replace('_', ' ').title()})"
        })
        
    current_target = st.session_state.get("target_party_id")
    clicked_key = render_kbc_options(options, current_target, "target-select")
    if clicked_key:
        st.session_state["target_party_id"] = clicked_key
        has_rewards = bool(turn_view.get("activePlayerHeldRewards", []))
        if has_rewards:
            st.session_state["gameplay_step"] = "play_reward"
        else:
            st.session_state["gameplay_step"] = "news_reactions"
        st.success(f"Target selected!")
        st.rerun()


def render_kbc_news_reactions(turn_view):
    st.markdown("<div class='kbc-question-title'>News Reactions</div>", unsafe_allow_html=True)
    news_items = list(turn_view.get("currentNews", []))
    
    if not news_items:
        st.info("No news items configured for this turn.")
        st.session_state["gameplay_step"] = "monthly_issue"
        st.rerun()
        return

    selected_reactions = st.session_state.setdefault("selected_news_reactions", {})
    
    for idx, news in enumerate(news_items):
        st.write(f"### News Item {idx + 1}: {news['title']}")
        st.write(news.get("description", ""))
        
        options = []
        for reaction in news.get("reactionOptions", []):
            options.append({
                "key": reaction["reactionKey"],
                "text": reaction["text"]
            })
            
        current_selection = selected_reactions.get(news["newsKey"])
        clicked_key = render_kbc_options(options, current_selection, f"news-react-{news['newsKey']}")
        if clicked_key:
            selected_reactions[news["newsKey"]] = clicked_key
            news_ready = all(n.get("newsKey") in selected_reactions for n in news_items)
            if news_ready:
                st.session_state["gameplay_step"] = "monthly_issue"
            st.rerun()
            
    news_ready = all(news.get("newsKey") in selected_reactions for news in news_items)
    if news_ready:
        st.success("All news reactions selected!")
        if st.button("Proceed to Monthly Issue", key="proceed-from-news", use_container_width=True):
            st.session_state["gameplay_step"] = "monthly_issue"
            st.rerun()


def render_kbc_monthly_issue(turn_view):
    st.markdown("<div class='kbc-question-title'>Monthly Issue</div>", unsafe_allow_html=True)
    issue = turn_view.get("currentIssue")
    if not issue:
        st.info("No monthly issue available for this turn.")
        st.session_state["selected_issue_option_key"] = "none" # placeholder
        if st.button("Proceed to Review & Submit", key="proceed-from-issue-none", use_container_width=True):
            st.session_state["gameplay_step"] = "review_submit"
            st.rerun()
        return

    st.write(f"### {issue['title']}")
    st.write(issue.get("description", ""))
    st.caption(f"Category: {issue.get('category', 'issue').replace('_', ' ').title()}")

    options = []
    for option in issue.get("options", []):
        options.append({
            "key": option["optionKey"],
            "text": option["text"]
        })
        
    current_selection = st.session_state.get("selected_issue_option_key")
    clicked_key = render_kbc_options(options, current_selection, f"issue-select-{issue['issueKey']}")
    if clicked_key:
        st.session_state["selected_issue_option_key"] = clicked_key
        st.session_state["gameplay_step"] = "review_submit"
        st.rerun()


def render_kbc_reward_selection(turn_view):
    st.markdown("<div class='kbc-question-title'>Play a Reward (Optional)</div>", unsafe_allow_html=True)
    
    held = turn_view.get("activePlayerHeldRewards", [])
    if not held:
        st.info("You don't have any rewards in your inventory right now. Click below to proceed.")
        if st.button("Proceed to News Reactions", use_container_width=True):
            st.session_state["gameplay_step"] = "news_reactions"
            st.rerun()
        return

    # Render held rewards as cards in a 3-column layout
    st.write("### Your Held Rewards")
    selected_reward_key = st.session_state.get("selected_reward_key")
    
    for row_start in range(0, len(held), 3):
        row_cols = st.columns(3)
        for col, r in zip(row_cols, held[row_start:row_start + 3]):
            with col:
                is_selected = (selected_reward_key == r["rewardKey"])
                border_css = "border: 2px solid #fbbf24; box-shadow: 0 0 15px rgba(251, 191, 36, 0.6);" if is_selected else "border: 2px solid #8b5cf6;"
                badge_html = "<span style='font-size: 11px; background-color: #fbbf24; color: #000000; font-weight: 900; padding: 2px 6px; border-radius: 4px; text-transform: uppercase;'>🔥 Selected</span>" if is_selected else f"<span style='font-size: 11px; background-color: #475569; color: #e2e8f0; font-weight: 900; padding: 2px 6px; border-radius: 4px; text-transform: uppercase;'>⏳ {r['turnsLeft']} turns</span>"
                
                st.markdown(
                    f"""<div style="background: linear-gradient(135deg, #1e1b4b 0%, #0d0b21 100%); {border_css} border-radius: 14px; padding: 16px; min-height: 160px; font-family: 'Montserrat', sans-serif; margin-bottom: 12px;">
<div style="display: flex; justify-content: space-between; align-items: flex-start;">
<span style="font-size: 11px; text-transform: uppercase; color: #a78bfa; font-weight: 700; letter-spacing: 0.05em;">🎁 REWARD</span>
{badge_html}
</div>
<div style="font-size: 16px; font-weight: 800; color: #ffffff; margin-top: 6px;">{r['name']}</div>
<div style="font-size: 12px; color: #e2e8f0; margin-top: 6px; opacity: 0.95; line-height: 1.4;">{r['description']}</div>
</div>""",
                    unsafe_allow_html=True
                )
                
                if is_selected:
                    if st.button("Deselect Reward", key=f"deselect-reward-{r['rewardKey']}", use_container_width=True):
                        st.session_state["selected_reward_key"] = None
                        st.session_state["reward_target_party_id"] = None
                        st.rerun()
                else:
                    if st.button("Select Reward", key=f"select-reward-{r['rewardKey']}", use_container_width=True):
                        st.session_state["selected_reward_key"] = r["rewardKey"]
                        st.session_state["reward_target_party_id"] = None
                        st.rerun()

    # Target selection if required
    selected_reward = next((r for r in held if r["rewardKey"] == selected_reward_key), None) if selected_reward_key else None
    
    if selected_reward and selected_reward.get("requiresTarget"):
        st.write("")
        st.write("### Target Selection")
        parties = turn_view.get("parties", [])
        active_party_id = turn_view.get("activeHumanPartyId")
        allowed = selected_reward.get("allowedTargets", "any")
        
        valid_targets = []
        for p in parties:
            if allowed == "self" and p["id"] == active_party_id:
                valid_targets.append(p)
            elif allowed == "opponent" and p["id"] != active_party_id:
                valid_targets.append(p)
            elif allowed == "any":
                valid_targets.append(p)
                
        target_options = {p["name"]: p["id"] for p in valid_targets}
        selected_target_name = st.selectbox("Select Target Party for Reward", list(target_options.keys()), key="reward-target-select")
        st.session_state["reward_target_party_id"] = target_options[selected_target_name]
    else:
        st.session_state["reward_target_party_id"] = None

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back", use_container_width=True):
            if card_requires_target(st.session_state.get("selected_card")):
                st.session_state["gameplay_step"] = "select_target"
            else:
                st.session_state["gameplay_step"] = "select_card"
            st.rerun()
    with col2:
        proceed_label = "Proceed with Selected Reward" if selected_reward_key else "Skip & Proceed"
        if st.button(proceed_label, use_container_width=True):
            st.session_state["gameplay_step"] = "news_reactions"
            st.rerun()


def render_kbc_review(turn_view):
    st.markdown("<div class='kbc-question-title'>Review Your Decisions</div>", unsafe_allow_html=True)
    st.write("Please review your finalized selections. Click any step to edit.")
    
    # Display selected card
    card = st.session_state.get("selected_card")
    st.write(f"**1. Chosen Card:** `{card['name']}` (Cost: {card['cost']} coins)")
    
    # Display target if required
    if card_requires_target(card):
        target_party_id = st.session_state.get("target_party_id")
        target_party = next((p for p in turn_view.get("parties", []) if p["id"] == target_party_id), None)
        target_name = target_party["name"] if target_party else "None Selected"
        st.write(f"**2. Target Party:** `{target_name}`")
        
    # Display played reward if selected
    selected_reward_key = st.session_state.get("selected_reward_key")
    if selected_reward_key:
        held = turn_view.get("activePlayerHeldRewards", [])
        reward_obj = next((r for r in held if r["rewardKey"] == selected_reward_key), None)
        if reward_obj:
            reward_target_party_id = st.session_state.get("reward_target_party_id")
            if reward_obj["requiresTarget"] and reward_target_party_id:
                t_party = next((p for p in turn_view.get("parties", []) if p["id"] == reward_target_party_id), None)
                t_name = t_party["name"] if t_party else "None Selected"
                st.write(f"**3. Played Reward:** `{reward_obj['name']}` targeting `{t_name}`")
            else:
                st.write(f"**3. Played Reward:** `{reward_obj['name']}`")
    else:
        st.write("**3. Played Reward:** `None selected (Skip)`")
        
    # Display news reactions
    st.write("**4. News Reactions Chosen:**")
    news_items = turn_view.get("currentNews", [])
    selected_news = st.session_state.get("selected_news_reactions", {})
    for news in news_items:
        reaction_key = selected_news.get(news["newsKey"])
        reaction_text = "None Selected"
        for reaction in news.get("reactionOptions", []):
            if reaction["reactionKey"] == reaction_key:
                reaction_text = reaction["text"]
                break
        st.write(f"- *{news['title']}*: `{reaction_text}`")
        
    # Display monthly issue
    issue = turn_view.get("currentIssue")
    if issue:
        option_key = st.session_state.get("selected_issue_option_key")
        option_text = "None Selected"
        for option in issue.get("options", []):
            if option["optionKey"] == option_key:
                option_text = option["text"]
                break
        st.write(f"**5. Monthly Issue Response:** `{option_text}`")
    else:
        st.write("**5. Monthly Issue Response:** `No issue to handle this month`")

    st.divider()
    st.markdown("### 🗳️ Place Your Bid for the Cycle Reward")
    bid_metric = turn_view.get("biddingMetric", "COINS")
    
    parties = turn_view.get("parties", [])
    active_party_id = turn_view.get("activeHumanPartyId")
    active_party = next((p for p in parties if p["id"] == active_party_id), None)
    
    if active_party:
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
        
        st.write(f"The bidding metric for this turn is **{bid_metric.replace('_', ' ').upper()}**. Your current value: **{max_bid}**.")
        if max_bid > 0:
            bid_val = st.slider("Select Bid Amount", min_value=0, max_value=max_bid, value=st.session_state.get("bid_amount", 0))
            st.session_state["bid_amount"] = bid_val
        else:
            st.write("Your value for this metric is 0. You cannot place a bid this turn.")
            st.session_state["bid_amount"] = 0
    else:
        st.session_state["bid_amount"] = 0


@st.dialog("Campaign Successful! 🏆")
def show_victory_dialog(state_name, last_results):
    st.balloons()
    st.markdown(
        f"""
        <div style="text-align: center; font-family: 'Montserrat', sans-serif;">
            <div style="font-size: 60px; margin-bottom: 10px;">👑</div>
            <h2 style="color: #fbbf24; font-weight: 800; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.05em;">Congratulations!</h2>
            <p style="font-size: 15px; color: #e2e8f0; line-height: 1.6; margin-bottom: 20px;">
                The <b>No-Confidence Motion</b> successfully passed! You have overthrown the incumbent government 
                and officially formed the new government in <b>{state_name}</b>.
            </p>
            <div style="background: rgba(34, 197, 94, 0.1); border: 1px solid #22c55e; border-radius: 8px; padding: 12px; margin-bottom: 20px; text-align: left;">
                <span style="font-size: 11px; font-weight: 700; color: #22c55e; display: block; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 3px;">Verdict</span>
                <span style="font-size: 13px; color: #ffffff;">{" ".join(last_results) if last_results else "You won the election campaign!"}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Return to Start Screen", key="victory_dialog_btn", type="primary", use_container_width=True):
        st.session_state["game_id"] = None
        st.session_state.pop("victory_dialog_shown", None)
        st.session_state.pop("defeat_dialog_shown", None)
        st.rerun()

@st.dialog("Campaign Defeated ❌")
def show_defeat_dialog(state_name, last_results):
    st.markdown(
        f"""
        <div style="text-align: center; font-family: 'Montserrat', sans-serif;">
            <div style="font-size: 60px; margin-bottom: 10px;">❌</div>
            <h2 style="color: #ef4444; font-weight: 800; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.05em;">Campaign Failed</h2>
            <p style="font-size: 15px; color: #e2e8f0; line-height: 1.6; margin-bottom: 20px;">
                You were unable to secure enough voter support to form the government in <b>{state_name}</b>.
            </p>
            <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; border-radius: 8px; padding: 12px; margin-bottom: 20px; text-align: left;">
                <span style="font-size: 11px; font-weight: 700; color: #ef4444; display: block; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 3px;">Verdict</span>
                <span style="font-size: 13px; color: #ffffff;">{" ".join(last_results) if last_results else "The opposition failed to form the government."}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Return to Start Screen", key="defeat_dialog_btn", type="primary", use_container_width=True):
        st.session_state["game_id"] = None
        st.session_state.pop("victory_dialog_shown", None)
        st.session_state.pop("defeat_dialog_shown", None)
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
        f"""<div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 16px 20px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.15); font-family: 'Montserrat', sans-serif;">
<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
<!-- Left Section: State and Date -->
<div>
<span style="font-size: 10px; color: #94a3b8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; display: block;">Location & Date</span>
<div style="font-size: 16px; font-weight: 800; color: #ffffff; display: flex; align-items: center; gap: 6px; margin-top: 2px;">
<span>📍</span> {state_name} <span style="color: #475569; font-weight: 400;">|</span> 📅 {formatted_date}
</div>
</div>
<!-- Middle Section: Election Countdown -->
<div>
<span style="font-size: 10px; color: #94a3b8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; display: block;">Election Countdown</span>
<div style="font-size: 15px; font-weight: 800; color: #e2e8f0; display: flex; align-items: center; gap: 6px; margin-top: 2px;">
<span>🗳️</span> {election_in} months left <span style="background-color: #22c55e; color: #ffffff; font-size: 9px; font-weight: 900; padding: 2px 6px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.05em; margin-left: 8px;">{status_label}</span>
</div>
</div>
<!-- Right Section: Progress Tracker -->
<div style="min-width: 220px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
<span style="font-size: 10px; color: #94a3b8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em;">60-Month Cycle Progress</span>
<span style="font-size: 11px; font-weight: 800; color: #ffffff;">Month {turn_number}/60</span>
</div>
<!-- Progress Bar: Red (done) and Green (left) -->
<div style="width: 100%; height: 8px; background-color: #22c55e; border-radius: 4px; overflow: hidden; display: flex; box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);">
<div style="width: {progress_pct}%; height: 100%; background-color: #ef4444; border-radius: 4px 0 0 4px;"></div>
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
        # Fallback for legacy GAME_OVER games
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
            
        # Display the Standings
        st.subheader("Final Party Standings")
        party_columns = st.columns(3)
        for index, party in enumerate(turn_view.get("parties", [])):
            with party_columns[index % 3]:
                render_party_panel(
                    party["role"].replace("_", " ").title(),
                    party,
                    turn_view.get("lastMetricDeltas", {}).get(party["id"], {}),
                )
                
        # Display final results and commentary logs
        st.write("")
        with st.expander("Final Logs & Verdict", expanded=True):
            st.write("**Final Election/Motion Results:**")
            for result in turn_view.get("lastResults", []):
                st.write(f"- {result}")
            st.write("**Campaign Commentary Log:**")
            for line in turn_view.get("lastRoundCommentary", []):
                st.write(f"- {line}")
                
        # Large return button
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
    
    top_col1, top_col2, top_col3 = st.columns([1.2, 1.2, 1.0], gap="medium")
    with top_col1:
        render_party_banner(active_party)
        
    with top_col2:
        if st.session_state.get("selected_card"):
            card = st.session_state["selected_card"]
            render_selected_card_panel(card)
            if card_requires_target(card):
                target_party_id = st.session_state.get("target_party_id")
                if target_party_id:
                    target_party = next((p for p in turn_view.get("parties", []) if p["id"] == target_party_id), None)
                    target_name = target_party["name"] if target_party else "Unknown"
                    st.success(f"Target Party: {target_name}")
                else:
                    st.warning("Target Party: Not Selected")
            if st.button("Cancel Selection", use_container_width=True):
                st.session_state.pop("selected_card", None)
                st.session_state["target_party_id"] = None
                st.session_state["gameplay_step"] = "select_card"
                st.rerun()
        else:
            st.info("💡 Select a card from the deck below to draft your campaign move.")

    with top_col3:
        render_sidebar_inventory(turn_view)


    st.markdown('<div id="stats-focus"></div>', unsafe_allow_html=True)
    st.markdown('<div class="standing-columns-marker"></div>', unsafe_allow_html=True)
    st.subheader("Current Party Standings")
    party_columns = st.columns(3)
    for index, party in enumerate(turn_view.get("parties", [])):
        with party_columns[index % 3]:
            render_party_panel(
                party["role"].replace("_", " ").title(),
                party,
                turn_view.get("lastMetricDeltas", {}).get(party["id"], {}),
            )

    # Active Bidding & Reward Cycle Banner (Moved below standings)
    bid_metric = turn_view.get("biddingMetric", "COINS")
    cycle_turn = ((turn_view["turnNumber"] - 1) % 5) + 1
    
    # Reward is not known from start (Blind bidding)
    reward_display_name = "❓ Mystery Reward"
    reward_display_desc = "Revealed and awarded at the end of Turn 5 of this cycle. Bidding is blind!"
    
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 18px; border-radius: 12px; border: 1px solid #fbbf24; margin-top: 25px; margin-bottom: 25px; box-shadow: 0 10px 25px rgba(0,0,0,0.3);">
            <div style="font-size: 11px; text-transform: uppercase; color: #fbbf24; font-weight: 700; letter-spacing: 0.1em; display: flex; align-items: center; gap: 6px;">
                <span>🏆</span> 5-Turn Reward Cycle (Round {cycle_turn}/5)
            </div>
            <div style="font-size: 18px; font-weight: 800; color: #ffffff; margin-top: 6px;">Active Cycle Reward: {reward_display_name}</div>
            <div style="font-size: 13px; color: #e2e8f0; opacity: 0.95; margin-top: 4px;">{reward_display_desc}</div>
            <div style="display: flex; gap: 30px; margin-top: 15px; border-top: 1px dashed rgba(251, 191, 36, 0.3); padding-top: 12px; flex-wrap: wrap;">
                <div>
                    <span style="font-size: 10px; color: #94a3b8; display: block; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em;">This Round's Bidding Metric</span>
                    <span style="font-size: 15px; font-weight: 800; color: #fbbf24; text-shadow: 0 0 8px rgba(251, 191, 36, 0.4);">⚡ {bid_metric.replace('_', ' ').upper()}</span>
                </div>
                <div>
                    <span style="font-size: 10px; color: #94a3b8; display: block; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em;">Current Cycle Wins</span>
                    <span style="font-size: 14px; font-weight: 800; color: #ffffff;">📊 {', '.join([f"{p['name']}: {turn_view.get('partyRoundWins', {}).get(p['id'], 0)}" for p in turn_view.get('parties', [])])}</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    last_submissions = turn_view.get("lastRoundSubmissions", [])
    if last_submissions:
        st.write("")
        st.subheader("Last Turn Details")
        
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
        dec_columns = st.columns(3)
        for index, party in enumerate(turn_view.get("parties", [])):
            with dec_columns[index % 3]:
                render_last_decisions_panel(
                    party,
                    last_by_party.get(party["id"]),
                    turn_view.get("lastRoundBiddingMetric"),
                    turn_view.get("lastRoundWinnerPartyId")
                )

    st.divider()
    
    # Combined Log expander containing party tabs, collapsing by default
    with st.expander("Logs & Round Summary", expanded=False):
        parties = turn_view.get("parties", [])
        active_party_id = turn_view.get("activeHumanPartyId")
        active_party = next((p for p in parties if p["id"] == active_party_id), None)
        
        # Build tabs list: player party first, other parties next, All Parties last
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

    st.divider()
    
    # Initialize gameplay step in session state if not set
    if "gameplay_step" not in st.session_state:
        st.session_state["gameplay_step"] = "select_card"
        
    card_ready = bool(st.session_state.get("selected_card"))
    target_required = card_requires_target(st.session_state["selected_card"]) if card_ready else False
    target_ready = not target_required or bool(st.session_state.get("target_party_id"))
    
    news_items = turn_view.get("currentNews", [])
    selected_news = st.session_state.get("selected_news_reactions", {})
    news_ready = all(news.get("newsKey") in selected_news for news in news_items)
    
    issue_ready = bool(st.session_state.get("selected_issue_option_key"))
    
    # Render Step Navigation Stepper
    st.subheader("Gameplay Action Panel")
    
    has_rewards = bool(turn_view.get("activePlayerHeldRewards", []))

    # Dynamically build steps list
    steps = [
        {"key": "select_card", "label": "1. Choose Card"},
    ]
    current_idx = 2
    if target_required:
        steps.append({"key": "select_target", "label": f"{current_idx}. Target Party"})
        current_idx += 1
        
    if has_rewards:
        steps.append({"key": "play_reward", "label": f"{current_idx}. Play Reward (Opt)"})
        current_idx += 1
        
    steps.extend([
        {"key": "news_reactions", "label": f"{current_idx}. News Reactions"},
        {"key": "monthly_issue", "label": f"{current_idx + 1}. Monthly Issue"},
        {"key": "review_submit", "label": f"{current_idx + 2}. Review & Lock"},
    ])
    
    # Draw Stepper buttons
    step_cols = st.columns(len(steps))
    for idx, step in enumerate(steps):
        is_active = (st.session_state["gameplay_step"] == step["key"])
        
        # Calculate disabled status
        is_disabled = True
        if step["key"] == "select_card":
            is_disabled = False
        elif step["key"] == "select_target":
            is_disabled = not card_ready
        elif step["key"] == "play_reward":
            is_disabled = not (card_ready and target_ready)
        elif step["key"] == "news_reactions":
            is_disabled = not (card_ready and target_ready)
        elif step["key"] == "monthly_issue":
            is_disabled = not (card_ready and target_ready and news_ready)
        elif step["key"] == "review_submit":
            is_disabled = not (card_ready and target_ready and news_ready and issue_ready)
            
        label = step["label"]
        if is_active:
            label = f"✨ {label} ✨"
            
        with step_cols[idx]:
            if st.button(label, key=f"step-nav-{step['key']}", disabled=is_disabled, use_container_width=True):
                st.session_state["gameplay_step"] = step["key"]
                st.rerun()
                
    st.write("") # Spacer
    
    # Render active step
    active_step = st.session_state["gameplay_step"]
    
    # Fallback to prevent stuck state
    if active_step == "select_target" and not target_required:
        if has_rewards:
            st.session_state["gameplay_step"] = "play_reward"
        else:
            st.session_state["gameplay_step"] = "news_reactions"
        st.rerun()
        
    if active_step == "play_reward" and not has_rewards:
        st.session_state["gameplay_step"] = "news_reactions"
        st.rerun()
        
    st.markdown("<div class='kbc-card-container'>", unsafe_allow_html=True)
    
    if active_step == "select_card":
        st.markdown("<div class='kbc-question-title'>Select Card</div>", unsafe_allow_html=True)
        render_card_deck(turn_view.get("availableCards", []), turn_view)
        if card_ready:
            st.divider()
            if st.button("Proceed to Next Step", key="proceed-from-card-deck", use_container_width=True):
                if target_required:
                    st.session_state["gameplay_step"] = "select_target"
                elif has_rewards:
                    st.session_state["gameplay_step"] = "play_reward"
                else:
                    st.session_state["gameplay_step"] = "news_reactions"
                st.rerun()
                
    elif active_step == "select_target":
        render_kbc_target_selection(turn_view)
        
    elif active_step == "play_reward":
        render_kbc_reward_selection(turn_view)
        
    elif active_step == "news_reactions":
        render_kbc_news_reactions(turn_view)
        
    elif active_step == "monthly_issue":
        render_kbc_monthly_issue(turn_view)
        
    elif active_step == "review_submit":
        render_kbc_review(turn_view)
        
        # Render advance turn button
        st.divider()
        if st.button("Lock Decisions & Advance Turn", disabled=not (card_ready and target_ready and news_ready and issue_ready), type="primary", use_container_width=True):
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
                st.session_state["gameplay_step"] = "select_card"
                st.session_state["scroll_to_stats"] = True
                st.success("Turn advanced successfully!")
                st.rerun()
            except requests.RequestException as exc:
                st.error(f"Could not advance turn: {exc}")
                
    st.markdown("</div>", unsafe_allow_html=True)

