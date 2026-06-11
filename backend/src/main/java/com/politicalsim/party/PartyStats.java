package com.politicalsim.party;

public class PartyStats {

    private int coins;
    private int partyMorale;
    private int corruptionScore;
    private int mediaImage;
    private int publicSupport;

    public PartyStats() {
    }

    public PartyStats(int coins, int partyMorale, int corruptionScore, int mediaImage, int publicSupport) {
        this.coins = coins;
        this.partyMorale = partyMorale;
        this.corruptionScore = corruptionScore;
        this.mediaImage = mediaImage;
        this.publicSupport = publicSupport;
    }

    public int getCoins() {
        return coins;
    }

    public void setCoins(int coins) {
        this.coins = coins;
    }

    public int getPartyMorale() {
        return partyMorale;
    }

    public void setPartyMorale(int partyMorale) {
        this.partyMorale = partyMorale;
    }

    public int getCorruptionScore() {
        return corruptionScore;
    }

    public void setCorruptionScore(int corruptionScore) {
        this.corruptionScore = corruptionScore;
    }

    public int getMediaImage() {
        return mediaImage;
    }

    public void setMediaImage(int mediaImage) {
        this.mediaImage = mediaImage;
    }

    public int getPublicSupport() {
        return publicSupport;
    }

    public void setPublicSupport(int publicSupport) {
        this.publicSupport = publicSupport;
    }
}
