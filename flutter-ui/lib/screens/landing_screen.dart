import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/game_provider.dart';

class LandingScreen extends StatefulWidget {
  final VoidCallback onPlayNow;

  const LandingScreen({Key? key, required this.onPlayNow}) : super(key: key);

  @override
  State<LandingScreen> createState() => _LandingScreenState();
}

class _LandingScreenState extends State<LandingScreen> {
  int _activeSlide = 0;

  final List<Map<String, String>> _slides = [
    {
      'title': 'Campaign Command Center',
      'desc': 'Analyze live state maps, track your core metrics (Coins, Morale, Support), and manage long-term infrastructure building projects like Mega Rallies and IT Cells.',
      'icon': '📊',
    },
    {
      'title': 'The State Chronicle Newspaper',
      'desc': 'React to monthly state-wide news events and regional crises. Select your stance wisely—every choice shapes public opinion and risks surprise backlashes.',
      'icon': '📰',
    },
    {
      'title': 'Bilateral Diplomacy Hub',
      'desc': 'Form coalition alliances, negotiate Non-Aggression Pacts, and trade assets (Coins, Morale, Support, or buildings) with other human or computer-controlled parties.',
      'icon': '🤝',
    }
  ];

  final List<Map<String, String>> _features = [
    {
      'icon': '⚡',
      'title': 'Dynamic Turn Resolution',
      'desc': 'An advance turn resolution cycle that applies strategic cards, evaluates project yields, normalizes voter shares, and reports tactical strategic commentaries.',
    },
    {
      'icon': '🛡️',
      'title': 'Smart AI Competitors',
      'desc': 'Play against responsive computer-controlled parties driven by unique strategic profiles (like Aggressive Populists) that hold grudges and retaliate dynamically.',
    },
    {
      'icon': '🏢',
      'title': 'Incremental Infrastructure',
      'desc': 'Fund long-term projects step-by-step. Achieve 100% completion to unlock persistent per-turn resource yields that pay back initial capital expenses.',
    },
    {
      'icon': '⚖️',
      'title': 'Bidding and Resource Bids',
      'desc': 'Submit blind bids using your party\'s reserves to win high-impact 5-turn cycle rewards, while managing safety limits to avoid bankruptcy.',
    }
  ];

