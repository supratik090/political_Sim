"""
insert_2021_scenarios.py
--------------------------
Inserts all 30 Indian state/UT scenarios for the year 2021.
(Telangana included. J&K is now a UT since Oct 2019 — included with
 BJP/LG-administration context vs NC as effective opposition.)

Political accuracy notes (all as of January 2021):
  Andhra Pradesh   – YSRCP (Jagan Reddy; won 2019 with 151/175 — largest-ever AP mandate) vs TDP
  Arunachal        – BJP (Pema Khandu; won 2019 with 41/60 seats) vs INC/NPP
  Assam            – BJP (Sarbananda Sonowal; won 2016; Himanta Sarma became CM post May 2021)
  Bihar            – JD(U)+BJP NDA (Nitish Kumar; won Nov 2020 narrowly, NDA 125/243) vs RJD (Tejashwi)
  Chhattisgarh     – INC (Bhupesh Baghel; won 2018 with 68/90 seats, ended 15 yrs of BJP rule)
  Delhi            – AAP (Arvind Kejriwal; won Feb 2020 with 62/70 seats — second landslide)
  Goa              – BJP (Pramod Sawant; CM since March 2019 after Parrikar's death)
  Gujarat          – BJP (Vijay Rupani; CM since Aug 2016; Bhupendra Patel took over Sep 2021)
  Haryana          – BJP (ML Khattar; won Oct 2019 with JJP support after narrow mandate, 40/90 seats)
  Himachal Pradesh – BJP (Jai Ram Thakur; won 2017 — HP alternation continued, 44/68 seats)
  J&K              – UT under LG since Oct 2019; BJP/Apni Party vs NC (Omar Abdullah) effective opp
  Jharkhand        – JMM (Hemant Soren; won Dec 2019 with JMM+INC+RJD Mahagathbandhan, 47+16 seats)
  Karnataka        – BJP (BS Yediyurappa; full BJP govt since Jul 2019; resigned Jul 2021 → Bommai)
  Kerala           – LDF/CPI-M (Pinarayi Vijayan; won 2016; re-elected May 2021 — historic consecutive)
  Madhya Pradesh   – BJP (Shivraj Chouhan; returned March 2020 after Kamal Nath fell via Jyotiraditya defections)
  Maharashtra      – MVA (Uddhav Thackeray SS+INC+NCP; formed Nov 2019 after BJP-SS post-election split)
  Manipur          – BJP (N. Biren Singh; won 2017; won 2022 re-election; first BJP CM of Manipur)
  Meghalaya        – NPP (Conrad Sangma; won 2018 MDA coalition — first non-INC Meghalaya govt)
  Mizoram          – MNF (Zoramthanga; won 2018 — returned to power defeating INC) vs ZPM
  Nagaland         – NDPP+BJP (Neiphiu Rio; won 2018 after forming NDPP — People's Democratic Alliance)
  Odisha           – BJD (Naveen Patnaik; won 2019 alone with 112/147 seats — 5th consecutive term)
  Punjab           – INC (Amarinder Singh; won 2017 with 77/117; resigned Sep 2021 → Channi)
  Rajasthan        – INC (Ashok Gehlot; won 2018 with 99/200; survived Sachin Pilot 2020 revolt)
  Sikkim           – SKM (Prem Singh Tamang/Golay; won 2019 — ended Chamling's 25-year SDF reign)
  Tamil Nadu       – AIADMK (Edappadi Palaniswami; CM since Feb 2017 after Jaya's Dec 2016 death)
  Telangana        – TRS (KCR; won 2018 in early dissolution snap-poll with 88/119 seats)
  Tripura          – BJP (Biplab Kumar Deb; won 2018 — ended CPI-M's 25-year Left rule, 36/60 seats)
  Uttarakhand      – BJP (Trivendra Singh Rawat; won 2017; resigned March 2021 → Tirath → Dhami Jul 2021)
  Uttar Pradesh    – BJP (Yogi Adityanath; won 2017 with massive 312/403 — biggest UP majority ever)
  West Bengal      – TMC (Mamata Banerjee; won May 2021 with 213/294 against BJP's national push)

COVID-19 context: All scenarios set Jan 2021 — first wave receding, second wave (Apr–May 2021)
looms. Vaccine rollout begins Jan 16, 2021. Every state government's pandemic response
was a defining political issue.

Run: python insert_2021_scenarios.py
Dependencies: pip install pymongo
"""

