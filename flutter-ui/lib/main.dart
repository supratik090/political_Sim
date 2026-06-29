import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'providers/game_provider.dart';
import 'screens/landing_screen.dart';
import 'screens/auth_screen.dart';
import 'screens/dashboard_screen.dart';
import 'screens/game_play_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => GameProvider()),
      ],
      child: const PoliticalSimApp(),
    ),
  );
}

class PoliticalSimApp extends StatefulWidget {
  const PoliticalSimApp({Key? key}) : super(key: key);

  @override
  State<PoliticalSimApp> createState() => _PoliticalSimAppState();
}

class _PoliticalSimAppState extends State<PoliticalSimApp> {
  bool _isPlayClicked = false;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      Provider.of<GameProvider>(context, listen: false).tryAutoLogin();
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Bharat Rajneeti',
      debugShowCheckedModeBanner: false,
      themeMode: ThemeMode.dark,
      darkTheme: ThemeData(
        brightness: Brightness.dark,
        fontFamily: 'Montserrat',
        colorScheme: const ColorScheme.dark(
          primary: Color(0xFF6366F1), // Indigo
          secondary: Color(0xFF10B981), // Emerald
          background: Color(0xFF0F172A), // Deep Slate 900
          surface: Color(0xFF1E293B), // Slate 800
          onPrimary: Colors.white,
          onSecondary: Colors.white,
          onBackground: Color(0xFFF8FAFC),
          onSurface: Color(0xFFF8FAFC),
        ),
        scaffoldBackgroundColor: const Color(0xFF0F172A),
        cardTheme: CardTheme(
          color: const Color(0xFF1E293B),
          elevation: 4,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
            side: const BorderSide(color: Color(0xFF334155), width: 1),
          ),
        ),
        inputDecorationTheme: InputDecorationTheme(
          filled: true,
          fillColor: const Color(0xFF0F172A),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(12),
            borderSide: const BorderSide(color: Color(0xFF334155)),
          ),
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(12),
            borderSide: const BorderSide(color: Color(0xFF334155)),
          ),
          focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(12),
            borderSide: const BorderSide(color: Color(0xFF6366F1), width: 2),
          ),
          labelStyle: const TextStyle(color: Color(0xFF94A3B8)),
        ),
      ),
      home: Consumer<GameProvider>(
        builder: (context, provider, child) {
          // 1. Splash check while restoring sessions
          if (provider.isAuthChecking) {
            return Scaffold(
              backgroundColor: const Color(0xFF0A0F1D),
              body: Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      width: 56,
                      height: 56,
                      child: const CircularProgressIndicator(
                        strokeWidth: 3,
                        valueColor: AlwaysStoppedAnimation<Color>(Color(0xFF38BDF8)),
                      ),
                    ),
                    const SizedBox(height: 24),
                    const Text(
                      'Restoring Campaign Session...',
                      style: TextStyle(
                        fontSize: 16,
                        color: Colors.white70,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 0.5,
                      ),
                    ),
                  ],
                ),
              ),
            );
          }

          // 2. Unauthenticated flows
          if (provider.user == null) {
            if (!_isPlayClicked) {
              return LandingScreen(
                onPlayNow: () {
                  setState(() {
                    _isPlayClicked = true;
                  });
                },
              );
            }
            return Stack(
              children: [
                const AuthScreen(),
                Positioned(
                  top: 20,
                  left: 20,
                  child: ElevatedButton.icon(
                    onPressed: () {
                      setState(() {
                        _isPlayClicked = false;
                      });
                    },
                    icon: const Icon(Icons.arrow_back_rounded, size: 14),
                    label: const Text('Back to Info'),
                    style: ElevatedButton.styleFrom(
                      primary: const Color(0x1DFFFFFF),
                      onPrimary: const Color(0xFF94A3B8),
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(30),
                        side: const BorderSide(color: Color(0x1AFFFFFF)),
                      ),
                      elevation: 0,
                    ),
                  ),
                ),
              ],
            );
          }

          // 3. Authenticated dashboard & routing flow
          if (provider.currentScreen == 'GAME' && provider.currentGameId != null) {
            return const GamePlayScreen();
          }

          // Default fallback is the main Dashboard setup screen
          return const DashboardScreen();
        },
      ),
    );
  }
}
