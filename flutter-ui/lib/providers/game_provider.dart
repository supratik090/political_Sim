import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../api/api_service.dart';
import '../models/models.dart';

class GameProvider extends ChangeNotifier {
  final ApiService _api = ApiService.instance;

  String get apiBaseUrl => _api.baseUrl;

  void updateApiBaseUrl(String url) {
    _api.baseUrl = url;
    notifyListeners();
  }

  bool _isLoading = false;
  bool get isLoading => _isLoading;

  bool _isAuthChecking = true;
  bool get isAuthChecking => _isAuthChecking;

  String? _currentGameId;
  String? get currentGameId => _currentGameId;

  TurnView? _currentTurnView;
  TurnView? get currentTurnView => _currentTurnView;

  List<ScenarioProgress> _scenarios = [];
  List<ScenarioProgress> get scenarios => _scenarios;

  List<GameSessionSummary> _savedGames = [];
  List<GameSessionSummary> get savedGames => _savedGames;

  User? _user;
  User? get user => _user;

  String _currentScreen = 'HOME'; // 'HOME', 'GAME', 'ADMIN'
  String get currentScreen => _currentScreen;

  String? _errorMessage;
  String? get errorMessage => _errorMessage;

  // --- Turn Decisions State ---
  StrategicCard? _selectedCard;
  StrategicCard? get selectedCard => _selectedCard;

  String? _targetPartyId;
  String? get targetPartyId => _targetPartyId;

  final Map<String, String> _selectedNewsReactions = {};
  Map<String, String> get selectedNewsReactions => _selectedNewsReactions;

  String? _selectedIssueOptionKey;
  String? get selectedIssueOptionKey => _selectedIssueOptionKey;

  int _bidAmount = 0;
  int get bidAmount => _bidAmount;

  bool _bidConfirmed = false;
  bool get bidConfirmed => _bidConfirmed;

  String? _selectedRewardKey;
  String? get selectedRewardKey => _selectedRewardKey;

  String? _rewardTargetPartyId;
  String? get rewardTargetPartyId => _rewardTargetPartyId;

  bool _rewardConfirmed = false;
  bool get rewardConfirmed => _rewardConfirmed;

  // --- Action 6 Party Building state ---
  final List<String> _draftProjectKeys = [];
  List<String> get draftProjectKeys => _draftProjectKeys;

  final Map<String, int> _fundingContributions = {};
  Map<String, int> get fundingContributions => _fundingContributions;

  bool _partyBuildingConfirmed = false;
  bool get partyBuildingConfirmed => _partyBuildingConfirmed;

  void setScreen(String screen) {
    _currentScreen = screen;
    notifyListeners();
  }

  void clearError() {
    _errorMessage = null;
    notifyListeners();
  }

  Future<void> tryAutoLogin() async {
    _isAuthChecking = true;
    notifyListeners();

    try {
      final prefs = await SharedPreferences.getInstance();
      final id = prefs.getString('developer_user_id');
      final email = prefs.getString('developer_email');
      final name = prefs.getString('developer_name');
      final loginTime = prefs.getInt('developer_login_time');

      if (email != null && loginTime != null && id != null) {
        final now = DateTime.now().millisecondsSinceEpoch;
        const fiveDaysInMillis = 5 * 24 * 60 * 60 * 1000;
        if (now - loginTime < fiveDaysInMillis) {
          _user = User(id: id, name: name ?? email.split('@')[0].toUpperCase(), email: email);
          await Future.wait([
            loadScenarios(),
            loadSavedGames(),
          ]);
        } else {
          // Session expired
          await prefs.remove('developer_user_id');
          await prefs.remove('developer_email');
          await prefs.remove('developer_name');
          await prefs.remove('developer_login_time');
        }
      }
    } catch (e) {
      _errorMessage = 'Auto login error: $e';
    } finally {
      _isAuthChecking = false;
      notifyListeners();
    }
  }

