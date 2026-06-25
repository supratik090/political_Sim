import json

SRC = "default_Monthly_issues.json"
OUT = "default_Monthly_issues_v1.json"

with open(SRC) as f:
    data = json.load(f)

items = data["issueItems"]
existing_keys = {i["issueKey"] for i in items}

def eff(coins=0, morale=0, corruption=0, media=0, support=0):
    return {"selfParty": {"coins": coins, "partyMorale": morale, "corruptionScore": corruption,
                           "mediaImage": media, "publicSupport": support}}

def delayed(minT, maxT, chance, commentary, **kw):
    return [{"minTurns": minT, "maxTurns": maxT, "chance": chance, "effects": eff(**kw), "commentary": commentary}]

def risk(chance, bad, **kw):
    return {"chance": chance, "badOutcome": bad, "effects": eff(**kw)}

def opt(key, text, coins_effect, **kw):
    morale = kw.pop("morale", 0); corruption = kw.pop("corruption", 0)
    media = kw.pop("media", 0); support = kw.pop("support", 0)
    d = kw.pop("delayed", None); r = kw.pop("risk", None)
    o = {"optionKey": key, "text": text, "cost": -coins_effect,
         "effects": eff(coins_effect, morale, corruption, media, support),
         "delayedEffects": d if d else []}
    if r:
        o["risk"] = r
    return o

def issue(key, roles, category, title, description, weight, options):
    assert key not in existing_keys, f"duplicate key {key}"
    existing_keys.add(key)
    return {"issueKey": key, "roleAllowed": roles, "category": category, "title": title,
            "description": description, "weight": weight, "options": options}

GOV = ["GOVERNMENT"]
OPP = ["OPPOSITION", "THIRD_PARTY"]

NEW = []

# ===========================================================================
# 1. RUMOUR MILL
# ===========================================================================
NEW.append(issue("gov_resignation_rumor_viral", GOV, "rumor_management",
    "Wild rumour claims the Chief Minister is about to resign",
    "An anonymous post claiming the CM is preparing to quit spreads rapidly with zero official confirmation behind it.",
    0.8, [
        opt("swift_official_denial", "Issue an immediate, firm denial through the official spokesperson.", -1, media=1,
            risk=risk(18, "Some read the swift denial itself as proof something is brewing.", media=-2, support=-1)),
        opt("ignore_and_let_die", "Make no comment at all, betting the rumour fades on its own.", 0, morale=-1, media=-2, support=-2,
            delayed=delayed(1, 3, 38, "The unanswered rumour keeps resurfacing on talk shows.", media=-1)),
        opt("counter_with_public_appearance", "Schedule a high-visibility public event to show the leader is firmly in charge.", -5, morale=2, media=3, support=2),
        opt("trace_and_expose_source", "Launch a hunt to identify and publicly expose whoever started the rumour.", -3, morale=1,
            risk=risk(22, "The source turns out to be a disgruntled party insider, raising new questions.", morale=-2, media=-2)),
    ]))

NEW.append(issue("opp_leader_resignation_rumor", OPP, "rumor_management",
    "Rumour mill claims the opposition's top leader wants out",
    "An anonymous post alleging the opposition chief is fed up and ready to quit politics spreads fast on social media.",
    0.8, [
        opt("swift_official_denial", "Issue an immediate, firm denial through the party's official channel.", -1, media=1,
            risk=risk(18, "The hurried denial is read by some as confirmation of internal trouble.", media=-2, support=-1)),
        opt("ignore_and_let_die", "Make no comment, betting the rumour quietly fades away.", 0, morale=-1, media=-2, support=-2,
            delayed=delayed(1, 3, 38, "The unanswered rumour keeps resurfacing in panel debates.", media=-1)),
        opt("counter_with_public_appearance", "Schedule a high-energy rally to show the leader is firmly committed.", -4, morale=2, media=3, support=2),
        opt("trace_and_expose_source", "Launch a hunt to expose whoever started the rumour.", -2, morale=1,
            risk=risk(22, "The source turns out to be a ruling-party troll account, fuelling a fresh row.", media=-2)),
    ]))

