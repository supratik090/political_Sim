import streamlit as st
from constants import (
    CATEGORY_COLORS,
    POST_IT_COLORS,
    CATEGORY_LABELS,
    SYMBOL_ART,
)


def stat_bar(label, value, max_value=100, suffix=""):
    value = int(value)
    pct = min(max(value / max_value, 0), 1)
    st.progress(pct, text=f"{label}: {value}{suffix}")


def metric_with_delta(label, value, delta=None, inverse=False, suffix=""):
    delta_text = None
    if delta is not None:
        sign = "+" if delta > 0 else ""
        delta_text = f"{sign}{delta}{suffix}"
    st.metric(label, f"{value}{suffix}", delta_text, delta_color="inverse" if inverse else "normal")


def inject_game_css():
    category_css = ""
    for cat, p_color in POST_IT_COLORS.items():
        border_color = CATEGORY_COLORS.get(cat, "#555555")
        category_css += f"""
        div[data-testid="column"]:has(.card-marker-{cat}) [data-testid="stExpander"],
        div:has(.card-marker-{cat}) ~ [data-testid="stExpander"] {{
          background-color: {p_color} !important;
          border: 1px solid rgba(0, 0, 0, 0.12) !important;
          border-left: 5px solid {border_color} !important;
          border-radius: 8px !important;
          margin-bottom: 12px !important;
        }}
        div[data-testid="column"]:has(.card-marker-{cat}) [data-testid="stExpander"] summary,
        div[data-testid="column"]:has(.card-marker-{cat}) [data-testid="stExpander"] summary > div,
        div[data-testid="column"]:has(.card-marker-{cat}) [data-testid="stExpander"] summary div,
        div:has(.card-marker-{cat}) ~ [data-testid="stExpander"] summary,
        div:has(.card-marker-{cat}) ~ [data-testid="stExpander"] summary > div,
        div:has(.card-marker-{cat}) ~ [data-testid="stExpander"] summary div {{
          background-color: transparent !important;
          color: #212529 !important;
          font-weight: 800 !important;
        }}
        div[data-testid="column"]:has(.card-marker-{cat}) [data-testid="stExpander"] summary:hover,
        div[data-testid="column"]:has(.card-marker-{cat}) [data-testid="stExpander"] summary div:hover,
        div:has(.card-marker-{cat}) ~ [data-testid="stExpander"] summary:hover,
        div:has(.card-marker-{cat}) ~ [data-testid="stExpander"] summary div:hover {{
          color: #111111 !important;
          background-color: transparent !important;
        }}
        div[data-testid="column"]:has(.card-marker-{cat}) [data-testid="stExpander"] summary svg,
        div:has(.card-marker-{cat}) ~ [data-testid="stExpander"] summary svg {{
          fill: #212529 !important;
        }}
        div[data-testid="column"]:has(.card-marker-{cat}) [data-testid="stExpander"] div[role="region"],
        div[data-testid="column"]:has(.card-marker-{cat}) [data-testid="stExpander"] div[role="region"] > div,
        div[data-testid="column"]:has(.card-marker-{cat}) [data-testid="stExpander"] div[role="region"] div,
        div:has(.card-marker-{cat}) ~ [data-testid="stExpander"] div[role="region"],
        div:has(.card-marker-{cat}) ~ [data-testid="stExpander"] div[role="region"] > div,
        div:has(.card-marker-{cat}) ~ [data-testid="stExpander"] div[role="region"] div {{
          background-color: transparent !important;
          color: #212529 !important;
          border-top: 1px dashed rgba(0, 0, 0, 0.12) !important;
        }}
        """

    base_css = """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap');

        .stApp {
          font-family: 'Montserrat', sans-serif !important;
        }
        
        /* Custom styled metric values */
        [data-testid="stMetricValue"] {
          font-size: 20px !important;
          font-weight: 800 !important;
        }
        [data-testid="stMetricLabel"] {
          font-size: 11px !important;
          font-weight: 700 !important;
          text-transform: uppercase !important;
          letter-spacing: 0.05em !important;
        }
        [data-testid="stMetricDelta"] {
          font-weight: 700 !important;
          font-size: 13px !important;
        }
        
        /* Softer Green & Orange Option Buttons */
        div.stButton > button {
          background: linear-gradient(135deg, #1b2e24 0%, #0d1611 100%) !important;
          color: #81c784 !important;
          border: 2px solid #4caf50 !important;
          border-radius: 25px !important;
          font-weight: 700 !important;
          font-size: 14px !important;
          letter-spacing: 0.05em !important;
          padding: 10px 20px !important;
          box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
          transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
          width: 100% !important;
        }
        div.stButton > button:hover {
          background: #4caf50 !important;
          color: #ffffff !important;
          border-color: #ffffff !important;
          box-shadow: 0 0 15px rgba(76, 175, 80, 0.7) !important;
          transform: translateY(-2px) !important;
        }
        div.stButton > button:active {
          transform: translateY(1px) !important;
        }
        div.stButton > button:disabled {
          border-color: #223326 !important;
          color: #55665a !important;
          background: #0d120e !important;
          box-shadow: none !important;
        }
        
        .kbc-card-container {
          background: radial-gradient(circle at center, #15271d 0%, #0b140f 100%);
          border: 2px solid #4caf50;
          border-radius: 18px;
          padding: 24px;
          margin-top: 15px;
          margin-bottom: 25px;
          box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .kbc-question-title {
          color: #ffffff;
          font-size: 20px;
          font-weight: 800;
          text-align: center;
          margin-bottom: 20px;
          text-transform: uppercase;
          letter-spacing: 0.1em;
          border-bottom: 2px solid #ef6c00;
          padding-bottom: 12px;
        }
        
        .party-flag {
          border-radius: 18px;
          padding: 14px 16px;
          color: white;
          min-height: 108px;
          box-shadow: 0 12px 28px rgba(0,0,0,.14);
        }
        .party-symbol {
          font-size: 26px;
          font-weight: 800;
          letter-spacing: .08em;
          text-transform: uppercase;
        }
        .symbol-medallion {
          width: 54px;
          height: 54px;
          border-radius: 18px;
          display: inline-flex;
          align-items: center;
          justify-content: center;
          margin-right: 10px;
          font-size: 12px;
          font-weight: 900;
          letter-spacing: .08em;
          color: #fff7df;
          background:
            radial-gradient(circle at 35% 25%, rgba(255,255,255,.35), transparent 24px),
            linear-gradient(135deg, rgba(255,255,255,.18), rgba(0,0,0,.28));
          border: 1px solid rgba(255,255,255,.35);
          box-shadow: inset 0 0 16px rgba(255,255,255,.14), 0 10px 20px rgba(0,0,0,.18);
        }
        .mini-move-card {
          border-radius: 14px;
          padding: 10px;
          margin-top: 10px;
          color: white;
          box-shadow: 0 8px 18px rgba(80, 62, 35, .10);
        }
        .mini-move-title {
          font-weight: 800;
          font-size: 13px;
        }
        .mini-move-meta {
          font-size: 11px;
          opacity: .8;
          margin-top: 3px;
        }
        .deck-card {
          border: 1px solid rgba(49, 43, 33, .18);
          border-radius: 16px;
          padding: 12px;
          color: white;
          min-height: 178px;
          box-shadow: 0 8px 18px rgba(80, 62, 35, .10);
        }
        .deck-card-title {
          font-weight: 800;
          font-size: 15px;
        }
        .deck-meta {
          font-size: 12px;
          opacity: .78;
          margin-top: 4px;
        }
        .effect-line {
          font-size: 12px;
          margin-top: 8px;
          background: rgba(255,255,255,.14);
          padding: 7px;
          border-radius: 10px;
        }
        
        @media (max-width: 768px) {
          [data-testid="stHorizontalBlock"] {
            flex-direction: column !important;
            gap: 12px !important;
          }
          [data-testid="column"] {
            width: 100% !important;
            min-width: 100% !important;
          }
          .kbc-card-container {
            padding: 14px !important;
          }
        }
    """
    st.markdown(base_css + category_css + "\n</style>", unsafe_allow_html=True)


