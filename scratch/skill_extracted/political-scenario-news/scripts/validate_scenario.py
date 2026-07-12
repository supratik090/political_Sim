#!/usr/bin/env python3
"""
Validate a scenario news JSON file against the political-scenario-news schema.

Usage:
    python3 validate_scenario.py <path/to/scenario.json>

Exits non-zero and prints every problem found if validation fails (it doesn't stop
at the first error — you get the full list to fix in one pass).
"""

import json
import re
import sys
from datetime import date

MONTH_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
VALID_ROLE_SETS = [
    {"GOVERNMENT"},
    {"OPPOSITION", "THIRD_PARTY"},
    {"GOVERNMENT", "OPPOSITION", "THIRD_PARTY"},
]
EFFECT_FIELDS = ["partyMorale", "corruptionScore", "mediaImage", "publicSupport"]
EXPECTED_SUFFIXES = ["gov_action", "opp_demands", "joint_forum", "no_comment"]

# Known boilerplate/template phrases from the old placeholder-style generation.
# If any reaction text or badOutcome contains one of these near-verbatim, it's a
# strong signal the item was templated instead of written specifically for that
# event. Matched case-insensitively as substrings.
BOILERPLATE_PHRASES = [
    "initiate a special government commission to resolve",
    "demand that the government address",
    "provide public subsidies",
    "propose a joint multi-party round table to build consensus on",
    "administrative delays stall the commission",
    "discussions break down due to partisan standoffs",
    "radical subgroups refuse to cooperate",
]

def strip_date_suffix(text):
    """Remove a trailing (YYYY-MM) date tag so month-to-month text can be compared."""
    return re.sub(r"\s*\(\d{4}-\d{2}\)\s*$", "", text or "").strip().lower()


def month_to_index(m):
    y, mo = m.split("-")
    return int(y) * 12 + int(mo)


def months_between(start, end):
    return month_to_index(end) - month_to_index(start) + 1


def check_effects_block(effects, path, errors):
    if not isinstance(effects, dict) or "playerParty" not in effects:
        errors.append(f"{path}: missing 'playerParty' effects block")
        return
    pp = effects["playerParty"]
    for f in EFFECT_FIELDS:
        if f not in pp:
            errors.append(f"{path}.playerParty: missing field '{f}'")
            continue
        v = pp[f]
        if not isinstance(v, int) or isinstance(v, bool):
            errors.append(f"{path}.playerParty.{f}: not an integer ({v!r})")
        elif not (-10 <= v <= 10):
            errors.append(f"{path}.playerParty.{f}: out of range -10..10 ({v})")


