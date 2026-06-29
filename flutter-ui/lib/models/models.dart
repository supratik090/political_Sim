class User {
  final String id;
  final String name;
  final String email;

  User({required this.id, required this.name, required this.email});

  factory User.fromJson(Map<String, dynamic> json) {
    // Backend may return user fields directly or nested under user object
    final userJson = json['user'] != null ? Map<String, dynamic>.from(json['user']) : json;
    return User(
      id: (userJson['id'] ?? userJson['_id'] ?? '').toString(),
      name: userJson['name'] ?? '',
      email: userJson['email'] ?? '',
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'email': email,
    };
  }
}

class ScenarioProgress {
  final String scenarioKey;
  final String name;
  final String description;
  final String stateName;
  final String status; // LOCKED, AVAILABLE, IN_PROGRESS, WON
  final ScenarioDefinition? scenarioDefinition;

  ScenarioProgress({
    required this.scenarioKey,
    required this.name,
    required this.description,
    required this.stateName,
    required this.status,
    this.scenarioDefinition,
  });

  factory ScenarioProgress.fromJson(Map<String, dynamic> json) {
    return ScenarioProgress(
      scenarioKey: json['scenarioKey'] ?? '',
      name: json['name'] ?? '',
      description: json['description'] ?? '',
      stateName: json['stateName'] ?? '',
      status: json['status'] ?? 'LOCKED',
      scenarioDefinition: json['scenarioDefinition'] != null
          ? ScenarioDefinition.fromJson(Map<String, dynamic>.from(json['scenarioDefinition']))
          : null,
    );
  }
}

class PartyStats {
  final int coins;
  final int partyMorale;
  final int corruptionScore;
  final int mediaImage;
  final int publicSupport;

  PartyStats({
    required this.coins,
    required this.partyMorale,
    required this.corruptionScore,
    required this.mediaImage,
    required this.publicSupport,
  });

  factory PartyStats.fromJson(Map<String, dynamic> json) {
    return PartyStats(
      coins: json['coins'] ?? 0,
      partyMorale: json['partyMorale'] ?? 0,
      corruptionScore: json['corruptionScore'] ?? 0,
      mediaImage: json['mediaImage'] ?? 0,
      publicSupport: json['publicSupport'] ?? 0,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'coins': coins,
      'partyMorale': partyMorale,
      'corruptionScore': corruptionScore,
      'mediaImage': mediaImage,
      'publicSupport': publicSupport,
    };
  }
}

class PartySetup {
  final String partyKey;
  final String name;
  final String role; // GOVERNMENT, OPPOSITION, THIRD_PARTY
  final String controllerType; // HUMAN, COMPUTER
  final String color;
  final String symbol;
  final String ideology;
  final Map<String, dynamic>? aiProfile;
  final PartyStats? startingStats;

  PartySetup({
    required this.partyKey,
    required this.name,
    required this.role,
    required this.controllerType,
    required this.color,
    required this.symbol,
    required this.ideology,
    this.aiProfile,
    this.startingStats,
  });

  factory PartySetup.fromJson(Map<String, dynamic> json) {
    return PartySetup(
      partyKey: json['partyKey'] ?? '',
      name: json['name'] ?? '',
      role: json['role'] ?? json['startingRole'] ?? '',
      controllerType: json['controllerType'] ?? json['defaultControllerType'] ?? 'COMPUTER',
      color: json['color'] ?? '#555555',
      symbol: json['symbol'] ?? 'Tiger',
      ideology: json['ideology'] ?? 'BALANCED',
      aiProfile: json['aiProfile'] != null ? Map<String, dynamic>.from(json['aiProfile']) : null,
      startingStats: json['startingStats'] != null
          ? PartyStats.fromJson(Map<String, dynamic>.from(json['startingStats']))
          : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'partyKey': partyKey,
      'name': name,
      'role': role,
      'controllerType': controllerType,
      'color': color,
      'symbol': symbol,
      'ideology': ideology,
      'aiProfile': aiProfile,
      'startingStats': startingStats?.toJson(),
    };
  }
}

