import json
import os
import sys

# Ensure we can import from the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from goa_items_2001_2005 import ITEMS_2001_2005 as goa_2001
from goa_items_2006_2010 import ITEMS_2006_2010 as goa_2006

from delhi_items_2001_2005 import ITEMS_2001_2005 as delhi_2001
from delhi_items_2006_2010 import ITEMS_2006_2010 as delhi_2006

from ap_items_2001_2005 import ITEMS_2001_2005 as ap_2001
from ap_items_2006_2010 import ITEMS_2006_2010 as ap_2006

from kerala_items_2001_2005 import ITEMS_2001_2005 as kerala_2001
from kerala_items_2006_2010 import ITEMS_2006_2010 as kerala_2006

def compile_state(review_dir, scenario_key, items, start_year, end_year, state_name):
    data = {
        "reviewStatus": "approved",
        "scenarioKey": scenario_key,
        "period": {
            "startMonth": f"{start_year}-01",
            "endMonth": f"{end_year}-12",
            "months": 60
        },
        "sourceNotes": f"{state_name} {start_year} scenario split news items ({start_year}-01 to {end_year}-12)",
        "defaults": {
            "weights": {
                "baseSelectionWeight": 1.0,
                "reactionProfile": "default"
            }
        },
        "newsItems": items
    }
    filepath = os.path.join(review_dir, f"{scenario_key}_news.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Compiled and saved {filepath}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    review_dir = os.path.join(base_dir, "review")
    os.makedirs(review_dir, exist_ok=True)

    # 1. Goa
    compile_state(review_dir, "goa_2001", goa_2001, 2001, 2005, "Goa")
    compile_state(review_dir, "goa_2006", goa_2006, 2006, 2010, "Goa")

    # 2. Delhi
    compile_state(review_dir, "delhi_2001", delhi_2001, 2001, 2005, "Delhi")
    compile_state(review_dir, "delhi_2006", delhi_2006, 2006, 2010, "Delhi")

    # 3. Andhra Pradesh
    compile_state(review_dir, "andhra_pradesh_2001", ap_2001, 2001, 2005, "Andhra Pradesh")
    compile_state(review_dir, "andhra_pradesh_2006", ap_2006, 2006, 2010, "Andhra Pradesh")

    # 4. Kerala
    compile_state(review_dir, "kerala_2001", kerala_2001, 2001, 2005, "Kerala")
    compile_state(review_dir, "kerala_2006", kerala_2006, 2006, 2010, "Kerala")

if __name__ == "__main__":
    main()