  Future<bool> registerUser({
    required String email,
    required String name,
    required String password,
  }) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      final res = await _api.registerUser(email: email, name: name, password: password);
      final registered = User.fromJson(res);
      _user = registered;
      
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString('developer_user_id', registered.id);
      await prefs.setString('developer_email', registered.email);
      await prefs.setString('developer_name', registered.name);
      await prefs.setInt('developer_login_time', DateTime.now().millisecondsSinceEpoch);

      await Future.wait([
        loadScenarios(),
        loadSavedGames(),
      ]);
      return true;
    } catch (e) {
      _errorMessage = e.toString().replaceFirst('Exception: ', '');
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> loginUser({
    required String email,
    required String password,
  }) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      final res = await _api.loginUserApi(email: email, password: password);
      final loggedIn = User.fromJson(res);
      _user = loggedIn;

      final prefs = await SharedPreferences.getInstance();
      await prefs.setString('developer_user_id', loggedIn.id);
      await prefs.setString('developer_email', loggedIn.email);
      await prefs.setString('developer_name', loggedIn.name);
      await prefs.setInt('developer_login_time', DateTime.now().millisecondsSinceEpoch);

      await Future.wait([
        loadScenarios(),
        loadSavedGames(),
      ]);
      return true;
    } catch (e) {
      _errorMessage = e.toString().replaceFirst('Exception: ', '');
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> logout() async {
    _user = null;
    _scenarios = [];
    _savedGames = [];
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.remove('developer_user_id');
      await prefs.remove('developer_email');
      await prefs.remove('developer_name');
      await prefs.remove('developer_login_time');
    } catch (e) {
      debugPrint('Failed to clear session: $e');
    }
    exitGame();
    notifyListeners();
  }

  Future<void> loadScenarios() async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      _scenarios = await _api.getScenarios();
    } catch (e) {
      _errorMessage = 'Failed to load scenarios: $e';
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> loadSavedGames() async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      _savedGames = await _api.listGames(userId: _user?.email);
    } catch (e) {
      _errorMessage = 'Failed to load saved games: $e';
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> createNewGame(Map<String, dynamic> payload) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    if (_user != null) {
      payload['userId'] = _user!.email;
    }

    try {
      final game = await _api.createGame(payload);
      _currentGameId = game['id'];
      if (_currentGameId != null) {
        await loadTurnView(_currentGameId!);
        resetDecisions();
        _currentScreen = 'GAME';
        return true;
      } else {
        _errorMessage = 'Server did not return a valid game ID';
        return false;
      }
    } catch (e) {
      _errorMessage = 'Failed to create game: $e';
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> loadGame(String gameId) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      _currentGameId = gameId;
      await loadTurnView(gameId);
      resetDecisions();
      _currentScreen = 'GAME';
      return true;
    } catch (e) {
      _errorMessage = 'Failed to load game $gameId: $e';
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> deleteGame(String gameId) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      await _api.deleteGame(gameId);
      await loadSavedGames();
    } catch (e) {
      _errorMessage = 'Failed to delete campaign: $e';
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> loadTurnView(String gameId) async {
    try {
      _currentTurnView = await _api.fetchTurnView(gameId);
    } catch (e) {
      _errorMessage = 'Failed to fetch turn details: $e';
      rethrow;
    }
  }

  void resetDecisions() {
    _selectedCard = null;
    _targetPartyId = null;
    _selectedNewsReactions.clear();
    _selectedIssueOptionKey = null;
    _bidAmount = 0;
    _bidConfirmed = false;
    _selectedRewardKey = null;
    _rewardTargetPartyId = null;
    _rewardConfirmed = false;
    _draftProjectKeys.clear();
    _fundingContributions.clear();
    _partyBuildingConfirmed = false;
  }

  // --- Decisions Mutators ---
  void selectCard(StrategicCard? card) {
    _selectedCard = card;
    _targetPartyId = null;
    notifyListeners();
  }

  void setCardTarget(String? targetId) {
    _targetPartyId = targetId;
    notifyListeners();
  }

  void selectNewsReaction(String newsKey, String optionKey) {
    _selectedNewsReactions[newsKey] = optionKey;
    notifyListeners();
  }

  void setIssueOption(String? optionKey) {
    _selectedIssueOptionKey = optionKey;
    notifyListeners();
  }

  void setBidAmount(int amount) {
    _bidAmount = amount;
    notifyListeners();
  }

  void setBidConfirmed(bool val) {
    _bidConfirmed = val;
    notifyListeners();
  }

  void selectReward(String? rewardKey) {
    _selectedRewardKey = rewardKey;
    _rewardTargetPartyId = null;
    _rewardConfirmed = false;
    notifyListeners();
  }

  void setRewardTarget(String? targetId) {
    _rewardTargetPartyId = targetId;
    _rewardConfirmed = false;
    notifyListeners();
  }

  void setRewardConfirmed(bool val) {
    _rewardConfirmed = val;
    notifyListeners();
  }

  // --- Action 6 Party Building state manipulation ---
  void addDraftProject(String projectKey) {
    if (!_draftProjectKeys.contains(projectKey)) {
      _draftProjectKeys.add(projectKey);
      _partyBuildingConfirmed = false;
      notifyListeners();
    }
  }

  void removeDraftProject(String projectKey) {
    _draftProjectKeys.remove(projectKey);
    _fundingContributions.remove(projectKey);
    _partyBuildingConfirmed = false;
    notifyListeners();
  }

  void updateFundingContribution(String projectKey, int progress) {
    _fundingContributions[projectKey] = progress;
    _partyBuildingConfirmed = false;
    notifyListeners();
  }

  void setPartyBuildingConfirmed(bool val) {
    _partyBuildingConfirmed = val;
    notifyListeners();
  }

  // --- Action 6 REST triggers ---
  Future<bool> fundProject(String partyId, String projectKey, int progress) async {
    if (_currentGameId == null) return false;
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      _currentTurnView = await _api.fundProject(_currentGameId!, partyId, projectKey, progress);
      _fundingContributions.remove(projectKey);
      _draftProjectKeys.remove(projectKey);
      _partyBuildingConfirmed = false;
      return true;
    } catch (e) {
      _errorMessage = 'Failed to fund project: $e';
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> destroyProject(String partyId, String projectKey) async {
    if (_currentGameId == null) return false;
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      _currentTurnView = await _api.destroyProject(_currentGameId!, partyId, projectKey);
      _fundingContributions.remove(projectKey);
      _draftProjectKeys.remove(projectKey);
      _partyBuildingConfirmed = false;
      return true;
    } catch (e) {
      _errorMessage = 'Failed to destroy project: $e';
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> setProjectTarget(String partyId, String projectKey, String targetPartyId) async {
    if (_currentGameId == null) return false;
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      _currentTurnView = await _api.setProjectTarget(_currentGameId!, partyId, projectKey, targetPartyId);
      return true;
    } catch (e) {
      _errorMessage = 'Failed to set target: $e';
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  // --- Action 7 Cooperation REST triggers ---
  Future<bool> proposeCooperationOffer(Map<String, dynamic> payload) async {
    if (_currentGameId == null) return false;
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      _currentTurnView = await _api.createCooperationOffer(_currentGameId!, payload);
      return true;
    } catch (e) {
      _errorMessage = 'Failed to submit proposal: $e';
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> respondToCooperationOffer(String offerId, bool accept) async {
    if (_currentGameId == null) return false;
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      _currentTurnView = await _api.respondToCooperationOffer(_currentGameId!, offerId, accept);
      return true;
    } catch (e) {
      _errorMessage = 'Failed to respond to proposal: $e';
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  // --- Decisions Validation ---
  bool get isReadyToSubmit {
    if (_currentTurnView == null) return false;

    // 1. Must select a card
    if (_selectedCard == null) return false;

    // 2. Must select target if required
    if (_selectedCard!.requiresTarget && (_targetPartyId == null || _targetPartyId!.isEmpty)) {
      return false;
    }

    // 3. Must react to all current news items
    for (var news in _currentTurnView!.currentNews) {
      if (!_selectedNewsReactions.containsKey(news.newsKey)) return false;
    }

    // 4. Must select choice for current active party issue
    if (_currentTurnView!.currentIssue != null && _selectedIssueOptionKey == null) {
      return false;
    }

    // 5. Must lock blind bidding
    if (!_bidConfirmed) return false;

    // 6. Must complete reward target if reward selected
    final selectedReward = _currentTurnView!.activePlayerHeldRewards
        .firstWhere((r) => r.rewardKey == _selectedRewardKey, orElse: () => HeldReward(rewardKey: '', name: '', description: '', turnsLeft: 0, requiresTarget: false));
    if (selectedReward.rewardKey.isNotEmpty) {
      if (selectedReward.requiresTarget && (_rewardTargetPartyId == null || _rewardTargetPartyId!.isEmpty)) {
        return false;
      }
      if (!_rewardConfirmed) return false;
    }

    // 7. Must lock building projects selection if there are active draft states
    final hasDraftStates = _draftProjectKeys.isNotEmpty || _fundingContributions.values.any((v) => v > 0);
    if (hasDraftStates && !_partyBuildingConfirmed) return false;

    return true;
  }

  // --- Advance Turn Loop ---
  Future<bool> submitTurn() async {
    if (_currentGameId == null || !isReadyToSubmit) return false;
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      final payload = {
        'selectedCardKey': _selectedCard!.cardKey,
        'targetPartyId': _selectedCard!.requiresTarget ? _targetPartyId : null,
        'selectedNewsReactions': _selectedNewsReactions,
        'selectedIssueOptionKey': _currentTurnView!.currentIssue != null ? _selectedIssueOptionKey : 'routine_maintenance',
        'bid': _bidAmount,
        'selectedRewardKey': _selectedRewardKey != null && _selectedRewardKey!.isNotEmpty ? _selectedRewardKey : null,
        'rewardTargetPartyId': _selectedRewardKey != null && _selectedRewardKey!.isNotEmpty && _rewardTargetPartyId != null ? _rewardTargetPartyId : null,
      };

      _currentTurnView = await _api.advanceTurn(_currentGameId!, payload);
      resetDecisions();
      await loadSavedGames();
      return true;
    } catch (e) {
      _errorMessage = e.toString().replaceFirst('Exception: ', '');
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> skipTurn(Map<String, String> defaultReactions, String defaultIssueOptionKey) async {
    if (_currentGameId == null) return false;
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      final payload = {
        'selectedCardKey': 'no_card',
        'targetPartyId': null,
        'selectedNewsReactions': defaultReactions,
        'selectedIssueOptionKey': defaultIssueOptionKey,
        'bid': 0,
        'selectedRewardKey': null,
        'rewardTargetPartyId': null,
      };

      _currentTurnView = await _api.advanceTurn(_currentGameId!, payload);
      resetDecisions();
      await loadSavedGames();
      return true;
    } catch (e) {
      _errorMessage = e.toString().replaceFirst('Exception: ', '');
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> forfeitActiveGame() async {
    if (_currentGameId == null) return false;
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      await _api.forfeitGame(_currentGameId!);
      exitGame();
      await loadSavedGames();
      return true;
    } catch (e) {
      _errorMessage = 'Failed to forfeit campaign: $e';
      return false;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  void exitGame() {
    _currentGameId = null;
    _currentTurnView = null;
    _currentScreen = 'HOME';
    resetDecisions();
    notifyListeners();
  }
}