  @override
  Widget build(BuildContext context) {
    final mediaQuery = MediaQuery.of(context);
    final isMobile = mediaQuery.size.width < 768;

    return Scaffold(
      backgroundColor: const Color(0xFF0A0F1D),
      body: SafeArea(
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              // Header/Navbar
              _buildHeader(isMobile),

              // Hero Section
              _buildHero(isMobile),

              // Walkthrough Carousel
              _buildCarousel(isMobile),

              const SizedBox(height: 60),

              // Features Grid
              _buildFeaturesGrid(isMobile),

              const SizedBox(height: 60),

              // Timeline: How to Play
              _buildTimeline(isMobile),

              // CTA Footer
              _buildFooter(isMobile),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildHeader(bool isMobile) {
    return Container(
      padding: EdgeInsets.symmetric(
        horizontal: isMobile ? 16 : 40,
        vertical: 20,
      ),
      decoration: const BoxDecoration(
        border: Border(
          bottom: BorderSide(color: Color(0x1A6594B1), width: 1),
        ),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: [
              Container(
                width: 36,
                height: 36,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(8),
                  gradient: const LinearGradient(
                    colors: [Color(0xFF38BDF8), Color(0xFF818CF8)],
                  ),
                ),
                child: const Center(
                  child: Text(
                    '🇮🇳',
                    style: TextStyle(fontSize: 20),
                  ),
                ),
              ),
              const SizedBox(width: 12),
              ShaderMask(
                shaderCallback: (bounds) => const LinearGradient(
                  colors: [Color(0xFF38BDF8), Color(0xFF818CF8)],
                ).createShader(bounds),
                child: const Text(
                  'BHARAT RAJNEETI',
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.w900,
                    letterSpacing: -0.5,
                    color: Colors.white,
                  ),
                ),
              ),
            ],
          ),
          ElevatedButton(
            onPressed: widget.onPlayNow,
            style: ElevatedButton.styleFrom(
              primary: Colors.transparent,
              shadowColor: Colors.transparent,
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(30),
              ),
            ).copyWith(
              backgroundColor: MaterialStateProperty.all(const Color(0xFF6366F1)),
            ),
            child: const Text(
              'Play Now',
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 13,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildHero(bool isMobile) {
    return Container(
      padding: EdgeInsets.symmetric(
        horizontal: isMobile ? 20 : 40,
        vertical: 80,
      ),
      child: Center(
        child: Container(
          constraints: const BoxConstraints(maxWidth: 800),
          child: Column(
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
                decoration: BoxDecoration(
                  color: const Color(0x1A38BDF8),
                  borderRadius: BorderRadius.circular(30),
                ),
                child: const Text(
                  'Grand Strategy Election Simulator',
                  style: TextStyle(
                    fontSize: 11,
                    fontWeight: FontWeight.w800,
                    color: Color(0xFF38BDF8),
                    letterSpacing: 1.5,
                  ),
                ),
              ),
              const SizedBox(height: 24),
              Text(
                'Experience the High-Stakes World of Indian Elections',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: isMobile ? 32 : 48,
                  fontWeight: FontWeight.w900,
                  color: Colors.white,
                  height: 1.1,
                  letterSpacing: -1,
                ),
              ),
              const SizedBox(height: 20),
              const Text(
                'Step into the boots of a campaign manager. Play strategy cards, govern news events, invest in mega-rallies, and sign diplomatic pacts to lead your party to power.',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 15,
                  color: Color(0xFF94A3B8),
                  height: 1.5,
                ),
              ),
              const SizedBox(height: 36),
              GestureDetector(
                onTap: widget.onPlayNow,
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 36, vertical: 16),
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(30),
                    gradient: const LinearGradient(
                      colors: [Color(0xFF0EA5E9), Color(0xFF6366F1)],
                    ),
                    boxShadow: const [
                      BoxShadow(
                        color: Color(0x666366F1),
                        blurRadius: 20,
                        offset: Offset(0, 8),
                      ),
                    ],
                  ),
                  child: const Text(
                    'Enter Campaign Board',
                    style: TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.w900,
                      color: Colors.white,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildCarousel(bool isMobile) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: isMobile ? 16 : 40),
      child: Center(
        child: Container(
          constraints: const BoxConstraints(maxWidth: 1000),
          child: Column(
            children: [
              const Text(
                'Interactive Gameplay Walkthrough',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 30),
              Container(
                decoration: BoxDecoration(
                  color: const Color(0x1A1E293B),
                  border: Border.all(color: const Color(0x336594B1), width: 1),
                  borderRadius: BorderRadius.circular(24),
                ),
                padding: const EdgeInsets.all(20),
                child: Column(
                  children: [
                    // Slide visual representer
                    Container(
                      height: isMobile ? 180 : 360,
                      width: double.infinity,
                      decoration: BoxDecoration(
                        color: const Color(0xFF070A13),
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(color: const Color(0x0DFFFFFF), width: 1),
                      ),
                      padding: const EdgeInsets.all(24),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Text(
                            _slides[_activeSlide]['icon']!,
                            style: const TextStyle(fontSize: 48),
                          ),
                          const SizedBox(height: 16),
                          Text(
                            _slides[_activeSlide]['title']!,
                            textAlign: TextAlign.center,
                            style: const TextStyle(
                              fontSize: 20,
                              fontWeight: FontWeight.bold,
                              color: Color(0xFF38BDF8),
                            ),
                          ),
                          const SizedBox(height: 12),
                          Expanded(
                            child: SingleChildScrollView(
                              child: Text(
                                _slides[_activeSlide]['desc']!,
                                textAlign: TextAlign.center,
                                style: const TextStyle(
                                  fontSize: 13,
                                  color: Color(0xFF94A3B8),
                                  height: 1.4,
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 20),
                    // Navigation selector
                    isMobile
                        ? Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: List.generate(
                              _slides.length,
                              (idx) => GestureDetector(
                                onTap: () => setState(() => _activeSlide = idx),
                                child: Container(
                                  margin: const EdgeInsets.symmetric(horizontal: 6),
                                  width: 12,
                                  height: 12,
                                  decoration: BoxDecoration(
                                    shape: BoxShape.circle,
                                    color: _activeSlide == idx
                                        ? const Color(0xFF38BDF8)
                                        : const Color(0x33FFFFFF),
                                  ),
                                ),
                              ),
                            ),
                          )
                        : GridView.count(
                            shrinkWrap: true,
                            physics: const NeverScrollableScrollPhysics(),
                            crossAxisCount: 3,
                            crossAxisSpacing: 16,
                            childAspectRatio: 2.2,
                            children: List.generate(_slides.length, (idx) {
                              final isActive = _activeSlide == idx;
                              return InkWell(
                                onTap: () => setState(() => _activeSlide = idx),
                                borderRadius: BorderRadius.circular(12),
                                child: Container(
                                  padding: const EdgeInsets.all(12),
                                  decoration: BoxDecoration(
                                    color: isActive
                                        ? const Color(0x266366F1)
                                        : Colors.transparent,
                                    border: Border.all(
                                      color: isActive
                                          ? const Color(0x666366F1)
                                          : const Color(0x0DFFFFFF),
                                      width: 1.5,
                                    ),
                                    borderRadius: BorderRadius.circular(12),
                                  ),
                                  child: Column(
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    mainAxisAlignment: MainAxisAlignment.center,
                                    children: [
                                      Text(
                                        _slides[idx]['title']!,
                                        style: TextStyle(
                                          fontSize: 13,
                                          fontWeight: FontWeight.bold,
                                          color: isActive
                                              ? const Color(0xFF38BDF8)
                                              : Colors.white,
                                        ),
                                      ),
                                      const SizedBox(height: 4),
                                      Text(
                                        _slides[idx]['desc']!,
                                        maxLines: 2,
                                        overflow: TextOverflow.ellipsis,
                                        style: const TextStyle(
                                          fontSize: 10,
                                          color: Color(0xFF94A3B8),
                                          height: 1.2,
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              );
                            }),
                          ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildFeaturesGrid(bool isMobile) {
    return Container(
      color: const Color(0xFF070A13),
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 60),
      child: Center(
        child: Container(
          constraints: const BoxConstraints(maxWidth: 1100),
          child: Column(
            children: [
              const Text(
                'Sophisticated Game Mechanics',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 26,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 10),
              const Text(
                'Every turn represents one month in a 5-year election cycle. Out-think your rival parties by balancing quick gains with long-term investments.',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 14,
                  color: Color(0xFF94A3B8),
                ),
              ),
              const SizedBox(height: 40),
              GridView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: isMobile ? 1 : 2,
                  crossAxisSpacing: 20,
                  mainAxisSpacing: 20,
                  childAspectRatio: isMobile ? 1.8 : 2.4,
                ),
                itemCount: _features.length,
                itemBuilder: (context, idx) {
                  final feat = _features[idx];
                  return Container(
                    padding: const EdgeInsets.all(20),
                    decoration: BoxDecoration(
                      color: const Color(0x0D1E293B),
                      border: Border.all(color: const Color(0x0DFFFFFF), width: 1),
                      borderRadius: BorderRadius.circular(16),
                    ),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Container(
                          width: 48,
                          height: 48,
                          decoration: BoxDecoration(
                            color: const Color(0x1A6366F1),
                            borderRadius: BorderRadius.circular(12),
                          ),
                          child: Center(
                            child: Text(
                              feat['icon']!,
                              style: const TextStyle(fontSize: 24),
                            ),
                          ),
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                feat['title']!,
                                style: const TextStyle(
                                  fontSize: 15,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white,
                                ),
                              ),
                              const SizedBox(height: 6),
                              Expanded(
                                child: Text(
                                  feat['desc']!,
                                  style: const TextStyle(
                                    fontSize: 12,
                                    color: Color(0xFF94A3B8),
                                    height: 1.3,
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  );
                },
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTimeline(bool isMobile) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 60),
      child: Center(
        child: Container(
          constraints: const BoxConstraints(maxWidth: 800),
          child: Column(
            children: [
              const Text(
                'How to Play a Round',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 26,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 40),
              _buildTimelineStep(1, 'Select strategy cards',
                  'Choose a role-based political card to play. Spend coins to launch smears, media campaigns, or legal challenges against target rival parties.'),
              _buildTimelineDivider(),
              _buildTimelineStep(2, 'React to state news',
                  'Read the monthly newspaper and make structural choices. Call audits, offer drought relief packages, or propose grassland reserves to boost support.'),
              _buildTimelineDivider(),
              _buildTimelineStep(3, 'Negotiate pacts & Bids',
                  'Submit blind bids for cycle rewards. Propose non-aggression treaties or request asset trades with rival parties before advancing the turn.'),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTimelineStep(int num, String title, String desc) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          width: 36,
          height: 36,
          decoration: const BoxDecoration(
            shape: BoxShape.circle,
            gradient: LinearGradient(
              colors: [Color(0xFF0EA5E9), Color(0xFF6366F1)],
            ),
          ),
          child: Center(
            child: Text(
              '$num',
              style: const TextStyle(
                fontWeight: FontWeight.bold,
                color: Colors.white,
                fontSize: 14,
              ),
            ),
          ),
        ),
        const SizedBox(width: 20),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                title,
                style: const TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 6),
              Text(
                desc,
                style: const TextStyle(
                  fontSize: 13,
                  color: Color(0xFF94A3B8),
                  height: 1.4,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildTimelineDivider() {
    return Container(
      margin: const EdgeInsets.only(left: 18, top: 8, bottom: 8),
      height: 30,
      width: 2,
      color: const Color(0x336594B1),
    );
  }

  Widget _buildFooter(bool isMobile) {
    return Container(
      color: const Color(0xFF070A13),
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 60),
      child: Center(
        child: Container(
          constraints: const BoxConstraints(maxWidth: 600),
          child: Column(
            children: [
              const Text(
                'Ready to Run Your Campaign?',
                textAlign: TextAlign.center,
                style: const TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 12),
              const Text(
                'Take command of active elections and see if you have the strategic mind to capture the assembly.',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 13,
                  color: Color(0xFF94A3B8),
                ),
              ),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: widget.onPlayNow,
                style: ElevatedButton.styleFrom(
                  primary: Colors.transparent,
                  shadowColor: Colors.transparent,
                  padding: const EdgeInsets.symmetric(horizontal: 36, vertical: 16),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(30),
                  ),
                ).copyWith(
                  backgroundColor: MaterialStateProperty.all(const Color(0xFF6366F1)),
                ),
                child: const Text(
                  'Start Playing',
                  style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(height: 40),
              const Text(
                '© 2026 Bharat Rajneeti. Built using premium responsive Web Technologies.',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 11,
                  color: Color(0xFF475569),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