class ScenarioDefinition {
  final String? id;
  final String scenarioKey;
  final String name;
  final String description;
  final String stateName;
  final String startDate;
  final int cycleLengthMonths;
  final List<PartySetup> politicalParties;
  final Map<String, dynamic>? publicState;
  final bool active;

  ScenarioDefinition({
    this.id,
    required this.scenarioKey,
    required this.name,
    required this.description,
    required this.stateName,
    required this.startDate,
    required this.cycleLengthMonths,
    required this.politicalParties,
    this.publicState,
    required this.active,
  });

  factory ScenarioDefinition.fromJson(Map<String, dynamic> json) {
    final partiesList = json['politicalParties'] as List? ?? [];
    return ScenarioDefinition(
      id: json['id']?.toString(),
      scenarioKey: json['scenarioKey'] ?? '',
      name: json['name'] ?? '',
      description: json['description'] ?? '',
      stateName: json['stateName'] ?? '',
      startDate: json['startDate'] ?? '2000-10-01',
      cycleLengthMonths: json['cycleLengthMonths'] ?? 60,
      politicalParties: partiesList.map((p) => PartySetup.fromJson(Map<String, dynamic>.from(p))).toList(),
      publicState: json['publicState'] != null ? Map<String, dynamic>.from(json['publicState']) : null,
      active: json['active'] ?? true,
    );
  }
}

class PartyProject {
  final String id;
  final String projectKey;
  final int progressPercent;
  final String? targetPartyId;

  PartyProject({
    required this.id,
    required this.projectKey,
    required this.progressPercent,
    this.targetPartyId,
  });

  factory PartyProject.fromJson(Map<String, dynamic> json) {
    return PartyProject(
      id: json['id'] ?? json['projectKey'] ?? '',
      projectKey: json['projectKey'] ?? '',
      progressPercent: json['progressPercent'] ?? 0,
      targetPartyId: json['targetPartyId'],
    );
  }
}

class Party {
  final String id;
  final String name;
  final String role; // GOVERNMENT, OPPOSITION, THIRD_PARTY, DEFEATED
  final String controllerType; // HUMAN, COMPUTER
  final String color;
  final String symbol;
  final String ideology;
  final PartyStats stats;
  final List<PartyProject> projects;
  final bool playerControlled;

  Party({
    required this.id,
    required this.name,
    required this.role,
    required this.controllerType,
    required this.color,
    required this.symbol,
    required this.ideology,
    required this.stats,
    required this.projects,
    required this.playerControlled,
  });

  factory Party.fromJson(Map<String, dynamic> json) {
    final projectsList = json['projects'] as List? ?? [];
    return Party(
      id: json['id'] ?? '',
      name: json['name'] ?? '',
      role: json['role'] ?? 'DEFEATED',
      controllerType: json['controllerType'] ?? 'COMPUTER',
      color: json['color'] ?? '#555555',
      symbol: json['symbol'] ?? 'Flag',
      ideology: json['ideology'] ?? 'BALANCED',
      stats: PartyStats.fromJson(Map<String, dynamic>.from(json['stats'] ?? {})),
      projects: projectsList.map((p) => PartyProject.fromJson(Map<String, dynamic>.from(p))).toList(),
      playerControlled: json['playerControlled'] ?? false,
    );
  }
}

class PublicState {
  final int undecidedSupport;
  final int publicMood;

  PublicState({
    required this.undecidedSupport,
    required this.publicMood,
  });

  factory PublicState.fromJson(Map<String, dynamic> json) {
    return PublicState(
      undecidedSupport: json['undecidedSupport'] ?? 0,
      publicMood: json['publicMood'] ?? 0,
    );
  }
}

