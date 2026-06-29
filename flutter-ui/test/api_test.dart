import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_ui/api/api_service.dart';

void main() {
  test('API Scenario Fetch Test', () async {
    print('Starting API Scenario Fetch Test inside Flutter Test Harness...');
    try {
      final service = ApiService.instance;
      print('Calling getScenarios from ${service.baseUrl}...');
      final scenarios = await service.getScenarios();
      print('Success! Fetched ${scenarios.length} scenarios.');
      for (var s in scenarios) {
        print('- ${s.name} (${s.scenarioKey}), active: ${s.active}');
        print('  Parties count: ${s.politicalParties.length}');
        for (var p in s.politicalParties) {
          print('    Party: ${p.name}, role: ${p.role}, stats: ${p.startingStats?.coins}');
        }
      }
      expect(scenarios, isNotEmpty);
    } catch (e, stack) {
      print('Failed with error: $e');
      print('Stack trace:');
      print(stack);
      fail('API request failed');
    }
  });
}
