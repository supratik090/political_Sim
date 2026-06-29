import 'package:flutter/material.dart';

class ActionAccordion extends StatelessWidget {
  final int num;
  final String title;
  final bool isCompleted;
  final bool isOptional;
  final bool isExpanded;
  final ValueChanged<bool> onToggle;
  final Widget child;

  const ActionAccordion({
    Key? key,
    required this.num,
    required this.title,
    required this.isCompleted,
    this.isOptional = false,
    required this.isExpanded,
    required this.onToggle,
    required this.child,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      decoration: BoxDecoration(
        color: Colors.white,
        border: Border.all(
          color: isExpanded ? const Color(0xFF213C51) : const Color(0xFFB0CBE0),
          width: isExpanded ? 2.0 : 1.0,
        ),
        borderRadius: BorderRadius.circular(12),
        boxShadow: const [
          BoxShadow(
            color: Color(0x08213C51),
            blurRadius: 12,
            offset: Offset(0, 4),
          ),
        ],
      ),
      clipBehavior: Clip.antiAlias,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Header Bar
          InkWell(
            onTap: () => onToggle(!isExpanded),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 15),
              color: isExpanded ? const Color(0x0A213C51) : const Color(0x03213C51),
              child: Row(
                children: [
                  // Circular Step Number
                  Container(
                    width: 24,
                    height: 24,
                    decoration: const BoxDecoration(
                      shape: BoxShape.circle,
                      color: Color(0xFF213C51),
                    ),
                    child: Center(
                      child: Text(
                        '$num',
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 12,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(width: 12),

                  // Accordion Title
                  Expanded(
                    child: Text(
                      title.toUpperCase(),
                      style: const TextStyle(
                        fontSize: 12.5,
                        fontWeight: FontWeight.w900,
                        color: Color(0xFF213C51),
                        letterSpacing: 0.5,
                      ),
                    ),
                  ),

                  // Accordion Status Pill Badge
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                    decoration: BoxDecoration(
                      color: isCompleted
                          ? const Color(0x2622C55E)
                          : (isOptional ? const Color(0x1F213C51) : const Color(0x26D23F31)),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Text(
                      isCompleted
                          ? '✅ READY'
                          : (isOptional ? 'ℹ️ OPTIONAL' : '⏳ PENDING'),
                      style: TextStyle(
                        fontSize: 9,
                        fontWeight: FontWeight.w900,
                        color: isCompleted
                            ? const Color(0xFF22C55E)
                            : (isOptional ? const Color(0xFF213C51) : const Color(0xFFD23F31)),
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),

                  // Rotation Arrow Indicator
                  Icon(
                    isExpanded ? Icons.keyboard_arrow_down : Icons.keyboard_arrow_right,
                    color: const Color(0xFF213C51),
                    size: 18,
                  ),
                ],
              ),
            ),
          ),

          // Collapsible Content area
          if (isExpanded)
            Padding(
              padding: const EdgeInsets.all(20),
              child: child,
            ),
        ],
      ),
    );
  }
}