class StrategicCard {
  final String cardKey;
  final String name;
  final String category;
  final int cost;
  final String description;
  final bool requiresTarget;
  final Map<String, dynamic>? selfEffects;
  final Map<String, dynamic>? opponentEffects;

  StrategicCard({
    required this.cardKey,
    required this.name,
    required this.category,
    required this.cost,
    required this.description,
    required this.requiresTarget,
    this.selfEffects,
    this.opponentEffects,
  });

  factory StrategicCard.fromJson(Map<String, dynamic> json) {
    final visibleEffects = json['visibleEffects'] != null
        ? Map<String, dynamic>.from(json['visibleEffects'])
        : null;
    
    return StrategicCard(
      cardKey: json['cardKey'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? '',
      cost: json['cost'] ?? 0,
      description: json['description'] ?? '',
      requiresTarget: json['requiresTarget'] ?? false,
      selfEffects: visibleEffects != null && visibleEffects['selfParty'] != null
          ? Map<String, dynamic>.from(visibleEffects['selfParty'])
          : null,
      opponentEffects: visibleEffects != null && visibleEffects['opponentParty'] != null
          ? Map<String, dynamic>.from(visibleEffects['opponentParty'])
          : null,
    );
  }
}

class NewsOption {
  final String optionKey;
  final String text;

  NewsOption({required this.optionKey, required this.text});

  factory NewsOption.fromJson(Map<String, dynamic> json) {
    return NewsOption(
      optionKey: json['optionKey'] ?? json['reactionKey'] ?? '',
      text: json['text'] ?? '',
    );
  }
}

class NewsItem {
  final String newsKey;
  final String title;
  final String description;
  final List<NewsOption> options;

  NewsItem({
    required this.newsKey,
    required this.title,
    required this.description,
    required this.options,
  });

  factory NewsItem.fromJson(Map<String, dynamic> json) {
    final optionsList = (json['options'] ?? json['reactionOptions'] ?? []) as List;
    return NewsItem(
      newsKey: json['newsKey'] ?? json['issueKey'] ?? '',
      title: json['title'] ?? '',
      description: json['description'] ?? '',
      options: optionsList.map((o) => NewsOption.fromJson(Map<String, dynamic>.from(o))).toList(),
    );
  }
}

class IssueOption {
  final String optionKey;
  final String text;

  IssueOption({required this.optionKey, required this.text});

  factory IssueOption.fromJson(Map<String, dynamic> json) {
    return IssueOption(
      optionKey: json['optionKey'] ?? json['reactionKey'] ?? '',
      text: json['text'] ?? '',
    );
  }
}

class IssueItem {
  final String issueKey;
  final String title;
  final String description;
  final List<IssueOption> options;

  IssueItem({
    required this.issueKey,
    required this.title,
    required this.description,
    required this.options,
  });

  factory IssueItem.fromJson(Map<String, dynamic> json) {
    final optionsList = (json['options'] ?? json['reactionOptions'] ?? []) as List;
    return IssueItem(
      issueKey: json['issueKey'] ?? '',
      title: json['title'] ?? '',
      description: json['description'] ?? '',
      options: optionsList.map((o) => IssueOption.fromJson(Map<String, dynamic>.from(o))).toList(),
    );
  }
}

class HeldReward {
  final String rewardKey;
  final String name;
  final String description;
  final int turnsLeft;
  final bool requiresTarget;
  final String? allowedTargets; // opponent, self, etc.

  HeldReward({
    required this.rewardKey,
    required this.name,
    required this.description,
    required this.turnsLeft,
    required this.requiresTarget,
    this.allowedTargets,
  });

  factory HeldReward.fromJson(Map<String, dynamic> json) {
    return HeldReward(
      rewardKey: json['rewardKey'] ?? '',
      name: json['name'] ?? '',
      description: json['description'] ?? '',
      turnsLeft: json['turnsLeft'] ?? 0,
      requiresTarget: json['requiresTarget'] ?? false,
      allowedTargets: json['allowedTargets'],
    );
  }
}

class ActivePact {
  final String id;
  final String partyAId;
  final String partyAName;
  final String partyBId;
  final String partyBName;
  final int turnsRemaining;

