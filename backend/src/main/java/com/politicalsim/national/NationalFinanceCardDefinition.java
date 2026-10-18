package com.politicalsim.national;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class NationalFinanceCardDefinition {

    private String id;
    private String name;
    private String icon;
    private String category;
    private String tagline;
    private String description;
    private String treasuryRating;
    private String cadreRating;
    private String moraleRating;
    private String scrutinyRating;
    private String strategicNote;

    private double pctFunds;
    private double pctWorkers;
    private double pctVolunteers;
    private double pctDonors;
    private int deltaCorruption;
    private int deltaMorale;
    private boolean megaFinance;
    private boolean grassroots;

    public NationalFinanceCardDefinition() {}

    public NationalFinanceCardDefinition(
            String id, String name, String icon, String category, String tagline, String description,
            String treasuryRating, String cadreRating, String moraleRating, String scrutinyRating, String strategicNote,
            double pctFunds, double pctWorkers, double pctVolunteers, double pctDonors,
            int deltaCorruption, int deltaMorale, boolean megaFinance, boolean grassroots) {
        this.id = id;
        this.name = name;
        this.icon = icon;
        this.category = category;
        this.tagline = tagline;
        this.description = description;
        this.treasuryRating = treasuryRating;
        this.cadreRating = cadreRating;
        this.moraleRating = moraleRating;
        this.scrutinyRating = scrutinyRating;
        this.strategicNote = strategicNote;
        this.pctFunds = pctFunds;
        this.pctWorkers = pctWorkers;
        this.pctVolunteers = pctVolunteers;
        this.pctDonors = pctDonors;
        this.deltaCorruption = deltaCorruption;
        this.deltaMorale = deltaMorale;
        this.megaFinance = megaFinance;
        this.grassroots = grassroots;
    }

    public static List<NationalFinanceCardDefinition> getAllCards() {
        List<NationalFinanceCardDefinition> list = new ArrayList<>();

        list.add(new NationalFinanceCardDefinition(
            "GRASSROOTS_COLLECTION",
            "Grassroots Collection Drive",
            "🌾",
            "Grassroots Public",
            "Door-to-door cadre outreach and public micro-coupons",
            "Mobilize party workers across neighborhood wards to collect small public donations. Reconnects cadre directly with ordinary voters.",
            "Modest Gain",
            "Moderate Influx",
            "Morale Boost",
            "Clean & Transparent",
            "Clean public micro-donations. Cools down corporate greed heat and lowers corruption.",
            0.10, 0.02, 0.15, 0.20,
            -4, 5, false, true
        ));

        list.add(new NationalFinanceCardDefinition(
            "MEMBERSHIP_DRIVE",
            "Mass Membership Drive",
            "👥",
            "Grassroots Public",
            "Mass enrollment across bazaars, campuses, and rural blocks",
            "Launch a nationwide missed-call and door-to-door party enrollment campaign with token subscription fees.",
            "Token Gain",
            "High Cadre Growth",
            "High Inspiration",
            "Clean & Transparent",
            "Expands volunteer foot soldiers and lowers corruption while cooling scrutiny heat.",
            0.05, 0.10, 0.25, 0.15,
            -2, 7, false, true
        ));

        list.add(new NationalFinanceCardDefinition(
            "COLLEGE_ELECTIONS",
            "College & Campus Elections",
            "🎓",
            "Youth Wing",
            "Deploy student wings to contest university union councils",
            "Fund and fight aggressive student union elections across major universities. Zero immediate revenue, but ignites fierce youthful dedication.",
            "Operational Expense",
            "Explosive Youth Surge",
            "Massive Inspiration",
            "Clean & Idealistic",
            "Zero funds this term, but surges passionate youth volunteers and national party morale.",
            -0.05, 0.06, 0.22, 0.0,
            -2, 15, false, true
        ));

        list.add(new NationalFinanceCardDefinition(
            "OPEN_PARTY_OFFICE",
            "Open District Party Offices",
            "🏢",
            "Infrastructure",
            "Inaugurate permanent district and taluka secretariat hubs",
            "Commit capital funds to establish permanent local party secretariats and meeting halls across key districts.",
            "Capital Investment",
            "Strong Cadre Anchor",
            "High Pride & Confidence",
            "Institutional Growth",
            "Significant immediate expense, but permanently establishes local workers and office bearers.",
            -0.15, 0.12, 0.18, 0.10,
            0, 10, false, false
        ));

        list.add(new NationalFinanceCardDefinition(
            "TRADE_UNION_ELECTIONS",
            "Trade Union Affiliation Drive",
            "⚙️",
            "Organized Labor",
            "Organize factory, transport, and dock worker union committees",
            "Contest leadership elections in major organized labor and transport unions. Strengthens party muscle for strikes and mass street rallies.",
            "Modest Levy Gain",
            "Massive Worker Surge",
            "Solidarity Surge",
            "Moderate Scrutiny",
            "Brings a disciplined influx of blue-collar workers and strike capability.",
            0.04, 0.15, 0.14, 0.08,
            2, 8, false, false
        ));

        list.add(new NationalFinanceCardDefinition(
            "MEDIA_OUTREACH",
            "Prime-Time Media Blitz",
            "📺",
            "PR & Broadcast",
            "Broadcast television advertisements, digital campaigns, and print op-eds",
            "Purchase high-impact news network ad slots and run a targeted digital campaign to dominate public news cycles.",
            "Heavy Advertising Cost",
            "Moderate Digital Influx",
            "High Public Visibility",
            "Paid Media Scrutiny",
            "Spends treasury reserves to boost national visibility, volunteers, and online supporters.",
            -0.10, 0.02, 0.12, 0.12,
            2, 6, false, false
        ));

        list.add(new NationalFinanceCardDefinition(
            "PRIVATE_DONOR_PARTY",
            "Private High-Worth Gala",
            "🍷",
            "Elite Donors",
            "Exclusive private dinner with wealthy patrons and industrialists",
            "Host closed-door dinner sessions for high-net-worth business owners and property magnates to solicit major political contributions.",
            "High Windfall",
            "None",
            "Minor Disillusionment",
            "Moderate Scrutiny Risk",
            "Fast major treasury injection, but starts accumulating corporate dependency heat.",
            0.25, 0.0, 0.0, 0.04,
            6, 1, true, false
        ));

        list.add(new NationalFinanceCardDefinition(
            "INVESTOR_SUMMIT",
            "National Investor Conclave",
            "💼",
            "Big Business",
            "Flagship economic conclave pitching industry policy reforms",
            "Bring together national conglomerates and financial houses for a summit pitching favorable reform blueprints in exchange for deep election funding.",
            "Substantial Windfall",
            "Liaison Cell Only",
            "Cadre Unease",
            "High Scrutiny Alert",
            "Heavy corporate funding influx. Increases corporate greed heat and media scrutiny.",
            0.40, 0.01, 0.0, 0.08,
            10, 2, true, false
        ));

        list.add(new NationalFinanceCardDefinition(
            "ELECTORAL_BONDS",
            "Electoral Bonds Encashed",
            "🏛️",
            "Institutional Cash",
            "Encash anonymous institutional corporate banking vouchers",
            "Redeem major tranches of opaque corporate electoral bonds through banking channels into the party central treasury.",
            "Massive Windfall",
            "None",
            "Cadre Cynicism",
            "Extreme Public Scrutiny",
            "Massive capital windfall. Incurs heavy corruption points and sharp crony heat penalties.",
            0.60, 0.0, 0.0, 0.02,
            18, -4, true, false
        ));

        return list;
    }

    public static NationalFinanceCardDefinition findById(String id) {
        if (id == null) return null;
        for (NationalFinanceCardDefinition card : getAllCards()) {
            if (card.getId().equalsIgnoreCase(id)) return card;
        }
        return null;
    }

    public static List<String> pickRandomVisibleCardIds(int count) {
        List<NationalFinanceCardDefinition> all = getAllCards();
        List<String> ids = new ArrayList<>();
        for (NationalFinanceCardDefinition c : all) {
            ids.add(c.getId());
        }
        Collections.shuffle(ids, new Random());
        return ids.subList(0, Math.min(count, ids.size()));
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getIcon() { return icon; }
    public void setIcon(String icon) { this.icon = icon; }
    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }
    public String getTagline() { return tagline; }
    public void setTagline(String tagline) { this.tagline = tagline; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getTreasuryRating() { return treasuryRating; }
    public void setTreasuryRating(String treasuryRating) { this.treasuryRating = treasuryRating; }
    public String getCadreRating() { return cadreRating; }
    public void setCadreRating(String cadreRating) { this.cadreRating = cadreRating; }
    public String getMoraleRating() { return moraleRating; }
    public void setMoraleRating(String moraleRating) { this.moraleRating = moraleRating; }
    public String getScrutinyRating() { return scrutinyRating; }
    public void setScrutinyRating(String scrutinyRating) { this.scrutinyRating = scrutinyRating; }
    public String getStrategicNote() { return strategicNote; }
    public void setStrategicNote(String strategicNote) { this.strategicNote = strategicNote; }
    public double getPctFunds() { return pctFunds; }
    public void setPctFunds(double pctFunds) { this.pctFunds = pctFunds; }
    public double getPctWorkers() { return pctWorkers; }
    public void setPctWorkers(double pctWorkers) { this.pctWorkers = pctWorkers; }
    public double getPctVolunteers() { return pctVolunteers; }
    public void setPctVolunteers(double pctVolunteers) { this.pctVolunteers = pctVolunteers; }
    public double getPctDonors() { return pctDonors; }
    public void setPctDonors(double pctDonors) { this.pctDonors = pctDonors; }
    public int getDeltaCorruption() { return deltaCorruption; }
    public void setDeltaCorruption(int deltaCorruption) { this.deltaCorruption = deltaCorruption; }
    public int getDeltaMorale() { return deltaMorale; }
    public void setDeltaMorale(int deltaMorale) { this.deltaMorale = deltaMorale; }
    public boolean isMegaFinance() { return megaFinance; }
    public void setMegaFinance(boolean megaFinance) { this.megaFinance = megaFinance; }
    public boolean isGrassroots() { return grassroots; }
    public void setGrassroots(boolean grassroots) { this.grassroots = grassroots; }
}
