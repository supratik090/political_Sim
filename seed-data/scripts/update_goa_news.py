import json
from pymongo import MongoClient

# Mapping of base issue keywords to handcrafted reaction texts for Goa
HANDCRAFTED_REACTIONS = {
    "tourism_growth": {
        "gov_action": "Deploy extra tourist police patrols and allocate funds to upgrade beach lighting and safety.",
        "opp_demands": "Criticize the government for ignoring local infrastructure strain and rise in drug peddling.",
        "joint_forum": "Convene a tourism stakeholder meeting to draft a sustainable carrying-capacity policy."
    },
    "mining_disputes": {
        "gov_action": "Mediate between barge unions and mining companies to resolve the freight rate deadlock.",
        "opp_demands": "Stand with the barge operators, demanding the government subsidize diesel for transporters.",
        "joint_forum": "Propose a tripartite port transport committee to fix annual freight schedules."
    },
    "political_alliance": {
        "gov_action": "Consolidate the ruling coalition by proposing a common minimum governance program.",
        "opp_demands": "Label the alliance an opportunistic power-grab and demand immediate mid-term assembly polls.",
        "joint_forum": "Propose a coalition coordination panel to resolve inter-party policy differences."
    },
    "crz_violations": {
        "gov_action": "Direct the Goa Coastal Zone Management Authority to issue demolition notices to illegal structures.",
        "opp_demands": "Accuse the government of shielding big builders while targeting traditional coastal shacks.",
        "joint_forum": "Propose a revised Coastal Zone Management Plan to balance ecology with traditional fishermen's rights."
    },
    "infrastructure_zuari": {
        "gov_action": "Enforce strict speed controls on the Zuari Bridge and deploy emergency ferry services.",
        "opp_demands": "Point out the extreme delay in building a new bridge, blaming the state for isolation of South Goa.",
        "joint_forum": "Appoint an expert engineer panel to assess bridge safety and expedite tender processes."
    },
    "garbage_sonsodo": {
        "gov_action": "Deploy fire tenders to control Sonsodo smoke and allocate funds for scientific capping.",
        "opp_demands": "Lead protests in Margao against the municipality's failure to handle waste management.",
        "joint_forum": "Propose a unified garbage treatment facility with advanced waste-to-energy technology."
    },
    "panchayat_reservations": {
        "gov_action": "Release the final ward reservation list to empower women and OBC representation in local bodies.",
        "opp_demands": "Accuse the state of Gerrymandering and manipulating ward reservation lists to favor ruling party candidates.",
        "joint_forum": "Propose an independent delimitation commission to ensure transparent ward allocation."
    },
    "portuguese_heritage": {
        "gov_action": "Seek central ASI grants to restore and protect historical monuments in Old Goa.",
        "opp_demands": "Raise concerns about the slow pace of heritage conservation and commercial encroachment near churches.",
        "joint_forum": "Draft a Heritage Zone protection master plan with local historians and church leaders."
    },
    "fishermen_clash": {
        "gov_action": "Deploy marine police to enforce the exclusive fishing zone for traditional fishermen.",
        "opp_demands": "Demand heavy penalties on commercial trawlers encroaching on near-shore waters.",
        "joint_forum": "Convene a round table of trawler owners and traditional Ramponkar unions to negotiate quotas."
    },
    "sez_scam": {
        "gov_action": "Order a high-level inquiry into the Special Economic Zone land allocations and cancel suspect deals.",
        "opp_demands": "Expose corrupt links between ministers and out-of-state developers, demanding a CBI probe.",
        "joint_forum": "Propose returning the unused SEZ land to the state industrial development corporation for local IT use."
    },
    "mining_royalties": {
        "gov_action": "Introduce a mining community development fund to directly benefit extraction-belt villages.",
        "opp_demands": "Demand that 20% of mining royalties be directly transferred to local panchayats for development.",
        "joint_forum": "Draft a mining royalty sharing bill to ensure resource revenue directly funds local schools and clinics."
    },
    "konkan_railway": {
        "gov_action": "Coordinate with the railways to build underpasses and overbridges to minimize farmland division.",
        "opp_demands": "Support farmer protests against track doubling in South Goa and demand alternative alignment.",
        "joint_forum": "Organize public hearings to address local environmental concerns and determine fair land compensation."
    },
    "casinos_mandovi": {
        "gov_action": "Impose a high entry fee for locals and outline a plan to eventually move casinos offshore.",
        "opp_demands": "Demand the immediate ban of floating casinos to protect local culture and Mandovi ecology.",
        "joint_forum": "Propose a strict gaming commission to regulate licensing, taxation, and pollution of casino vessels."
    },
    "mining_boom": {
        "gov_action": "Mandate the use of tarpaulins on iron ore trucks and spray water on transport routes.",
        "opp_demands": "Block mining transport routes to protest health hazards and demand air-quality monitoring.",
        "joint_forum": "Suggest a dedicated bypass corridor for ore trucks to keep dust away from residential zones."
    },
    "political_defections": {
        "gov_action": "Appeal to alliance partners for stability and seek a trust vote to prove assembly majority.",
        "opp_demands": "Expose defection offers and challenge the ruling coalition's moral authority to govern.",
        "joint_forum": "Convene a special legislative session to address anti-defection provisions and restore governance stability."
    },
    "mega_resorts": {
        "gov_action": "Declare Morjim beach an eco-sensitive zone and ban permanent construction near turtle nesting grounds.",
        "opp_demands": "Criticize the tourism department for permitting mega resorts that destroy fragile coastal habitats.",
        "joint_forum": "Propose a community-led eco-tourism model that recruits locals to protect the turtle nesting habitats."
    },
    "infrastructure_mopa": {
        "gov_action": "Fast-track land acquisition for Mopa Airport to establish a state-of-the-art aviation hub.",
        "opp_demands": "Lead protests in Pernem demanding higher compensation and secure jobs for displaced landholders.",
        "joint_forum": "Convene an advisory board of North and South Goa tourism stakeholders to balance airport usage."
    },
    "garbage_sonsodo_update": {
        "gov_action": "Appoint a special administrator to oversee the installation of the solid waste plant.",
        "opp_demands": "Demand the resignation of the urban development minister over the persistent dump yard crisis.",
        "joint_forum": "Convene a Margao civil society round table to plan decentralized waste sorting initiatives."
    },
    "assembly_elections": {
        "gov_action": "Announce the scrapping of controversial land-conversion zones in Regional Plan 2021.",
        "opp_demands": "Expose builder-politician nexus behind the regional plan and promise a new grassroots plan.",
        "joint_forum": "Convene village level panels to redraft the state development plan from the ground up."
    },
    "konkani_marathi": {
        "gov_action": "Provide government grants to primary schools teaching in Konkani and Marathi languages.",
        "opp_demands": "Support parent associations demanding parent choice for English-medium primary school grants.",
        "joint_forum": "Propose a bilingual language policy that balances mother-tongue education with English proficiency."
    },
    "fishermen_trawlers": {
        "gov_action": "Enforce the 61-day monsoon fishing ban strictly to protect marine breeding cycles.",
        "opp_demands": "Expose violations by out-of-state trawlers and accuse local fisheries officials of taking bribes.",
        "joint_forum": "Form a joint surveillance squad comprising fisheries staff and traditional fishermen representatives."
    },
    "tourist_scam": {
        "gov_action": "Coordinate with FEMA to investigate illegal benami property acquisitions in coastal villages.",
        "opp_demands": "Expose local politicians aiding foreigners in circumventing agricultural land buyout laws.",
        "joint_forum": "Propose a land registration bill requiring residency proof for purchasing rural property."
    },
    "nh17_widening": {
        "gov_action": "Modify the highway layout to reduce the demolition of ancestral houses and local shops.",
        "opp_demands": "Protest alongside local committees against the high-handed eviction methods of NHAI.",
        "joint_forum": "Suggest a joint bypass routing solution to preserve village heritage while widening lanes."
    },
    "eco_tourism": {
        "gov_action": "Approve low-impact nature resorts in Netravali and Cotigao to boost hinterland tourism.",
        "opp_demands": "Oppose private commercial exploitation of forest reserves under the guise of eco-tourism.",
        "joint_forum": "Draft a forest community tourism policy that ensures all jobs and management remain with local tribes."
    }
}

def get_base_issue(news_key):
    # newsKey looks like ga2001_2001_01_tourism_growth or ga2006_2008_02_mining_boom
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
    
    query = {"scenarioKey": {"$in": ["goa_2001", "goa_2006"]}}
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
