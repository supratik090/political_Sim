import json
from pymongo import MongoClient

# Mapping of base issue keywords to handcrafted reaction texts for Delhi
HANDCRAFTED_REACTIONS = {
    "cng_transition": {
        "gov_action": "Provide government subsidies for CNG kit installations and fast-track CNG dispensing stations.",
        "opp_demands": "Protest the chaotic transition plan and demand compensation for stranded commuters and drivers.",
        "joint_forum": "Convene a panel of transporters, environmentalists, and officials to coordinate a phased transition."
    },
    "metro_phase_1": {
        "gov_action": "Expedite Metro construction and expand feeder bus connectivity for a seamless transit network.",
        "opp_demands": "Criticize delays, high project costs, and high fares that isolate lower-income commuters.",
        "joint_forum": "Set up a unified transport board to integrate Metro planning with existing road networks."
    },
    "power_privatization": {
        "gov_action": "Back privatization to eliminate power theft and invest in upgrading the transmission grid.",
        "opp_demands": "Accuse the government of selling public assets and failing to prevent private monopoly pricing.",
        "joint_forum": "Establish a strict electricity regulatory commission to monitor discom tariffs and performance."
    },
    "slum_demolition": {
        "gov_action": "Relocate affected families to outer Delhi colonies and clear the riverbed for environmental restoration.",
        "opp_demands": "Condemn the evictions as inhumane, demanding in-situ rehabilitation and basic amenities.",
        "joint_forum": "Form a rehabilitation task force to plan sustainable resettlement with livelihoods."
    },
    "water_tankers": {
        "gov_action": "Deploy DJB tankers to scarcity zones under strict police monitoring to bypass unauthorized networks.",
        "opp_demands": "Expose official collusion with the water tanker mafia and demand immediate piped water supply.",
        "joint_forum": "Propose a cooperative local water management committee and rainwater harvesting mandates."
    },
    "unauthorized_colonies": {
        "gov_action": "Announce provisional development schemes and lay pipelines in unauthorized colonies.",
        "opp_demands": "Demand complete and unconditional regularization along with registry rights for residents.",
        "joint_forum": "Draft a comprehensive town planning bill to regularize colonies with basic civic amenities."
    },
    "blueline_buses": {
        "gov_action": "Enforce strict speed governors and cancel permits of repeat-offender Blueline bus operators.",
        "opp_demands": "Blame the administration's regulatory failure for rising road fatalities and demand a state-run replacement.",
        "joint_forum": "Propose a public-private partnership model to phase out Bluelines with corporate-managed clusters."
    },
    "industry_relocation": {
        "gov_action": "Establish dedicated industrial parks in Bawana and Narela to facilitate smooth relocation.",
        "opp_demands": "Protest the loss of livelihood for lakhs of industrial workers and demand transition support.",
        "joint_forum": "Form a joint council of trade associations and environmental experts to structure a compensation package."
    },
    "delhi_blasts": {
        "gov_action": "Set up high-alert checkpoints in busy markets and deploy anti-sabotage police teams.",
        "opp_demands": "Condemn the massive security failure and demand immediate relief packages for blast victims.",
        "joint_forum": "Coordinate all-party peace marches to maintain communal harmony and support law enforcement."
    },
    "municipal_reforms": {
        "gov_action": "Push for trifurcation of the MCD to streamline administration and local service delivery.",
        "opp_demands": "Accuse the ruling party of trying to weaken municipal power for political gains.",
        "joint_forum": "Convene a round table of council members to negotiate administrative reforms without division."
    },
    "flyover_boom": {
        "gov_action": "Celebrate the flyover boom for cutting commute times and boosting Delhi's urban aesthetics.",
        "opp_demands": "Point out that flyovers cater only to private car owners while ignoring pedestrian and cyclist safety.",
        "joint_forum": "Propose a comprehensive urban mobility plan focusing on public transit and pedestrian paths."
    },
    "school_infrastructure": {
        "gov_action": "Launch a school modernization drive to upgrade classrooms, labs, and sanitary facilities.",
        "opp_demands": "Expose persistent vacancies in teacher posts and lack of desks in outer Delhi schools.",
        "joint_forum": "Suggest a joint educational audit committee involving parent-teacher associations."
    },
    "cwg_scam": {
        "gov_action": "Order a time-bound administrative inquiry and promise strict action against corrupt officials.",
        "opp_demands": "Demand a CBI probe into inflated project contracts and the immediate resignation of organizers.",
        "joint_forum": "Establish a bipartisan oversight committee to monitor CWG budget spending and project delivery."
    },
    "metro_phase_2": {
        "gov_action": "Celebrate the expansion of Metro Phase 2 as a massive leap for NCR integration and green transit.",
        "opp_demands": "Demand that the state subsidize multi-modal ticketing to make Metro affordable for daily wage earners.",
        "joint_forum": "Propose a joint NCR transit authority to coordinate regional bus networks and metro feeds."
    },
    "brt_corridor": {
        "gov_action": "Defend the BRT corridor as a progressive step giving priority to public buses over private cars.",
        "opp_demands": "Lead protests against the massive traffic bottlenecks caused by the dedicated bus lanes.",
        "joint_forum": "Convene traffic safety experts to redesign the corridor safety features and pedestrian access."
    },
    "delhi_blasts_2008": {
        "gov_action": "Create the Special Cell Counter-Terrorism unit and fast-track installation of CCTVs across NCR.",
        "opp_demands": "Blame intelligence complacency and demand immediate accountability of the home department.",
        "joint_forum": "Propose a unified security coordination committee between Delhi Police and NCR state borders."
    },
    "colony_regularization": {
        "gov_action": "Distribute provisional regularization certificates to ensure registry rights and basic services.",
        "opp_demands": "Label provisional certificates a political stunt before elections and demand full legal status.",
        "joint_forum": "Call for a streamlined spatial mapping process to finalize boundaries of regularized zones."
    },
    "power_tariffs": {
        "gov_action": "Subsidize power bills for low-consumption domestic consumers using state budget funds.",
        "opp_demands": "Support Resident Welfare Associations (RWAs) in protesting arbitrary tariff hikes by private discoms.",
        "joint_forum": "Advocate for a public DERC tariff review petition and mandatory CAG audit of discom accounts."
    },
    "yamuna_cleaning": {
        "gov_action": "Construct new Sewage Treatment Plants (STPs) and crack down on untreated industrial discharge.",
        "opp_demands": "Expose the failure of the Yamuna Action Plan despite crores of public funds spent.",
        "joint_forum": "Propose a statutory Yamuna River Zone Authority to integrate ecological restoration."
    },
    "mcd_sealing": {
        "gov_action": "Enact a provisional moratorium on sealing while seeking amendments to the Delhi Master Plan.",
        "opp_demands": "Support the striking merchants and accuse the corporation of killing local businesses.",
        "joint_forum": "Call for a consensus-based zoning policy to regularize non-polluting mixed-land usage."
    },
    "low_floor_buses": {
        "gov_action": "Procure disabled-friendly air-conditioned low-floor buses to modernize public transit.",
        "opp_demands": "Raise concerns about the high maintenance costs and recent fire incidents in DTC low-floor fleets.",
        "joint_forum": "Propose a dedicated transit safety board to investigate vehicle reliability and driver training."
    },
    "hospital_swine_flu": {
        "gov_action": "Establish dedicated isolation wards in all government hospitals and stockpile Tamiflu.",
        "opp_demands": "Expose the extreme shortage of ventilator beds and test kits in neighborhood clinics.",
        "joint_forum": "Launch a joint public health campaign to spread awareness and open free screening centers."
    },
    "admission_nursery": {
        "gov_action": "Digitize the nursery admission system and implement a transparent lottery for EWS quotas.",
        "opp_demands": "Accuse elite private schools of fabricating income certificates and ignoring the EWS mandate.",
        "joint_forum": "Form a legislative committee to draft strict regulatory guidelines for nursery school admission criteria."
    },
    "cwg_opening": {
        "gov_action": "Celebrate the global prestige of hosting the 2010 Games and display Delhi's modern infrastructure.",
        "opp_demands": "Highlight the massive displacement of street vendors and legacy costs of unused stadiums.",
        "joint_forum": "Draft a post-games legacy plan to utilize CWG infrastructure for public sports training."
    }
}

def get_base_issue(news_key):
    # newsKey looks like dl2001_2001_01_cng_transition
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
    
    query = {"scenarioKey": {"$in": ["delhi_2001", "delhi_2006"]}}
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
