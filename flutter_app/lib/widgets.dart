import 'package:flutter/material.dart';

const kTeal = Color(0xFF0D676B);
const kMark = Color(0xFFF5C451);
const kMarkInk = Color(0xFF2B2000);

Color goodColor(BuildContext c) =>
    Theme.of(c).brightness == Brightness.dark ? const Color(0xFF71D19B) : const Color(0xFF24774A);
Color badColor(BuildContext c) =>
    Theme.of(c).brightness == Brightness.dark ? const Color(0xFFF2917C) : const Color(0xFFB23E2B);

final _inline = RegExp(r'\*\*(.+?)\*\*|\[\[(.+?)\]\]|\*([^*\s][^*]*?)\*');

/// Text with **bold**, *italic* and [[highlighted keyword]] support.
List<InlineSpan> inlineSpans(String s, {bool showMarks = true}) {
  final spans = <InlineSpan>[];
  var last = 0;
  for (final m in _inline.allMatches(s)) {
    if (m.start > last) spans.add(TextSpan(text: s.substring(last, m.start)));
    if (m.group(1) != null) {
      spans.add(TextSpan(text: m.group(1), style: const TextStyle(fontWeight: FontWeight.w700)));
    } else if (m.group(2) != null) {
      spans.add(TextSpan(
        text: m.group(2),
        style: showMarks
            ? const TextStyle(backgroundColor: kMark, color: kMarkInk, fontWeight: FontWeight.w600)
            : null,
      ));
    } else {
      spans.add(TextSpan(text: m.group(3), style: const TextStyle(fontStyle: FontStyle.italic)));
    }
    last = m.end;
  }
  if (last < s.length) spans.add(TextSpan(text: s.substring(last)));
  return spans;
}

class Rich extends StatelessWidget {
  const Rich(this.text, {super.key, this.style, this.showMarks = true});
  final String text;
  final TextStyle? style;
  final bool showMarks;

  @override
  Widget build(BuildContext context) {
    final base = style ?? DefaultTextStyle.of(context).style;
    return Text.rich(TextSpan(style: base, children: inlineSpans(text, showMarks: showMarks)));
  }
}

class Bar extends StatelessWidget {
  const Bar(this.value, {super.key, this.height = 8});
  final double value;
  final double height;

  @override
  Widget build(BuildContext context) {
    return ClipRRect(
      borderRadius: BorderRadius.circular(height),
      child: LinearProgressIndicator(
        value: value.clamp(0.0, 1.0),
        minHeight: height,
        backgroundColor: Theme.of(context).colorScheme.surfaceContainerHighest,
      ),
    );
  }
}

class Label extends StatelessWidget {
  const Label(this.text, {super.key});
  final String text;

  @override
  Widget build(BuildContext context) {
    return Text(
      text.toUpperCase(),
      style: Theme.of(context).textTheme.labelSmall?.copyWith(
            letterSpacing: 1.1,
            color: Theme.of(context).colorScheme.onSurfaceVariant,
          ),
    );
  }
}

/// Renders lesson blocks made by app/build.js.
class Blocks extends StatelessWidget {
  const Blocks(this.blocks, {super.key});
  final List<dynamic> blocks;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [for (final b in blocks) _block(context, b as Map<String, dynamic>)],
    );
  }

  Widget _block(BuildContext context, Map<String, dynamic> b) {
    final t = Theme.of(context).textTheme;
    final scheme = Theme.of(context).colorScheme;
    final body = t.bodyLarge?.copyWith(height: 1.55);
    final type = b['t'] as String;

    if (type == 'h') {
      final level = (b['l'] as num).toInt();
      final style = level <= 2
          ? t.titleLarge?.copyWith(fontWeight: FontWeight.w800)
          : t.titleMedium?.copyWith(fontWeight: FontWeight.w700);
      return Padding(
        padding: const EdgeInsets.only(top: 20, bottom: 6),
        child: Rich(b['x'] as String, style: style),
      );
    }
    if (type == 'p') {
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: 6),
        child: Rich(b['x'] as String, style: body),
      );
    }
    if (type == 'hr') return const Divider(height: 32);
    if (type == 'q') {
      return Container(
        margin: const EdgeInsets.symmetric(vertical: 8),
        padding: const EdgeInsets.fromLTRB(14, 6, 12, 6),
        decoration: BoxDecoration(
          color: scheme.surfaceContainerHighest,
          border: const Border(left: BorderSide(color: kMark, width: 4)),
          borderRadius: const BorderRadius.horizontal(right: Radius.circular(10)),
        ),
        child: Blocks(b['b'] as List<dynamic>),
      );
    }
    if (type == 'ul' || type == 'ol') {
      final items = (b['items'] as List).map((x) => x as String).toList();
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: 4),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            for (var i = 0; i < items.length; i++)
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 3),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    SizedBox(width: 26, child: Text(type == 'ol' ? '${i + 1}.' : '•', style: body)),
                    Expanded(child: Rich(items[i], style: body)),
                  ],
                ),
              ),
          ],
        ),
      );
    }
    if (type == 'table') {
      final rows = (b['rows'] as List).map((r) => (r as List).map((x) => x as String).toList()).toList();
      final cols = rows.fold<int>(0, (n, r) => r.length > n ? r.length : n);
      final small = t.bodyMedium;
      return Padding(
        padding: const EdgeInsets.symmetric(vertical: 8),
        child: Table(
          border: TableBorder(horizontalInside: BorderSide(color: scheme.outlineVariant)),
          defaultVerticalAlignment: TableCellVerticalAlignment.top,
          children: [
            for (var r = 0; r < rows.length; r++)
              TableRow(
                decoration: r == 0 ? BoxDecoration(color: scheme.surfaceContainerHighest) : null,
                children: [
                  for (var c = 0; c < cols; c++)
                    Padding(
                      padding: const EdgeInsets.all(8),
                      child: Rich(
                        c < rows[r].length ? rows[r][c] : '',
                        style: r == 0 ? small?.copyWith(fontWeight: FontWeight.w700) : small,
                      ),
                    ),
                ],
              ),
          ],
        ),
      );
    }
    return const SizedBox.shrink();
  }
}
