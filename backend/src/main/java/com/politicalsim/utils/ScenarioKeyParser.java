package com.politicalsim.util;

import java.time.LocalDate;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ScenarioKeyParser {

    // Regex breakdown: Match everything up to the last underscore, followed by exactly 4 digits
    private static final Pattern SCENARIO_PATTERN = Pattern.compile("^(.*)_(\\d{4})$");

    /**
     * Extracts the last 4 digits as an integer year.
     * Fallback: 2001 if null, poorly formatted, or non-numeric.
     */
    public static int extractYear(String scenarioKey) {
        if (scenarioKey == null || scenarioKey.isBlank()) {
            return 2001;
        }

        Matcher matcher = SCENARIO_PATTERN.matcher(scenarioKey.trim());
        if (matcher.matches()) {
            try {
                return Integer.parseInt(matcher.group(2)); // Group 2 captures the 4 digits
            } catch (NumberFormatException e) {
                return 2001;
            }
        }

        return 2001;
    }

    /**
     * Extracts the state name portion (everything before the trailing _YYYY).
     * Fallback: "unknown" if null or poorly formatted.
     */
    public static String extractStateName(String scenarioKey) {
        if (scenarioKey == null || scenarioKey.isBlank()) {
            return "unknown";
        }

        Matcher matcher = SCENARIO_PATTERN.matcher(scenarioKey.trim());
        if (matcher.matches()) {
            String state = matcher.group(1); // Group 1 captures the text before the year
            return state.isBlank() ? "unknown" : state;
        }

        // If it doesn't end in _YYYY, return the whole key cleaned up as a fallback
        return scenarioKey.trim();
    }
}