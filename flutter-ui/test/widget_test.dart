import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:flutter_ui/main.dart';
import 'package:flutter_ui/providers/game_provider.dart';

void main() {
  setUp(() {
    SharedPreferences.setMockInitialValues({});
  });

  testWidgets('App starts and displays Login Screen', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => GameProvider()),
        ],
        child: const PoliticalSimApp(),
      ),
    );

    // Let the initial frame render
    await tester.pump();
    
    // Provide a small timed pump to allow the async tryAutoLogin call to resolve SharedPreferences and rebuild
    await tester.pump(const Duration(milliseconds: 200));

    // Verify that the Developer Bypass login screen details are rendered
    expect(find.text('DEVELOPER BYPASS LOGIN'), findsOneWidget);
    expect(find.text('Proceed with Mock User'), findsOneWidget);
  });
}
