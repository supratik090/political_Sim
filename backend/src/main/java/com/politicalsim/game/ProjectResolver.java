package com.politicalsim.game;

import com.politicalsim.party.BuildingProject;
import com.politicalsim.party.PartyState;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class ProjectResolver {
    private final RoundResolutionEngine engine;

    public ProjectResolver(RoundResolutionEngine engine) {
        this.engine = engine;
    }

    public void logProjectFundingActivity(GameSession session, List<String> commentary, List<String> resultLines) {
        Map<String, Map<String, Integer>> projectContribs = session.getProjectContributionsThisTurn();
        if (projectContribs != null && !projectContribs.isEmpty()) {
            commentary.add("🏗️ Project Funding Activity:");
            for (Map.Entry<String, Map<String, Integer>> entry : projectContribs.entrySet()) {
                PartyState party = engine.findParty(session, entry.getKey());
                for (Map.Entry<String, Integer> projEntry : entry.getValue().entrySet()) {
                    String projectKey = projEntry.getKey();
                    int progressAdded = projEntry.getValue();
                    BuildingProject def = BuildingProject.valueOf(projectKey);
                    int coinsCost = (int) Math.ceil((double) def.getCostCoins() * progressAdded / 100.0);
                    int moraleCost = (int) Math.ceil((double) def.getCostMorale() * progressAdded / 100.0);
                    int corruptionCost = (int) Math.ceil((double) def.getCostCorruption() * progressAdded / 100.0);
                    int mediaCost = (int) Math.ceil((double) def.getCostMedia() * progressAdded / 100.0);
                    int supportCost = (int) Math.ceil((double) def.getCostSupport() * progressAdded / 100.0);
                    
                    List<String> costDetails = new ArrayList<>();
                    if (coinsCost > 0) costDetails.add(coinsCost + " Coins");
                    if (moraleCost > 0) costDetails.add(moraleCost + " Morale");
                    if (corruptionCost > 0) costDetails.add(corruptionCost + " Corruption");
                    if (mediaCost > 0) costDetails.add(mediaCost + " Media Image");
                    if (supportCost > 0) costDetails.add(supportCost + "% Public Support");
                    
                    String costStr = String.join(", ", costDetails);
                    String msg = party.getName() + " funded project '" + def.getName() + "' (Progress: +" + progressAdded + "%, Cost: " + costStr + ")";
                    commentary.add("  - " + msg);
                    resultLines.add(msg);
                }
            }
            projectContribs.clear(); // Clear for next turn
        } else {
            commentary.add("🏗️ Project Funding Activity: No projects were funded this turn.");
        }
    }

    public void resolveBuildingProjects(GameSession session, Map<String, Integer> supportPressure, List<String> commentary) {
        for (PartyState party : session.getParties()) {
            if (!party.isActive()) {
                continue;
            }
            if (party.getProjects() == null) {
                continue;
            }
            for (ProjectState project : party.getProjects()) {
                if (project.getProgressPercent() < 100) {
                    continue;
                }

                BuildingProject def = BuildingProject.valueOf(project.getProjectKey());
                boolean logCommentary = project.isJustCompleted();
                if (logCommentary) {
                    commentary.add("🏗️ " + party.getName() + " completed project '" + def.getName() + "'!");
                }

                if (def.isRequiresTarget()) {
                    if (project.getTargetPartyId() == null || project.getTargetPartyId().isBlank()) {
                        if (logCommentary) {
                            commentary.add("  ⚠️ Warning: No target assigned to '" + def.getName() + "'. No effect this turn.");
                        }
                        project.setJustCompleted(false);
                        continue;
                    }
                    PartyState target = session.getParties().stream()
                            .filter(p -> p.getId().equals(project.getTargetPartyId()))
                            .findFirst().orElse(null);
                    if (target == null || !target.isActive()) {
                        if (logCommentary) {
                            commentary.add("  ⚠️ Warning: Targeted party is no longer active. Assign a new target.");
                        }
                        project.setJustCompleted(false);
                        continue;
                    }

                    // Check if project is hostile and violates a non-aggression pact
                    boolean projectHostile = def.getBenefitCoins() < 0 
                                          || def.getBenefitMorale() < 0 
                                          || def.getBenefitMedia() < 0 
                                          || def.getBenefitCorruption() > 0 
                                          || def.getBenefitSupport() < 0;
                    if (projectHostile) {
                        engine.checkAndProcessPactViolation(session, party, target, "hostile project '" + def.getName() + "'", commentary);
                    }

                    // Record grudge: target holds a grudge against project owner
                    Map<String, Map<String, Integer>> grudges = session.getGrudges();
                    Map<String, Integer> targetGrudges = grudges.computeIfAbsent(target.getId(), k -> new LinkedHashMap<>());
                    targetGrudges.put(party.getId(), targetGrudges.getOrDefault(party.getId(), 0) + 1);

                    if (def.getBenefitCoins() != 0) {
                        int coinDrain = Math.min(target.getStats().getCoins(), Math.abs(def.getBenefitCoins()));
                        if (coinDrain > 0) {
                            target.getStats().setCoins(target.getStats().getCoins() - coinDrain);
                            if (logCommentary) {
                                commentary.add("  💥 Drained " + target.getName() + "'s Coins by -" + coinDrain + ".");
                            }
                        }
                    }
                    if (def.getBenefitMorale() != 0) {
                        target.getStats().setPartyMorale(Math.max(0, target.getStats().getPartyMorale() + def.getBenefitMorale()));
                        if (logCommentary) {
                            commentary.add("  💥 Drained " + target.getName() + "'s Morale by " + Math.abs(def.getBenefitMorale()) + ".");
                        }
                    }
                    if (def.getBenefitMedia() != 0) {
                        target.getStats().setMediaImage(Math.max(0, target.getStats().getMediaImage() + def.getBenefitMedia()));
                        if (logCommentary) {
                            commentary.add("  💥 Drained " + target.getName() + "'s Media Image by " + Math.abs(def.getBenefitMedia()) + ".");
                        }
                    }
                    if (def.getBenefitCorruption() != 0) {
                        target.getStats().setCorruptionScore(Math.min(100, target.getStats().getCorruptionScore() + def.getBenefitCorruption()));
                        if (logCommentary) {
                            commentary.add("  💥 Exposed " + target.getName() + ", raising their Corruption by +" + def.getBenefitCorruption() + ".");
                        }
                    }
                    if (def.getBenefitSupport() != 0) {
                        int supportDrain = Math.min(target.getStats().getPublicSupport(), Math.abs(def.getBenefitSupport()));
                        if (supportDrain > 0) {
                            target.getStats().setPublicSupport(target.getStats().getPublicSupport() - supportDrain);
                            session.getPublicState().setUndecidedSupport(session.getPublicState().getUndecidedSupport() + supportDrain);
                            if (logCommentary) {
                                commentary.add("  💥 Drained " + target.getName() + "'s Public Support by -" + supportDrain + "%.");
                            }
                        }
                    }
                } else {
                    if (def.getBenefitCoins() != 0) {
                        party.getStats().setCoins(party.getStats().getCoins() + def.getBenefitCoins());
                        if (logCommentary) {
                            commentary.add("  💰 Received +" + def.getBenefitCoins() + " Coins.");
                        }
                    }
                    if (def.getBenefitMorale() != 0) {
                        party.getStats().setPartyMorale(Math.min(100, party.getStats().getPartyMorale() + def.getBenefitMorale()));
                        if (logCommentary) {
                            commentary.add("  ⚡ Received +" + def.getBenefitMorale() + " Morale.");
                        }
                    }
                    if (def.getBenefitMedia() != 0) {
                        party.getStats().setMediaImage(Math.min(100, party.getStats().getMediaImage() + def.getBenefitMedia()));
                        if (logCommentary) {
                            commentary.add("  📢 Received +" + def.getBenefitMedia() + " Media Image.");
                        }
                    }
                    if (def.getBenefitCorruption() != 0) {
                        party.getStats().setCorruptionScore(Math.max(0, party.getStats().getCorruptionScore() + def.getBenefitCorruption()));
                        if (logCommentary) {
                            commentary.add("  🛡️ Reduced Corruption by " + Math.abs(def.getBenefitCorruption()) + ".");
                        }
                    }
                    if (def.getBenefitSupport() != 0) {
                        int undecided = session.getPublicState().getUndecidedSupport();
                        int supportGain = Math.min(undecided, def.getBenefitSupport());
                        if (supportGain > 0) {
                            party.getStats().setPublicSupport(party.getStats().getPublicSupport() + supportGain);
                            session.getPublicState().setUndecidedSupport(undecided - supportGain);
                            if (logCommentary) {
                                commentary.add("  📈 Gained +" + supportGain + "% Public Support from Undecided voters.");
                            }
                        } else {
                            if (logCommentary) {
                                commentary.add("  📈 No Undecided voters available to gain support.");
                            }
                        }
                    }
                }
                project.setJustCompleted(false);
            }
        }
    }
}