# ===========================================================================
# 2. GAME SHOW APPEARANCE
# ===========================================================================
NEW.append(issue("gov_leader_game_show_appearance", GOV, "media_image",
    "Chief Minister is invited onto a popular celebrity game show",
    "A wildly popular celebrity quiz show wants the CM as a special guest -- huge visibility, but real risk of an awkward on-air moment.",
    0.7, [
        opt("go_all_in_charm_offensive", "Accept enthusiastically and prep hard to be warm, funny, and relatable on air.", -6, morale=3, media=5, support=4,
            risk=risk(24, "A planted 'gotcha' question catches the leader off guard on live TV.", media=-4, support=-2)),
        opt("accept_but_play_it_safe", "Accept the invite but stick strictly to pre-approved talking points.", -3, morale=1, media=2, support=1),
        opt("decline_politely", "Decline citing a packed schedule, avoiding any on-air risk entirely.", 0, morale=-1, media=-1, support=-1),
        opt("send_a_deputy_instead", "Send a popular junior leader in the CM's place to test the format first.", -2, morale=1, media=1, support=1,
            delayed=delayed(1, 3, 42, "The deputy's relaxed charm on air builds a following of their own.", support=1)),
    ]))

NEW.append(issue("opp_leader_game_show_appearance", OPP, "media_image",
    "Opposition's top leader gets invited onto a hit celebrity game show",
    "A nationally loved game show wants the opposition chief as a guest -- a rare chance to look human and relatable to a huge audience.",
    0.7, [
        opt("go_all_in_charm_offensive", "Accept enthusiastically and prep hard to be warm and likeable on screen.", -5, morale=3, media=5, support=4,
            risk=risk(24, "A loaded question catches the leader off guard, and the clip spreads fast.", media=-4, support=-2)),
        opt("accept_but_play_it_safe", "Accept the invite but stick to safe, rehearsed answers only.", -2, morale=1, media=2, support=1),
        opt("decline_politely", "Decline citing campaign commitments, avoiding any on-air risk.", 0, morale=-1, media=-1, support=-1),
        opt("send_a_deputy_instead", "Send a popular younger leader instead, to test the waters first.", -1, morale=1, media=1, support=1,
            delayed=delayed(1, 3, 42, "The deputy's easy charm wins over a new slice of viewers.", support=1)),
    ]))

# ===========================================================================
# 3. MEDIA BLUFF STORY
# ===========================================================================
NEW.append(issue("gov_media_bluff_story", GOV, "media_narrative",
    "A rival news channel runs a wildly exaggerated story about the government",
    "A sensational, mostly-unverified report claims a flagship scheme is 'secretly bankrupt,' and it's trending before anyone can check the facts.",
    0.8, [
        opt("demand_on_air_correction", "Send officials to demand the channel issue an on-air correction with hard data.", -3, morale=1, media=3, support=1,
            risk=risk(20, "The channel resists, turning the correction demand into a fresh standoff story.", media=-2)),
        opt("release_counter_data_dossier", "Publish a detailed counter-data dossier through every other media outlet.", -6, morale=1, media=2, support=2),
        opt("sue_for_defamation", "File a formal defamation notice against the channel.", -8, morale=2, media=-1,
            risk=risk(26, "The legal threat is painted as an attack on press freedom.", media=-4, support=-2)),
        opt("ignore_the_bluff", "Refuse to dignify the story with any official response.", 0, morale=-1, media=-2, support=-2),
    ]))