def render_party_panel(title, party, deltas=None):
    stats = party["stats"]
    deltas = deltas or {}
    badge = "Player" if party["playerControlled"] else "AI"
    color = party.get("color") or "#555555"
    
    with st.container(border=True):
        st.markdown(
            f"<div style='font-size: 16px; font-weight: 800; margin-bottom: 8px;'>"
            f"<span style='color: {color};'>●</span> {party['name']} "
            f"<span style='font-size: 11px; opacity: 0.6;'>({badge} - {title})</span>"
            f"</div>",
            unsafe_allow_html=True
        )
        
        col1, col2 = st.columns(2)
        with col1:
            metric_with_delta("Coins", stats["coins"], deltas.get("coins"))
            metric_with_delta("Corruption", stats["corruptionScore"], deltas.get("corruptionScore"), inverse=True)
        with col2:
            metric_with_delta("Morale", stats["partyMorale"], deltas.get("partyMorale"))
            metric_with_delta("Media", stats["mediaImage"], deltas.get("mediaImage"))
            
        metric_with_delta("Public Support", stats["publicSupport"], deltas.get("publicSupport"), suffix="%")
        st.progress(stats["publicSupport"] / 100.0)


def render_last_decisions_panel(party, submission, bidding_metric=None, last_round_winner_id=None):
    color = party.get("color") or "#555555"
    badge = "Player" if party["playerControlled"] else "AI"
    
    def truncate_text(text, max_len=35):
        if len(text) > max_len:
            return text[:max_len] + "..."
        return text
    
    with st.container(border=True):
        st.markdown(
            f"<div style='font-size: 15px; font-weight: 800; margin-bottom: 8px;'>"
            f"<span style='color: {color};'>●</span> {party['name']} "
            f"<span style='font-size: 11px; opacity: 0.6;'>({badge})</span>"
            f"</div>",
            unsafe_allow_html=True
        )
        
        if not submission:
            st.caption("No decisions recorded for last turn.")
            return
            
        # Played Card
        card_key = submission.get("cardKey")
        card_def = st.session_state.get("card_definitions", {}).get(card_key)
        category = card_def.get("category", "other") if card_def else "other"
        color = CATEGORY_COLORS.get(category, "#555555")
        
        target = submission.get("targetPartyName")
        target_line = f"Target: {target}" if target else "Self / Public Move"
        st.markdown(
            f"""
            <div style="border-left: 4px solid {color}; padding-left: 10px; margin-bottom: 10px; background: rgba(0,0,0,0.02); border-radius: 4px; padding: 6px 10px;">
                <div style="font-size: 10px; text-transform: uppercase; color: {color}; font-weight: 700; letter-spacing: 0.05em;">Card Played</div>
                <div style="font-size: 13px; font-weight: 700; margin-top: 1px;">🃏 {submission.get('cardName', 'No card')}</div>
                <div style="font-size: 11px; opacity: 0.7; margin-top: 1px;">{target_line}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Played Reward (if any)
        reward_key = submission.get("selectedRewardKey")
        if reward_key:
            reward_name = submission.get("rewardName") or reward_key
            r_target = submission.get("rewardTargetPartyName")
            r_target_line = f"Target: {r_target}" if r_target else "Self"
            st.markdown(
                f"""
                <div style="border-left: 4px solid #9c27b0; padding-left: 10px; margin-bottom: 10px; background: rgba(0,0,0,0.02); border-radius: 4px; padding: 6px 10px;">
                    <div style="font-size: 10px; text-transform: uppercase; color: #9c27b0; font-weight: 700; letter-spacing: 0.05em;">Reward Played</div>
                    <div style="font-size: 13px; font-weight: 700; margin-top: 1px;">🎁 {reward_name}</div>
                    <div style="font-size: 11px; opacity: 0.7; margin-top: 1px;">{r_target_line}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Bidding info
        bid_val = submission.get("bid", 0)
        metric_name = bidding_metric if bidding_metric else "Metric"
        is_winner = (last_round_winner_id is not None and party["id"] == last_round_winner_id)
        crown = " 👑" if is_winner else ""
        st.markdown(
            f"""
            <div style="border-left: 4px solid #00bcd4; padding-left: 10px; margin-bottom: 10px; background: rgba(0,0,0,0.02); border-radius: 4px; padding: 6px 10px;">
                <div style="font-size: 10px; text-transform: uppercase; color: #00bcd4; font-weight: 700; letter-spacing: 0.05em;">Bidding</div>
                <div style="font-size: 13px; font-weight: 700; margin-top: 1px;">🗳️ Bid: {bid_val} ({metric_name}){crown}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        # News Reactions
        news_reactions = submission.get("newsReactions", {})
        if news_reactions:
            st.markdown(
                """
                <div style="font-size: 10px; text-transform: uppercase; opacity: 0.6; font-weight: 700; letter-spacing: 0.05em; margin-bottom: 4px; margin-top: 10px;">News Reactions</div>
                """,
                unsafe_allow_html=True
            )
            for news_key, reaction_key in news_reactions.items():
                news_def = st.session_state.get("news_definitions", {}).get(news_key)
                if news_def:
                    news_title = news_def.get("title", news_key)
                    reaction_opt = next((opt for opt in news_def.get("reactionOptions", []) if opt.get("reactionKey") == reaction_key), None)
                    reaction_text = reaction_opt.get("text", reaction_key) if reaction_opt else reaction_key
                else:
                    news_title = news_key
                    reaction_text = reaction_key
                    
                news_title_short = truncate_text(news_title, 35)
                reaction_text_short = truncate_text(reaction_text, 35)
                
                if len(news_title) > 35 or len(reaction_text) > 35:
                    st.markdown(
                        f"""<details style="border-left: 3px solid #ff9800; padding-left: 8px; margin-bottom: 8px; background: rgba(0,0,0,0.01); border-radius: 3px; padding: 4px 8px; cursor: pointer; font-family: 'Montserrat', sans-serif;">
<summary style="font-size: 11px; font-weight: 700; color: #212529; outline: none; list-style: none;">
📰 {news_title_short} <span style="font-size: 9px; color: #888; font-weight: normal; margin-left: 4px;">(click to view)</span>
<div style="font-size: 11px; opacity: 0.8; margin-top: 2px; font-weight: 500;">↳ {reaction_text_short}</div>
</summary>
<div style="font-size: 11px; opacity: 0.95; margin-top: 6px; padding-top: 6px; border-top: 1px dashed rgba(0,0,0,0.05); color: #111;">
<strong>News:</strong> {news_title}<br/>
<strong>Reaction:</strong> {reaction_text}
</div>
</details>""",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"""<div style="border-left: 3px solid #ff9800; padding-left: 8px; margin-bottom: 8px; background: rgba(0,0,0,0.01); border-radius: 3px; padding: 4px 8px; font-family: 'Montserrat', sans-serif;">
<div style="font-size: 11px; font-weight: 700;">📰 {news_title}</div>
<div style="font-size: 11px; opacity: 0.8; margin-top: 2px;">↳ {reaction_text}</div>
</div>""",
                        unsafe_allow_html=True
                    )
                
        # Monthly Issue Response
        if submission.get("issueTitle"):
            issue_title = submission.get("issueTitle")
            option_text = submission.get("issueOptionText", "Response chosen")
            issue_title_short = truncate_text(issue_title, 35)
            option_text_short = truncate_text(option_text, 35)
            
            if len(issue_title) > 35 or len(option_text) > 35:
                st.markdown(
                    f"""<details style="border-left: 4px solid #4caf50; padding-left: 10px; margin-top: 10px; background: rgba(0,0,0,0.02); border-radius: 4px; padding: 6px 10px; cursor: pointer; font-family: 'Montserrat', sans-serif;">
<summary style="font-size: 10px; text-transform: uppercase; opacity: 0.6; font-weight: 700; letter-spacing: 0.05em; color: #4caf50; outline: none; list-style: none;">
📋 Monthly Issue <span style="font-size: 9px; color: #888; font-weight: normal; margin-left: 4px; text-transform: none; letter-spacing: normal;">(click to view)</span>
<div style="font-size: 12px; font-weight: 700; margin-top: 1px; color: #212529;">{issue_title_short}</div>
<div style="font-size: 11px; opacity: 0.8; margin-top: 2px; font-weight: 500; color: #212529;">↳ {option_text_short}</div>
</summary>
<div style="font-size: 11px; opacity: 0.95; margin-top: 6px; padding-top: 6px; border-top: 1px dashed rgba(0,0,0,0.05); color: #111;">
<strong>Issue:</strong> {issue_title}<br/>
<strong>Response:</strong> {option_text}
</div>
</details>""",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""<div style="border-left: 4px solid #4caf50; padding-left: 10px; margin-top: 10px; background: rgba(0,0,0,0.02); border-radius: 4px; padding: 6px 10px; font-family: 'Montserrat', sans-serif;">
<div style="font-size: 10px; text-transform: uppercase; opacity: 0.6; font-weight: 700; letter-spacing: 0.05em; color: #4caf50;">Monthly Issue</div>
<div style="font-size: 12px; font-weight: 700; margin-top: 1px;">📋 {issue_title}</div>
<div style="font-size: 11px; opacity: 0.8; margin-top: 2px;">↳ {option_text}</div>
</div>""",
                    unsafe_allow_html=True
                )


def render_last_round_summary(turn_view, selected_filter="All Parties"):
    commentary = turn_view.get("lastRoundCommentary", [])
    if not commentary:
        return
        
    if selected_filter != "All Parties":
        commentary = [line for line in commentary if selected_filter.lower() in line.lower()]
        
    with st.expander("Commentary", expanded=False):
        if commentary:
            for line in commentary:
                st.write(f"- {line}")
        else:
            st.write("No commentary found matching this party.")


def render_current_round_submissions(turn_view):
    submissions = turn_view.get("currentRoundSubmissions", [])
    if not submissions:
        return
    with st.expander("Submitted This Month", expanded=False):
        for submission in submissions:
            st.write(f"- {submission['partyName']} locked `{submission['cardName']}`")


def render_party_banner(party):
    color = party.get("color") or "#3c4a57"
    symbol = party.get("symbol") or party["name"][:2].upper()
    symbol_art = SYMBOL_ART.get(symbol, symbol[:3].upper())
    stats = party["stats"]
    st.markdown(
        f"""
        <div class="party-flag" style="background: linear-gradient(135deg, {color}, #1d1d1d);">
          <div style="display:flex;align-items:center;">
            <div class="symbol-medallion">{symbol_art}</div>
            <div>
              <div class="party-symbol">{symbol}</div>
              <div style="font-size:20px;font-weight:800;margin-top:4px;">{party['name']}</div>
            </div>
          </div>
          <div style="margin-top:5px;">{party['role'].replace('_', ' ').title()} | {party.get('humanPlayerLabel') or party['controllerType']}</div>
          <div style="margin-top:10px;font-size:13px;">Coins {stats['coins']} | Morale {stats['partyMorale']} | Media {stats['mediaImage']} | Support {stats['publicSupport']}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def summarize_effects(card, target_key):
    effects = card.get("visibleEffects", {}).get(target_key, {})
    if not effects:
        scheduled = card.get("visibleEffects", {}).get("scheduled", [])
        if scheduled:
            effects = scheduled[0].get("effects", {}).get(target_key, {})
    if not effects:
        return "No visible effect"
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
    return ", ".join(parts) if parts else "No visible effect"


def card_requires_target(card):
    target = card.get("target", {})
    opponent_effects = card.get("visibleEffects", {}).get("opponentParty", {})
    scheduled = card.get("visibleEffects", {}).get("scheduled", [])
    if not opponent_effects and scheduled:
        opponent_effects = scheduled[0].get("effects", {}).get("opponentParty", {})
    return bool(target.get("opponentParty")) or bool(opponent_effects)


def render_playable_card(card, turn_view):
    category = card.get("category", "other")
    color = CATEGORY_COLORS.get(category, "#555555")
    post_it_color = POST_IT_COLORS.get(category, "#fff2cc")
    timing = card.get("timing", {})
    risk = card.get("riskRoll", {})
    risk_text = f"{risk.get('chance', 0)}% risk" if risk else "Low risk"
    selected_key = f"select-card-{card.get('cardKey', card['name'])}"
    selected_card_key = st.session_state.get("selected_card", {}).get("cardKey")
    
    active_party_id = turn_view.get("activeHumanPartyId")
    active_party = next((p for p in turn_view.get("parties", []) if p["id"] == active_party_id), None)
    current_coins = active_party["stats"]["coins"] if active_party else 0
    insufficient_funds = card.get("cost", 0) > current_coins
    
    usage = turn_view.get("cardUsageByParty", {}).get(active_party_id, {})
    used_uses = usage.get(card.get("cardKey"), 0)
    remaining_uses = card.get("maxUsesPerCycle", 2) - used_uses
    if selected_card_key == card.get("cardKey"):
        remaining_uses -= 1
    remaining_uses = max(0, remaining_uses)
    
    label = CATEGORY_LABELS.get(category, category.replace("_", " ").title())
    expander_title = f"🃏 {card['name']} (Cost: {card['cost']})"
    if selected_card_key == card.get("cardKey"):
        expander_title = f"🔥 {card['name']} (SELECTED) 🔥"
    st.markdown(f'<div class="card-marker-{category}"></div>', unsafe_allow_html=True)
    with st.expander(expander_title, expanded=False):
        st.markdown(
            f"""
            <div style="font-family: 'Montserrat', sans-serif; line-height: 1.5; padding: 8px 0;">
                <div style="font-size: 11px; text-transform: uppercase; color: #555555; font-weight: 700; letter-spacing: 0.05em;">{label}</div>
                <div style="font-size: 14px; font-weight: 800; margin-top: 4px; margin-bottom: 8px; color: #111111;">🃏 {card['name']}</div>
                <div style="font-size: 12px; margin-bottom: 10px; color: #2d3748;">{card.get('description', 'No description available.')}</div>
                <div style="background: rgba(0,0,0,0.03); border-radius: 6px; padding: 8px; margin-bottom: 10px; font-size: 12px;">
                    <div style="margin-bottom: 4px;"><b>🟢 Self Effects:</b> {summarize_effects(card, 'selfParty')}</div>
                    <div><b>🔴 Opponent Effects:</b> {summarize_effects(card, 'opponentParty')}</div>
                </div>
                <div style="font-size: 11px; border-top: 1px dashed rgba(0,0,0,0.15); padding-top: 6px; color: #555555;">
                    <b>Cost:</b> {card['cost']} coins | <b>Uses:</b> {remaining_uses}/{card.get('maxUsesPerCycle', 2)}<br/>
                    <b>Risk:</b> {risk_text} | <b>Resolution:</b> {timing.get('minTurns', 1)}-{timing.get('maxTurns', 1)} m
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if insufficient_funds:
            st.warning("⚠️ Insufficient coins to play this card.")
        elif remaining_uses <= 0:
            st.warning("⚠️ No remaining uses for this cycle.")
        
        st.write("") # Spacer
        if st.button("Select Card", key=selected_key, use_container_width=True, disabled=(remaining_uses <= 0) or insufficient_funds):
            st.session_state["selected_card"] = card
            st.session_state["target_party_id"] = None
            has_rewards = bool(turn_view.get("activePlayerHeldRewards", []))
            if card_requires_target(card):
                st.session_state["gameplay_step"] = "select_target"
            elif has_rewards:
                st.session_state["gameplay_step"] = "play_reward"
            else:
                st.session_state["gameplay_step"] = "news_reactions"
            st.success(f"Selected: {card['name']}")
            st.rerun()

    if st.session_state.get("selected_card", {}).get("cardKey") == card.get("cardKey"):
        st.info("Selected for this turn")


def render_selected_card_panel(card):
    category = card.get("category", "other")
    color = CATEGORY_COLORS.get(category, "#555555")
    timing = card.get("timing", {})
    risk = card.get("riskRoll", {})
    risk_text = f"{risk.get('chance', 0)}% risk" if risk else "Low risk"
    st.markdown(
        f"""
        <div class="deck-card" style="background: linear-gradient(135deg, {color}, #222); min-height: 150px;">
          <div class="deck-card-title">{card['name']}</div>
          <div class="deck-meta">Cost {card['cost']} | {CATEGORY_LABELS.get(category, category)}</div>
          <div class="deck-meta">Result: {timing.get('minTurns', 1)}-{timing.get('maxTurns', 1)} months | {risk_text}</div>
          <div class="effect-line"><b>Self:</b> {summarize_effects(card, 'selfParty')}</div>
          <div class="effect-line"><b>Opponent:</b> {summarize_effects(card, 'opponentParty')}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar_inventory(turn_view):
    st.subheader("🎒 Held Rewards")
    held = turn_view.get("activePlayerHeldRewards", [])
    if not held:
        st.caption("No rewards in inventory. Win bidding rounds to earn rewards at the end of the 5-turn cycle!")
        return
    for r in held:
        with st.container(border=True):
            st.markdown(f"**🎁 {r['name']}**")
            st.caption(r['description'])
            st.markdown(f"<span style='color: #ff9800; font-size: 11px; font-weight: 700;'>⏳ Expires in {r['turnsLeft']} turn(s)</span>", unsafe_allow_html=True)
