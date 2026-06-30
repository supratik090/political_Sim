import json
from pymongo import MongoClient

# Mapping of base issue keywords to handcrafted reaction texts for Andhra Pradesh
HANDCRAFTED_REACTIONS = {
    "cyberabad_it": {
        "gov_action": "Inaugurate Cyberabad Phase 1 and announce tax breaks for multinational tech giants.",
        "opp_demands": "Criticize the tech focus as elitist, demanding equal focus on rural development.",
        "joint_forum": "Propose a public-private partnership model to build tech parks in tier-2 cities."
    },
    "farmer_suicides": {
        "gov_action": "Announce a direct loan waiver package and emergency relief for distressed farming families.",
        "opp_demands": "Organize state-wide rallies accusing the government of negligence and demand a judicial probe.",
        "joint_forum": "Convene an all-party agricultural committee to restructure crop insurance and credit terms."
    },
    "trs_formation": {
        "gov_action": "Downplay the division movement and emphasize regional development boards for Telangana.",
        "opp_demands": "Accuse the government of neglecting Telangana's resource allocation, fueling separatist sentiments.",
        "joint_forum": "Propose a legislative committee to review regional backwardness and employment quotas."
    },
    "naxal_attack": {
        "gov_action": "Authorize Greyhounds special forces to launch combing operations in border forests.",
        "opp_demands": "Condemn the security lapse and demand high-level protection for rural political workers.",
        "joint_forum": "Establish a developmental peace council to address the socio-economic roots of left-wing extremism."
    },
    "ysr_padayatra": {
        "gov_action": "Dismiss the padayatra as a political stunt and highlight the ruling party's welfare statistics.",
        "opp_demands": "Mobilize massive public receptions for YSR's padayatra to highlight local grievances.",
        "joint_forum": "Urge the assembly to debate the ground realities of rural distress raised during the march."
    },
    "microfinance_crisis": {
        "gov_action": "Introduce strict interest caps and registration laws to curb microfinance exploitation.",
        "opp_demands": "Demand the immediate arrest of predatory lenders and debt relief for affected women.",
        "joint_forum": "Propose strengthening state-run self-help groups to counter unregulated private lenders."
    },
    "irrigation_protests": {
        "gov_action": "Deploy security forces to safeguard the canals and request tribunal arbitration.",
        "opp_demands": "Accuse the government of failing to protect the water rights of downstream farmers.",
        "joint_forum": "Convene a bipartisan delta-region commission to negotiate temporary sharing quotas."
    },
    "power_subsidy_demand": {
        "gov_action": "Initiate feasibility studies to provide subsidized agricultural power during daytime.",
        "opp_demands": "Demand 9 hours of uninterrupted free electricity daily for all registered farmers.",
        "joint_forum": "Propose an energy task force to balance state power utility debts and farm subsidies."
    },
    "godavari_pushkaram": {
        "gov_action": "Allocate special state funds to expand ghats and upgrade crowd-control infrastructure.",
        "opp_demands": "Criticize the lack of basic amenities and safety measures, alleging fund mismanagement.",
        "joint_forum": "Form a joint regulatory body with religious leaders to manage future festival crowds safely."
    },
    "industrial_park": {
        "gov_action": "Acquire land for the Vizag Pharma City while promising local employment quotas.",
        "opp_demands": "Protest against forced land acquisition and highlight potential pollution in coastal waters.",
        "joint_forum": "Advocate for a comprehensive environmental impact assessment and fair compensation rates."
    },
    "tribal_rights": {
        "gov_action": "Enforce the 1/70 land transfer regulation strictly to protect tribal land rights.",
        "opp_demands": "Demand the immediate rollback of industrial mining leases in protected tribal areas.",
        "joint_forum": "Establish a tribal advisory council to resolve historical land claims and forest rights."
    },
    "cooperative_bank": {
        "gov_action": "Order a CID investigation into the cooperative bank fraud and freeze directors' assets.",
        "opp_demands": "Demand that the state government guarantee the deposits of middle-class families.",
        "joint_forum": "Propose strict RBI-aligned regulatory oversight for all state cooperative institutions."
    },
    "aarogyasri_launch": {
        "gov_action": "Launch the Aarogyasri scheme to provide free tertiary healthcare to BPL families.",
        "opp_demands": "Expose loopholes where private hospitals exploit the system, and demand public sector upgrades.",
        "joint_forum": "Suggest a joint steering committee to monitor insurance claims and hospital compliance."
    },
    "jalayagnam_audits": {
        "gov_action": "Defend Jalayagnam as the lifeline of Andhra agriculture and order audits to show transparency.",
        "opp_demands": "Label the project 'Dhanayagnam' and demand a judicial commission to probe mobilization advance scams.",
        "joint_forum": "Propose a legislative panel to review project costs, timelines, and execution status."
    },
    "telangana_agitations": {
        "gov_action": "Appeals for peace while offering medical supervision to KCR and consulting the central cabinet.",
        "opp_demands": "Criticize the state government's delayed response and demand an immediate assembly resolution.",
        "joint_forum": "Hold a multi-party meeting to maintain law and order and de-escalate regional tensions."
    },
    "satyam_collapse": {
        "gov_action": "Coordinate with federal agencies for a bailout and safeguard the employment of tech workers.",
        "opp_demands": "Blame the administration's close ties with corporate heads for lack of regulatory oversight.",
        "joint_forum": "Establish an emergency corporate governance task force to restore investor confidence."
    },
    "ysr_helicopter": {
        "gov_action": "Announce state mourning, coordinate a thorough crash investigation, and appeal for calm.",
        "opp_demands": "Pay deep condolences while demanding transparency in the crash investigation findings.",
        "joint_forum": "Convene an all-party legislative session to stabilize the administration and prevent unrest."
    },
    "indiramma_housing": {
        "gov_action": "Allocate funds for Indiramma housing, prioritizing landless poor and marginalized communities.",
        "opp_demands": "Expose political favoritism in beneficiary lists and demand a transparent lottery system.",
        "joint_forum": "Suggest an independent social audit mechanism to verify house construction and quality."
    },
    "coastal_corridor": {
        "gov_action": "Re-evaluate the PCPIR corridor route to minimize displacement of fertile farming lands.",
        "opp_demands": "Organize fishermen and farmers' protests against corporate land grabbing along the coast.",
        "joint_forum": "Propose a coastal zone dialogue to balance industrial growth with maritime livelihoods."
    },
    "pavala_vaddi": {
        "gov_action": "Provide subsidized 3% interest loans (Pavala Vaddi) to boost rural women self-help groups.",
        "opp_demands": "Argue the credit limits are too low and demand complete interest-free loans instead.",
        "joint_forum": "Coordinate with public sector banks to streamline credit delivery and prevent middleman commissions."
    },
    "naxal_surrenders": {
        "gov_action": "Offer a generous rehabilitation policy with land and job training for surrendered cadres.",
        "opp_demands": "Urge the state to halt extrajudicial encounters and ensure fair trials for suspects.",
        "joint_forum": "Advocate for deep development funding in tribal zones to prevent recruitment back into extremism."
    },
    "obulapuram_mining": {
        "gov_action": "Suspend illegal mining leases and order boundary surveys along the AP-Karnataka border.",
        "opp_demands": "Demand a CBI probe into iron ore smuggling and the immediate arrest of the mining barons.",
        "joint_forum": "Call for a mining policy revision to preserve natural resources and protect forest reserves."
    },
    "fee_reimbursement": {
        "gov_action": "Initiate fee reimbursement to ensure financial hurdles do not block professional education.",
        "opp_demands": "Highlight delayed government payouts which force colleges to withhold students' certificates.",
        "joint_forum": "Propose a direct benefit transfer portal to prevent bureaucratic delays in fee clearance."
    },
    "hyderabad_blasts": {
        "gov_action": "Enforce strict security measures, enhance CCTV surveillance, and fast-track counter-terror trials.",
        "opp_demands": "Condemn intelligence lapses and demand immediate support packages for the blast victims.",
        "joint_forum": "Coordinate communal harmony committees to prevent partisan polarization in Hyderabad."
    }
}

