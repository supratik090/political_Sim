package com.politicalsim.content;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "national_themes")
public class NationalTheme {

    @Id
    private String id;
    private String themeKey;
    private String title;
    private String icon = "💼";
    private String category = "ECONOMIC"; // e.g. ECONOMIC, SOCIAL_JUSTICE, DEVELOPMENT
    private String themeType = "AGITATION"; // "AGITATION" (Opposition) or "GOVERNANCE" (Ruling/Government)
    private String description;
    private List<Integer> activeEras = new ArrayList<>();
    private int streakTargetMin = 3;
    private int streakTargetMax = 6;

    // Supported actions map: actionKey -> effect definition
    // Keys: RALLY, AGITATION, MEDIA_DEBATE, DHARNA, BANDH, or governance actions
    private Map<String, Map<String, Object>> actionEffects = new LinkedHashMap<>();

    public NationalTheme() {}

    public String getThemeType() { return themeType; }
    public void setThemeType(String themeType) { this.themeType = themeType; }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getThemeKey() { return themeKey; }
    public void setThemeKey(String themeKey) { this.themeKey = themeKey; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getIcon() { return icon; }
    public void setIcon(String icon) { this.icon = icon; }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public List<Integer> getActiveEras() { return activeEras; }
    public void setActiveEras(List<Integer> activeEras) { this.activeEras = activeEras; }

    public int getStreakTargetMin() { return streakTargetMin; }
    public void setStreakTargetMin(int streakTargetMin) { this.streakTargetMin = streakTargetMin; }

    public int getStreakTargetMax() { return streakTargetMax; }
    public void setStreakTargetMax(int streakTargetMax) { this.streakTargetMax = streakTargetMax; }

    public Map<String, Map<String, Object>> getActionEffects() { return actionEffects; }
    public void setActionEffects(Map<String, Map<String, Object>> actionEffects) { this.actionEffects = actionEffects; }
}