  ActivePact({
    required this.id,
    required this.partyAId,
    required this.partyAName,
    required this.partyBId,
    required this.partyBName,
    required this.turnsRemaining,
  });

  factory ActivePact.fromJson(Map<String, dynamic> json) {
    return ActivePact(
      id: json['id'] ?? '',
      partyAId: json['partyAId'] ?? '',
      partyAName: json['partyAName'] ?? '',
      partyBId: json['partyBId'] ?? '',
      partyBName: json['partyBName'] ?? '',
      turnsRemaining: json['turnsRemaining'] ?? 0,
    );
  }
}

class CooperationOffer {
  final String id;
  final String senderPartyId;
  final String senderPartyName;
  final String recipientPartyId;
  final String recipientPartyName;
  final String type; // EXCHANGE, NON_AGGRESSION
  final int offeredCoins;
  final int offeredMorale;
  final int offeredSupport;
  final List<String> offeredBuildingKeys;
  final int requestedCoins;
  final int requestedMorale;
  final int requestedSupport;
  final int durationTurns;
  final bool senderPaysPact;
  final String? pactPaymentResource;
  final int pactPaymentValue;
  final List<String> pactPaymentBuildingKeys;
  final String status; // PENDING, ACCEPTED, REJECTED

  CooperationOffer({
    required this.id,
    required this.senderPartyId,
    required this.senderPartyName,
    required this.recipientPartyId,
    required this.recipientPartyName,
    required this.type,
    required this.offeredCoins,
    required this.offeredMorale,
    required this.offeredSupport,
    required this.offeredBuildingKeys,
    required this.requestedCoins,
    required this.requestedMorale,
    required this.requestedSupport,
    required this.durationTurns,
    required this.senderPaysPact,
    this.pactPaymentResource,
    required this.pactPaymentValue,
    required this.pactPaymentBuildingKeys,
    required this.status,
  });

  factory CooperationOffer.fromJson(Map<String, dynamic> json) {
    return CooperationOffer(
      id: json['id'] ?? '',
      senderPartyId: json['senderPartyId'] ?? '',
      senderPartyName: json['senderPartyName'] ?? '',
      recipientPartyId: json['recipientPartyId'] ?? '',
      recipientPartyName: json['recipientPartyName'] ?? '',
      type: json['type'] ?? 'EXCHANGE',
      offeredCoins: json['offeredCoins'] ?? 0,
      offeredMorale: json['offeredMorale'] ?? 0,
      offeredSupport: json['offeredSupport'] ?? 0,
      offeredBuildingKeys: List<String>.from(json['offeredBuildingKeys'] ?? []),
      requestedCoins: json['requestedCoins'] ?? 0,
      requestedMorale: json['requestedMorale'] ?? 0,
      requestedSupport: json['requestedSupport'] ?? 0,
      durationTurns: json['durationTurns'] ?? 0,
      senderPaysPact: json['senderPaysPact'] ?? false,
      pactPaymentResource: json['pactPaymentResource'],
      pactPaymentValue: json['pactPaymentValue'] ?? 0,
      pactPaymentBuildingKeys: List<String>.from(json['pactPaymentBuildingKeys'] ?? []),
      status: json['status'] ?? 'PENDING',
    );
  }
}

class TurnView {
  final String gameId;
  final String scenarioKey;
  final String stateName;
  final String currentDate;
  final int turnNumber;
  final int monthInCycle;
  final String status;
  final String? activeHumanPartyId;
  final String? activeHumanPartyName;
  final int monthsUntilMandatoryElection;
  final bool noConfidenceAvailable;
  final String noConfidenceReason;
  final List<Party> parties;
  final PublicState publicState;
  final List<StrategicCard> availableCards;
  final List<dynamic> delayedEffects;
  final List<dynamic> pendingResults;
  final List<NewsItem> currentNews;
  final IssueItem? currentIssue;
  
