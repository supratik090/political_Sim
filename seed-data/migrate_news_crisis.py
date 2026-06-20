import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

DEFAULT_API_BASE_URL = "http://localhost:7810"

# Specific known crises to configure
KNOWN_CRISES = {
    "wb2001_2001_01_chit_fund_collapse": {
        "crisisTriggerKey": "scam_panic",
        "crisisDuration": 3
    },
    "wb2001_2001_04_ration_dealer_scam": {
        "crisisTriggerKey": "scam_panic",
        "crisisDuration": 2
    },
    "wb2001_2001_05_cyclone_relief_mismanagement": {
        "crisisTriggerKey": "drought_crisis",
        "crisisDuration": 3
    }
}

def request_json(method, url, **kwargs):
    params = kwargs.get("params")
    if params:
        url = f"{url}?{urlencode(params)}"

    body = None
    headers = {}
    if "json" in kwargs:
        body = json.dumps(kwargs["json"]).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = Request(url, data=body, headers=headers, method=method)
    try:
        with urlopen(request, timeout=20) as response:
            content = response.read()
            if content:
                return json.loads(content.decode("utf-8"))
            return None
    except HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{method} {url} failed with HTTP {exc.code}: {details}") from exc
    except URLError as exc:
        raise RuntimeError(f"{method} {url} failed: {exc.reason}") from exc

def update_json_files(review_dir):
    json_files = list(review_dir.glob("*.json"))
    updated_files_count = 0
    updated_news_count = 0

    for file_path in json_files:
        try:
            data = json.loads(file_path.read_text())
        except Exception:
            continue
        
        # Check if it has newsItems
        if "newsItems" not in data:
            continue
            
        is_modified = False
        for item in data["newsItems"]:
            news_key = item.get("newsKey")
            
            # Default values if missing
            if "crisisTriggerKey" not in item:
                item["crisisTriggerKey"] = None
                is_modified = True
            if "crisisDuration" not in item or item["crisisDuration"] <= 0:
                item["crisisDuration"] = 2
                is_modified = True
                
            # Overwrite for known crises
            if news_key in KNOWN_CRISES:
                item["crisisTriggerKey"] = KNOWN_CRISES[news_key]["crisisTriggerKey"]
                item["crisisDuration"] = KNOWN_CRISES[news_key]["crisisDuration"]
                is_modified = True
                updated_news_count += 1
                
        if is_modified:
            file_path.write_text(json.dumps(data, indent=2))
            updated_files_count += 1
            
    print(f"Updated {updated_files_count} local JSON review files. Customized {updated_news_count} news items.")

def update_mongodb():
    print(f"Connecting to Spring Boot Admin REST API at {DEFAULT_API_BASE_URL}...")
    try:
        news_items = request_json("GET", f"{DEFAULT_API_BASE_URL}/api/admin/news")
    except Exception as e:
        print(f"Error fetching active news collection. Is the Spring Boot backend running? Detail: {e}")
        return

    print(f"Fetched {len(news_items)} news definitions from MongoDB.")
    updated_count = 0
    custom_count = 0

    for item in news_items:
        news_key = item.get("newsKey")
        news_id = item.get("id")
        if not news_id:
            continue

        item["crisisTriggerKey"] = None
        item["crisisDuration"] = 2

        if news_key in KNOWN_CRISES:
            item["crisisTriggerKey"] = KNOWN_CRISES[news_key]["crisisTriggerKey"]
            item["crisisDuration"] = KNOWN_CRISES[news_key]["crisisDuration"]
            custom_count += 1

        try:
            request_json("PUT", f"{DEFAULT_API_BASE_URL}/api/admin/news/{news_id}", json=item)
            updated_count += 1
        except Exception as e:
            print(f"Failed to update news key {news_key}: {e}")

    print(f"Successfully migrated {updated_count} news definitions in MongoDB via REST. Applied custom crisis rules to {custom_count} items.")

def main():
    base_dir = Path(__file__).resolve().parent
    review_dir = base_dir / "review"
    
    # 1. Update JSON files first
    update_json_files(review_dir)
    
    # 2. Update MongoDB via REST API
    update_mongodb()

if __name__ == "__main__":
    main()