NEW.append(issue("opp_media_bluff_story", OPP, "media_narrative",
    "A friendly channel runs a wildly exaggerated story favouring the opposition",
    "A sympathetic news channel airs a sensational, barely-verified claim that the government is about to collapse -- great optics, shaky facts.",
    0.8, [
        opt("amplify_without_checking", "Amplify the story across party channels while it's hot, facts be damned.", -2, morale=3, media=2, support=2,
            risk=risk(30, "The claim is debunked publicly, and the party is blamed for spreading it.", media=-4, support=-3)),
        opt("verify_before_sharing", "Quietly verify the claim with the channel's sources before sharing anything officially.", -2, morale=1, media=0, support=0),
        opt("distance_from_the_story", "Publicly note the party has no role in the story and cannot vouch for it.", 0, morale=0, media=0, support=-1),
        opt("use_it_to_raise_real_questions", "Use the story as a hook to raise genuine, separately-verified questions about governance.", -4, morale=1, media=2, support=1),
    ]))

# ===========================================================================
# 4. LEADER GOOF-UP
# ===========================================================================
NEW.append(issue("gov_leader_goof_up_viral", GOV, "leadership_image",
    "Chief Minister fumbles a key statistic on live television",
    "During a primetime interview, the CM cites a wildly wrong figure for a flagship scheme, and clips of the slip are already circulating.",
    0.8, [
        opt("own_it_with_humor", "Publicly laugh it off and issue the correct figure with a self-deprecating joke.", -1, morale=2, media=2, support=1),
        opt("issue_quiet_correction", "Have the office quietly issue a written correction without further comment.", 0, media=0, support=-1),
        opt("blame_aides_for_briefing", "Blame the briefing team for feeding the wrong number.", -1, morale=-2, media=-2, support=-2,
            risk=risk(20, "The blamed aide pushes back publicly, turning it into an internal spat.", morale=-2)),
        opt("double_down_on_wrong_number", "Insist the original number was correct despite the contradiction.", 0, morale=1, media=-4, support=-3,
            risk=risk(32, "Independent fact-checkers publicly debunk the insistence in detail.", media=-3, support=-2)),
    ]))

NEW.append(issue("opp_leader_goof_up_viral", OPP, "leadership_image",
    "Opposition leader botches a key fact during a press conference",
    "While slamming a government scheme, the opposition leader cites a completely wrong figure, and the slip is already a trending clip.",
    0.8, [
        opt("own_it_with_humor", "Laugh it off, correct the number on the spot, and move on confidently.", -1, morale=2, media=2, support=1),
        opt("issue_quiet_correction", "Quietly issue a written correction without further comment.", 0, media=0, support=-1),
        opt("blame_staff_for_briefing", "Blame the research team for feeding the wrong figure.", -1, morale=-2, media=-2, support=-2,
            risk=risk(20, "The blamed staffer pushes back publicly, turning it into an internal row.", morale=-2)),
        opt("double_down_on_wrong_number", "Insist the figure was right despite the pushback.", 0, morale=1, media=-4, support=-3,
            risk=risk(32, "Fact-checkers publicly and thoroughly debunk the insistence.", media=-3, support=-2)),
    ]))

# ===========================================================================
# 5. BUSINESS OPPORTUNITY -- MEGA INVESTMENT
# ===========================================================================
NEW.append(issue("gov_mega_investment_proposal", GOV, "industry_investment",
    "A global industrial group proposes a multi-thousand-crore investment",
    "A major manufacturer has proposed a flagship plant in the state, contingent on fast-tracked approvals and incentives.",
    0.9, [
        opt("fast_track_with_incentives", "Fast-track approvals and offer a generous incentive package to seal the deal quickly.", -14, morale=3, media=4, support=3,
            delayed=delayed(2, 5, 48, "The plant's groundbreaking ceremony brings a fresh wave of positive coverage.", media=1, support=1),
            risk=risk(22, "Critics allege the incentives were too generous, smelling of cronyism.", corruption=3, media=-3)),
        opt("negotiate_harder_on_terms", "Push back to negotiate better terms for the state before agreeing.", -4, morale=1, media=1, support=1,
            risk=risk(22, "The investor walks away to a more accommodating neighbouring state.", media=-2, support=-2)),
        opt("open_competitive_bidding", "Open the opportunity to competitive bidding among multiple investors.", -2, media=2, support=1),
        opt("decline_citing_environment_concerns", "Decline the proposal over environmental and land-acquisition concerns.", 0, morale=-1, support=-1),
    ]))