  // Last round metrics
  final List<dynamic> lastRoundSubmissions; // Map matching submissions
  final Map<String, dynamic> lastMetricDeltas;
  final List<String> lastRoundCommentary;
  final List<String> lastResults;
  final String? currentRewardName;
  final String? currentRewardDescription;
  final Map<String, int> partyRoundWins;
  final Map<String, int> lastRoundBids;
  final String? lastRoundBiddingMetric;
  final String? lastRoundWinnerPartyId;
  final String biddingMetric;
  final List<HeldReward> activePlayerHeldRewards;
  final List<ActivePact> activePacts;
  final List<CooperationOffer> cooperationOffers;

  // early election results flag
  final bool lastElectionHeld;
  final String? lastElectionWinner;
  final Map<String, int>? lastElectionVoteShares;

  TurnView({
    required this.gameId,
    required this.scenarioKey,
    required this.stateName,
    required this.currentDate,
    required this.turnNumber,
    required this.monthInCycle,
    required this.status,
    this.activeHumanPartyId,
    this.activeHumanPartyName,
    required this.monthsUntilMandatoryElection,
    required this.noConfidenceAvailable,
    required this.noConfidenceReason,
    required this.parties,
    required this.publicState,
    required this.availableCards,
    required this.delayedEffects,
    required this.pendingResults,
    required this.currentNews,
    this.currentIssue,
    this.lastRoundSubmissions = const [],
    this.lastMetricDeltas = const {},
    this.lastRoundCommentary = const [],
    this.lastResults = const [],
    this.currentRewardName,
    this.currentRewardDescription,
    this.partyRoundWins = const {},
    this.lastRoundBids = const {},
    this.lastRoundBiddingMetric,
    this.lastRoundWinnerPartyId,
    this.biddingMetric = 'COINS',
    this.activePlayerHeldRewards = const [],
    this.activePacts = const [],
    this.cooperationOffers = const [],
    this.lastElectionHeld = false,
    this.lastElectionWinner,
    this.lastElectionVoteShares,
  });

