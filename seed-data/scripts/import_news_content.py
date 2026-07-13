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


def replace_collection(api_base_url, resource_path, scenario_key, items):
    existing = request_json(
        "GET",
        f"{api_base_url}{resource_path}",
        params={"scenarioKey": scenario_key},
    )
    for item in existing:
        request_json("DELETE", f"{api_base_url}{resource_path}/{item['id']}")

    created = []
    for item in items:
        payload = dict(item)
        payload["scenarioKey"] = scenario_key
        payload.pop("id", None)
        created.append(request_json("POST", f"{api_base_url}{resource_path}", json=payload))

    return len(existing), len(created)


def main():
    parser = argparse.ArgumentParser(description="Import reviewed cards/news into MongoDB via the Spring backend.")
    parser.add_argument("scenario_key", help="The scenario key (e.g. haryana_2001)")
    parser.add_argument("--api-base-url", default=DEFAULT_API_BASE_URL)
    parser.add_argument("--news-file", default=None)
    args = parser.parse_args()

    scenario_key = args.scenario_key
    news_file = args.news_file if args.news_file else f"../review/{scenario_key}_news.json"

    base_dir = Path(__file__).resolve().parent
    news_data = json.loads((base_dir / news_file).read_text())


    deleted_news, created_news = replace_collection(
        args.api_base_url,
        "/api/admin/news",
        scenario_key,
        news_data["newsItems"],
    )

    print(f"News: deleted {deleted_news}, inserted {created_news}")


if __name__ == "__main__":
    main()
