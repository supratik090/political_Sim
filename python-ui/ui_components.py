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
    base_css = """
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap');
        /* Force page background to Sage Grey-Green (#B0BA99) and body text to Black */
        html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stMain"], section.main, .stApp {
          background-color: #B0BA99 !important;
          background: #B0BA99 !important;
          color: #000000 !important;
        }

        /* Ensure the main block container is transparent to reveal the page background */
        .block-container, [data-testid="stMainBlockContainer"] {
          background-color: transparent !important;
          background: transparent !important;
        }

        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, .stApp p, .stApp label, .stApp li, .stApp span {
          color: #000000 !important;
        }
        /* Styled tabs */
        button[data-baseweb="tab"] {
          color: #000000 !important;
          font-weight: 600 !important;
          background-color: transparent !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
          color: #213C51 !important;
          border-bottom-color: #213C51 !important;
        }

        /* Inputs styling: select boxes #213C51 background and white text */
        [data-testid="stTextInput"] input,
        [data-testid="stTextInput"] input * {
          background-color: #213C51 !important;
          color: #ffffff !important;
        }
        [data-testid="stTextInput"] div[data-baseweb="base-input"] {
          border: 1.5px solid #6594B1 !important;
          border-radius: 4px !important;
        }
        [data-testid="stNumberInput"] input,
        [data-testid="stNumberInput"] input * {
          background-color: #213C51 !important;
          color: #ffffff !important;
        }
        [data-testid="stNumberInput"] div[data-baseweb="base-input"] {
          border: 1.5px solid #6594B1 !important;
          border-radius: 4px !important;
          background-color: #213C51 !important;
        }
        [data-testid="stNumberInput"] button,
        [data-testid="stNumberInput"] button * {
          background-color: #213C51 !important;
          color: #ffffff !important;
          fill: #ffffff !important;
          border-color: #6594B1 !important;
        }
        [data-testid="stSelectbox"] div[data-baseweb="select"] > div,
        [data-testid="stSelectbox"] div[data-baseweb="select"] span,
        [data-testid="stSelectbox"] div[data-baseweb="select"] div,
        [data-testid="stSelectbox"] div[data-baseweb="select"] * {
          background-color: #213C51 !important;
          color: #ffffff !important;
        }
        [data-testid="stSelectbox"] div[data-baseweb="select"] {
          border: 1.5px solid #6594B1 !important;
          border-radius: 4px !important;
        }
        /* Custom styled metric values: Black by default on page */
        [data-testid="stMetricValue"] {
          font-size: 20px !important;
          font-weight: 800 !important;
          color: #000000 !important;
        }
        [data-testid="stMetricLabel"] {
          font-size: 11px !important;
          font-weight: 700 !important;
          text-transform: uppercase !important;
          letter-spacing: 0.05em !important;
          color: #000000 !important;
          opacity: 0.8;
        }
        [data-testid="stMetricDelta"] {
          font-weight: 700 !important;
          font-size: 13px !important;
        }

        /* Globally Styled Buttons (Secondary / Standard - select boxes #213C51, text white) */
        div.stButton > button {
          background: #213C51 !important;
          color: #ffffff !important;
          border: 1px solid #213C51 !important;
          border-radius: 8px !important;
          font-weight: 600 !important;
          font-size: 13px !important;
          letter-spacing: 0.03em !important;
          padding: 8px 16px !important;
          box-shadow: 0 4px 6px rgba(33, 60, 81, 0.15) !important;
          transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
          width: 100% !important;
        }
        /* Prevent global text color override from making button text dark/unreadable */
        div.stButton > button,
        div.stButton > button p,
        div.stButton > button span {
          color: #ffffff !important;
        }
        div.stButton > button:hover {
          background: #192e3e !important;
          border-color: #192e3e !important;
          box-shadow: 0 6px 12px rgba(33, 60, 81, 0.25) !important;
          transform: translateY(-2px) !important;
        }
        div.stButton > button:hover p,
        div.stButton > button:hover span {
          color: #ffffff !important;
        }
        div.stButton > button:active {
          transform: translateY(1px) !important;
        }
        div.stButton > button:disabled {
          border-color: rgba(33, 60, 81, 0.1) !important;
          color: rgba(255, 255, 255, 0.6) !important;
          background: #192e3e !important;
          box-shadow: none !important;
        }
        /* Selected Select Option Buttons: text changes to Green (#22c55e) once selected */
        div.stButton > button[kind="primary"],
        div.stButton > button[data-testid="stBaseButton-primary"] {
          background: #213C51 !important;
          color: #22c55e !important;
          border: 1.5px solid #22c55e !important;
          font-weight: 700 !important;
          box-shadow: 0 4px 10px rgba(34, 197, 94, 0.2) !important;
        }
        div.stButton > button[kind="primary"],
        div.stButton > button[kind="primary"] p,
        div.stButton > button[kind="primary"] span,
        div.stButton > button[data-testid="stBaseButton-primary"],
        div.stButton > button[data-testid="stBaseButton-primary"] p,
        div.stButton > button[data-testid="stBaseButton-primary"] span {
          color: #22c55e !important;
        }
        div.stButton > button[kind="primary"]:hover,
        div.stButton > button[data-testid="stBaseButton-primary"]:hover {
          background: #192e3e !important;
          border-color: #22c55e !important;
          box-shadow: 0 6px 15px rgba(34, 197, 94, 0.3) !important;
        }
        div.stButton > button[kind="primary"]:hover p,
        div.stButton > button[kind="primary"]:hover span,
        div.stButton > button[data-testid="stBaseButton-primary"]:hover p,
        div.stButton > button[data-testid="stBaseButton-primary"]:hover span {
          color: #22c55e !important;
        }

        /* Clean and soft expanders inside dashboard */
        [data-testid="stExpander"] {
          background-color: #ffffff !important;
          border: 1px solid #213C51 !important;
          border-radius: 8px !important;
        }
        [data-testid="stExpander"] summary div {
          color: #000000 !important;
          font-weight: 700 !important;
        }

        /* Bidding Station Background (#6594B1) and White text */
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.bidding-station-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .bidding-station-marker)) {
          background: #6594B1 !important;
          background-color: #6594B1 !important;
          border: 2px solid #213C51 !important;
          border-radius: 12px !important;
          padding: 16px !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.bidding-station-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .bidding-station-marker)) *:not([data-testid="stMetricDelta"]):not([data-testid="stMetricDelta"] *) {
          color: #ffffff !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.bidding-station-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .bidding-station-marker)) [data-testid="stMetricValue"],
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.bidding-station-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .bidding-station-marker)) [data-testid="stMetricLabel"] {
          color: #ffffff !important;
        }
        /* Standings & Last Decisions: White background (#ffffff) and Black text */
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.standings-panel-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .standings-panel-marker)),
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.last-decisions-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .last-decisions-marker)) {
          background: #ffffff !important;
          background-color: #ffffff !important;
          border: 2px solid #213C51 !important;
          border-radius: 12px !important;
          padding: 16px !important;
          box-shadow: 0 4px 10px rgba(33, 60, 81, 0.05) !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.standings-panel-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .standings-panel-marker)) *:not([data-testid="stMetricDelta"]):not([data-testid="stMetricDelta"] *):not(.party-panel-title):not(.party-panel-title *),
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.last-decisions-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .last-decisions-marker)) *:not([data-testid="stMetricDelta"]):not([data-testid="stMetricDelta"] *):not(.last-decisions-title):not(.last-decisions-title *) {
          color: #000000 !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.standings-panel-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .standings-panel-marker)) [data-testid="stMetricValue"],
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.standings-panel-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .standings-panel-marker)) [data-testid="stMetricLabel"] {
          color: #000000 !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.standings-panel-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .standings-panel-marker)) .party-panel-badge {
          color: #475569 !important;
        }
        /* Cards container: background #DDAED3 with #213C51 border and black text */
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.playable-card-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .playable-card-marker)) {
          background: #DDAED3 !important;
          background-color: #DDAED3 !important;
          border: 2px solid #213C51 !important;
          border-top: 6px solid #213C51 !important;
          border-radius: 12px !important;
          padding: 14px !important;
          box-shadow: 0 4px 10px rgba(33, 60, 81, 0.05) !important;
          transition: all 0.2s ease-in-out !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.playable-card-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .playable-card-marker)) h4,
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.playable-card-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .playable-card-marker)) summary,
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.playable-card-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .playable-card-marker)) p:not(button):not(button *),
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.playable-card-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .playable-card-marker)) span:not(.card-cost-value):not(.card-effect-self):not(.card-effect-opp):not(button *),
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.playable-card-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .playable-card-marker)) div:not(.card-effect-self):not(.card-effect-opp):not(button):not(button *) {
          color: #000000 !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.playable-card-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .playable-card-marker)) .card-cost-value {
          color: #213C51 !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.playable-card-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .playable-card-marker)) .card-effect-self,
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.playable-card-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .playable-card-marker)) .card-effect-self * {
          color: #0d9488 !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.playable-card-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .playable-card-marker)) .card-effect-opp,
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.playable-card-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .playable-card-marker)) .card-effect-opp * {
          color: #be123c !important;
        }

        /* Targeted vertical block containers (News Reactions, Party Decisions, Play Reward): White background, Steel Blue border, Black text */
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.news-reactions-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .news-reactions-marker)),
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.party-decisions-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .party-decisions-marker)),
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.play-reward-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .play-reward-marker)) {
          background-color: #ffffff !important;
          background: #ffffff !important;
          border: 2px solid #6594B1 !important;
          border-radius: 12px !important;
          padding: 16px !important;
          box-shadow: 0 4px 10px rgba(101, 148, 177, 0.08) !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.news-reactions-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .news-reactions-marker)) *:not(button):not(button *),
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.party-decisions-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .party-decisions-marker)) *:not(button):not(button *),
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.play-reward-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .play-reward-marker)) *:not(button):not(button *) {
          color: #000000 !important;
        }
        /* Held Rewards container: background #DDAED3 with #213C51 border and black text */
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.held-rewards-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .held-rewards-marker)) {
          background-color: #DDAED3 !important;
          background: #DDAED3 !important;
          border: 2px solid #213C51 !important;
          border-radius: 12px !important;
          padding: 16px !important;
          box-shadow: 0 4px 10px rgba(33, 60, 81, 0.05) !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.held-rewards-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .held-rewards-marker)) *:not(button):not(button *) {
          color: #000000 !important;
        }
        /* Developer Bypass: background #DDAED3 with #213C51 border and black text */
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.developer-bypass-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .developer-bypass-marker)) {
          background-color: #DDAED3 !important;
          background: #DDAED3 !important;
          border: 2px solid #213C51 !important;
          border-radius: 12px !important;
          padding: 20px !important;
          box-shadow: 0 4px 10px rgba(33, 60, 81, 0.05) !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.developer-bypass-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .developer-bypass-marker)) *:not(button):not(button *):not(input) {
          color: #000000 !important;
        }
        /* Projects container: background #E6E6FA (Lavender) with #213C51 border and black text */
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.projects-panel-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .projects-panel-marker)) {
          background-color: #E6E6FA !important;
          background: #E6E6FA !important;
          border: 2px solid #213C51 !important;
          border-radius: 12px !important;
          padding: 16px !important;
          box-shadow: 0 4px 10px rgba(33, 60, 81, 0.05) !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:has(.projects-panel-marker):not(:has(div[data-testid="stVerticalBlockBorderWrapper"] .projects-panel-marker)) *:not(button):not(button *) {
          color: #000000 !important;
        }
        /* Force active player banner top left card to have bright white text */
        div[data-testid="stAppViewContainer"] .party-flag,
        div[data-testid="stAppViewContainer"] .party-flag *,
        .party-flag, .party-flag * {
          color: #ffffff !important;
        }

        /* Increase size and readability of the bidding slider */
        [data-testid="stSlider"] {
          padding-top: 12px !important;
          padding-bottom: 12px !important;
          margin-left: 12px !important;
          margin-right: 12px !important;
        }
        [data-testid="stSlider"] label,
        [data-testid="stSlider"] label * {
          font-size: 13px !important;
          font-weight: 800 !important;
          color: #ffffff !important;
        }
        [data-testid="stSlider"] div[data-baseweb="slider"] {
          height: 10px !important;
          margin-top: 6px !important;
          margin-bottom: 6px !important;
        }
        [data-testid="stSlider"] div[role="slider"] {
          width: 20px !important;
          height: 20px !important;
          background-color: #213C51 !important;
          border: 2px solid #ffffff !important;
        }
        [data-testid="stSlider"] div[data-baseweb="slider"] + div,
        [data-testid="stSlider"] div[data-baseweb="slider"] + div * {
          display: none !important;
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
          background-color: #D6FB61 !important;
          border: 2px solid #39B1D1 !important;
          border-radius: 16px;
          padding: 12px;
          color: #1e293b !important;
          min-height: 178px;
          box-shadow: 0 8px 18px rgba(80, 62, 35, .10);
        }
        .deck-card * {
          color: #1e293b !important;
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

        .party-panel-title {
          font-size: 15px;
          font-weight: 800;
          margin-bottom: 8px;
        }
        .party-panel-badge {
          font-size: 11px;
          opacity: 0.6;
        }
        .playable-card-body {
          font-family: 'Montserrat', sans-serif;
          line-height: 1.5;
          padding: 8px 0;
        }
        .playable-card-category {
          font-size: 11px;
          text-transform: uppercase;
          color: #555555;
          font-weight: 700;
          letter-spacing: 0.05em;
        }
        .playable-card-title {
          font-size: 14px;
          font-weight: 800;
          margin-top: 4px;
          margin-bottom: 8px;
          color: #111111;
        }
        .playable-card-description {
          font-size: 12px;
          margin-bottom: 10px;
          color: #2d3748;
        }
        .playable-card-effects {
          background: rgba(0,0,0,0.03);
          border-radius: 6px;
          padding: 8px;
          margin-bottom: 10px;
          font-size: 12px;
          color: #2d3748;
        }
        .playable-card-meta {
          font-size: 11px;
          border-top: 1px dashed rgba(0,0,0,0.15);
          padding-top: 6px;
          color: #555555;
        }
        @media (max-width: 768px) {
          /* Force all horizontal blocks to cascade (stack) vertically on mobile */
          [data-testid="stHorizontalBlock"] {
            flex-direction: column !important;
            gap: 12px !important;
          }
          [data-testid="stHorizontalBlock"] > [data-testid="column"] {
            width: 100% !important;
            min-width: 100% !important;
          }
          /* Mobile slider sizing adjustments to prevent text overflow */
          [data-testid="stSlider"] {
            padding-top: 4px !important;
            padding-bottom: 4px !important;
          }
          [data-testid="stSlider"] label,
          [data-testid="stSlider"] label * {
            font-size: 11px !important;
          }
          [data-testid="stSlider"] div[data-baseweb="slider"] {
            height: 6px !important;
            margin-top: 4px !important;
            margin-bottom: 4px !important;
          }
          [data-testid="stSlider"] div[role="slider"] {
            width: 14px !important;
            height: 14px !important;
          }
          [data-testid="stSlider"] div[data-baseweb="slider"] + div,
          [data-testid="stSlider"] div[data-baseweb="slider"] + div * {
            display: none !important;
          }
          .kbc-card-container {
            padding: 14px !important;
            border-radius: 10px !important;
          }
          .kbc-question-title {
            font-size: 15px !important;
            margin-bottom: 12px !important;
            padding-bottom: 8px !important;
          }
          h1 {
            font-size: 20px !important;
          }
          h2 {
            font-size: 15px !important;
          }
          h3 {
            font-size: 13px !important;
          }

          /* Scaled down metrics display */
          [data-testid="stMetricValue"] {
            font-size: 11px !important;
          }
          [data-testid="stMetricLabel"] {
            font-size: 8px !important;
          }
          [data-testid="stMetricDelta"] {
            font-size: 8px !important;
          }

          /* Scaled down option buttons */
          div.stButton > button {
            font-size: 10px !important;
            padding: 4px 8px !important;
            border-radius: 12px !important;
          }

          /* Compact card expanders on mobile */
          div[data-testid="stExpander"] {
            margin-bottom: 4px !important;
            border-radius: 4px !important;
          }
          div[data-testid="stExpander"] summary {
            padding: 4px 6px !important;
          }
          div[data-testid="stExpander"] summary div {
            font-size: 10px !important;
          }
          div[data-testid="stExpander"] div[role="region"] div {
            font-size: 9px !important;
            padding: 4px 6px !important;
          }

          /* Scaled down party panel text */
          .party-panel-title {
            font-size: 10px !important;
            margin-bottom: 4px !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
          }
          .party-panel-badge {
            font-size: 7px !important;
            display: block !important;
            margin-top: 1px !important;
          }
          /* Scaled down playable cards HTML content */
          .playable-card-body {
            padding: 4px 0 !important;
          }
          .playable-card-category {
            font-size: 8px !important;
          }
          .playable-card-title {
            font-size: 10px !important;
            margin-top: 2px !important;
            margin-bottom: 4px !important;
          }
          .playable-card-description {
            font-size: 9px !important;
            margin-bottom: 6px !important;
          }
          .playable-card-effects {
            font-size: 9px !important;
            padding: 4px !important;
            margin-bottom: 6px !important;
          }
          .playable-card-meta {
            font-size: 8px !important;
            padding-top: 4px !important;
          }

          /* Compact party banners and flags */
          .party-flag {
            min-height: 75px !important;
            padding: 8px 12px !important;
            border-radius: 10px !important;
          }
          .party-flag-title {
            font-size: 12px !important;
          }
          .party-flag-subtitle {
            font-size: 9px !important;
          }
          .symbol-medallion {
            width: 40px !important;
            height: 40px !important;
            border-radius: 10px !important;
          }
          .party-symbol {
            font-size: 18px !important;
          }
        }
    """
    st.markdown("<style>\n" + category_css + base_css + "\n</style>", unsafe_allow_html=True)