  factory TurnView.fromJson(Map<String, dynamic> json) {
    final partiesList = json['parties'] as List? ?? [];
    final cardsList = json['availableCards'] as List? ?? [];
    final newsList = json['currentNews'] as List? ?? [];
    final rewardsList = json['activePlayerHeldRewards'] as List? ?? [];
    final pactsList = json['activePacts'] as List? ?? [];
    final offersList = json['cooperationOffers'] as List? ?? [];

    Map<String, int> winsMap = {};
    if (json['partyRoundWins'] != null) {
      Map<String, dynamic>.from(json['partyRoundWins']).forEach((k, v) {
        winsMap[k] = int.tryParse(v.toString()) ?? 0;
      });
    }

    Map<String, int> bidsMap = {};
    if (json['lastRoundBids'] != null) {
      Map<String, dynamic>.from(json['lastRoundBids']).forEach((k, v) {
        bidsMap[k] = int.tryParse(v.toString()) ?? 0;
      });
    }

    Map<String, int> electionShares = {};
    if (json['lastElectionVoteShares'] != null) {
      Map<String, dynamic>.from(json['lastElectionVoteShares']).forEach((k, v) {
        electionShares[k] = int.tryParse(v.toString()) ?? 0;
      });
    }

    return TurnView(
      gameId: json['gameId'] ?? json['id'] ?? '',
      scenarioKey: json['scenarioKey'] ?? '',
      stateName: json['stateName'] ?? '',
      currentDate: json['currentDate'] ?? '',
      turnNumber: json['turnNumber'] ?? 1,
      monthInCycle: json['monthInCycle'] ?? 1,
      status: json['status'] ?? 'ONGOING',
      activeHumanPartyId: json['activeHumanPartyId'],
      activeHumanPartyName: json['activeHumanPartyName'],
      monthsUntilMandatoryElection: json['monthsUntilMandatoryElection'] ?? 60,
      noConfidenceAvailable: json['noConfidenceAvailable'] ?? false,
      noConfidenceReason: json['noConfidenceReason'] ?? '',
      parties: partiesList.map((p) => Party.fromJson(Map<String, dynamic>.from(p))).toList(),
      publicState: PublicState.fromJson(Map<String, dynamic>.from(json['publicState'] ?? {})),
      availableCards: cardsList.map((c) => StrategicCard.fromJson(Map<String, dynamic>.from(c))).toList(),
      delayedEffects: json['delayedEffects'] as List? ?? [],
      pendingResults: json['pendingResults'] as List? ?? [],
      currentNews: newsList.map((n) => NewsItem.fromJson(Map<String, dynamic>.from(n))).toList(),
      currentIssue: json['currentIssue'] != null
          ? IssueItem.fromJson(Map<String, dynamic>.from(json['currentIssue']))
          : null,
      lastRoundSubmissions: json['lastRoundSubmissions'] as List? ?? [],
      lastMetricDeltas: json['lastMetricDeltas'] != null ? Map<String, dynamic>.from(json['lastMetricDeltas']) : {},
      lastRoundCommentary: List<String>.from(json['lastRoundCommentary'] ?? []),
      lastResults: List<String>.from(json['lastResults'] ?? []),
      currentRewardName: json['currentRewardName'],
      currentRewardDescription: json['currentRewardDescription'],
      partyRoundWins: winsMap,
      lastRoundBids: bidsMap,
      lastRoundBiddingMetric: json['lastRoundBiddingMetric'],
      lastRoundWinnerPartyId: json['lastRoundWinnerPartyId'],
      biddingMetric: json['biddingMetric'] ?? 'COINS',
      activePlayerHeldRewards: rewardsList.map((r) => HeldReward.fromJson(Map<String, dynamic>.from(r))).toList(),
      activePacts: pactsList.map((p) => ActivePact.fromJson(Map<String, dynamic>.from(p))).toList(),
      cooperationOffers: offersList.map((o) => CooperationOffer.fromJson(Map<String, dynamic>.from(o))).toList(),
      lastElectionHeld: json['lastElectionHeld'] ?? false,
      lastElectionWinner: json['lastElectionWinner'],
      lastElectionVoteShares: electionShares.isNotEmpty ? electionShares : null,
    );
  }
}

class GameSessionSummary {
  final String id;
  final String scenarioKey;
  final String? scenarioName;
  final String currentDate;
  final int turnNumber;
  final String status;
  final String? createdAt;
  final String? playerPartyId;
  final String? lastElectionWinner;
  final List<Party>? parties;

  GameSessionSummary({
    required this.id,
    required this.scenarioKey,
    this.scenarioName,
    required this.currentDate,
    required this.turnNumber,
    required this.status,
    this.createdAt,
    this.playerPartyId,
    this.lastElectionWinner,
    this.parties,
  });

  factory GameSessionSummary.fromJson(Map<String, dynamic> json) {
    final partiesList = json['parties'] as List?;
    return GameSessionSummary(
      id: json['id'] ?? '',
      scenarioKey: json['scenarioKey'] ?? '',
      scenarioName: json['scenarioName'],
      currentDate: json['currentDate'] ?? '',
      turnNumber: json['turnNumber'] ?? 1,
      status: json['status'] ?? 'ONGOING',
      createdAt: json['createdAt'],
      playerPartyId: json['playerPartyId'],
      lastElectionWinner: json['lastElectionWinner'],
      parties: partiesList != null
          ? partiesList.map((p) => Party.fromJson(Map<String, dynamic>.from(p))).toList()
          : null,
    );
  }
}