NEW.append(issue("opp_mega_investment_pledge", OPP, "industry_investment",
    "A global industrial group publicly backs the opposition's economic vision",
    "A major industrial group signals it would invest heavily in the state under a different government, citing the current policy climate.",
    0.9, [
        opt("embrace_publicly", "Publicly welcome and amplify the endorsement as proof of a better economic vision.", -5, morale=3, media=4, support=3,
            risk=risk(24, "The ruling party questions the legitimacy of an unelected party getting business backing.", media=-2)),
        opt("ask_for_specifics", "Ask the investor to put concrete numbers on record rather than vague support.", -1, morale=1, media=1, support=1),
        opt("low_key_acknowledgement", "Acknowledge it quietly without making it a campaign centrepiece.", 0, morale=1),
        opt("decline_for_neutrality", "Decline public association, citing the need to stay above corporate lobbying.", 0, morale=-1, support=-1),
    ]))

# ===========================================================================
# 6. DEEPFAKE VIDEO SCANDAL
# ===========================================================================
NEW.append(issue("gov_deepfake_video_scandal", GOV, "scandal_crisis",
    "A convincing deepfake video shows the CM 'admitting' to a scam",
    "A technically sophisticated deepfake, appearing to show the Chief Minister confessing to corruption, is spreading before anyone can verify it.",
    0.9, [
        opt("rapid_forensic_debunking", "Commission an immediate forensic analysis and publish proof of the fabrication.", -7, morale=1, media=3, support=2,
            delayed=delayed(1, 3, 55, "The clear technical debunking restores most of the lost ground.", support=1)),
        opt("legal_action_against_platforms", "Demand platforms take the video down immediately and pursue its creators legally.", -5, morale=1, media=1, support=1),
        opt("counter_with_real_footage", "Release real footage of the same event to expose the manipulation by contrast.", -2, morale=2, media=2, support=2),
        opt("stay_silent_to_avoid_amplifying", "Avoid commenting officially to prevent giving the video more attention.", 0, morale=-2, media=-3, support=-3,
            risk=risk(28, "The silence is read by many as an implicit admission.", media=-3, support=-2)),
    ]))

NEW.append(issue("opp_deepfake_video_scandal", OPP, "scandal_crisis",
    "A convincing deepfake video shows an opposition leader 'taking a bribe'",
    "A realistic deepfake clip appearing to show a senior opposition leader accepting cash is spreading rapidly online.",
    0.9, [
        opt("rapid_forensic_debunking", "Commission an immediate forensic analysis and publish clear proof of the fabrication.", -6, morale=1, media=3, support=2,
            delayed=delayed(1, 3, 55, "The technical debunking restores most of the lost ground.", support=1)),
        opt("legal_action_against_platforms", "Demand platforms remove the clip and pursue its creators legally.", -4, morale=1, media=1, support=1),
        opt("counter_with_real_footage", "Release real footage from the same event to expose the manipulation by contrast.", -2, morale=2, media=2, support=2),
        opt("stay_silent_to_avoid_amplifying", "Avoid commenting to prevent giving the fake clip more oxygen.", 0, morale=-2, media=-3, support=-3,
            risk=risk(28, "The silence is widely read as an implicit admission of guilt.", media=-3, support=-2)),
    ]))

