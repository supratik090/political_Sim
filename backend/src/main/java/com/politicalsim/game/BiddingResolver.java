package com.politicalsim.game;

import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class BiddingResolver {
    private final RoundResolutionEngine engine;

    public BiddingResolver(RoundResolutionEngine engine) {
        this.engine = engine;
    }

    public void resolveBidding(GameSession session, String biddingMetric, List<String> commentary) {
        // Bidding Winner determination
        int highestBid = -1;
        List<RoundSubmission> winners = new ArrayList<>();
        for (RoundSubmission sub : session.getCurrentRoundSubmissions()) {
            PartyState party = engine.findParty(session, sub.getPartyId());
            if (party.getRole() == com.politicalsim.party.PartyRole.DEFEATED) {
                continue;
            }
            if (sub.getBid() > highestBid) {
                highestBid = sub.getBid();
                winners.clear();
                winners.add(sub);
            } else if (sub.getBid() == highestBid) {
                winners.add(sub);
            }
        }

        RoundSubmission roundWinnerSub = null;
        if (winners.size() == 1) {
            roundWinnerSub = winners.get(0);
        } else if (winners.size() > 1) {
            int highestSupport = -1;
            List<RoundSubmission> supportWinners = new ArrayList<>();
            for (RoundSubmission sub : winners) {
                PartyState party = engine.findParty(session, sub.getPartyId());
                int support = party.getStats().getPublicSupport();
                if (support > highestSupport) {
                    highestSupport = support;
                    supportWinners.clear();
                    supportWinners.add(sub);
                } else if (support == highestSupport) {
                    supportWinners.add(sub);
                }
            }

            if (supportWinners.size() == 1) {
                roundWinnerSub = supportWinners.get(0);
            } else {
                for (PartyRole role : List.of(PartyRole.GOVERNMENT, PartyRole.OPPOSITION, PartyRole.THIRD_PARTY)) {
                    for (RoundSubmission sub : supportWinners) {
                        PartyState party = engine.findParty(session, sub.getPartyId());
                        if (party.getRole() == role) {
                            roundWinnerSub = sub;
                            break;
                        }
                    }
                    if (roundWinnerSub != null) break;
                }
            }
        }

        String winnerPartyId = null;
        if (roundWinnerSub != null) {
            winnerPartyId = roundWinnerSub.getPartyId();
            PartyState winnerParty = engine.findParty(session, winnerPartyId);
            int currentWins = session.getPartyRoundWins().getOrDefault(winnerPartyId, 0);
            session.getPartyRoundWins().put(winnerPartyId, currentWins + 1);
            
            // Deduct bid only for the winner
            int winnerBid = roundWinnerSub.getBid();
            engine.deductStatValue(winnerParty, biddingMetric, winnerBid);
            
            commentary.add("Bidding Winner: " + winnerParty.getName() + " wins the bidding round with a bid of " + highestBid + " " + biddingMetric + "!");
            commentary.add("💸 Bidding Cost: " + winnerParty.getName() + " paid " + winnerBid + " " + biddingMetric + " for winning the bidding round.");
        } else {
            commentary.add("Bidding Winner: No winner for this round.");
        }

        Map<String, Integer> roundBids = new LinkedHashMap<>();
        for (RoundSubmission sub : session.getCurrentRoundSubmissions()) {
            PartyState party = engine.findParty(session, sub.getPartyId());
            if (party.getRole() == com.politicalsim.party.PartyRole.DEFEATED) {
                continue;
            }
            roundBids.put(sub.getPartyId(), sub.getBid());
        }
        session.setLastRoundBids(roundBids);
        session.setLastRoundBiddingMetric(biddingMetric);
        session.setLastRoundWinnerPartyId(winnerPartyId);

        // Update held rewards expiration countdown
        for (Map.Entry<String, List<HeldReward>> entry : session.getPartyHeldRewards().entrySet()) {
            List<HeldReward> list = entry.getValue();
            if (list != null) {
                List<HeldReward> kept = new ArrayList<>();
                for (HeldReward hr : list) {
                    hr.setTurnsLeft(hr.getTurnsLeft() - 1);
                    if (hr.getTurnsLeft() > 0) {
                        kept.add(hr);
                    } else {
                        commentary.add("Expired: " + hr.getName() + " in " + engine.findParty(session, entry.getKey()).getName() + "'s inventory has expired.");
                    }
                }
                entry.setValue(kept);
            }
        }

        // Cycle complete check at turn 5
        int cycleTurn = ((session.getTurnNumber() - 1) % 5) + 1;
        if (cycleTurn == 5) {
            int maxWins = -1;
            List<String> cycleWinners = new ArrayList<>();
            for (Map.Entry<String, Integer> entry : session.getPartyRoundWins().entrySet()) {
                if (entry.getValue() > maxWins) {
                    maxWins = entry.getValue();
                    cycleWinners.clear();
                    cycleWinners.add(entry.getKey());
                } else if (entry.getValue() == maxWins) {
                    cycleWinners.add(entry.getKey());
                }
            }

            String cycleWinnerPartyId = null;
            if (cycleWinners.size() == 1) {
                cycleWinnerPartyId = cycleWinners.get(0);
            } else if (cycleWinners.size() > 1) {
                int highestSupport = -1;
                for (String pId : cycleWinners) {
                    PartyState party = engine.findParty(session, pId);
                    if (party.getStats().getPublicSupport() > highestSupport) {
                        highestSupport = party.getStats().getPublicSupport();
                        cycleWinnerPartyId = pId;
                    }
                }
            }

            if (cycleWinnerPartyId != null) {
                PartyState cycleWinner = engine.findParty(session, cycleWinnerPartyId);
                RewardDefinition reward = engine.selectRandomReward(session);
                HeldReward hr = new HeldReward(reward.key(), reward.name(), reward.description(), 15, reward.requiresTarget(), reward.targetType());
                session.getPartyHeldRewards().computeIfAbsent(cycleWinnerPartyId, k -> new ArrayList<>()).add(hr);
                session.getPartyRoundWins().clear(); // reset wins
                commentary.add("🎁 Cycle Complete: " + cycleWinner.getName() + " won the 5-turn cycle with the most bidding wins! Awarded reward: '" + reward.name() + "'.");
                session.setLastBiddingWinnerPartyId(cycleWinnerPartyId);
                
                // Select next reward
                RewardDefinition nextReward = engine.selectRandomReward(session);
                session.setNextBiddingReward(nextReward);
            }
        }
    }
}
