def risk(chance, bad, eff):
    return {"chance": chance, "badOutcome": bad, "effects": {"playerParty": eff}}

def reaction(suffix, text, roles, eff, hidden, risk_obj=None, weight=1.0):
    r = {
        "reactionKey": None,
        "text": text,
        "roleAllowed": roles,
        "effects": {"playerParty": eff},
        "hiddenEffects": {"publicMemory": hidden},
        "risk": risk_obj if risk_obj is not None else {},
        "weight": weight,
    }
    return suffix, r

def no_comment(suffix="no_comment", morale=-2, corr=1, media=-3, support=-4,
               hidden=None, weight=0.2):
    if hidden is None:
        hidden = {"issueIgnoredMemory": 2}
    r = {
        "reactionKey": None,
        "text": "No comment.",
        "roleAllowed": ["GOVERNMENT", "OPPOSITION", "THIRD_PARTY"],
        "effects": {"playerParty": {
            "partyMorale": morale, "corruptionScore": corr,
            "mediaImage": media, "publicSupport": support
        }},
        "hiddenEffects": {"publicMemory": hidden},
        "risk": {},
        "weight": weight,
    }
    return suffix, r

def make_news(key, month, title, desc, tags, base_w, profile, reactions,
              crisis_key=None, crisis_dur=2):
    opts = []
    for suffix, r in reactions:
        r = dict(r)
        r["reactionKey"] = f"{key}__{suffix}"
        opts.append(r)
    return {
        "newsKey": key,
        "month": month,
        "title": title,
        "description": desc,
        "issueTags": tags,
        "weights": {"baseSelectionWeight": base_w, "reactionProfile": profile},
        "reactionOptions": opts,
        "type": "external",
        "monthTags": [month],
        "crisisTriggerKey": crisis_key,
        "crisisDuration": crisis_dur,
    }

def eff(morale, corr, media, support):
    return {"partyMorale": morale, "corruptionScore": corr, "mediaImage": media, "publicSupport": support}