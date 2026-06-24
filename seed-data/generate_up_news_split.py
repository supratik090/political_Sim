import json
import os
import sys

# Ensure seed-data is in the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from up_items_2001_2005 import ITEMS_2001_2005
    from up_items_2006_2010 import ITEMS_2006_2010
except Exception as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

print(f"Loaded {len(ITEMS_2001_2005)} news items for Uttar Pradesh 2001-2005")
print(f"Loaded {len(ITEMS_2006_2010)} news items for Uttar Pradesh 2006-2010")

# Compiling Uttar Pradesh 2001
data_2001 = {
    "reviewStatus": "draft_for_review_not_inserted",
    "scenarioKey": "uttar_pradesh_2001",
    "period": {
        "startMonth": "2001-01",
        "endMonth": "2005-12",
        "months": 60
    },
    "sourceNotes": [
        "Historical-inspired, fictionalized for gameplay; does not use real party names in playable text.",
        "Covers 2001-2005 Uttar Pradesh events with expanded categories: corruption/scams, sports, economy, welfare, health, and law & order.",
        "Key anchors include Rajnath Singh's OBC sub-quota push, 2002 hung assembly and President's Rule, Mayawati's BJP-backed coalition, Madhumita Shukla case, Taj Corridor dispute, Raju Pal murder, and Krishnanand Rai shootout."
    ],
    "defaults": {
        "type": "external",
        "weights": {
            "baseSelectionWeight": 1.0,
            "historicalAnchorWeight": 0.8,
            "scenarioFlavorWeight": 1.2
        },
        "reactionRule": "Each news item contains its own 3 active reactions plus no_comment. Reaction weights and effects vary by issue profile.",
        "thirdPartyReactionRule": "THIRD_PARTY can use opposition-compatible and neutral reactions."
    },
    "newsItems": ITEMS_2001_2005
}

# Compiling Uttar Pradesh 2006
data_2006 = {
    "reviewStatus": "draft_for_review_not_inserted",
    "scenarioKey": "uttar_pradesh_2006",
    "period": {
        "startMonth": "2006-01",
        "endMonth": "2010-12",
        "months": 60
    },
    "sourceNotes": [
        "Historical-inspired, fictionalized for gameplay; does not use real party names in playable text.",
        "Covers 2006-2010 Uttar Pradesh events with expanded categories: corruption/scams, sports, economy, welfare, health, and law & order.",
        "Key anchors include Varanasi temple blasts, Mayawati's 2007 absolute majority victory, Ganga/Yamuna Expressway farmer agitations, Nithari serial killings, Bundelkhand droughts, and the 2010 Allahabad HC Ayodhya title suit verdict."
    ],
    "defaults": {
        "type": "external",
        "weights": {
            "baseSelectionWeight": 1.0,
            "historicalAnchorWeight": 0.8,
            "scenarioFlavorWeight": 1.2
        },
        "reactionRule": "Each news item contains its own 3 active reactions plus no_comment. Reaction weights and effects vary by issue profile.",
        "thirdPartyReactionRule": "THIRD_PARTY can use opposition-compatible and neutral reactions."
    },
    "newsItems": ITEMS_2006_2010
}

review_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "review")
os.makedirs(review_dir, exist_ok=True)

path_2001 = os.path.join(review_dir, "uttar_pradesh_2001_news.json")
path_2006 = os.path.join(review_dir, "uttar_pradesh_2006_news.json")

with open(path_2001, "w", encoding="utf-8") as f:
    json.dump(data_2001, f, indent=2, ensure_ascii=False)
print(f"Successfully compiled and saved to {path_2001}")

with open(path_2006, "w", encoding="utf-8") as f:
    json.dump(data_2006, f, indent=2, ensure_ascii=False)
print(f"Successfully compiled and saved to {path_2006}")
