import json
import os
import sys

# Ensure we can import from the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bihar_items_2001_2005 import ITEMS_2001_2005
from bihar_items_2006_2010 import ITEMS_2006_2010

def compile_split():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    review_dir = os.path.join(base_dir, "review")
    os.makedirs(review_dir, exist_ok=True)

    # 2001-2005 compilation
    data_2001 = {
        "reviewStatus": "approved",
        "scenarioKey": "bihar_2001",
        "period": {
            "startMonth": "2001-01",
            "endMonth": "2005-12",
            "months": 60
        },
        "sourceNotes": "Bihar 2001 scenario split news items (2001-01 to 2005-12)",
        "defaults": {
            "weights": {
                "baseSelectionWeight": 1.0,
                "reactionProfile": "default"
            }
        },
        "newsItems": ITEMS_2001_2005
    }

    # 2006-2010 compilation
    data_2006 = {
        "reviewStatus": "approved",
        "scenarioKey": "bihar_2006",
        "period": {
            "startMonth": "2006-01",
            "endMonth": "2010-12",
            "months": 60
        },
        "sourceNotes": "Bihar 2006 scenario split news items (2006-01 to 2010-12)",
        "defaults": {
            "weights": {
                "baseSelectionWeight": 1.0,
                "reactionProfile": "default"
            }
        },
        "newsItems": ITEMS_2006_2010
    }

    file_2001_path = os.path.join(review_dir, "bihar_2001_news.json")
    file_2006_path = os.path.join(review_dir, "bihar_2006_news.json")

    with open(file_2001_path, "w", encoding="utf-8") as f:
        json.dump(data_2001, f, indent=2, ensure_ascii=False)
    print(f"Compiled and saved {file_2001_path}")

    with open(file_2006_path, "w", encoding="utf-8") as f:
        json.dump(data_2006, f, indent=2, ensure_ascii=False)
    print(f"Compiled and saved {file_2006_path}")

if __name__ == "__main__":
    compile_split()
