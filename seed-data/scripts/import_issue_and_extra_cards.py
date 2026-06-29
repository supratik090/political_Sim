import argparse
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEFAULT_API_BASE_URL = "http://localhost:7810"


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


def delete_matching(api_base_url, resource_path, scenario_key, key_field, keys):
    existing = request_json(
        "GET",
        f"{api_base_url}{resource_path}",
        params={"scenarioKey": scenario_key},
    )
    deleted = 0
    for item in existing:
        if item.get(key_field) in keys:
            request_json("DELETE", f"{api_base_url}{resource_path}/{item['id']}")
            deleted += 1
    return deleted


def insert_items(api_base_url, resource_path, scenario_key, items):
    inserted = 0
    for item in items:
        payload = dict(item)
        payload["scenarioKey"] = scenario_key
        payload.pop("id", None)
        request_json("POST", f"{api_base_url}{resource_path}", json=payload)
        inserted += 1
    return inserted


def main():
    parser = argparse.ArgumentParser(description="Import reviewed monthly issues and extra funding cards.")
    parser.add_argument("--api-base-url", default=DEFAULT_API_BASE_URL)
    parser.add_argument("--scenario-key", default="default")
    parser.add_argument("--issues-file", default="review/default_Monthly_issues.json")
    parser.add_argument("--cards-file", default="review/west_bengal_2000_extra_funding_cards_review.json")
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent
    issues_data = json.loads((base_dir / args.issues_file).read_text())
    cards_data = json.loads((base_dir / args.cards_file).read_text())

    issues = issues_data["issueItems"]
    cards = cards_data["cards"]

    request_json("GET", f"{args.api_base_url}/api/admin/scenarios")

    deleted_issues = delete_matching(
        args.api_base_url,
        "/api/admin/issues",
        args.scenario_key,
        "issueKey",
        {issue["issueKey"] for issue in issues},
    )
    inserted_issues = insert_items(args.api_base_url, "/api/admin/issues", args.scenario_key, issues)

    deleted_cards = delete_matching(
        args.api_base_url,
        "/api/admin/cards",
        args.scenario_key,
        "cardKey",
        {card["cardKey"] for card in cards},
    )
    inserted_cards = insert_items(args.api_base_url, "/api/admin/cards", args.scenario_key, cards)

    print(f"Issues: deleted {deleted_issues}, inserted {inserted_issues}")
    print(f"Extra cards: deleted {deleted_cards}, inserted {inserted_cards}")


if __name__ == "__main__":
    main()
