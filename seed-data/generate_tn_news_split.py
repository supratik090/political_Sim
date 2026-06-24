import json
import os
import sys

# Ensure seed-data is in the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from tn_items_2001_2005 import ITEMS_2001_2005
    from tn_items_2006_2010 import ITEMS_2006_2010
except Exception as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

print(f"Loaded {len(ITEMS_2001_2005)} news items for Tamil Nadu 2001-2005")
print(f"Loaded {len(ITEMS_2006_2010)} news items for Tamil Nadu 2006-2010")

# Compiling Tamil Nadu 2001
data_2001 = {
    "reviewStatus": "draft_for_review_not_inserted",
    "scenarioKey": "tamil_nadu_2001",
    "period": {
        "startMonth": "2001-01",
        "endMonth": "2005-12",
        "months": 60
    },
    "sourceNotes": [
        "Historical-inspired, fictionalized for gameplay; does not use real party names in playable text.",
        "Covers 2001-2005 Tamil Nadu events with expanded categories: corruption/scams, environment, welfare, health, and law & order.",
        "Key anchors include PMK sub-quota push, 2001 AIADMK victory, Karunanidhi's arrest, OPS's first CM term, POTA arrests, government employee strike, killing of Veerappan, Kanchi Seer arrest, and the 2004 Tsunami."
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

# Compiling Tamil Nadu 2006
data_2006 = {
    "reviewStatus": "draft_for_review_not_inserted",
    "scenarioKey": "tamil_nadu_2006",
    "period": {
        "startMonth": "2006-01",
        "endMonth": "2010-12",
        "months": 60
    },
    "sourceNotes": [
        "Historical-inspired, fictionalized for gameplay; does not use real party names in playable text.",
        "Covers 2006-2010 Tamil Nadu events with expanded categories: corruption/scams, infrastructure, welfare, health, and law & order.",
        "Key anchors include 2006 assembly hung polls, DMK minority cabinet, free color TV and Rs 2/kg rice rollouts, Hogenakkal water row, Madurai newspaper office attack, Sethusamudram row, Sri Lankan civil war protests, Stalin's Deputy CM promotion, Semmozhi conference, Pennagaram by-election, and 2G spectrum controversy."
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

path_2001 = os.path.join(review_dir, "tamil_nadu_2001_news.json")
path_2006 = os.path.join(review_dir, "tamil_nadu_2006_news.json")

with open(path_2001, "w", encoding="utf-8") as f:
    json.dump(data_2001, f, indent=2, ensure_ascii=False)
print(f"Successfully compiled and saved to {path_2001}")

with open(path_2006, "w", encoding="utf-8") as f:
    json.dump(data_2006, f, indent=2, ensure_ascii=False)
print(f"Successfully compiled and saved to {path_2006}")
