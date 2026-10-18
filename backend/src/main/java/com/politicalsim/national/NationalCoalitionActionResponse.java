package com.politicalsim.national;

public class NationalCoalitionActionResponse {
    private boolean success;
    private CoalitionResponseCode responseCode;
    private String responseMessage;
    private NationalGame game;
    private NationalContract counterProposal; // populated when AI sends a counter offer

    public NationalCoalitionActionResponse() {}

    public NationalCoalitionActionResponse(boolean success, CoalitionResponseCode responseCode, String responseMessage, NationalGame game) {
        this.success = success;
        this.responseCode = responseCode;
        this.responseMessage = responseMessage != null && !responseMessage.isEmpty() 
            ? responseMessage 
            : (responseCode != null ? responseCode.getDefaultMessage() : "");
        this.game = game;
    }

    public static NationalCoalitionActionResponse success(CoalitionResponseCode code, String message, NationalGame game) {
        return new NationalCoalitionActionResponse(true, code, message, game);
    }

    public static NationalCoalitionActionResponse refusal(CoalitionResponseCode code, String message, NationalGame game) {
        return new NationalCoalitionActionResponse(false, code, message, game);
    }

    public static NationalCoalitionActionResponse counter(String message, NationalContract counterProposal, NationalGame game) {
        NationalCoalitionActionResponse r = new NationalCoalitionActionResponse(false, CoalitionResponseCode.COUNTER_PROPOSAL, message, game);
        r.counterProposal = counterProposal;
        return r;
    }

    public boolean isSuccess() { return success; }
    public void setSuccess(boolean success) { this.success = success; }

    public CoalitionResponseCode getResponseCode() { return responseCode; }
    public void setResponseCode(CoalitionResponseCode responseCode) { this.responseCode = responseCode; }

    public String getResponseMessage() { return responseMessage; }
    public void setResponseMessage(String responseMessage) { this.responseMessage = responseMessage; }

    public NationalGame getGame() { return game; }
    public void setGame(NationalGame game) { this.game = game; }

    public NationalContract getCounterProposal() { return counterProposal; }
    public void setCounterProposal(NationalContract counterProposal) { this.counterProposal = counterProposal; }
}