from datetime import datetime
from pymongo import MongoClient

MONGO_URI  = "mongodb+srv://supratikde090:ztDTTjn5upUs2gai@cluster0.hgdwptz.mongodb.net/political_sim"
DB_NAME    = "political_sim"
COLLECTION = "scenario_definitions"

YDP_STATS = {"coins": 400, "partyMorale": 80, "corruptionScore": 10,
             "mediaImage": 65, "publicSupport": 15}
YDP_PARTY = {
    "partyKey": "ydp", "name": "Youth Development Party (YDP)",
    "startingRole": "THIRD_PARTY", "defaultControllerType": "HUMAN",
    "color": "#D8B4FE", "symbol": "Star", "ideology": "REGIONAL_PRIDE",
    "aiProfile": None, "startingStats": YDP_STATS,
}
RULE_WEIGHTS = {
    "antiIncumbencyGrowthPerTurn": 1.0, "scandalFatigueLimit": 5.0,
    "noConfidenceSupportThreshold": 35.0, "noConfidenceMoraleThreshold": 35.0,
    "electionCoinReductionPercent": 70.0, "publicMemoryDecayPerTurn": 0.4,
}
CLASS      = "com.politicalsim.content.ScenarioDefinition"
START_DATE = datetime(2021, 1, 1)
CYCLE      = 60


def s(morale, corruption, media, support):
    return {"coins": 400, "partyMorale": morale, "corruptionScore": corruption,
            "mediaImage": media, "publicSupport": support}


def party(key, name, role, st, ideology="DEVELOPMENT_FIRST",
          color="#E15554", symbol="Flag"):
    return {"partyKey": key, "name": name, "startingRole": role,
            "defaultControllerType": "COMPUTER", "color": color,
            "symbol": symbol, "ideology": ideology, "aiProfile": None,
            "startingStats": st}


def ud(g, o):
    return max(0, 100 - g["publicSupport"] - o["publicSupport"] - 15)


def build(key, name, desc, state, gname, oname, gkey, okey, gs, os,
          gideo, oideo, mood, issues, hint):
    return {
        "scenarioKey": key, "name": name, "description": desc,
        "stateName": state, "startDate": START_DATE,
        "cycleLengthMonths": CYCLE,
        "governmentPartyName": gname, "oppositionPartyName": oname,
        "thirdPartyName": "Youth Development Party (YDP)",
        "governmentStartingStats": gs, "oppositionStartingStats": os,
        "thirdPartyStartingStats": YDP_STATS,
        "politicalParties": [
            party(gkey, gname, "GOVERNMENT", gs, gideo),
            party(okey, oname, "OPPOSITION", os, oideo, "#3F88C5", "Hand"),
            YDP_PARTY,
        ],
        "publicState": {
            "undecidedSupport": ud(gs, os), "mood": mood,
            "mainIssues": issues, "memoryHint": hint,
        },
        "ruleWeights": RULE_WEIGHTS,
        "active": True, "_class": CLASS,
    }


