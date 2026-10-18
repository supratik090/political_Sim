package com.politicalsim.national;

public class NationalActivityLogEntry {
    private int season;
    private String event;
    private String detail;
    private String timestamp;

    public int getSeason() { return season; }
    public void setSeason(int season) { this.season = season; }
    public String getEvent() { return event; }
    public void setEvent(String event) { this.event = event; }
    public String getDetail() { return detail; }
    public void setDetail(String detail) { this.detail = detail; }
    public String getTimestamp() { return timestamp; }
    public void setTimestamp(String timestamp) { this.timestamp = timestamp; }
}
