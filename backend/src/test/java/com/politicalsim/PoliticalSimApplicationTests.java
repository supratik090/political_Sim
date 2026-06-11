package com.politicalsim;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;

import org.junit.jupiter.api.Test;

class PoliticalSimApplicationTests {

    @Test
    void applicationClassCanBeLoaded() {
        assertDoesNotThrow(() -> Class.forName("com.politicalsim.PoliticalSimApplication"));
    }
}