# ===========================================================================
# 7. VIRAL MEME MOCKERY
# ===========================================================================
NEW.append(issue("gov_viral_meme_mockery", GOV, "media_narrative",
    "A savage meme mocking the government goes viral",
    "A cleverly edited meme mocking a recent government decision has exploded online, with even neutral users sharing it for laughs.",
    0.7, [
        opt("laugh_along_publicly", "Have the official handle respond with good humour, defusing it with self-aware wit.", -1, morale=2, media=2, support=1),
        opt("ignore_completely", "Take no notice and let the meme's moment pass.", 0, morale=-1, media=-1, support=-1),
        opt("counter_meme_campaign", "Launch a counter-meme campaign mocking the opposition in turn.", -3, morale=2, media=1,
            risk=risk(22, "The counter-campaign is seen as thin-skinned, amplifying the original meme further.", media=-2)),
        opt("request_platform_takedown", "Formally request platforms take the meme down as misleading.", -2, media=-3, support=-2,
            risk=risk(30, "The takedown request becomes the bigger story, mocked as censorship.", media=-3)),
    ]))

NEW.append(issue("opp_viral_meme_mockery", OPP, "media_narrative",
    "A savage meme mocking the opposition goes viral",
    "A cleverly edited meme mocking a recent opposition statement has exploded online, even drawing laughs from sympathisers.",
    0.7, [
        opt("laugh_along_publicly", "Respond with good-natured humour, defusing the meme with self-aware wit.", -1, morale=2, media=2, support=1),
        opt("ignore_completely", "Take no notice and let the meme's moment pass.", 0, morale=-1, media=-1, support=-1),
        opt("counter_meme_campaign", "Launch a counter-meme campaign targeting the ruling party in return.", -2, morale=2, media=1,
            risk=risk(22, "The counter-campaign looks thin-skinned and keeps the original meme alive.", media=-2)),
        opt("request_platform_takedown", "Formally request platforms take the meme down as misleading.", -1, media=-3, support=-2,
            risk=risk(30, "The request itself becomes the story, mocked as an attempt at censorship.", media=-3)),
    ]))

# ===========================================================================
# 8. LEAKED PARTY WHATSAPP CHAT
# ===========================================================================
NEW.append(issue("gov_leaked_party_whatsapp_chat", GOV, "party_discipline",
    "A leaked internal WhatsApp chat embarrasses the party",
    "Screenshots from an internal party group, full of candid and unflattering remarks about voters and allies, have leaked online.",
    0.8, [
        opt("apologize_and_discipline", "Issue a public apology and discipline those responsible for the remarks.", -2, morale=-2, corruption=-1, media=2, support=1),
        opt("claim_chat_was_doctored", "Claim the screenshots were selectively edited or fabricated.", 0, morale=1, media=-2, support=-2,
            risk=risk(34, "The original, unedited messages surface, proving the claim false.", media=-4, support=-3)),
        opt("tighten_internal_communication_rules", "Quietly tighten internal communication protocols going forward.", -1, morale=-1, media=-1, support=-1),
        opt("downplay_as_private_banter", "Dismiss it as harmless private banter blown out of proportion.", 0, media=-2, support=-2),
    ]))

NEW.append(issue("opp_leaked_party_whatsapp_chat", OPP, "party_discipline",
    "A leaked internal WhatsApp chat embarrasses the opposition",
    "Screenshots from an internal opposition group, full of unflattering remarks about allies and supporters, have leaked online.",
    0.8, [
        opt("apologize_and_discipline", "Issue a public apology and discipline those responsible.", -2, morale=-2, corruption=-1, media=2, support=1),
        opt("claim_chat_was_doctored", "Claim the screenshots were selectively edited or fabricated.", 0, morale=1, media=-2, support=-2,
            risk=risk(34, "The original, unedited messages surface, proving the claim false.", media=-4, support=-3)),
        opt("tighten_internal_communication_rules", "Quietly tighten internal communication protocols going forward.", -1, morale=-1, media=-1, support=-1),
        opt("downplay_as_private_banter", "Dismiss it as harmless private banter blown out of proportion.", 0, media=-2, support=-2),
    ]))