def validate(data):
    errors = []
    warnings = []

    for key in ["reviewStatus", "scenarioKey", "period", "sourceNotes", "defaults", "newsItems"]:
        if key not in data:
            errors.append(f"top-level: missing key '{key}'")
    if errors:
        return errors, warnings  # can't safely continue without top-level keys

    period = data["period"]
    for key in ["startMonth", "endMonth", "months"]:
        if key not in period:
            errors.append(f"period: missing key '{key}'")
    if "startMonth" in period and "endMonth" in period:
        if not MONTH_RE.match(period["startMonth"]):
            errors.append(f"period.startMonth: bad format '{period['startMonth']}'")
        if not MONTH_RE.match(period["endMonth"]):
            errors.append(f"period.endMonth: bad format '{period['endMonth']}'")
        if MONTH_RE.match(period["startMonth"]) and MONTH_RE.match(period["endMonth"]):
            expected_months = months_between(period["startMonth"], period["endMonth"])
            if period.get("months") != expected_months:
                errors.append(
                    f"period.months: says {period.get('months')}, "
                    f"but startMonth..endMonth spans {expected_months} months"
                )

    news_items = data["newsItems"]
    if not isinstance(news_items, list) or len(news_items) == 0:
        errors.append("newsItems: must be a non-empty list")
        return errors, warnings

    seen_news_keys = set()
    seen_reaction_keys = set()
    months_seen = []
    title_map = {}          # normalized title -> [newsKey,...]
    description_map = {}    # normalized description -> [newsKey,...]
    reaction_text_map = {}  # normalized reaction text -> [reactionKey,...]

    for i, item in enumerate(news_items):
        tag = f"newsItems[{i}]"
        for key in ["newsKey", "month", "title", "description", "issueTags",
                    "weights", "reactionOptions", "type", "monthTags",
                    "crisisTriggerKey", "crisisDuration"]:
            if key not in item:
                errors.append(f"{tag}: missing key '{key}'")

        nk = item.get("newsKey")
        if nk:
            if nk in seen_news_keys:
                errors.append(f"{tag}: duplicate newsKey '{nk}'")
            seen_news_keys.add(nk)

        norm_title = strip_date_suffix(item.get("title"))
        if norm_title:
            title_map.setdefault(norm_title, []).append(nk or tag)
        norm_desc = strip_date_suffix(item.get("description"))
        if norm_desc:
            description_map.setdefault(norm_desc, []).append(nk or tag)

        m = item.get("month")
        if m:
            if not MONTH_RE.match(m):
                errors.append(f"{tag}.month: bad format '{m}'")
            else:
                months_seen.append(m)
                if "startMonth" in period and "endMonth" in period:
                    if MONTH_RE.match(period["startMonth"]) and MONTH_RE.match(period["endMonth"]):
                        if not (month_to_index(period["startMonth"]) <= month_to_index(m) <= month_to_index(period["endMonth"])):
                            errors.append(f"{tag}.month: '{m}' falls outside period range")

        if item.get("monthTags") != [m]:
            warnings.append(f"{tag}.monthTags: expected ['{m}'], got {item.get('monthTags')!r}")

        if item.get("type") == "crisis":
            if item.get("crisisTriggerKey") in (None, ""):
                errors.append(f"{tag}: type is 'crisis' but crisisTriggerKey is null/empty")
            if not isinstance(item.get("crisisDuration"), int) or item.get("crisisDuration", 0) <= 2:
                warnings.append(f"{tag}: crisis item's crisisDuration should usually be > 2")
        elif item.get("type") == "external":
            if item.get("crisisTriggerKey") is not None:
                warnings.append(f"{tag}: type is 'external' but crisisTriggerKey is not null")

        reactions = item.get("reactionOptions", [])
        if len(reactions) != 4:
            errors.append(f"{tag}.reactionOptions: expected exactly 4, got {len(reactions)}")

        found_suffixes = set()
        for j, r in enumerate(reactions):
            rtag = f"{tag}.reactionOptions[{j}]"
            for key in ["reactionKey", "text", "roleAllowed", "effects",
                        "hiddenEffects", "risk", "weight"]:
                if key not in r:
                    errors.append(f"{rtag}: missing key '{key}'")

            rk = r.get("reactionKey", "")
            if rk in seen_reaction_keys:
                errors.append(f"{rtag}: duplicate reactionKey '{rk}'")
            seen_reaction_keys.add(rk)

            rtext = (r.get("text") or "").strip()
            if rtext:
                reaction_text_map.setdefault(rtext.lower(), []).append(rk or rtag)
            for phrase in BOILERPLATE_PHRASES:
                if phrase in rtext.lower():
                    errors.append(
                        f"{rtag}.text: contains known boilerplate phrase "
                        f"('{phrase}') — rewrite this reaction to be specific to "
                        f"the actual event and the real party involved"
                    )
            bad_outcome = (r.get("risk") or {}).get("badOutcome", "") or ""
            for phrase in BOILERPLATE_PHRASES:
                if phrase in bad_outcome.lower():
                    errors.append(
                        f"{rtag}.risk.badOutcome: contains known boilerplate phrase "
                        f"('{phrase}') — write a specific failure mode for this event"
                    )

            matched_suffix = None
            for suf in EXPECTED_SUFFIXES:
                if suf in rk:
                    matched_suffix = suf
                    break
            if matched_suffix:
                found_suffixes.add(matched_suffix)
            else:
                errors.append(f"{rtag}.reactionKey: doesn't contain any of {EXPECTED_SUFFIXES}")

            roles = set(r.get("roleAllowed", []))
            if roles not in VALID_ROLE_SETS:
                errors.append(f"{rtag}.roleAllowed: {sorted(roles)} is not one of the expected role sets")

            if "effects" in r:
                check_effects_block(r["effects"], rtag + ".effects", errors)

            risk = r.get("risk", {})
            if risk:
                if not (0 <= risk.get("chance", -1) <= 100):
                    errors.append(f"{rtag}.risk.chance: out of range 0-100 ({risk.get('chance')})")
                if "badOutcome" not in risk or not risk["badOutcome"]:
                    errors.append(f"{rtag}.risk: missing/empty badOutcome")
                if "effects" in risk:
                    check_effects_block(risk["effects"], rtag + ".risk.effects", errors)

            w = r.get("weight")
            if not isinstance(w, (int, float)) or w <= 0:
                errors.append(f"{rtag}.weight: must be a positive number ({w!r})")

        missing_suffixes = set(EXPECTED_SUFFIXES) - found_suffixes
        if missing_suffixes:
            errors.append(f"{tag}.reactionOptions: missing reaction types {sorted(missing_suffixes)}")

    for norm_title, keys in title_map.items():
        if len(keys) > 1:
            errors.append(
                f"title repeated across {len(keys)} items (same story reused instead "
                f"of a distinct researched event per month): {keys} — title (date "
                f"stripped): '{norm_title}'"
            )
    for norm_desc, keys in description_map.items():
        if len(keys) > 1:
            errors.append(
                f"description repeated across {len(keys)} items: {keys} — this is "
                f"the recurring-template pattern this skill must avoid"
            )
    for rtext, keys in reaction_text_map.items():
        if len(keys) > 1:
            errors.append(
                f"reaction text identical across {len(keys)} reactions: {keys} — "
                f"'{rtext[:80]}...' — reactions must be specific to each event"
            )

    if len(months_seen) != len(set(months_seen)):
        dupes = sorted({m for m in months_seen if months_seen.count(m) > 1})
        warnings.append(f"newsItems: multiple items share the same month: {dupes} "
                         f"(fine only if the game engine supports >1 news/month)")

    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 validate_scenario.py <path/to/scenario.json>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        sys.exit(1)

    errors, warnings = validate(data)

    if warnings:
        print(f"⚠️  {len(warnings)} warning(s):")
        for w in warnings:
            print(f"   - {w}")
        print()

    if errors:
        print(f"❌ {len(errors)} error(s):")
        for e in errors:
            print(f"   - {e}")
        sys.exit(1)

    n_items = len(data.get("newsItems", []))
    print(f"✅ Valid: {n_items} news items, {n_items * 4} reaction options, no errors.")
    sys.exit(0)


if __name__ == "__main__":
    main()