def render_party_panel(title, party, deltas=None):
    stats = party["stats"]
    deltas = deltas or {}
    is_active = party.get("active", True)
    badge = "ELIMINATED" if not is_active else ("Player" if party["playerControlled"] else "AI")
    color = "#718096" if not is_active else (party.get("color") or "#555555")

    with st.container(border=True):
        st.markdown("<div class='standings-panel-marker'></div>", unsafe_allow_html=True)
        st.markdown(
            f"<div class='party-panel-title' style='color: {color};'>"
            f"<span style='color: {color};'>●</span> {party['name']} "
            f"<span class='party-panel-badge'>({badge} - {title})</span>"
            f"</div>",
            unsafe_allow_html=True
        )

        if not is_active:
            st.info("💀 Politically Eliminated")
        else:
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
        st.markdown("<div class='last-decisions-marker'></div>", unsafe_allow_html=True)
        st.markdown(
            f"<div class='last-decisions-title' style='font-size: 15px; font-weight: 800; margin-bottom: 8px; color: {color} !important;'>"
            f"<span style='color: {color};'>●</span> {party['name']} "
            f"<span style='font-size: 11px; opacity: 0.6; color: #475569 !important;'>({badge})</span>"
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
                    reaction_opts = news_def.get("reactionOptions") or news_def.get("options") or []
                    reaction_opt = next((opt for opt in reaction_opts if (opt.get("reactionKey") or opt.get("optionKey")) == reaction_key), None)
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

        # Party Decision Response
        if submission.get("issueTitle"):
            issue_title = submission.get("issueTitle")
            option_text = submission.get("issueOptionText", "Response chosen")
            issue_title_short = truncate_text(issue_title, 35)
            option_text_short = truncate_text(option_text, 35)

            if len(issue_title) > 35 or len(option_text) > 35:
                st.markdown(
                    f"""<details style="border-left: 4px solid #4caf50; padding-left: 10px; margin-top: 10px; background: rgba(0,0,0,0.02); border-radius: 4px; padding: 6px 10px; cursor: pointer; font-family: 'Montserrat', sans-serif;">
<summary style="font-size: 10px; text-transform: uppercase; opacity: 0.6; font-weight: 700; letter-spacing: 0.05em; color: #4caf50; outline: none; list-style: none;">
📋 Party Decision <span style="font-size: 9px; color: #888; font-weight: normal; margin-left: 4px; text-transform: none; letter-spacing: normal;">(click to view)</span>
<div style="font-size: 12px; font-weight: 700; margin-top: 1px; color: #212529;">{issue_title_short}</div>
<div style="font-size: 11px; opacity: 0.8; margin-top: 2px; font-weight: 500; color: #212529;">↳ {option_text_short}</div>
</summary>
<div style="font-size: 11px; opacity: 0.95; margin-top: 6px; padding-top: 6px; border-top: 1px dashed rgba(0,0,0,0.05); color: #111;">
<strong>Decision:</strong> {issue_title}<br/>
<strong>Response:</strong> {option_text}
</div>
</details>""",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""<div style="border-left: 4px solid #4caf50; padding-left: 10px; margin-top: 10px; background: rgba(0,0,0,0.02); border-radius: 4px; padding: 6px 10px; font-family: 'Montserrat', sans-serif;">
<div style="font-size: 10px; text-transform: uppercase; opacity: 0.6; font-weight: 700; letter-spacing: 0.05em; color: #4caf50;">Party Decision</div>
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
        <div class="party-flag" style="background: linear-gradient(135deg, {color}, #1d1d1d); color: #ffffff !important;">
          <div style="display:flex;align-items:center; color: #ffffff !important;">
            <div class="symbol-medallion" style="color: #ffffff !important;">{symbol_art}</div>
            <div style="color: #ffffff !important;">
              <div class="party-symbol" style="color: #ffffff !important;">{symbol}</div>
              <div style="font-size:20px;font-weight:800;margin-top:4px; color: #ffffff !important;">{party['name']}</div>
            </div>
          </div>
          <div style="margin-top:5px; color: #ffffff !important;">{party['role'].replace('_', ' ').title()} | {party.get('humanPlayerLabel') or party['controllerType']}</div>
          <div style="margin-top:10px;font-size:13px; color: #ffffff !important;">Coins {stats['coins']} | Morale {stats['partyMorale']} | Media {stats['mediaImage']} | Support {stats['publicSupport']}%</div>
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
def get_card_description(card):
    desc = card.get("description")
    if desc and isinstance(desc, str) and desc.strip() and desc != "No description available.":
        return desc

    name_key = card.get("name", "").lower().strip()

    CARD_DESCRIPTIONS = {
        "launch welfare scheme": "Introduce structured financial assistance and welfare programs to support low-income families and build voter gratitude.",
        "announce infrastructure project": "Unveil major development projects like highways, bridges, and power plants to showcase governance capability.",
        "law and order drive": "Initiate a crack-down on local crime, boosting citizens' sense of safety and reinforcing your administrative strength.",
        "farmer loan relief": "Announce debt waivers and subsidies for small-scale farmers to win rural loyalty and ease agricultural distress.",
        "youth employment mission": "Launch skill training programs and job creation initiatives to attract the crucial young demographic.",
        "women safety campaign": "Deploy special surveillance units and helpline infrastructure to address safety concerns and win women's support.",
        "subsidy announcement": "Introduce subsidized food, electricity, or water supplies to provide immediate relief to underprivileged households.",
        "education reform bill": "Revamp public schooling systems, launch teacher training drives, and allocate scholarships to improve education.",
        "disaster relief package": "Distribute emergency funds, food supplies, and rebuilding grants in response to local flooding or droughts.",
        "cleanliness mission": "Organize state-wide sanitation and solid waste management campaigns to improve public health and hygiene.",
        "unity march": "Lead party cadres on a peaceful march through diverse neighborhoods to champion communal harmony and social solidarity.",
        "public grievance camp": "Set up direct outreach desks where citizens can meet officials to resolve pending administrative issues.",
        "media blitz": "Buy prime-time TV slots and full-page newspaper advertisements to flood the public sphere with positive achievements.",
        "attack opposition manifesto": "Deconstruct the opposition's policy declarations, highlighting fiscal irresponsibility and unfeasible promises.",
        "cabinet reshuffle": "Replace underperforming ministers with fresh faces to project reformist intent and manage internal party dynamics.",
        "promote popular leader": "Focus your media campaign and rallies on an iconic leader to tap into personal charisma and mass appeal.",
        "cadre training camp": "Conduct strategic bootcamps for grassroots party workers to align messaging and prepare for election mobilization.",
        "strengthen party base": "Re-engage traditional voters and key community leaders to secure your core constituency support.",
        "organize fundraiser": "Host dinners and corporate outreach programs to secure campaign funds and financial resources.",
        "regional pride campaign": "Highlight regional achievements, language, and cultural heritage to invoke native identity support.",
        "community leader outreach": "Initiate private negotiations and alliance building with powerful local community influencers.",
        "anti-corruption raid on opposition": "Order federal or state agencies to raid opposition leaders under investigation for financial fraud.",
        "investigate opposition funding": "Initiate a formal audit into foreign donations and corporate backers of key rival political entities.",
        "expose opposition infighting": "Leak internal communications and private disputes of the rival party to highlight their leadership crisis.",
        "order independent inquiry": "Appoint a retired judge to lead a public probe into a recent administrative slip-up, buying time for the party.",
        "release documents": "Leak verified files regarding rival party leaders' assets, real-estate deals, or illegal transactions.",
        "sacrifice minister": "Force a controversial cabinet member to resign, absorbing public outrage and shielding the chief leader.",
        "media defense campaign": "Deploy your best party spokespersons to television debates to counter hostile narratives and clarify policy.",
        "legal notice": "Send cease-and-desist letters to media houses or rival politicians publishing defamatory statements.",
        "suppress protest": "Deploy law enforcement units to place barriers, impose curfews, and dissolve public demonstrations.",
        "anti-corruption march": "Lead a public march demanding actions against corrupt ministers, capitalizing on middle-class outrage.",
        "farmer agitation": "Support rural strikes and highway blockades to protest state crop pricing and demand financial packages.",
        "student movement": "Mobilize college unions for protests against rising tuition, job scarcity, or administrative high-handedness.",
        "price rise protest": "Organize mock market demonstrations with empty gas cylinders to highlight inflation and rising food prices.",
        "public yatra": "Embark on a walking tour across the state to connect with grassroots voters and listen to local concerns.",
        "cleanliness drive": "Lead party cadres in cleaning local parks and markets, presenting a positive civic-minded image.",
        "blood donation camp": "Establish volunteer camps to donate blood and coordinate medical help, demonstrating social responsibility.",
        "relief work during crisis": "Deploy party volunteers to distribute drinking water, dry rations, and medical kits during a heatwave or flood.",
        "public listening sabha": "Convene open-town halls in rural blocks where party representatives sit down to answer community questions.",
        "media debate challenge": "Publicly challenge the rival leader to a televised, one-on-one live debate on development and governance.",
        "social media campaign": "Launch coordinated viral campaigns, memes, and video snippets on YouTube and WhatsApp to sway opinion.",
        "release shadow budget": "Present a detailed alternative budget highlighting how your party would fund welfare without increasing debt.",
        "build booth network": "Set up dedicated committees for every single voting booth to manage voter turn-out on election day.",
        "regional pride rally": "Hold a mega convention celebrating local historical icons and achievements to counter national narratives.",
        "expose teacher admission scam": "Expose systemic bribes in public teacher recruitments, targeting the ruling coalition's governance credibility.",
        "expose local corruption": "Publish details of bribery in municipal road contracts or local ration distribution networks.",
        "demand judicial inquiry": "Formally request a high court-monitored investigation into recent state administrative failures."
    }

    if name_key in CARD_DESCRIPTIONS:
        return CARD_DESCRIPTIONS[name_key]

    category = card.get("category", "other")
    cost = card.get("cost", 0)

    cat_desc_map = {
        "governance": f"Deploy resources to strengthen administrative efficiency, implement policy changes, and improve your public support.",
        "positive_service": f"Organize public service initiatives, welfare camps, and citizen outreach campaigns to build local goodwill.",
        "agitation_movement": f"Mobilize party workers for protests and grassroot movements to put pressure on rivals and capture media focus.",
        "scandal_accusation": f"Expose rival corruptions and administrative leaks to damage their reputation and morale.",
        "defensive_counter": f"Launch protective public relations campaigns to minimize damage from opponent allegations and rumors.",
        "media_narrative": f"Coordinate media appearances and narratives to boost your party's image and public perception.",
        "organization_resource": f"Reorganize party cadres, raise funds, and build inner-party morale to prepare for election battles.",
        "ideology_identity": f"Anchor your campaign on core ideological values and identity outreach to secure your base demographics.",
        "constitutional_power_move": f"Utilize legislative and constitutional procedures to secure political leverage and challenge rival coalitions."
    }

    return cat_desc_map.get(category, f"Conduct a strategic {category.replace('_', ' ').lower()} campaign move costing {cost} coins.")
def render_playable_card(card, turn_view):
    category = card.get("category", "other")
    color = CATEGORY_COLORS.get(category, "#555555")
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

    is_selected = selected_card_key == card.get("cardKey")
    if is_selected:
        remaining_uses -= 1
    remaining_uses = max(0, remaining_uses)

    with st.container(border=True):
        selected_class = "card-selected-marker" if is_selected else ""
        st.markdown(f"<div class='playable-card-marker card-category-{category} {selected_class}'></div>", unsafe_allow_html=True)

        # Heading and Cost directly in container
        st.markdown(
            f"""
            <div style="display: flex; justify-content: space-between; align-items: flex-start; font-family: 'Montserrat', sans-serif;">
                <h4 style="margin: 0; font-weight: 800; color: #1e293b; font-size: 14px; flex: 1; padding-right: 8px; line-height: 1.3;">
                    🃏 {card['name']}
                </h4>
                <span class="card-cost-value" style="font-weight: 800; color: #39B1D1; font-size: 13px; white-space: nowrap;">⚡ {card['cost']} coins</span>
            </div>
            <details style="margin-top: 10px; font-size: 11px; cursor: pointer; color: #1e293b; font-family: 'Montserrat', sans-serif;">
                <summary style="font-weight: 700; color: #1e293b; outline: none; margin-bottom: 6px;">🔎 Expand Details</summary>
                <div style="background: rgba(57, 177, 209, 0.05); padding: 8px; border-radius: 6px; margin-top: 4px; border-left: 3px solid #39B1D1; color: #1e293b;">
                    <div style="margin-bottom: 8px; font-weight: 500; line-height: 1.4; color: #1e293b;">
                        {get_card_description(card)}
                    </div>
                    <div style="margin-bottom: 6px; font-weight: 600; color: #1e293b;">
                        Uses Left: <span style="background-color: rgba(57, 177, 209, 0.1); padding: 1px 6px; border-radius: 8px; font-weight: 700; font-size: 10px;">{remaining_uses}/{card.get('maxUsesPerCycle', 2)}</span>
                    </div>
                    <div class="card-effect-self" style="margin-bottom: 4px; color: #0d9488;"><b>🟢 Self:</b> {summarize_effects(card, 'selfParty')}</div>
                    <div class="card-effect-opp" style="color: #be123c;"><b>🔴 Opponent:</b> {summarize_effects(card, 'opponentParty')}</div>
                    <div style="margin-top: 6px; opacity: 0.8; font-size: 10px; color: #1e293b; border-top: 1px solid rgba(57, 177, 209, 0.1); padding-top: 4px;">
                        Risk: <b>{risk_text}</b> | Timing: <b>{timing.get('minTurns', 1)}-{timing.get('maxTurns', 1)}</b> months
                    </div>
                </div>
            </details>
            <div style="margin-top: 10px;"></div>
            """,
            unsafe_allow_html=True
        )

        btn_label = "Deselect Card" if is_selected else "Select a Political Card"
        btn_type = "primary" if is_selected else "secondary"

        if st.button(btn_label, key=selected_key, use_container_width=True, type=btn_type, disabled=((remaining_uses <= 0 or insufficient_funds) and not is_selected)):
            if is_selected:
                st.session_state.pop("selected_card", None)
                st.session_state["target_party_id"] = None
            else:
                st.session_state["selected_card"] = card
                st.session_state["target_party_id"] = None
            st.rerun()

        if insufficient_funds:
            st.warning("⚠️ Insufficient coins")
        elif remaining_uses <= 0 and not is_selected:
            st.warning("⚠️ No remaining uses")
def render_selected_card_panel(card):
    category = card.get("category", "other")
    timing = card.get("timing", {})
    risk = card.get("riskRoll", {})
    risk_text = f"{risk.get('chance', 0)}% risk" if risk else "Low risk"
    st.markdown(
        f"""
        <div class="deck-card" style="background-color: #DDAED3 !important; border: 2px solid #213C51 !important; color: #1e293b !important; min-height: 150px; border-radius: 12px; padding: 16px;">
          <div class="deck-card-title" style="color: #1e293b !important; font-weight: 800; font-size: 15px;">🃏 {card['name']}</div>
          <div class="deck-meta" style="color: #1e293b !important; opacity: 0.8; font-size: 12px; margin-top: 4px;">Cost {card['cost']} | {CATEGORY_LABELS.get(category, category)}</div>
          <div class="deck-meta" style="color: #1e293b !important; opacity: 0.8; font-size: 12px; margin-top: 4px;">Result: {timing.get('minTurns', 1)}-{timing.get('maxTurns', 1)} months | {risk_text}</div>
          <div class="effect-line" style="color: #0d9488 !important; font-size: 12px; margin-top: 8px; background: rgba(0,0,0,0.03); padding: 7px; border-radius: 10px;"><b>Self:</b> {summarize_effects(card, 'selfParty')}</div>
          <div class="effect-line" style="color: #be123c !important; font-size: 12px; margin-top: 8px; background: rgba(0,0,0,0.03); padding: 7px; border-radius: 10px;"><b>Opponent:</b> {summarize_effects(card, 'opponentParty')}</div>
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
            st.markdown(f"<span style='color: #ff9800 !important; font-size: 11px; font-weight: 700;'>⏳ Expires in {r['turnsLeft']} turn(s)</span>", unsafe_allow_html=True)
def render_active_crisis_banner(turn_view):
    crisis_name = turn_view.get("activeCrisisName", "State Crisis")
    crisis_desc = turn_view.get("activeCrisisDescription", "")
    turns_left = turn_view.get("activeCrisisTurnsLeft", 0)
    crisis_key = turn_view.get("activeCrisisKey", "")

    # Custom text based on crisis key
    penalties = ""
    if crisis_key == "drought_crisis":
        penalties = "⚠️ <strong>Rural & Welfare Cards</strong> cost +5 Coins. <strong>Government</strong> support decays by 2% pressure and morale by 3 per turn. mitigatable by Welfare card plays."
    elif crisis_key == "industrial_strike":
        penalties = "⚠️ <strong>All Cards</strong> cost +2 Coins. <strong>All Parties</strong> lose 3 Coins per turn. Public support drifts to Undecided. mitigatable by Governance card plays."
    elif crisis_key == "scam_panic":
        penalties = "⚠️ <strong>Corruption gains</strong> and <strong>Media losses</strong> are doubled. <strong>Government</strong> with >40 corruption loses support/media. mitigatable by defensive counter plays."
    st.markdown(
        f"""
        <div style="background-color: #fcf8ec; border: 3px solid #f06c46; border-radius: 12px; padding: 18px; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 26px; margin-right: 12px;">🚨</span>
                <div>
                    <h3 style="color: #f06c46 !important; margin: 0; font-size: 22px; font-weight: 800;">ACTIVE STATE CRISIS: {crisis_name}</h3>
                    <span style="background-color: #f06c46; color: white; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: bold; text-transform: uppercase; display: inline-block; margin-top: 4px;">{turns_left} months remaining</span>
                </div>
            </div>
            <p style="color: #4e6587 !important; font-size: 14px; margin: 6px 0 12px 0; line-height: 1.4;">{crisis_desc}</p>
            <div style="background-color: rgba(240, 108, 70, 0.1); border-left: 4px solid #f06c46; padding: 10px 14px; border-radius: 0 6px 6px 0;">
                <span style="color: #4e6587 !important; font-size: 13px; font-family: sans-serif; display: block; line-height: 1.4;">
                    {penalties}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_building_projects_panel(turn_view):
    from api_client import fund_project, set_project_target
    from math import ceil

    active_party_id = turn_view.get("activeHumanPartyId")
    game_id = turn_view.get("gameId")
    if not active_party_id or not game_id:
        return

    parties = turn_view.get("parties", [])
    active_party = next((p for p in parties if p["id"] == active_party_id), None)
    if not active_party:
        return

    projects = active_party.get("projects", [])
    if not projects:
        return

    project_defs = {
        "PARTY_HQ": {
            "name": "🏢 Party Headquarters",
            "cost": "100 Coins, 20 Morale",
            "costCoins": 100,
            "costMorale": 20,
            "costCorruption": 0,
            "yield": "💰 +12 Coins, 📢 +3 Media Image per turn",
            "offensive": False,
        },
        "IT_CELL": {
            "name": "💻 IT Cell (Digital Bureau)",
            "cost": "60 Coins, 10 Corruption",
            "costCoins": 60,
            "costMorale": 0,
            "costCorruption": 10,
            "yield": "📢 +2 Media Image, 📈 +1% Public Support per turn (from undecided)",
            "offensive": False,
        },
        "CADRE_OFFICE": {
            "name": "🏘️ District Cadre Offices",
            "cost": "50 Coins, 30 Morale",
            "costCoins": 50,
            "costMorale": 30,
            "costCorruption": 0,
            "yield": "⚡ +4 Morale, 📈 +1% Public Support per turn (from undecided)",
            "offensive": False,
        },
        "THINK_TANK": {
            "name": "🧠 Policy Research Think Tank",
            "cost": "40 Coins, 10 Morale",
            "costCoins": 40,
            "costMorale": 10,
            "costCorruption": 0,
            "yield": "💰 +2 Coins, 📢 +4 Media Image per turn",
            "offensive": False,
        },
        "TRAINING_ACADEMY": {
            "name": "🏫 Grassroots Training Academy",
            "cost": "45 Coins, 20 Morale",
            "costCoins": 45,
            "costMorale": 20,
            "costCorruption": 0,
            "yield": "⚡ +5 Morale per turn",
            "offensive": False,
        },
        "YOUTH_WING": {
            "name": "✊ Youth Wing Network",
            "cost": "35 Coins, 15 Morale",
            "costCoins": 35,
            "costMorale": 15,
            "costCorruption": 0,
            "yield": "⚡ +3 Morale, 📈 +1% Public Support per turn (from undecided)",
            "offensive": False,
        },
        "DISSENT_NEWSPAPER": {
            "name": "📰 Dissenting Newspaper",
            "cost": "65 Coins, 15 Morale",
            "costCoins": 65,
            "costMorale": 15,
            "costCorruption": 0,
            "yield": "💥 -1% Public Support from Target (transfers to Undecided)",
            "offensive": True,
        },
        "MEDIA_HOUSE": {
            "name": "📺 Hostile Media House",
            "cost": "55 Coins, 10 Corruption",
            "costCoins": 55,
            "costMorale": 0,
            "costCorruption": 10,
            "yield": "💥 -4 Media Image to Target per turn",
            "offensive": True,
        },
        "PARTY_DISSENT": {
            "name": "📣 Encourage Rank Dissent",
            "cost": "45 Coins, 25 Morale",
            "costCoins": 45,
            "costMorale": 25,
            "costCorruption": 0,
            "yield": "💥 -3 Morale to Target per turn",
            "offensive": True,
        },
        "CORRUPTION_EXPOSE": {
            "name": "🔍 Expose Corruption Center",
            "cost": "40 Coins, 5 Corruption",
            "costCoins": 40,
            "costMorale": 0,
            "costCorruption": 5,
            "yield": "💥 +3 Corruption to Target per turn",
            "offensive": True,
        },
    }

    def progress_cost(project_def, progress):
        return {
            "coins": int(ceil(project_def["costCoins"] * progress / 100.0)),
            "morale": int(ceil(project_def["costMorale"] * progress / 100.0)),
            "corruption": int(ceil(project_def["costCorruption"] * progress / 100.0)),
        }

    def format_cost(cost):
        parts = []
        if cost["coins"]:
            parts.append(f"{cost['coins']} coins")
        if cost["morale"]:
            parts.append(f"{cost['morale']} morale")
        if cost["corruption"]:
            parts.append(f"{cost['corruption']} corruption")
        return ", ".join(parts) if parts else "No cost"

    def can_afford(cost):
        stats = active_party.get("stats", {})
        return stats.get("coins", 0) >= cost["coins"] and stats.get("partyMorale", 0) >= cost["morale"]

    def view_model(project_state):
        key = project_state["projectKey"]
        project_def = project_defs[key]
        return {
            "key": key,
            "name": project_def["name"],
            "cost": project_def["cost"],
            "yield": project_def["yield"],
            "offensive": project_def["offensive"],
            "progress": project_state.get("progressPercent", 0),
            "targetPartyId": project_state.get("targetPartyId"),
            "targetPartyName": project_state.get("targetPartyName"),
            "def": project_def,
        }

    def render_target_picker(p):
        opponents = [opp for opp in parties if opp["id"] != active_party_id and opp.get("active", True)]
        opp_options = ["Select Target"] + [opp["name"] for opp in opponents]

        current_target_idx = 0
        if p["targetPartyId"]:
            for idx, opp in enumerate(opponents):
                if opp["id"] == p["targetPartyId"]:
                    current_target_idx = idx + 1
                    break

        selected_opp = st.selectbox("🎯 Target Party:", opp_options, index=current_target_idx, key=f"target_sel_{p['key']}")
        if selected_opp != "Select Target":
            chosen_opp = next((opp for opp in opponents if opp["name"] == selected_opp), None)
            if chosen_opp and chosen_opp["id"] != p["targetPartyId"]:
                try:
                    set_project_target(game_id, active_party_id, p["key"], chosen_opp["id"])
                    st.toast(f"Target updated to: {chosen_opp['name']}", icon="🎯")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error setting target: {e}")

    def render_funding_controls(p):
        remaining = 100 - p["progress"]
        presets = [0]
        for val in [20, 40, 60, 80, 100]:
            if val <= remaining:
                presets.append(val)
        if remaining not in presets:
            presets.append(remaining)
        presets = sorted(set(presets))

        select_key = f"selected_contrib_{p['key']}"
        current_contrib = st.session_state.setdefault(select_key, 0)
        if current_contrib not in presets:
            current_contrib = 0
            st.session_state[select_key] = 0

        st.write("")
        st.caption("Select funding contribution:")
        for row_idx in range(0, len(presets), 3):
            cols = st.columns(3)
            for col_idx, val in enumerate(presets[row_idx:row_idx + 3]):
                cost = progress_cost(p["def"], val)
                is_selected = current_contrib == val
                is_finish = val == remaining and val > 0
                if val == 0:
                    label = "💤 None"
                elif is_finish:
                    label = f"🔥 Finish: {format_cost(cost)}"
                else:
                    label = f"🏗️ {format_cost(cost)}"
                disabled = val > 0 and not can_afford(cost)
                with cols[col_idx]:
                    if st.button(
                        label,
                        key=f"contrib_preset_{p['key']}_{val}",
                        use_container_width=True,
                        type="primary" if is_selected else "secondary",
                        disabled=disabled,
                    ):
                        st.session_state[select_key] = val
                        st.rerun()

        if current_contrib > 0:
            selected_cost = progress_cost(p["def"], current_contrib)
            st.write("")
            st.markdown(
                f"<div style='font-size:12px; font-weight:700;'>Selected spend: {format_cost(selected_cost)}</div>",
                unsafe_allow_html=True,
            )
            if st.button("🏗️ Confirm Funding", key=f"fund_btn_{p['key']}", type="primary", use_container_width=True):
                try:
                    fund_project(game_id, active_party_id, p["key"], current_contrib)
                    st.toast(f"Successfully funded project: {p['name']}", icon="✅")
                    st.session_state[select_key] = 0
                    st.rerun()
                except Exception as e:
                    st.error(f"Error funding project: {e}")

    def render_project_detail(p, selected_keys):
        with st.container(border=True):
            title_col, remove_col = st.columns([4, 1])
            with title_col:
                st.markdown(f"#### {p['name']}")
            with remove_col:
                remove_disabled = p["progress"] > 0
                remove_clicked = st.button(
                    "❌",
                    key=f"remove_selected_project_{p['key']}",
                    use_container_width=True,
                    disabled=remove_disabled,
                    help="Remove project" if not remove_disabled else "Projects can only be removed before funding starts.",
                )
            if remove_clicked:
                if p["key"] in selected_keys:
                    selected_keys.remove(p["key"])
                    st.session_state["selected_building_project_keys"] = selected_keys
                st.session_state.pop(f"selected_contrib_{p['key']}", None)
                st.rerun()

            st.markdown(
                f"<div style='font-size:12px; color:#4e6587;'><b>Total Cost:</b> {p['cost']}<br/><b>Yield:</b> {p['yield']}</div>",
                unsafe_allow_html=True,
            )
            st.progress(p["progress"] / 100.0)
            st.caption(f"Progress: {p['progress']}%")

            if p["progress"] >= 100:
                st.markdown("<span style='color:green; font-size:12px; font-weight:700;'>🌟 Completed</span>", unsafe_allow_html=True)
                if p["offensive"]:
                    render_target_picker(p)
                else:
                    st.markdown("<span style='color:green; font-size:12px; font-weight:700;'>🛡️ Passive yield active</span>", unsafe_allow_html=True)
            else:
                render_funding_controls(p)

    st.write("")
    with st.container(border=True):
        all_projects = [view_model(project_state) for project_state in projects if project_state["projectKey"] in project_defs]

        selected_keys = st.session_state.setdefault("selected_building_project_keys", [])
        old_selected_key = st.session_state.pop("selected_building_project_key", None)
        if old_selected_key and old_selected_key not in selected_keys:
            selected_keys.append(old_selected_key)
        added_keys = st.session_state.pop("added_projects", [])
        for key in added_keys:
            if key not in selected_keys:
                selected_keys.append(key)

        completed_projects = [p for p in all_projects if p["progress"] >= 100]
        selected_projects = [
            p for p in all_projects
            if p["progress"] < 100 and (p["progress"] > 0 or p["key"] in selected_keys)
        ]
        projects_ready = bool(completed_projects or selected_projects)

        st.markdown("<div class='projects-panel-marker'></div>", unsafe_allow_html=True)
        st.markdown("### 🏗️ Party Infrastructure Projects · " + ("✅ Done" if projects_ready else "⏳ Pending"))
        st.caption("Fund long-term construction projects for passive campaign engine building or offensive actions.")

        if completed_projects:
            st.write("")
            st.markdown("##### Completed Projects")
            for p in completed_projects:
                render_project_detail(p, selected_keys)

        if selected_projects:
            st.write("")
            st.markdown("##### Selected Projects")
            for p in selected_projects:
                render_project_detail(p, selected_keys)
        elif not completed_projects:
            st.info("No selected projects yet. Choose one from the available projects below.")

        st.write("")
        st.markdown("##### Select From Available Projects")
        category_filter = st.selectbox(
            "📁 Filter Category:",
            ["Build Party", "Target other party"],
            key="projects_category_filter",
        )

        available_projects = [
            p for p in all_projects
            if p["progress"] == 0
            and p["key"] not in selected_keys
            and ((category_filter == "Target other party" and p["offensive"]) or (category_filter == "Build Party" and not p["offensive"]))
        ]

        if not available_projects:
            st.info("No projects available for this category.")
            return

        cols = st.columns(2)
        for i, p in enumerate(available_projects):
            with cols[i % 2]:
                with st.container(border=True):
                    st.markdown(f"##### {p['name']}")
                    st.markdown(
                        f"<div style='font-size:11px; color:#4e6587;'><b>Ready to start</b><br/><b>Total Cost:</b> {p['cost']}<br/><b>Yield:</b> {p['yield']}</div>",
                        unsafe_allow_html=True,
                    )
                    st.progress(p["progress"] / 100.0)
                    st.caption(f"Progress: {p['progress']}%")

                    if st.button(
                        "Select Project",
                        key=f"select_project_{p['key']}",
                        use_container_width=True,
                        type="secondary",
                    ):
                        selected_keys.append(p["key"])
                        st.session_state["selected_building_project_keys"] = selected_keys
                        st.rerun()
