package com.politicalsim.ai;

import com.politicalsim.content.CardDefinition;

public record AiDecision(AiIntent intent, CardDefinition card) {
}