def get_base_issue(news_key):
    # newsKey looks like ap2001_2001_01_cyberabad_it or ap2006_2010_12_hyderabad_blasts
    parts = news_key.split("_")
    # Join parts from index 3 to end
    return "_".join(parts[3:])

def main():
    from dotenv import load_dotenv
    import os
    
    env_path = os.path.join(os.path.dirname(__file__), "..", "..", "backend", ".env")
    load_dotenv(env_path)
    
    uri = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/political_sim")
    client = MongoClient(uri)
    db = client.get_default_database()
    
    print(f"Connected to database: {db.name}")
    
    news_collection = db["news_definitions"]
    
    query = {"scenarioKey": {"$in": ["andhra_pradesh_2001", "andhra_pradesh_2006"]}}
    news_items = list(news_collection.find(query))
    print(f"Found {len(news_items)} news items to update.")
    
    updated_count = 0
    for item in news_items:
        base_issue = get_base_issue(item.get("newsKey", item.get("issueKey", "")))
        
        if base_issue not in HANDCRAFTED_REACTIONS:
            print(f"Warning: Base issue '{base_issue}' not found in handcrafted mappings.")
            continue
            
        reactions = item.get("reactionOptions", item.get("options", []))
        modified = False
        
        for ropt in reactions:
            reaction_key = ropt.get("reactionKey", ropt.get("optionKey", ""))
            
            # Identify which type of reaction this is
            if "gov_action" in reaction_key:
                ropt["text"] = HANDCRAFTED_REACTIONS[base_issue]["gov_action"]
                modified = True
            elif "opp_demands" in reaction_key:
                ropt["text"] = HANDCRAFTED_REACTIONS[base_issue]["opp_demands"]
                modified = True
            elif "joint_forum" in reaction_key:
                ropt["text"] = HANDCRAFTED_REACTIONS[base_issue]["joint_forum"]
                modified = True
            elif "no_comment" in reaction_key:
                pass
                
        if modified:
            update_data = {"reactionOptions": reactions}
            if "options" in item:
                update_data["options"] = reactions
            news_collection.update_one({"_id": item["_id"]}, {"$set": update_data})
            updated_count += 1
            
    print(f"Successfully updated {updated_count} news items with handcrafted responses.")

if __name__ == "__main__":
    main()
