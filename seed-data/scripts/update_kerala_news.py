import json
from pymongo import MongoClient

# Mapping of base issue keywords to handcrafted reaction texts
HANDCRAFTED_REACTIONS = {
    "remittance_boom": {
        "gov_action": "Launch state-backed infrastructure bonds to productively channel Gulf remittances.",
        "opp_demands": "Criticize the government for relying on Gulf money while ignoring local job creation.",
        "joint_forum": "Form a multi-party task force with NRK representatives to plan long-term investments."
    },
    "plantation_strikes": {
        "gov_action": "Mandate immediate wage revisions and order plantation owners to provide medical benefits.",
        "opp_demands": "Join the strike lines and demand nationalization of defaulting tea estates.",
        "joint_forum": "Propose a tripartite discussion between workers, estate owners, and the government."
    },
    "political_violence": {
        "gov_action": "Deploy additional police battalions to Kannur and enforce strict curfews.",
        "opp_demands": "Accuse the ruling party of state-sponsored terror and demand a CBI inquiry.",
        "joint_forum": "Call for an all-party peace meeting to de-escalate tensions in the region."
    },
    "tourism_campaign": {
        "gov_action": "Increase funding for the 'God's Own Country' campaign to target international tourists.",
        "opp_demands": "Highlight the environmental degradation caused by unregulated tourism resorts.",
        "joint_forum": "Suggest a sustainable tourism framework balancing economic growth and ecology."
    },
    "marad_clashes": {
        "gov_action": "Initiate a swift judicial probe and establish a permanent police outpost at the beach.",
        "opp_demands": "Demand immediate compensation for victims and accuse the government of intelligence failure.",
        "joint_forum": "Organize joint communal harmony marches led by all major political factions."
    },
    "panchayat_funding": {
        "gov_action": "Highlight the success of decentralized planning and announce bonus funds for top panchayats.",
        "opp_demands": "Allege massive corruption in local fund allocation and demand a state audit.",
        "joint_forum": "Propose a bipartisan oversight committee for transparent panchayat fund utilization."
    },
    "hartal_protests": {
        "gov_action": "Declare the hartal illegal and deploy police to keep essential services running.",
        "opp_demands": "Fully endorse the trade unions and lead the protests against anti-people policies.",
        "joint_forum": "Urge the central government to intervene and review the recent fuel price hikes."
    },
    "cashew_industry": {
        "gov_action": "Announce a special financial bailout package for struggling cashew factories in Kollam.",
        "opp_demands": "Protest against the administration's failure to protect traditional industry workers.",
        "joint_forum": "Convene a round table with bank officials and factory owners to ease credit terms."
    },
    "silent_valley": {
        "gov_action": "Strictly enforce the buffer zone and deploy forest guards to prevent encroachments.",
        "opp_demands": "Demand adequate rehabilitation and compensation for the displaced local farmers.",
        "joint_forum": "Draft a comprehensive eco-development plan balancing conservation and tribal rights."
    },
    "state_lottery": {
        "gov_action": "Implement stringent regulations to crack down on illegal parallel lottery mafias.",
        "opp_demands": "Accuse the government of promoting gambling and exploiting the poor.",
        "joint_forum": "Suggest directing all lottery revenue exclusively towards public healthcare schemes."
    },
    "education_reforms": {
        "gov_action": "Defend the self-financing college bill as a necessary step to modernize higher education.",
        "opp_demands": "Lead student protests against the commercialization of the education sector.",
        "joint_forum": "Propose an independent fee regulatory committee to ensure affordability and merit."
    },
    "water_scarcity": {
        "gov_action": "Launch emergency drought relief and dispatch drinking water trucks to Palakkad.",
        "opp_demands": "Blame the government for poor water management and demand compensation for crop loss.",
        "joint_forum": "Advocate for a long-term interstate water sharing dialogue and rainwater harvesting."
    },
    "munnar_evictions": {
        "gov_action": "Fully back the demolition drive to reclaim government land from illegal resorts.",
        "opp_demands": "Accuse the task force of selective evictions targeting small traders and political rivals.",
        "joint_forum": "Call for a clear, uniform land policy to prevent future encroachments."
    },
    "smartcity_kochi": {
        "gov_action": "Celebrate the agreement as a historic milestone for Kerala's IT sector growth.",
        "opp_demands": "Raise concerns over the land lease terms and demand full transparency in the contract.",
        "joint_forum": "Form a joint legislative committee to oversee the project's timely execution."
    },
    "endosulfan_ban": {
        "gov_action": "Enforce a strict statewide ban on the pesticide and announce relief for victims.",
        "opp_demands": "Demand immediate federal intervention and comprehensive healthcare for Kasaragod.",
        "joint_forum": "Unite to petition the central government for a nationwide ban on Endosulfan."
    },
    "vizhinjam_port": {
        "gov_action": "Fast-track the port tenders and promise massive job creation for the coastal belt.",
        "opp_demands": "Question the financial viability of the bids and demand protection for local fishermen.",
        "joint_forum": "Propose an expert panel to assess the environmental impact on the coastline."
    },
    "coir_subsidies": {
        "gov_action": "Distribute modernization grants to boost the traditional coir weaving cooperatives.",
        "opp_demands": "Claim the subsidies are too little, too late, and demand debt waivers for weavers.",
        "joint_forum": "Collaborate on a global marketing strategy to revive Kerala's coir exports."
    },
    "sabarmala_crowds": {
        "gov_action": "Deploy extra police and health officials to ensure a safe and smooth pilgrimage season.",
        "opp_demands": "Criticize the lack of basic amenities and mismanagement at the base camps.",
        "joint_forum": "Propose a permanent master plan for sustainable infrastructure at the hill shrine."
    },
    "land_reforms": {
        "gov_action": "Initiate a high-level inquiry into the Harrisons Malayalam lease violations.",
        "opp_demands": "Demand immediate government takeover of all disputed plantation lands.",
        "joint_forum": "Form a bipartisan legal team to expedite the resolution of historical lease cases."
    },
    "school_it": {
        "gov_action": "Mandate Free and Open-Source Software in schools to pioneer digital education.",
        "opp_demands": "Highlight the lack of trained teachers and hardware infrastructure in rural schools.",
        "joint_forum": "Suggest a phased rollout with comprehensive training programs for educators."
    },
    "chital_fever": {
        "gov_action": "Deploy emergency healthcare units and launch statewide mosquito eradication drives.",
        "opp_demands": "Accuse the health department of negligence and demand free treatment for all.",
        "joint_forum": "Call for an all-party sanitation campaign to combat the Chikungunya outbreak."
    },
    "kseb_privatization": {
        "gov_action": "Clarify that the reorganization is for efficiency and rule out total privatization.",
        "opp_demands": "Support the KSEB unions and organize massive protests against unbundling.",
        "joint_forum": "Propose an independent regulatory review to balance consumer tariffs and board debts."
    },
    "paddy_protection": {
        "gov_action": "Strictly enforce the Wetland Conservation Act to ensure food security.",
        "opp_demands": "Argue the act penalizes poor farmers while exempting large real estate lobbies.",
        "joint_forum": "Form a committee to provide financial incentives for farmers to retain paddy cultivation."
    },
    "gulf_layoffs": {
        "gov_action": "Announce a comprehensive rehabilitation and loan package for returning NRKs.",
        "opp_demands": "Blame the state for failing to create local jobs and leaving workers vulnerable.",
        "joint_forum": "Urge the central government to establish a dedicated welfare fund for Gulf returnees."
    }
}

def get_base_issue(news_key):
    # newsKey looks like kl2001_2001_01_remittance_boom
    parts = news_key.split("_")
    # Join parts from index 3 to end
    return "_".join(parts[3:])

def main():
    # Connect to local MongoDB instance, fallback to the one in .env if needed
    # But since we're running it here, let's use the local mongodb or the remote one from .env
    from dotenv import load_dotenv
    import os
    
    env_path = os.path.join(os.path.dirname(__file__), "..", "..", "backend", ".env")
    load_dotenv(env_path)
    
    uri = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/political_sim")
    client = MongoClient(uri)
    db = client.get_default_database()
    
    print(f"Connected to database: {db.name}")
    
    news_collection = db["news_definitions"]
    
    query = {"scenarioKey": {"$in": ["kerala_2001", "kerala_2006"]}}
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
                # No comment remains standard
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
