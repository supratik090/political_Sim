package com.politicalsim.national;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class NationalStateIssueDefinition {
    private String id;
    private String stateCode;
    private String title;
    private String icon;
    private String category;
    private String description;
    private double baseImpact;

    public NationalStateIssueDefinition() {}

    public NationalStateIssueDefinition(String id, String stateCode, String title, String icon, String category, String description, double baseImpact) {
        this.id = id;
        this.stateCode = stateCode;
        this.title = title;
        this.icon = icon;
        this.category = category;
        this.description = description;
        this.baseImpact = baseImpact;
    }

    public static List<Map<String, Object>> getTacticalActions() {
        List<Map<String, Object>> actions = new ArrayList<>();

        actions.add(Map.of(
            "key", "RALLY",
            "label", "Mass Public Rally",
            "icon", "🚩",
            "costCr", 1.0,
            "baseSupportDelta", 1.0,
            "description", "Mobilize thousands in the state capital or major district headquarters to demonstrate electoral strength."
        ));
        actions.add(Map.of(
            "key", "AGITATION",
            "label", "Street Agitation & Blockade",
            "icon", "📢",
            "costCr", 0.5,
            "baseSupportDelta", 1.4,
            "description", "Aggressive confrontation on regional injustice, drawing aggressive youth and cadre."
        ));
        actions.add(Map.of(
            "key", "MEDIA_DEBATE",
            "label", "Regional Media Blitz",
            "icon", "📺",
            "costCr", 0.4,
            "baseSupportDelta", 0.7,
            "description", "Saturate vernacular newspapers and prime-time regional debate channels."
        ));
        actions.add(Map.of(
            "key", "DHARNA",
            "label", "Indefinite Collectorate Dharna",
            "icon", "🪑",
            "costCr", 0.3,
            "baseSupportDelta", 0.9,
            "description", "Disciplined peaceful sit-in at government offices demanding administrative redressal."
        ));
        actions.add(Map.of(
            "key", "BANDH",
            "label", "State-Wide Commercial Bandh",
            "icon", "🚫",
            "costCr", 1.2,
            "baseSupportDelta", 2.0,
            "description", "Complete shutdown of transport and markets. Massive display of grassroots muscle."
        ));
        actions.add(Map.of(
            "key", "PADAYATRA",
            "label", "Grassroots Padayatra",
            "icon", "🚶",
            "costCr", 0.6,
            "baseSupportDelta", 1.2,
            "description", "A foot march through villages, directly listening to grievance and recruiting rural volunteers."
        ));
        actions.add(Map.of(
            "key", "GHERAO",
            "label", "Secretariat Gherao",
            "icon", "✊",
            "costCr", 0.5,
            "baseSupportDelta", 1.3,
            "description", "Surround state ministry offices to bring administrative machinery to a standstill."
        ));
        actions.add(Map.of(
            "key", "RATH_YATRA",
            "label", "High-Voltage Rath Yatra",
            "icon", "🛞",
            "costCr", 2.2,
            "baseSupportDelta", 2.2,
            "description", "State-wide motorized yatra with speeches across dozens of assembly constituencies."
        ));
        actions.add(Map.of(
            "key", "JAN_SABHA",
            "label", "Constituency Jan Sabha",
            "icon", "👥",
            "costCr", 0.4,
            "baseSupportDelta", 0.8,
            "description", "Town hall gatherings focused on local civic corruption and public infrastructure."
        ));
        actions.add(Map.of(
            "key", "MEMORANDUM",
            "label", "Memorandum to Governor",
            "icon", "📜",
            "costCr", 0.1,
            "baseSupportDelta", 0.5,
            "description", "High-level delegation submitting constitutional petition, gaining institutional gravitas."
        ));

        return actions;
    }

    public static List<NationalStateIssueDefinition> getIssuesForState(String stateCode) {
        List<NationalStateIssueDefinition> list = new ArrayList<>();
        if (stateCode == null) return list;

        String sc = stateCode.toUpperCase().trim();
        switch (sc) {
            case "UP":
            case "UTTAR PRADESH":
                list.add(new NationalStateIssueDefinition(
                    "UP_CASTE_VIOLENCE", "UP",
                    "Caste Violence & Social Justice", "⚖️", "SOCIAL_JUSTICE",
                    "Escalating inter-caste violence, Dalit atrocities, and friction over representation in state bureaucracy.",
                    1.4
                ));
                list.add(new NationalStateIssueDefinition(
                    "UP_LAW_ORDER", "UP",
                    "Law & Order Collapse & Mafia Raj", "🚔", "SECURITY",
                    "Organized extortion gangs, political patronage for crime lords, and rampant highway robberies.",
                    1.5
                ));
                list.add(new NationalStateIssueDefinition(
                    "UP_AGRARIAN_DISTRESS", "UP",
                    "Sugarcane Arrears & Agrarian Distress", "🌾", "AGRICULTURE",
                    "Millions owed to sugarcane growers by defaulting private sugar mills, triggering farmer demonstrations.",
                    1.3
                ));
                list.add(new NationalStateIssueDefinition(
                    "UP_MANDAL_POLITICS", "UP",
                    "Identity Polarization & Reservation Clashes", "🗳️", "POLITICAL",
                    "High-voltage electoral mobilization around backward class sub-quotas and upper caste backlash.",
                    1.2
                ));
                list.add(new NationalStateIssueDefinition(
                    "UP_POWER_CRISIS", "UP",
                    "Chronic Power Deficit & Grid Collapse", "⚡", "INFRASTRUCTURE",
                    "Severe load-shedding of 16+ hours a day in Purvanchal and Bundelkhand, paralyzing local workshops.",
                    1.1
                ));
                break;

            case "BIHAR":
                list.add(new NationalStateIssueDefinition(
                    "BIHAR_JUNGLE_RAJ", "BIHAR",
                    "'Jungle Raj' & Lawlessness", "🚨", "SECURITY",
                    "Kidnapping for ransom operates as a parallel industry with alleged political impunity across Patna and districts.",
                    1.6
                ));
                list.add(new NationalStateIssueDefinition(
                    "BIHAR_CASTE_POLARIZATION", "BIHAR",
                    "Caste Polarization & Private Senas", "⚔️", "SOCIAL_JUSTICE",
                    "Feudal private militias and armed agrarian uprisings clash in central Bihar's rural heartland.",
                    1.5
                ));
                list.add(new NationalStateIssueDefinition(
                    "BIHAR_FLOOD_DISASTER", "BIHAR",
                    "Kosi Flood Devastation & Embankment Breaches", "🌊", "DISASTER",
                    "Annual monsoon inundations sweep North Bihar villages amid corruption allegations in embankment contracts.",
                    1.3
                ));
                list.add(new NationalStateIssueDefinition(
                    "BIHAR_EDUCATION_CRISIS", "BIHAR",
                    "Education Decay & Examination Paper Leaks", "📚", "EDUCATION",
                    "Teacher absenteeism, ghost colleges, and widespread cheating scandals erode state degree credibility.",
                    1.2
                ));
                list.add(new NationalStateIssueDefinition(
                    "BIHAR_INFRA_COLLAPSE", "BIHAR",
                    "Potholed Highways & Healthcare Collapse", "🏥", "INFRASTRUCTURE",
                    "Dilapidated National and State highways isolate remote blocks, while primary healthcare centers lack doctors.",
                    1.4
                ));
                break;

            case "MAHARASHTRA":
                list.add(new NationalStateIssueDefinition(
                    "MH_VIDARBHA_FARMER_CRISIS", "MAHARASHTRA",
                    "Vidarbha Agrarian Crisis & Farmer Suicides", "🌾", "AGRICULTURE",
                    "BT Cotton crop failures, spiraling moneylender debts, and unseasonal weather trigger alarming suicide rates.",
                    1.6
                ));
                list.add(new NationalStateIssueDefinition(
                    "MH_MUMBAI_INFRA_STRAIN", "MAHARASHTRA",
                    "Mumbai Infrastructure Strain & Slum Transit", "🚆", "URBAN",
                    "Overcrowded local trains, slum rehabilitation standoffs, and seasonal flood vulnerability in the financial capital.",
                    1.3
                ));
                list.add(new NationalStateIssueDefinition(
                    "MH_COALITION_FRICTION", "MAHARASHTRA",
                    "Coalition Instability & Alliance Friction", "🤝", "POLITICAL",
                    "Constant skirmishes between Congress-NCP partners and vocal regional resistance from the Shiv Sena-BJP front.",
                    1.2
                ));
                list.add(new NationalStateIssueDefinition(
                    "MH_MILL_WORKERS_CRISIS", "MAHARASHTRA",
                    "Girni Kamgar (Mill Workers) Displacement", "🏭", "LABOR",
                    "Redevelopment of Central Mumbai textile mill lands into luxury complexes leaves thousands of workers unpaid.",
                    1.3
                ));
                list.add(new NationalStateIssueDefinition(
                    "MH_REGIONAL_IMBALANCE", "MAHARASHTRA",
                    "Development Gap: Western MH vs Marathwada", "⚖️", "ECONOMY",
                    "Disproportionate allocation of state irrigation and industrial budgets favoring sugar belt baronies.",
                    1.1
                ));
                break;

            case "WEST_BENGAL":
                list.add(new NationalStateIssueDefinition(
                    "WB_INDUSTRIAL_STAGNATION", "WEST_BENGAL",
                    "Industrial Flight & De-industrialization", "🏭", "ECONOMY",
                    "Closed jute mills, militant unionism, and flight of private manufacturing capital trigger acute youth joblessness.",
                    1.4
                ));
                list.add(new NationalStateIssueDefinition(
                    "WB_LAND_ACQUISITION_TENSIONS", "WEST_BENGAL",
                    "Agrarian Land Rights & Peasant Anxiety", "🌾", "AGRICULTURE",
                    "Operation Barga legacy clashes with proposals for industrial land acquisition in fertile multi-crop belts.",
                    1.5
                ));
                list.add(new NationalStateIssueDefinition(
                    "WB_POLITICAL_CLASHES", "WEST_BENGAL",
                    "Cadre Hegemony & Rural Political Clashes", "⚔️", "SECURITY",
                    "Intense village-level turf wars between Left Front cadres and Trinamool Congress activists.",
                    1.3
                ));
                list.add(new NationalStateIssueDefinition(
                    "WB_BORDER_INFILTRATION", "WEST_BENGAL",
                    "Porous Border Smuggling & River Erosion", "🌊", "BORDER",
                    "Farakka riverbank erosion submerges border villages while unfenced riverine stretches fuel security concerns.",
                    1.2
                ));
                list.add(new NationalStateIssueDefinition(
                    "WB_URBAN_UNEMPLOYMENT", "WEST_BENGAL",
                    "Educated Youth Unemployment & Brain Drain", "🎓", "LABOR",
                    "Scarcity of modern service and IT jobs in Kolkata pushes top college graduates out of the state.",
                    1.2
                ));
                break;

            case "RAJASTHAN":
                list.add(new NationalStateIssueDefinition(
                    "RJ_DROUGHT_DISTRESS", "RAJASTHAN",
                    "Chronic Thar Drought & Groundwater Depletion", "☀️", "ENVIRONMENT",
                    "Back-to-back monsoon failures trigger severe cattle mortality and massive drinking water distress across desert districts.",
                    1.5
                ));
                list.add(new NationalStateIssueDefinition(
                    "RJ_CASTE_RESERVATION_TENSIONS", "RAJASTHAN",
                    "Caste Reservation & Social Agitations", "⚖️", "SOCIAL",
                    "Competing OBC and ST inclusion demands spark highway and railway blockades between regional agrarian communities.",
                    1.4
                ));
                list.add(new NationalStateIssueDefinition(
                    "RJ_FARM_POWER_CRISIS", "RAJASTHAN",
                    "Agricultural Power Cuts & Tubewell Tariffs", "⚡", "ENERGY",
                    "Frequent 8-hour rural power cuts during Rabi sowing season cause angry farmers to gherao electricity substations.",
                    1.3
                ));
                list.add(new NationalStateIssueDefinition(
                    "RJ_MINING_ILLEGALITIES", "RAJASTHAN",
                    "Aravalli Illegal Stone & Marble Mining", "⛰️", "ENVIRONMENT",
                    "Unchecked quarrying degrades ecologically fragile Aravalli hills and pollutes groundwater near marble clusters.",
                    1.2
                ));
                list.add(new NationalStateIssueDefinition(
                    "RJ_HERITAGE_TOURISM_STAGNATION", "RAJASTHAN",
                    "Tourism Infrastructure & Artisan Stagnation", "🏰", "ECONOMY",
                    "Neglected regional forts and low minimum earnings for desert folk musicians and block-print artisans.",
                    1.1
                ));
                break;

            case "ASSAM":
                list.add(new NationalStateIssueDefinition(
                    "AS_BRAHMAPUTRA_FLOODS", "ASSAM",
                    "Catastrophic Brahmaputra Flood Inundation", "🌊", "DISASTER",
                    "Annual monsoon floods wash away thousands of riverine char hamlets and submerge Kaziranga national park.",
                    1.6
                ));
                list.add(new NationalStateIssueDefinition(
                    "AS_IMMIGRATION_NRC", "ASSAM",
                    "Undocumented Immigration & Assam Accord Grievance", "📜", "CITIZENSHIP",
                    "Demands for full implementation of the 1985 Assam Accord to protect indigenous cultural and economic identity.",
                    1.5
                ));
                list.add(new NationalStateIssueDefinition(
                    "AS_TEA_TRIBE_DISTRESS", "ASSAM",
                    "Tea Garden Labor Wages & Healthcare Crisis", "🍵", "LABOR",
                    "Low statutory cash wages, poor sanitation, and maternal mortality across British-era plantation lines.",
                    1.3
                ));
                list.add(new NationalStateIssueDefinition(
                    "AS_INSURGENCY_PEACE_TALKS", "ASSAM",
                    "Insurgency Ceasefires & Infrastructure Security", "🕊️", "SECURITY",
                    "Extortion threats and volatile peace negotiations with armed militant factions along the oil pipeline belt.",
                    1.4
                ));
                list.add(new NationalStateIssueDefinition(
                    "AS_ETHNIC_AUTONOMY", "ASSAM",
                    "Tribal Autonomy & Sixth Schedule Decentralization", "🛡️", "GOVERNANCE",
                    "Demands for increased developmental funds and administrative powers across Bodoland and hill autonomous councils.",
                    1.2
                ));
                break;

            case "TAMIL_NADU":
                list.add(new NationalStateIssueDefinition(
                    "TN_CAUVERY_WATER_DISPUTE", "TAMIL_NADU",
                    "Cauvery Water Sharing Standoff with Karnataka", "💧", "WATER",
                    "Upstream storage disputes in Karnataka leave Delta paddy farmers dry, precipitating statewide bandhs.",
                    1.6
                ));
                list.add(new NationalStateIssueDefinition(
                    "TN_FREEBIES_WELFARE_RIVALRY", "TAMIL_NADU",
                    "Competitive Welfare Populism & Public Debt", "🎁", "WELFARE",
                    "Escalating election promises of free consumer durables and cash transfers stretching state fiscal health.",
                    1.4
                ));
                list.add(new NationalStateIssueDefinition(
                    "TN_DRAVIDIAN_LANGUAGE_IDENTITY", "TAMIL_NADU",
                    "Linguistic Federalism & Anti-Hindi Imposition", "🗣️", "IDENTITY",
                    "Vocal resistance to centralized uniform educational curricula and staunch defense of Tamil classical autonomy.",
                    1.3
                ));
                list.add(new NationalStateIssueDefinition(
                    "TN_SRI_LANKAN_TAMIL_ISSUE", "TAMIL_NADU",
                    "Fishermen Arrests & Sri Lankan Tamil Crisis", "🇱🇰", "GEOPOLITICS",
                    "Maritime boundary arrests of Rameswaram fishermen by the Sri Lankan Navy and welfare of refugee camps.",
                    1.4
                ));
                list.add(new NationalStateIssueDefinition(
                    "TN_TEXTILE_POWER_CRISIS", "TAMIL_NADU",
                    "Tirupur Textile Export Squeeze & Power Deficit", "⚡", "INDUSTRY",
                    "Severe load-shedding and high effluent treatment costs undermining global competitiveness of knitwear exporters.",
                    1.2
                ));
                break;

            default:
                break;
        }

        return list;
    }

    // Getters
    public String getId() { return id; }
    public String getStateCode() { return stateCode; }
    public String getTitle() { return title; }
    public String getIcon() { return icon; }
    public String getCategory() { return category; }
    public String getDescription() { return description; }
    public double getBaseImpact() { return baseImpact; }
}