SCENARIOS = [

    # 1. ANDHRA PRADESH 2021
    # YSRCP (Jagan Reddy) won 2019 with 151/175 seats and 49.9% vote share — historic.
    # Naidu's TDP routed but remains main opposition. Jagan's welfare wave: Rythu Bharosa,
    # Amma Vodi, village secretariat system. Covid response rated decent.
    build("andhra_pradesh_2021", "Andhra Pradesh 2021",
          "Jagan Reddy's YSRCP commands AP on its historic 2019 mandate — welfare schemes, decentralised capitals, and TDP's distant opposition.",
          "Andhra Pradesh", "YSRCP", "TDP", "ysrcp", "tdp",
          s(68, 42, 58, 52), s(46, 45, 42, 24),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Welfare scheme delivery", "Three-capital controversy", "Covid response"],
          "Jagan's welfare-first governance enjoys mass rural loyalty; three-capital controversy tests his credibility with urban AP."),

    # 2. ARUNACHAL PRADESH 2021
    # BJP (Pema Khandu) won 2019 with 41/60 seats. BJP sweeps northeast on Modi wave.
    # INC and NPP form scattered opposition. Cross-border tensions with China growing.
    build("arunachal_pradesh_2021", "Arunachal Pradesh 2021",
          "Pema Khandu's BJP consolidates Arunachal's northeast frontier — border infrastructure, Modi wave, and a fragmented opposition.",
          "Arunachal Pradesh", "BJP", "INC", "bjp", "inc",
          s(65, 40, 55, 50), s(32, 42, 30, 16),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Border infrastructure", "China tensions", "Development"],
          "BJP's Arunachal grip is firm; China's incursion claims put border infrastructure at the top of the political agenda."),

    # 3. ASSAM 2021
    # BJP (Sarbananda Sonowal, won 2016). BJP won May 2021 election — Himanta Biswa Sarma
    # became CM after election. Jan 2021: Sonowal BJP governing, heading to polls.
    # INC-led Mahajot alliance (with AIUDF, BPF) in opposition.
    build("assam_2021", "Assam 2021",
          "Sarbananda Sonowal's BJP completes Assam's first full term as NRC implementation, CAA protests, and Covid define the election.",
          "Assam", "BJP", "INC", "bjp", "inc",
          s(62, 42, 55, 46), s(52, 48, 48, 32),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["NRC implementation", "CAA protests", "Covid response"],
          "BJP holds Assam on development and NRC nationalism; INC's Mahajot alliance gives it a credible path back to power."),

    # 4. BIHAR 2021
    # JD(U)+BJP NDA (Nitish Kumar) won Nov 2020 narrowly — NDA 125/243.
    # RJD (Tejashwi Yadav) is energised opposition — RJD alone won 75 seats (biggest single party).
    # Nitish's pro-tem lead relies on BJP's 74 seats.
    build("bihar_2021", "Bihar 2021",
          "Nitish Kumar's razor-thin NDA win in Bihar masks the RJD surge — Tejashwi's youth campaign reshapes Bihar's political landscape.",
          "Bihar", "JD(U)", "RJD", "jdu", "rjd",
          s(55, 38, 52, 38), s(68, 45, 62, 42),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Employment", "Covid relief", "Youth unemployment"],
          "Nitish governs but RJD's Tejashwi took 75 seats alone — Bihar's political centre of gravity is shifting to the young."),

    # 5. CHHATTISGARH 2021
    # INC (Bhupesh Baghel) won 2018 decisively — 68/90 seats, ended Raman Singh's 15-yr reign.
    # BJP (Raman Singh) in opposition. Naxal violence persists.
    build("chhattisgarh_2021", "Chhattisgarh 2021",
          "Bhupesh Baghel's INC mid-term delivers farmer debt waiver and tribal welfare after ending BJP's 15-year Chhattisgarh rule.",
          "Chhattisgarh", "INC", "BJP", "inc", "bjp",
          s(65, 42, 58, 48), s(48, 45, 42, 26),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Farmer debt waiver", "Naxalism", "Tribal welfare"],
          "Baghel's INC has delivered on farm debt waiver and welfare; BJP's Raman Singh is out of fresh ideas post-15-year rule."),

    # 6. DELHI 2021
    # AAP (Arvind Kejriwal) won Feb 2020 with 62/70 seats — second historic mandate.
    # BJP has only 8 seats. Delhi Covid second wave will hit hard Apr 2021.
    # Mohalla clinics, free electricity/water, schools-first governance popular.
    build("delhi_2021", "Delhi 2021",
          "Kejriwal's AAP governs Delhi on its second massive mandate — mohalla clinics, education transformation, and Covid oxygen crisis ahead.",
          "Delhi", "AAP", "BJP", "aap", "bjp",
          s(70, 22, 68, 56), s(48, 42, 46, 24),
          "ANTI_CORRUPTION", "DEVELOPMENT_FIRST",
          "Watchful",
          ["Covid management", "Health and education", "LG jurisdiction battle"],
          "AAP's welfare delivery model is nationally admired; the April 2021 oxygen crisis will test Kejriwal's governance reputation."),

    # 7. GOA 2021
    # BJP (Pramod Sawant) became CM March 2019 after Manohar Parrikar died.
    # Sawant lacks Parrikar's personal mass appeal. INC, TMC, AAP all entering Goa.
    # Heading into Feb 2022 election.
    build("goa_2021", "Goa 2021",
          "Pramod Sawant's BJP governs post-Parrikar Goa as INC, AAP, and TMC crowd the 2022 election space in a fragmented contest.",
          "Goa", "BJP", "INC", "bjp", "inc",
          s(50, 52, 44, 34), s(48, 50, 42, 22),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Post-Parrikar governance", "Tourism collapse (Covid)", "Multi-party contest"],
          "Sawant governs in Parrikar's long shadow; Covid devastates Goa's tourism economy while opposition parties multiply."),

    # 8. GUJARAT 2021
    # BJP (Vijay Rupani, CM since Aug 2016). Bhupendra Patel takes over Sep 2021 after
    # BJP refreshes state leadership. Covid second wave hit Gujarat hard.
    # INC is distant, weak opposition.
    build("gujarat_2021", "Gujarat 2021",
          "Vijay Rupani's BJP navigates Gujarat's bruising Covid second wave ahead of a leadership refresh and 2022 state election.",
          "Gujarat", "BJP", "INC", "bjp", "inc",
          s(58, 48, 52, 48), s(38, 42, 35, 18),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Covid second wave", "Development", "2022 election preparation"],
          "Gujarat BJP faces rare public anger over Covid oxygen shortages; Rupani's replacement by Patel signals internal refresh ahead of 2022."),

    # 9. HARYANA 2021
    # BJP (ML Khattar, won Oct 2019 narrowly — 40/90 seats; JJP coalition with Dushyant Chautala).
    # INC (Bhupinder Hooda) is main opposition. Farm laws protests hit Haryana badly.
    build("haryana_2021", "Haryana 2021",
          "ML Khattar's BJP-JJP coalition bears the brunt of Haryana farmers' anger over the three farm laws at Delhi's gates.",
          "Haryana", "BJP", "INC", "bjp", "inc",
          s(46, 42, 42, 34), s(58, 45, 52, 36),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Restless",
          ["Farm laws protest", "Farmers' agitation", "Covid response"],
          "Farm law protests devastate BJP's rural Haryana base; Hooda's INC is the natural beneficiary of a deeply agitated farmer vote."),

    # 10. HIMACHAL PRADESH 2021
    # BJP (Jai Ram Thakur, won Dec 2017 — HP alternation held, 44/68 seats).
    # INC (Pratibha Singh/Virbhadra Singh, who died Jul 2021) in opposition.
    # Heading into Dec 2022 election.
    build("himachal_pradesh_2021", "Himachal Pradesh 2021",
          "Jai Ram Thakur's BJP navigates HP mid-term with Covid relief as Virbhadra Singh's INC prepares its final electoral battle.",
          "Himachal Pradesh", "BJP", "INC", "bjp", "inc",
          s(58, 38, 52, 42), s(58, 42, 50, 40),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Covid relief", "Apple economy", "Hydro power"],
          "Thakur's BJP performs adequately in mid-term; Virbhadra Singh's passing later in 2021 reshapes INC's HP leadership entirely."),

    # 11. JAMMU & KASHMIR 2021
    # J&K became UT in Oct 2019 after Art 370 abrogation. Under LG (Manoj Sinha since Aug 2020).
    # No elected government. NC (Omar Abdullah) and PDP (Mehbooba) are largest parties.
    # Apni Party (Altaf Bukhari, BJP-backed) is pro-establishment force.
    # Delimitiation process ongoing; elections expected 2024.
    build("jammu_kashmir_2021", "Jammu & Kashmir 2021",
          "J&K under LG administration post-Art 370 — NC and PDP demand statehood restoration while BJP consolidates its direct administration.",
          "Jammu & Kashmir", "BJP (LG Admin)", "NC", "bjp_lg", "nc",
          s(40, 42, 38, 22), s(55, 42, 50, 30),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Restless",
          ["Statehood restoration demand", "Art 370 legacy", "Development"],
          "J&K's UT status removes elected governance; NC and PDP demand statehood while BJP pursues a Jammu-centric development narrative."),

    # 12. JHARKHAND 2021
    # JMM (Hemant Soren, won Dec 2019 with JMM+INC+RJD Mahagathbandhan — 47+16+1 = 64/81 seats).
    # BJP (Raghubar Das/Babulal Marandi) comprehensively defeated in 2019.
    build("jharkhand_2021", "Jharkhand 2021",
          "Hemant Soren's JMM Mahagathbandhan delivers Jharkhand's most stable government — tribal rights, MNREGA boost, and BJP's reset.",
          "Jharkhand", "JMM", "BJP", "jmm", "bjp",
          s(65, 40, 55, 44), s(48, 45, 42, 28),
          "REGIONAL_PRIDE", "DEVELOPMENT_FIRST",
          "Watchful",
          ["Tribal land rights", "MNREGA expansion", "Covid relief"],
          "Hemant Soren's coalition is the most secure Jharkhand government ever; BJP rebuilds under Babulal Marandi after a crushing 2019 loss."),

    # 13. KARNATAKA 2021
    # BJP (BS Yediyurappa, full govt since Jul 2019 after SC verdict; resigned Jul 2021,
    # replaced by Basavaraj Bommai). Mining/corruption cloud persists.
    # INC (Siddaramaiah + DK Shivakumar) is a united and energised opposition.
    build("karnataka_2021", "Karnataka 2021",
          "BS Yediyurappa's BJP governs Karnataka amid corruption allegations as INC's Siddaramaiah-DKS duo builds a credible 2023 campaign.",
          "Karnataka", "BJP", "INC", "bjp", "inc",
          s(48, 62, 40, 34), s(62, 44, 56, 34),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Corruption allegations", "Covid response", "INC's united challenge"],
          "Yediyurappa's advanced age and corruption perception hurt BJP; Siddaramaiah and DKS unite INC for a formidable 2023 comeback."),

    # 14. KERALA 2021
    # LDF/CPI-M (Pinarayi Vijayan, won 2016; re-elected May 2021 — historic consecutive Left win).
    # Jan 2021: Vijayan LDF still in first term; heading to polls. UDF/INC (Ramesh Chennithala) opp.
    build("kerala_2021", "Kerala 2021",
          "Pinarayi Vijayan's LDF shatters Kerala's alternation tradition — development delivery, Covid response, and Chennithala's UDF challenge.",
          "Kerala", "LDF (CPI-M)", "UDF (INC)", "ldf_cpim", "udf_inc",
          s(70, 32, 65, 50), s(54, 42, 50, 36),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Covid management", "K-Rail SilverLine", "Development"],
          "Pinarayi's disciplined Covid response earns rare Kerala incumbency win; UDF's Chennithala campaigns hard but faces the anti-alternation tide."),

    # 15. MADHYA PRADESH 2021
    # BJP (Shivraj Singh Chouhan) returned to power March 2020 after 22 Jyotiraditya Scindia-led
    # INC MLAs defected. Kamal Nath INC government fell after 15 months.
    # INC (Kamal Nath) is opposition. Shivraj's 4th CM stint.
    build("madhya_pradesh_2021", "Madhya Pradesh 2021",
          "Shivraj Singh Chouhan's BJP reclaims MP through Operation Lotus — a politically engineered comeback that shook national politics.",
          "Madhya Pradesh", "BJP", "INC", "bjp", "inc",
          s(62, 45, 56, 46), s(48, 52, 42, 26),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Operation Lotus legacy", "Covid relief", "Agriculture"],
          "Shivraj's return via Scindia defections gives BJP MP but INC's Kamal Nath keeps the government under moral legitimacy pressure."),

    # 16. MAHARASHTRA 2021
    # MVA (Uddhav Thackeray — Shiv Sena+INC+NCP coalition; formed Nov 2019 after BJP-SS split
    # over CM post). BJP (Devendra Fadnavis) in opposition.
    # Covid hit Maharashtra hardest — India's worst-affected state.
    build("maharashtra_2021", "Maharashtra 2021",
          "Uddhav Thackeray's MVA coalition manages India's hardest-hit Covid state — Mumbai under siege, Fadnavis in potent opposition.",
          "Maharashtra", "MVA (Shiv Sena)", "BJP", "mva_shivsena", "bjp",
          s(52, 48, 50, 36), s(62, 42, 58, 32),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Restless",
          ["Covid second wave (worst in India)", "MVA coalition tensions", "Economic recovery"],
          "Uddhav's MVA handles Maharashtra's Covid crisis under enormous pressure; BJP's Fadnavis waits for coalition fault lines to widen."),

    # 17. MANIPUR 2021
    # BJP (N. Biren Singh, won 2017 — first-ever BJP CM of Manipur). Won 2022 again.
    # INC (Okram Ibobi Singh, 3-term ex-CM) is main opposition.
    build("manipur_2021", "Manipur 2021",
          "N. Biren Singh's BJP builds Manipur mid-term on development, AFSPA review debate, and northeast connectivity ahead of 2022 polls.",
          "Manipur", "BJP", "INC", "bjp", "inc",
          s(60, 40, 52, 40), s(46, 50, 38, 24),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["AFSPA review", "Northeast connectivity", "Covid relief"],
          "Biren Singh's BJP governs Manipur competently; AFSPA review and connectivity projects are key issues heading to 2022 polls."),

    # 18. MEGHALAYA 2021
    # NPP (Conrad Sangma, won Feb 2018 with MDA coalition — first non-INC majority Meghalaya govt).
    # INC (Mukul Sangma, father of Conrad's rival) is main opposition.
    build("meghalaya_2021", "Meghalaya 2021",
          "Conrad Sangma's NPP-led MDA coalition governs Meghalaya mid-term — coal mining ban, Covid, and a historic non-INC governance era.",
          "Meghalaya", "NPP", "INC", "npp", "inc",
          s(62, 42, 52, 40), s(46, 52, 38, 22),
          "DEVELOPMENT_FIRST", "REGIONAL_PRIDE",
          "Watchful",
          ["Coal mining ban", "Covid response", "Development"],
          "Conrad Sangma's NPP brings fresh governance energy to Meghalaya; INC struggles to remain relevant after losing its northeast dominance."),

    # 19. MIZORAM 2021
    # MNF (Zoramthanga, won Nov 2018 with 26/40 seats — returned to power after defeating INC).
    # ZPM (Zoram People's Movement — Lalduhoma) is emerging challenger. INC collapsed.
    build("mizoram_2021", "Mizoram 2021",
          "Zoramthanga's MNF governs Mizoram mid-term as ZPM emerges as a powerful new challenger, reshaping Mizoram's two-party dynamics.",
          "Mizoram", "MNF", "ZPM", "mnf", "zpm",
          s(62, 32, 55, 46), s(62, 28, 58, 32),
          "REGIONAL_PRIDE", "ANTI_CORRUPTION",
          "Watchful",
          ["Development", "Myanmar refugee crisis", "ZPM challenge"],
          "Zoramthanga's MNF governs amid Mizoram's Myanmar refugee solidarity stance; ZPM's clean-image challenge is building rapidly."),

    # 20. NAGALAND 2021
    # NDPP+BJP (Neiphiu Rio, formed NDPP after leaving NPF in 2017; won 2018 with PDA coalition —
    # NDPP 18+BJP 12+others = 32+ seats, majority).
    # NPF (Shürhozelie Liezietsu) is main opposition after Rio left.
    build("nagaland_2021", "Nagaland 2021",
          "Neiphiu Rio's NDPP-BJP coalition steers Nagaland through NSCN peace-talk urgency and a Covid-hit development agenda.",
          "Nagaland", "NDPP", "NPF", "ndpp", "npf",
          s(62, 42, 52, 44), s(44, 48, 38, 20),
          "REGIONAL_PRIDE", "ANTI_CORRUPTION",
          "Watchful",
          ["NSCN peace accord delay", "Covid response", "Development"],
          "Rio's NDPP-BJP holds Nagaland with a shared tribal-development mandate; the delayed NSCN final accord tests political patience."),

    # 21. ODISHA 2021
    # BJD (Naveen Patnaik, won 2019 alone with 112/147 seats — 5th consecutive term).
    # BJP (Samit Patra/state unit) grew from 10 to 23 seats in 2019 but still distant.
    build("odisha_2021", "Odisha 2021",
          "Naveen Patnaik's BJD enters a fifth consecutive mandate commanding Odisha's politics with welfare schemes and disaster resilience.",
          "Odisha", "BJD", "BJP", "bjd", "bjp",
          s(75, 30, 70, 60), s(55, 40, 50, 22),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Welfare schemes", "Covid response", "Cyclone preparedness"],
          "Naveen's BJD is near-unbeatable — five terms of welfare delivery make Odisha's anti-incumbency nearly non-existent."),

    # 22. PUNJAB 2021
    # INC (Amarinder Singh, won 2017 with 77/117). Amarinder resigned Sep 2021 → Channi.
    # SAD (Sukhbir Badal) weakened; AAP (Bhagwant Mann) building strongly.
    # Farm laws hit Punjab hardest — Amarinder's contradiction between Centre and farmers.
    build("punjab_2021", "Punjab 2021",
          "Amarinder Singh's INC walks a tightrope — supporting farmers' protest while managing Centre relations as AAP builds Punjab momentum.",
          "Punjab", "INC", "AAP", "inc", "aap",
          s(45, 52, 40, 34), s(68, 20, 65, 38),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Restless",
          ["Farm laws protest", "Drug menace", "AAP's Punjab surge"],
          "Amarinder's INC is squeezed between the Centre and an angry farmer vote; AAP's Bhagwant Mann is becoming Punjab's defining political voice."),

    # 23. RAJASTHAN 2021
    # INC (Ashok Gehlot, won Dec 2018 with 99/200). Survived Sachin Pilot's rebellion Jul 2020.
    # BJP (Vasundhara Raje) in opposition. Covid hit Rajasthan's desert districts badly.
    build("rajasthan_2021", "Rajasthan 2021",
          "Ashok Gehlot's INC stabilises post-Pilot rebellion Rajasthan — social welfare delivery, Covid management, and a BJP in internal disarray.",
          "Rajasthan", "INC", "BJP", "inc", "bjp",
          s(60, 48, 54, 44), s(52, 44, 48, 32),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Post-Pilot rebellion stability", "Covid relief", "Social welfare"],
          "Gehlot's political skill saved INC from collapse; Vasundhara Raje battles BJP's internal resistance to her Rajasthan leadership."),

    # 24. SIKKIM 2021
    # SKM (Prem Singh Tamang/Golay, won May 2019 — 17/32 seats, ended Chamling's 25-yr SDF reign).
    # SDF (Pawan Chamling, 11/32) is main opposition. Golay had criminal conviction — SC gave relief.
    build("sikkim_2021", "Sikkim 2021",
          "Prem Singh Tamang's SKM consolidates Sikkim's new political era after ending Chamling's 25-year SDF dominance.",
          "Sikkim", "SKM", "SDF", "skm", "sdf",
          s(65, 35, 58, 52), s(48, 35, 44, 28),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["New governance era", "Development", "Covid relief"],
          "Golay's SKM has delivered a genuine political alternation in Sikkim; Chamling's SDF adjusts to an unfamiliar opposition role."),

    # 25. TAMIL NADU 2021
    # AIADMK (Edappadi Palaniswami, CM since Feb 2017 after Jayalalithaa's Dec 2016 death).
    # DMK (MK Stalin) won May 2021 with 133/234 — ended AIADMK's decade.
    # Jan 2021: EPS still governing but severely weakened. OPS-EPS internal feud visible.
    build("tamil_nadu_2021", "Tamil Nadu 2021",
          "Edappadi Palaniswami's AIADMK heads into its 2021 election defence hobbled by post-Jaya identity crisis and Stalin's dominant DMK wave.",
          "Tamil Nadu", "AIADMK", "DMK", "aiadmk", "dmk",
          s(42, 58, 36, 30), s(70, 38, 66, 46),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Post-Jayalalithaa identity", "OPS-EPS feud", "Stalin's DMK wave"],
          "AIADMK's post-Jaya era lacks a towering figure; MK Stalin's patient decade-long groundwork makes DMK the clear 2021 favourite."),

    # 26. TELANGANA 2021
    # TRS (KCR, won Dec 2018 snap election with 88/119 seats — early dissolution gamble paid off).
    # BJP (Bandi Sanjay) rising sharply from 1 to 4 seats; INC collapsed to 19.
    build("telangana_2021", "Telangana 2021",
          "KCR's TRS commands Telangana mid-term as BJP launches an aggressive state expansion and INC continues its post-bifurcation collapse.",
          "Telangana", "TRS", "BJP", "trs", "bjp",
          s(65, 45, 60, 50), s(60, 38, 58, 25),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Kaleshwaram project", "Rythu Bandhu", "BJP's state surge"],
          "KCR's welfare schemes cement TRS loyalty; BJP's rapid Telangana growth makes it the primary challenger, displacing INC entirely."),

    # 27. TRIPURA 2021
    # BJP (Biplab Kumar Deb, won Feb 2018 with 36/60 seats — ended CPI-M's 25-year Left rule).
    # CPI-M (Manik Sarkar) in opposition after historic defeat. Post-Left transition turbulent.
    build("tripura_2021", "Tripura 2021",
          "Biplab Kumar Deb's BJP mid-term in Tripura faces post-Left transition challenges — violence, governance gaps, and Manik Sarkar's resilient opposition.",
          "Tripura", "BJP", "Left Front (CPI-M)", "bjp", "cpi_m_left_front",
          s(54, 45, 48, 44), s(55, 28, 52, 28),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Post-Left governance", "Development", "Political violence"],
          "Biplab Deb's BJP governs a post-Left Tripura but political violence and governance quality concerns complicate the transition."),

    # 28. UTTARAKHAND 2021
    # BJP (Trivendra Singh Rawat, won 2017 with 57/70 seats). Resigned March 2021 →
    # Tirath Singh Rawat (March-Jul 2021) → Pushkar Singh Dhami (Jul 2021).
    # Jan 2021: Trivendra Singh Rawat BJP. Three CMs in 2021 signals instability.
    build("uttarakhand_2021", "Uttarakhand 2021",
          "Trivendra Singh Rawat's BJP faces mid-term leadership turbulence in Uttarakhand — a year with three CMs ahead of the 2022 election.",
          "Uttarakhand", "BJP", "INC", "bjp", "inc",
          s(50, 42, 46, 38), s(55, 42, 50, 32),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Leadership instability", "Covid and Kumbh Mela", "Development"],
          "BJP's three CMs in 2021 signals internal chaos; INC's Harish Rawat positions himself for 2022 as the change narrative builds."),

    # 29. UTTAR PRADESH 2021
    # BJP (Yogi Adityanath, won 2017 with enormous 312/403 seats). Heading to Feb 2022 election.
    # SP (Akhilesh Yadav) is revitalised opposition. Covid second wave hit UP badly;
    # Ganga bodies became a defining political image.
    build("uttar_pradesh_2021", "Uttar Pradesh 2021",
          "Yogi Adityanath's BJP defends India's most important state — law-order, Hindutva identity, and the devastating Covid second wave image.",
          "Uttar Pradesh", "BJP", "SP", "bjp", "sp",
          s(62, 45, 58, 48), s(65, 48, 60, 32),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Watchful",
          ["Covid second wave", "Law and order", "Caste arithmetic for 2022"],
          "Yogi's BJP defends a massive mandate but Ganga bodies and oxygen shortage images haunt 2021; Akhilesh's SP builds a united caste coalition."),

    # 30. WEST BENGAL 2021
    # TMC (Mamata Banerjee, incumbent; won May 2021 with 213/294 — defeating BJP's national push).
    # BJP (Dilip Ghosh/Suvendu Adhikari) made unprecedented 77-seat gains but lost.
    # Jan 2021: Mamata TMC incumbent heading into the most watched election of the cycle.
    build("west_bengal_2021", "West Bengal 2021",
          "Mamata Banerjee's TMC faces BJP's most aggressive state campaign — a do-or-die Bengal battle with massive national stakes for both parties.",
          "West Bengal", "TMC", "BJP", "tmc", "bjp",
          s(65, 55, 62, 50), s(68, 40, 68, 38),
          "DEVELOPMENT_FIRST", "ANTI_CORRUPTION",
          "Restless",
          ["Sonar Bangla vs Jai Shri Ram", "BJP's national push", "Didi's identity politics"],
          "Bengal 2021 is India's most electrifying contest; Mamata's regional identity versus BJP's Modi wave will define Bengali politics for a decade."),
]


def main():
    client = MongoClient(MONGO_URI)
    col = client[DB_NAME][COLLECTION]
    existing = set(col.distinct("scenarioKey"))
    to_insert = [sc for sc in SCENARIOS if sc["scenarioKey"] not in existing]
    skipped = [sc["scenarioKey"] for sc in SCENARIOS if sc["scenarioKey"] in existing]
    if skipped:
        print(f"Skipping {len(skipped)} existing: {skipped}")
    if not to_insert:
        print("All 2021 scenarios already exist. Nothing inserted.")
        client.close()
        return
    result = col.insert_many(to_insert)
    print(f"\n✅ Inserted {len(result.inserted_ids)} 2021 scenarios:")
    for sc, _id in zip(to_insert, result.inserted_ids):
        print(f"   {sc['scenarioKey']:45s} → {_id}")
    client.close()


if __name__ == "__main__":
    main()
