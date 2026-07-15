package com.politicalsim.game;

import com.politicalsim.party.FactionState;
import com.politicalsim.party.PartyManagementRepository;
import com.politicalsim.party.PartyManagementState;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.ScheduledPost;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class SpecialRewardsService {

    @Value("${game.special-rewards.enabled:true}")
    private boolean enabled;

    private final PartyManagementRepository partyManagementRepository;

    public SpecialRewardsService(PartyManagementRepository partyManagementRepository) {
        this.partyManagementRepository = partyManagementRepository;
    }

    public boolean isEnabled() {
        return enabled;
    }

    public boolean isSpecialReward(String rewardKey) {
        return rewardKey != null && rewardKey.startsWith("special_");
    }

    public void applySpecialReward(GameSession session, PartyState target, String rewardKey, List<String> commentary) {
        if (!enabled) return;

        switch (rewardKey) {
            case "special_pause_projects" -> {
                target.setProjectBuildingPausedTurns(10);
                commentary.add("⏳ Project Freeze: " + target.getName() + "'s project building is paused for 10 turns!");
            }
            case "special_double_yields" -> {
                target.setDoubleProjectYieldsTurns(5);
                target.setDoubleProjectYieldsCount(0);
                commentary.add("💰 Yield Doubler: " + target.getName() + " will receive double yields from up to 10 development projects for the next 5 turns!");
            }
            case "special_stop_legislation" -> {
                target.setStopLegislationTurns(10);
                commentary.add("🏛️ Legislative Blockade: " + target.getName() + " is stopped from tabling any legislative bills for 10 turns (but can still vote)!");
            }
            case "special_block_cards" -> {
                target.setBlockCardsTurns(5);
                commentary.add("❄️ Card Lockout: " + target.getName() + " is frozen! Card play is blocked for 5 turns (only Skip Card allowed)!");
            }
            case "special_immune_shield" -> {
                target.setImmuneShieldTurns(5);
                commentary.add("🛡️ Immune Shield: " + target.getName() + " activated an immune shield! Hostile targeted projects are halted for 5 rounds.");
            }
            case "special_populist_surge" -> {
                target.setPopulistSurgeTurns(5);
                commentary.add("📈 Populist Surge: " + target.getName() + " activated a populist surge! All support gains are multiplied by 1.5x for 5 turns.");
            }
            case "special_reset_opponent_posts" -> {
                resetOpponentPosts(session, target, commentary);
            }
            case "special_gain_party_post" -> {
                gainPartyPost(session, target, commentary);
            }
            case "special_faction_loyalty_self" -> {
                applyFactionLoyaltyBoost(target, +20, commentary,
                        "🤝 Faction Rally: All factions of " + target.getName() + " gained +20 loyalty!");
            }
            case "special_faction_loyalty_opponent" -> {
                applyFactionLoyaltyBoost(target, -20, commentary,
                        "💥 Faction Destabilisation: All factions of " + target.getName() + " lost -20 loyalty!");
            }
        }
    }

    private void applyFactionLoyaltyBoost(PartyState target, int delta, List<String> commentary, String msg) {
        for (FactionState fs : target.getFactions()) {
            if (fs.isActive()) {
                fs.setLoyalty(Math.max(0, Math.min(100, fs.getLoyalty() + delta)));
            }
        }
        commentary.add(msg);
    }

    private void resetOpponentPosts(GameSession session, PartyState target, List<String> commentary) {
        if (partyManagementRepository == null) return;
        Optional<PartyManagementState> optPms = partyManagementRepository.findByGameIdAndPartyId(session.getId(), target.getId());
        if (optPms.isEmpty()) return;

        PartyManagementState pms = optPms.get();
        List<String> postsToReset = new ArrayList<>();

        // Collect up to 5 posts currently assigned to target's factions
        for (FactionState fs : target.getFactions()) {
            if (fs.isActive() && fs.getPost() != null) {
                Iterator<String> it = fs.getPost().iterator();
                while (it.hasNext() && postsToReset.size() < 5) {
                    String postKey = it.next();
                    postsToReset.add(postKey);
                    it.remove(); // Remove from faction
                }
            }
        }

        if (!postsToReset.isEmpty()) {
            // Update scheduled posts status in PartyManagementState back to AVAILABLE
            for (ScheduledPost sp : pms.getPosts()) {
                if (postsToReset.contains(sp.getPostKey()) || postsToReset.contains(sp.getPostName())) {
                    sp.setStatus(ScheduledPost.Status.AVAILABLE);
                    sp.setAssignedFactionKey(null);
                }
            }
            partyManagementRepository.save(pms);
            commentary.add("⚡ Post Purge: Reset " + postsToReset.size() + " post allocations for " + target.getName() + " back to unallocated.");
        } else {
            commentary.add("⚡ Post Purge: " + target.getName() + " has no assigned posts to reset.");
        }
    }

    private void gainPartyPost(GameSession session, PartyState target, List<String> commentary) {
        if (partyManagementRepository == null) return;
        if (target.getGainedPostsCount() >= 5) {
            commentary.add("🎁 Post Unlock: Gain post limit reached (Max 5 gained posts allowed).");
            return;
        }

        Optional<PartyManagementState> optPms = partyManagementRepository.findByGameIdAndPartyId(session.getId(), target.getId());
        if (optPms.isEmpty()) return;

        PartyManagementState pms = optPms.get();
        ScheduledPost pendingPost = pms.getPosts().stream()
                .filter(sp -> sp.getStatus() == ScheduledPost.Status.PENDING)
                .findFirst()
                .orElse(null);

        if (pendingPost != null) {
            pendingPost.setStatus(ScheduledPost.Status.AVAILABLE);
            target.setGainedPostsCount(target.getGainedPostsCount() + 1);
            partyManagementRepository.save(pms);
            commentary.add("🎁 Post Unlock: Instantly unlocked post '" + pendingPost.getPostName() + "' for " + target.getName() + "!");
        } else {
            commentary.add("🎁 Post Unlock: No pending posts available to unlock.");
        }
    }

    public void tickDurations(GameSession session, List<String> commentary) {
        if (!enabled) return;

        for (PartyState party : session.getParties()) {
            if (!party.isActive()) continue;

            if (party.getProjectBuildingPausedTurns() > 0) {
                party.setProjectBuildingPausedTurns(party.getProjectBuildingPausedTurns() - 1);
                if (party.getProjectBuildingPausedTurns() == 0) {
                    commentary.add("⏳ Info: Project Freeze expired for " + party.getName() + ".");
                }
            }
            if (party.getDoubleProjectYieldsTurns() > 0) {
                party.setDoubleProjectYieldsTurns(party.getDoubleProjectYieldsTurns() - 1);
                if (party.getDoubleProjectYieldsTurns() == 0) {
                    commentary.add("💰 Info: Yield Doubler expired for " + party.getName() + ".");
                }
            }
            if (party.getStopLegislationTurns() > 0) {
                party.setStopLegislationTurns(party.getStopLegislationTurns() - 1);
                if (party.getStopLegislationTurns() == 0) {
                    commentary.add("🏛️ Info: Legislative Blockade expired for " + party.getName() + ".");
                }
            }
            if (party.getBlockCardsTurns() > 0) {
                party.setBlockCardsTurns(party.getBlockCardsTurns() - 1);
                if (party.getBlockCardsTurns() == 0) {
                    commentary.add("❄️ Info: Card Lockout expired for " + party.getName() + ".");
                }
            }
            if (party.getImmuneShieldTurns() > 0) {
                party.setImmuneShieldTurns(party.getImmuneShieldTurns() - 1);
                if (party.getImmuneShieldTurns() == 0) {
                    commentary.add("🛡️ Info: Immune Shield expired for " + party.getName() + ".");
                }
            }
            if (party.getPopulistSurgeTurns() > 0) {
                party.setPopulistSurgeTurns(party.getPopulistSurgeTurns() - 1);
                if (party.getPopulistSurgeTurns() == 0) {
                    commentary.add("📈 Info: Populist Surge expired for " + party.getName() + ".");
                }
            }
        }
    }

    public void triggerTenRoundRewardDrop(GameSession session, List<String> commentary) {
        if (!enabled) return;

        List<PartyState> activeParties = session.getParties().stream()
                .filter(PartyState::isActive)
                .toList();

        if (activeParties.isEmpty()) return;

        PartyState chosenParty = activeParties.get(new Random().nextInt(activeParties.size()));
        RewardDefinition chosenReward = null;
        if (!RoundResolutionEngine.REWARD_POOL.isEmpty()) {
            chosenReward = RoundResolutionEngine.REWARD_POOL.get(new Random().nextInt(RoundResolutionEngine.REWARD_POOL.size()));
        }

        if (chosenReward != null) {
            HeldReward hr = new HeldReward(chosenReward.key(), chosenReward.name(), chosenReward.description(), 15, chosenReward.requiresTarget(), chosenReward.allowedTargets());
            session.getPartyHeldRewards().computeIfAbsent(chosenParty.getId(), k -> new ArrayList<>()).add(hr);

            commentary.add("🎁 10-ROUND DROP: " + chosenParty.getName() + " received a free random reward: " + chosenReward.name() + " (" + chosenReward.description() + ")!");

            Map<String, Object> dropData = new LinkedHashMap<>();
            dropData.put("partyId", chosenParty.getId());
            dropData.put("partyName", chosenParty.getName());
            dropData.put("rewardName", chosenReward.name());
            dropData.put("rewardDescription", chosenReward.description());
            session.setLastRoundDroppedReward(dropData);
        }
    }

    public boolean isProjectBuildingPaused(PartyState party) {
        return enabled && party.getProjectBuildingPausedTurns() > 0;
    }

    public boolean isDoubleYieldsActive(PartyState party) {
        return enabled && party.getDoubleProjectYieldsTurns() > 0 && party.getDoubleProjectYieldsCount() < 10;
    }

    public boolean isLegislationStopped(PartyState party) {
        return enabled && party.getStopLegislationTurns() > 0;
    }

    public boolean isCardPlayingBlocked(PartyState party) {
        return enabled && party.getBlockCardsTurns() > 0;
    }

    public boolean isImmuneShieldActive(PartyState party) {
        return enabled && party.getImmuneShieldTurns() > 0;
    }

    public boolean isPopulistSurgeActive(PartyState party) {
        return enabled && party.getPopulistSurgeTurns() > 0;
    }

    public boolean shouldSnipe(PartyState party, RewardDefinition reward, String metric) {
        if (!enabled) return false;
        if (reward == null) return false;

        // Snipe on any Special Reward, or if player profile bids aggressively
        if (isSpecialReward(reward.key())) {
            return true;
        }

        // High need check
        int support = party.getStats().getPublicSupport();
        int morale = party.getStats().getPartyMorale();
        int coins = party.getStats().getCoins();

        if (reward.publicSupportEffect() > 0 && support < 25) return true;
        if (reward.moraleEffect() > 0 && morale < 30) return true;
        if (reward.coinsEffect() > 0 && coins < 50) return true;

        return false;
    }
}
