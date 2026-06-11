package com.politicalsim.game;

public class GameNotFoundException extends RuntimeException {

    public GameNotFoundException(String gameId) {
        super("Game not found: " + gameId);
    }
}