# ===========================================================================
# 9. ASTROLOGER PREDICTION BUZZ
# ===========================================================================
NEW.append(issue("gov_astrologer_prediction_buzz", GOV, "media_narrative",
    "A popular TV astrologer's election prediction goes viral",
    "A well-known astrologer has predicted a dramatic outcome for the ruling party, and clips of the prediction are being shared everywhere.",
    0.5, [
        opt("embrace_if_favorable", "Publicly welcome the prediction as a sign of confidence.", -1, morale=2, media=1, support=1),
        opt("dismiss_as_superstition", "Dismiss astrology as having no place in serious politics.", 0, media=-1, support=-1),
        opt("stay_neutral_no_comment", "Avoid commenting either way on the prediction.", 0),
        opt("commission_rival_astrologer", "Quietly arrange for a rival astrologer to offer a more favourable counter-prediction.", -4, morale=1, corruption=1, media=-1,
            risk=risk(26, "The obvious counter-prediction stunt draws public ridicule.", media=-3)),
    ]))

NEW.append(issue("opp_astrologer_prediction_buzz", OPP, "media_narrative",
    "A popular TV astrologer's prediction about the opposition goes viral",
    "A well-known astrologer has made a dramatic prediction about the opposition's prospects, and it's the talk of every panel show.",
    0.5, [
        opt("embrace_if_favorable", "Publicly welcome the prediction as a sign of momentum.", -1, morale=2, media=1, support=1),
        opt("dismiss_as_superstition", "Dismiss astrology as having no place in serious politics.", 0, media=-1, support=-1),
        opt("stay_neutral_no_comment", "Avoid commenting either way on the prediction.", 0),
        opt("commission_rival_astrologer", "Quietly arrange for a rival astrologer to offer a more favourable counter-prediction.", -3, morale=1, corruption=1, media=-1,
            risk=risk(26, "The obvious stunt draws public ridicule.", media=-3)),
    ]))

# ===========================================================================
# 10. FOREIGN INVESTOR DELEGATION VISIT
# ===========================================================================
NEW.append(issue("gov_foreign_investor_delegation_visit", GOV, "industry_investment",
    "A high-profile foreign investor delegation tours the state",
    "A delegation from an Asian manufacturing hub is evaluating potential sites in the state against other competing states.",
    0.7, [
        opt("roll_out_red_carpet", "Organise a lavish, highly visible welcome with top leadership personally hosting.", -10, morale=2, media=4, support=3,
            delayed=delayed(2, 5, 45, "Word gets back that the delegation was genuinely impressed.", support=1)),
        opt("low_key_professional_tour", "Keep the visit professional and low-key, letting officials handle logistics.", -3, morale=1, media=1, support=1),
        opt("offer_aggressive_tax_breaks", "Offer an aggressive tax-break package to win the delegation over.", -9, morale=1, media=2, support=1,
            risk=risk(24, "Critics question why incentives weren't offered to local industry first.", media=-2, support=-1)),
        opt("let_the_visit_pass_routinely", "Treat it as a routine visit without any special effort.", -1, media=-1, support=-1,
            risk=risk(26, "The delegation later signs with a rival state that made more effort.", media=-2)),
    ]))

NEW.append(issue("opp_foreign_investor_meeting", OPP, "industry_investment",
    "Opposition leaders hold a closed-door meeting with a visiting investor delegation",
    "The opposition has arranged a private meeting with a touring foreign investor delegation, eager to pitch an alternative governance vision.",
    0.7, [
        opt("publicize_the_meeting", "Publicise the meeting widely as proof of credible alternative leadership.", -4, morale=2, media=3, support=2,
            risk=risk(22, "The ruling party dismisses it as a photo-op with no real substance.", media=-2)),
        opt("keep_it_low_key", "Keep the meeting private and avoid making it a media event.", -1, morale=1),
        opt("present_a_detailed_policy_pitch", "Present a detailed, costed policy pitch to genuinely impress the delegation.", -5, morale=2, media=1, support=1),
        opt("decline_due_to_optics", "Decline the meeting, wary of optics around dealing with corporate interests.", 0, morale=-1, support=-1),
    ]))

with open(OUT_LOG := "checkpoint1_count.txt", "w") as f:
    f.write(str(len(NEW)))

print("Checkpoint 1 -- issues so far:", len(NEW))
