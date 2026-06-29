import 'dart:convert';
import 'dart:io' show Platform;
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:http/http.dart' as http;
import '../models/models.dart';

class ApiService {
  static final ApiService instance = ApiService._internal();

  ApiService._internal();

  String _baseUrl = _getDefaultBaseUrl();

  static String _getDefaultBaseUrl() {
    if (kIsWeb) {
      return 'http://localhost:7810';
    }
    try {
      if (Platform.isAndroid) {
        return 'http://10.0.2.2:7810';
      }
    } catch (_) {}
    return 'http://localhost:7810';
  }

  String get baseUrl => _baseUrl;

  set baseUrl(String url) {
    _baseUrl = url;
  }

  Future<List<ScenarioProgress>> getScenarios() async {
    final response = await http.get(Uri.parse('$_baseUrl/api/admin/scenarios'));
    if (response.statusCode == 200) {
      final List<dynamic> data = json.decode(response.body);
      return data
          .map((item) => ScenarioProgress.fromJson(Map<String, dynamic>.from(item)))
          .toList();
    } else {
      throw Exception('Failed to load scenarios. Status code: ${response.statusCode}');
    }
  }

  Future<List<GameSessionSummary>> listGames({String? userId}) async {
    final uri = Uri.parse('$_baseUrl/api/games').replace(
      queryParameters: userId != null ? {'userId': userId} : null,
    );
    final response = await http.get(uri);
    if (response.statusCode == 200) {
      final List<dynamic> data = json.decode(response.body);
      return data
          .map((item) => GameSessionSummary.fromJson(Map<String, dynamic>.from(item)))
          .toList();
    } else {
      throw Exception('Failed to load saved games. Status code: ${response.statusCode}');
    }
  }

  Future<Map<String, dynamic>> createGame(Map<String, dynamic> payload) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/api/games'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode(payload),
    );
    if (response.statusCode == 201 || response.statusCode == 200) {
      return json.decode(response.body) as Map<String, dynamic>;
    } else {
      throw Exception('Failed to create game: ${response.body}');
    }
  }

  Future<TurnView> fetchTurnView(String gameId) async {
    final response = await http.get(Uri.parse('$_baseUrl/api/games/$gameId/turn-view'));
    if (response.statusCode == 200) {
      return TurnView.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to fetch turn view: ${response.body}');
    }
  }

  Future<TurnView> advanceTurn(String gameId, Map<String, dynamic> payload) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/api/games/$gameId/turn/advance'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode(payload),
    );
    if (response.statusCode == 200 || response.statusCode == 201) {
      return TurnView.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to advance turn: ${response.body}');
    }
  }

  Future<Map<String, dynamic>> forfeitGame(String gameId) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/api/games/$gameId/forfeit'),
    );
    if (response.statusCode == 200) {
      return json.decode(response.body) as Map<String, dynamic>;
    } else {
      throw Exception('Failed to forfeit game: ${response.body}');
    }
  }

  Future<void> deleteGame(String gameId) async {
    final response = await http.delete(
      Uri.parse('$_baseUrl/api/games/$gameId'),
    );
    if (response.statusCode != 200 && response.statusCode != 204) {
      throw Exception('Failed to delete game: ${response.body}');
    }
  }

  Future<Map<String, dynamic>> getCampaignProgress({String? userId}) async {
    final uri = Uri.parse('$_baseUrl/api/scenarios/progress').replace(
      queryParameters: userId != null ? {'userId': userId} : null,
    );
    final response = await http.get(uri);
    if (response.statusCode == 200) {
      return json.decode(response.body) as Map<String, dynamic>;
    } else {
      throw Exception('Failed to fetch campaign progress: ${response.body}');
    }
  }

  Future<Map<String, dynamic>> fetchBuildingProjects() async {
    final response = await http.get(
      Uri.parse('$_baseUrl/api/games/building-projects/definitions'),
    );
    if (response.statusCode == 200) {
      return json.decode(response.body) as Map<String, dynamic>;
    } else {
      throw Exception('Failed to fetch building project definitions: ${response.body}');
    }
  }

  Future<TurnView> fundProject(String gameId, String partyId, String projectKey, int progress) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/api/games/$gameId/parties/$partyId/projects/fund?projectKey=$projectKey&progress=$progress'),
    );
    if (response.statusCode == 200 || response.statusCode == 201) {
      return TurnView.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to fund project: ${response.body}');
    }
  }

  Future<TurnView> destroyProject(String gameId, String partyId, String projectKey) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/api/games/$gameId/parties/$partyId/projects/destroy?projectKey=$projectKey'),
    );
    if (response.statusCode == 200 || response.statusCode == 201) {
      return TurnView.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to destroy project: ${response.body}');
    }
  }

  Future<TurnView> setProjectTarget(String gameId, String partyId, String projectKey, String targetPartyId) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/api/games/$gameId/parties/$partyId/projects/$projectKey/target?targetPartyId=$targetPartyId'),
    );
    if (response.statusCode == 200 || response.statusCode == 201) {
      return TurnView.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to set project target: ${response.body}');
    }
  }

  Future<TurnView> createCooperationOffer(String gameId, Map<String, dynamic> payload) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/api/games/$gameId/cooperation/offer'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode(payload),
    );
    if (response.statusCode == 200 || response.statusCode == 201) {
      return TurnView.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to propose diplomatic offer: ${response.body}');
    }
  }

  Future<TurnView> respondToCooperationOffer(String gameId, String offerId, bool accept) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/api/games/$gameId/cooperation/respond?offerId=$offerId&accept=$accept'),
    );
    if (response.statusCode == 200 || response.statusCode == 201) {
      return TurnView.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to respond to diplomatic offer: ${response.body}');
    }
  }

  Future<Map<String, dynamic>> registerUser({
    required String email,
    required String name,
    required String password,
  }) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/api/auth/register'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({
        'email': email.trim().toLowerCase(),
        'name': name.trim(),
        'password': password,
      }),
    );
    if (response.statusCode == 201 || response.statusCode == 200) {
      return json.decode(response.body) as Map<String, dynamic>;
    } else {
      final body = json.decode(response.body);
      throw Exception(body['error'] ?? 'Registration failed (${response.statusCode})');
    }
  }

  Future<Map<String, dynamic>> loginUserApi({
    required String email,
    required String password,
  }) async {
    final response = await http.post(
      Uri.parse('$_baseUrl/api/auth/login'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({
        'email': email.trim().toLowerCase(),
        'password': password,
      }),
    );
    if (response.statusCode == 200) {
      return json.decode(response.body) as Map<String, dynamic>;
    } else {
      final body = json.decode(response.body);
      throw Exception(body['error'] ?? 'Login failed (${response.statusCode})');
    }
  }
}
