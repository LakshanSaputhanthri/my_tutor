import 'dart:convert';
import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'content.dart';
import 'widgets.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final raw = await rootBundle.loadString('assets/content.json');
  final content = Content.fromJson(jsonDecode(raw) as Map<String, dynamic>);
  final prefs = await SharedPreferences.getInstance();
  runApp(BridgeApp(state: AppState(prefs, content)));
}

class BridgeApp extends StatelessWidget {
  const BridgeApp({super.key, required this.state});
  final AppState state;

  ThemeData _theme(Brightness b) => ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: kTeal, brightness: b),
      );

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AWS Bridge',
      debugShowCheckedModeBanner: false,
      theme: _theme(Brightness.light),
      darkTheme: _theme(Brightness.dark),
      home: Shell(state: state),
    );
  }
}

String pctText(double f) {
  final p = f * 100;
  return p > 0 && p < 10 ? p.toStringAsFixed(1) : p.round().toString();
}

class OverallBar extends StatelessWidget {
  const OverallBar({super.key, required this.state});
  final AppState state;

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: state,
      builder: (context, _) => Padding(
        padding: const EdgeInsets.fromLTRB(16, 0, 16, 10),
        child: Row(children: [
          Expanded(child: Bar(state.overall, height: 10)),
          const SizedBox(width: 12),
          Text('${pctText(state.overall)}% ready',
              style: Theme.of(context).textTheme.labelLarge?.copyWith(fontWeight: FontWeight.w700)),
        ]),
      ),
    );
  }
}

class Shell extends StatefulWidget {
  const Shell({super.key, required this.state});
  final AppState state;

  @override
  State<Shell> createState() => _ShellState();
}

class _ShellState extends State<Shell> {
  int tab = 0;

  void goTab(int i) => setState(() => tab = i);

  @override
  Widget build(BuildContext context) {
    final s = widget.state;
    return Scaffold(
      appBar: AppBar(
        title: const Text('AWS English Bridge', style: TextStyle(fontWeight: FontWeight.w800)),
        bottom: PreferredSize(preferredSize: const Size.fromHeight(34), child: OverallBar(state: s)),
      ),
      body: IndexedStack(index: tab, children: [
        HomePage(state: s, goTab: goTab),
        LessonsPage(state: s),
        WordsPage(state: s),
        PracticePage(state: s),
        GamePage(state: s),
      ]),
      bottomNavigationBar: NavigationBar(
        selectedIndex: tab,
        onDestinationSelected: goTab,
        destinations: const [
          NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home), label: 'Home'),
          NavigationDestination(icon: Icon(Icons.menu_book_outlined), selectedIcon: Icon(Icons.menu_book), label: 'Lessons'),
          NavigationDestination(icon: Icon(Icons.style_outlined), selectedIcon: Icon(Icons.style), label: 'Words'),
          NavigationDestination(icon: Icon(Icons.fact_check_outlined), selectedIcon: Icon(Icons.fact_check), label: 'Practice'),
          NavigationDestination(icon: Icon(Icons.bolt_outlined), selectedIcon: Icon(Icons.bolt), label: 'Game'),
        ],
      ),
    );
  }
}

void openLesson(BuildContext context, AppState s, Lesson l) =>
    Navigator.push(context, MaterialPageRoute(builder: (_) => LessonReader(state: s, lesson: l)));

void openSet(BuildContext context, AppState s, QSet q) =>
    Navigator.push(context, MaterialPageRoute(builder: (_) => QuizPage(state: s, set: q)));

/* ---------------- HOME ---------------- */

class NextStep {
  NextStep(this.label, this.note, this.go);
  final String label;
  final String note;
  final void Function(BuildContext) go;
}

NextStep nextStep(AppState s, void Function(int) goTab) {
  final c = s.content;
  if (s.known.length < 10) {
    return NextStep('Words 10ක් ඉගෙන ගන්න', 'මුලින්ම exam English වචන 10ක්.', (_) => goTab(2));
  }
  final bridge = c.setById('bridge')!;
  if (s.answersOf('bridge').length < bridge.qs.length) {
    return NextStep('Sinhala bridge questions', 'සිංහල උදව් එක්ක questions 20.', (ctx) => openSet(ctx, s, bridge));
  }
  for (final l in c.lessons) {
    if (!s.lessonsDone.contains(l.id)) {
      return NextStep('කියවන්න: ${l.short}', 'ඊළඟට කියවන්න ඕන lesson එක.', (ctx) => openLesson(ctx, s, l));
    }
  }
  for (final q in c.sets) {
    if (s.correctOf(q.id) < q.qs.length * .85) {
      return NextStep('Practice: ${q.title}', '85%ට අඩු set එක.', (ctx) => openSet(ctx, s, q));
    }
  }
  return NextStep('Mock exam 2 ආයෙත්', 'ඔක්කොම 85%+ — exam එක book කරන්න පුළුවන්!',
      (ctx) => openSet(ctx, s, c.setById('mock2')!));
}

class HomePage extends StatefulWidget {
  const HomePage({super.key, required this.state, required this.goTab});
  final AppState state;
  final void Function(int) goTab;

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final _backup = TextEditingController();
  String _msg = '';
  bool _resetArmed = false;

  @override
  void dispose() {
    _backup.dispose();
    super.dispose();
  }

  Widget _stat(String label, String value, double? f) => Padding(
        padding: const EdgeInsets.symmetric(vertical: 6),
        child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
          Row(children: [
            Expanded(child: Text(label, style: const TextStyle(fontWeight: FontWeight.w600))),
            Text(value, style: const TextStyle(fontWeight: FontWeight.w700)),
          ]),
          if (f != null) ...[const SizedBox(height: 6), Bar(f)],
        ]),
      );

  Widget _stage(String n, String title, String days, String text) => Card(
        child: Padding(
          padding: const EdgeInsets.all(14),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [
              Text(n, style: const TextStyle(fontSize: 28, fontWeight: FontWeight.w800, color: kTeal)),
              const SizedBox(width: 12),
              Expanded(child: Text(title, style: Theme.of(context).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.w700))),
              Chip(label: Text(days), visualDensity: VisualDensity.compact),
            ]),
            const SizedBox(height: 4),
            Rich(text),
          ]),
        ),
      );

  @override
  Widget build(BuildContext context) {
    final s = widget.state;
    final c = s.content;
    final t = Theme.of(context).textTheme;
    return ListenableBuilder(
      listenable: s,
      builder: (context, _) {
        final next = nextStep(s, widget.goTab);
        return ListView(padding: const EdgeInsets.all(16), children: [
          Rich('ලොකු English දැනුමක් ඕන නෑ. Exam එකේ නැවත නැවත එන **English වචන ${c.words.length}**, **question patterns ${c.patterns.length}** සහ **keywords** ටික හඳුනගත්තම ඇති. මුලින් සිංහලෙන්, ඊට පස්සේ ටික ටික English විතරක්.',
              style: t.bodyLarge),
          const SizedBox(height: 12),
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                const Label('Your progress'),
                const SizedBox(height: 6),
                _stat('Lessons', '${s.lessonsDone.length} / ${c.lessons.length}', s.lessonsDone.length / c.lessons.length),
                _stat('Words', '${s.known.length} / ${c.words.length}', s.known.length / c.words.length),
                _stat('Questions correct', '${s.totalCorrect} / ${c.totalQuestions}', s.totalCorrect / c.totalQuestions),
                _stat('Mock exam best', s.mockBest > 0 ? '${s.mockBest}%' : '–', s.mockBest / 100),
                _stat('Game best streak', '${s.gameBest}', null),
                const SizedBox(height: 10),
                FilledButton(onPressed: () => next.go(context), child: Text(next.label)),
                const SizedBox(height: 6),
                Text(next.note, style: t.bodySmall),
              ]),
            ),
          ),
          const SizedBox(height: 12),
          Text('දවස් 21 පාලම', style: t.titleLarge?.copyWith(fontWeight: FontWeight.w800)),
          const SizedBox(height: 4),
          const Rich('Stage එකෙන් stage එකට සිංහල උදව් අඩු වෙනවා. Practice එකේ **Sinhala bridge** set එකේ mode එක මාරු කරන්න.'),
          const SizedBox(height: 8),
          _stage('1', 'සිංහලෙන් තේරුම් ගන්න', 'Day 1–7', 'Episodes 1–3 කියවන්න. Bridge questions **"සිංහල උදව්"** mode එකේ. දවසකට words 10ක්.'),
          _stage('2', 'Keywords දඩයම', 'Day 8–14', 'Episodes 4–5. Mode එක **"Keywords"**. Patterns 12 ඔක්කොම. Episode questions කරන්න.'),
          _stage('3', 'English විතරයි', 'Day 15–21', 'Mode එක **"English"**. Mock exams 2ම. **ඇයි කියලා සිංහලෙන් ශබ්ද නඟලා කියන්න.** 85%+ → book කරන්න.'),
          const SizedBox(height: 8),
          Card(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: const [
                Label('Every day · 30 minutes'),
                SizedBox(height: 8),
                Rich('1. **Words — විනාඩි 10.** අලුත් වචන 10ක්.'),
                SizedBox(height: 4),
                Rich('2. **Lesson — විනාඩි 10.** Episode එකක කොටසක් ශබ්ද නඟලා කියවන්න.'),
                SizedBox(height: 4),
                Rich('3. **Practice — විනාඩි 5.** Questions 5–10ක්.'),
                SizedBox(height: 4),
                Rich('4. **Keyword game — විනාඩි 5.** වේගයෙන්.'),
              ]),
            ),
          ),
          Card(
            child: ExpansionTile(
              title: const Text('English බය නැති කරන නීති 6'),
              childrenPadding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
              expandedCrossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Rich('• **හැම වචනයම translate කරන්න එපා.** වැදගත් වචන 2–3 හොයන්න.'),
                Rich('• **අන්තිම වාක්‍යය මුලින් කියවන්න.** "Which service…?" එකෙන් අහන දේ දැනගන්න.'),
                Rich('• **පොඩි වචන 4:** [[MOST]] · [[LEAST]] · [[NOT]] · [[TWO]].'),
                Rich('• **Service names translate කරන්න ඕන නෑ.**'),
                Rich('• **Book කරන්න කලින් ESL +30 minutes ඉල්ලන්න.**'),
                Rich('• **තේරෙන්නේ නැත්නම් flag කරලා යන්න.**'),
              ],
            ),
          ),
          Card(
            child: ExpansionTile(
              title: const Text('Progress backup / reset'),
              childrenPadding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
              expandedCrossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                const Rich('Phone එක මාරු කරනවා නම්: **Copy backup** ඔබලා code එක save කරගන්න. අලුත් phone එකේ paste කරලා **Restore** ඔබන්න. Web app එකේ backup code එකත් මෙතන වැඩ.'),
                const SizedBox(height: 8),
                TextField(
                  controller: _backup,
                  minLines: 2,
                  maxLines: 4,
                  decoration: const InputDecoration(border: OutlineInputBorder(), hintText: 'Backup code'),
                ),
                const SizedBox(height: 8),
                Wrap(spacing: 8, runSpacing: 8, children: [
                  OutlinedButton(
                    onPressed: () async {
                      final code = s.backupCode();
                      _backup.text = code;
                      await Clipboard.setData(ClipboardData(text: code));
                      setState(() => _msg = 'Backup copy කළා. Notes එකක save කරගන්න.');
                    },
                    child: const Text('Copy backup'),
                  ),
                  OutlinedButton(
                    onPressed: () => setState(() => _msg = s.restore(_backup.text) ? 'Restore කළා!' : 'Backup code එක වැරදියි.'),
                    child: const Text('Restore'),
                  ),
                  OutlinedButton(
                    style: OutlinedButton.styleFrom(foregroundColor: badColor(context)),
                    onPressed: () {
                      if (!_resetArmed) {
                        setState(() => _resetArmed = true);
                        Future.delayed(const Duration(seconds: 4), () {
                          if (mounted) setState(() => _resetArmed = false);
                        });
                        return;
                      }
                      s.reset();
                      setState(() {
                        _resetArmed = false;
                        _msg = 'Progress මැකුවා.';
                      });
                    },
                    child: Text(_resetArmed ? 'ආයෙත් ඔබන්න — ඔක්කොම මැකෙනවා' : 'Reset all progress'),
                  ),
                ]),
                if (_msg.isNotEmpty) Padding(padding: const EdgeInsets.only(top: 8), child: Text(_msg)),
              ],
            ),
          ),
          const SizedBox(height: 24),
        ]);
      },
    );
  }
}

/* ---------------- LESSONS ---------------- */

class LessonsPage extends StatelessWidget {
  const LessonsPage({super.key, required this.state});
  final AppState state;

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: state,
      builder: (context, _) => ListView(
        padding: const EdgeInsets.all(16),
        children: [
          for (final l in state.content.lessons)
            Card(
              child: InkWell(
                borderRadius: BorderRadius.circular(12),
                onTap: () => openLesson(context, state, l),
                child: Padding(
                  padding: const EdgeInsets.all(14),
                  child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                    Row(children: [
                      Expanded(child: Text(l.title, style: Theme.of(context).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.w700))),
                      const SizedBox(width: 8),
                      state.lessonsDone.contains(l.id)
                          ? Icon(Icons.check_circle, color: goodColor(context))
                          : const Icon(Icons.radio_button_unchecked),
                    ]),
                    ..._setProgress(context, l.id),
                  ]),
                ),
              ),
            ),
        ],
      ),
    );
  }

  List<Widget> _setProgress(BuildContext context, String id) {
    final q = state.content.setById(id);
    if (q == null) return const [];
    final c = state.correctOf(id);
    return [
      const SizedBox(height: 10),
      Bar(c / q.qs.length),
      const SizedBox(height: 4),
      Text('Questions: $c / ${q.qs.length} correct', style: Theme.of(context).textTheme.bodySmall),
    ];
  }
}

class LessonReader extends StatelessWidget {
  const LessonReader({super.key, required this.state, required this.lesson});
  final AppState state;
  final Lesson lesson;

  @override
  Widget build(BuildContext context) {
    final set = state.content.setById(lesson.id);
    return Scaffold(
      appBar: AppBar(title: Text(lesson.short)),
      body: ListView(
        padding: const EdgeInsets.fromLTRB(16, 8, 16, 32),
        children: [
          Text(lesson.title, style: Theme.of(context).textTheme.headlineSmall?.copyWith(fontWeight: FontWeight.w800)),
          const SizedBox(height: 8),
          lesson.patterns ? PatternsView(patterns: state.content.patterns) : Blocks(lesson.blocks),
        ],
      ),
      bottomNavigationBar: SafeArea(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
          child: ListenableBuilder(
            listenable: state,
            builder: (context, _) {
              final done = state.lessonsDone.contains(lesson.id);
              return Row(children: [
                Expanded(
                  child: done
                      ? OutlinedButton.icon(
                          onPressed: () => state.toggleLesson(lesson.id),
                          icon: const Icon(Icons.check),
                          label: const Text('කියවලා ඉවරයි'))
                      : FilledButton(
                          onPressed: () => state.toggleLesson(lesson.id),
                          child: const Text('ඉවරයි කියලා mark කරන්න')),
                ),
                if (set != null) ...[
                  const SizedBox(width: 8),
                  OutlinedButton(onPressed: () => openSet(context, state, set), child: const Text('Questions')),
                ],
              ]);
            },
          ),
        ),
      ),
    );
  }
}

class PatternsView extends StatelessWidget {
  const PatternsView({super.key, required this.patterns});
  final List<List<String>> patterns;

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    Widget row(String label, String text) => Padding(
          padding: const EdgeInsets.only(top: 6),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [Label(label), Rich(text, style: t.bodyMedium)]),
        );
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      Rich('Exam questions **එකම හැඩයෙන්** නැවත නැවත එනවා. Pattern එක හඳුනගත්තම ඉතුරු English වචන ගොඩක් තේරෙන්න ඕන නෑ.', style: t.bodyLarge),
      const SizedBox(height: 8),
      for (var i = 0; i < patterns.length; i++)
        Card(
          child: Padding(
            padding: const EdgeInsets.all(14),
            child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Label('Pattern ${i + 1}'),
              const SizedBox(height: 4),
              Rich(patterns[i][0], style: t.titleMedium),
              row('සිංහලෙන්', patterns[i][1]),
              row('කරන්න', patterns[i][2]),
              row('Example', patterns[i][3]),
            ]),
          ),
        ),
    ]);
  }
}

/* ---------------- WORDS ---------------- */

const wordGroups = {'all': 'All', 'Q': 'Question', r'$': 'Money', 'S': 'Security', 'T': 'Tech'};

class WordsPage extends StatefulWidget {
  const WordsPage({super.key, required this.state});
  final AppState state;

  @override
  State<WordsPage> createState() => _WordsPageState();
}

class _WordsPageState extends State<WordsPage> {
  List<int> order = [];
  int idx = 0;
  bool flipped = false;

  AppState get s => widget.state;
  List<int> get pool => [
        for (var i = 0; i < s.content.words.length; i++)
          if (s.wFilter == 'all' || s.content.words[i][2] == s.wFilter) i
      ];

  @override
  void initState() {
    super.initState();
    _buildOrder();
  }

  void _buildOrder() {
    final p = pool;
    final unknown = p.where((i) => !s.known.contains(i)).toList();
    order = unknown.isNotEmpty ? unknown : p;
    idx = 0;
    flipped = false;
  }

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    final scheme = Theme.of(context).colorScheme;
    return ListenableBuilder(
      listenable: s,
      builder: (context, _) {
        if (order.isEmpty) _buildOrder();
        final p = pool;
        final knownInPool = p.where(s.known.contains).length;
        final i = order[idx % order.length];
        final w = s.content.words[i];
        return ListView(padding: const EdgeInsets.all(16), children: [
          Wrap(spacing: 6, runSpacing: 6, children: [
            for (final e in wordGroups.entries)
              ChoiceChip(
                label: Text(e.value),
                selected: s.wFilter == e.key,
                onSelected: (_) {
                  s.setFilter(e.key);
                  setState(_buildOrder);
                },
              ),
          ]),
          const SizedBox(height: 12),
          Row(children: [
            Expanded(child: Bar(p.isEmpty ? 0 : knownInPool / p.length)),
            const SizedBox(width: 10),
            Text('$knownInPool / ${p.length} known'),
          ]),
          const SizedBox(height: 12),
          GestureDetector(
            onTap: () => setState(() => flipped = !flipped),
            child: Card(
              child: Container(
                constraints: const BoxConstraints(minHeight: 230),
                padding: const EdgeInsets.all(20),
                alignment: Alignment.center,
                child: Column(mainAxisSize: MainAxisSize.min, children: [
                  Chip(label: Text('${wordGroups[w[2]]}${s.known.contains(i) ? ' · known' : ''}'), visualDensity: VisualDensity.compact),
                  const SizedBox(height: 10),
                  Text(w[0], textAlign: TextAlign.center, style: t.headlineMedium?.copyWith(fontWeight: FontWeight.w800)),
                  const SizedBox(height: 12),
                  if (flipped) ...[
                    Text(w[1], textAlign: TextAlign.center, style: t.titleLarge?.copyWith(color: scheme.primary, fontWeight: FontWeight.w700)),
                    const SizedBox(height: 8),
                    Text(w[3], textAlign: TextAlign.center, style: t.bodyMedium?.copyWith(color: scheme.onSurfaceVariant)),
                  ] else
                    Text('තේරුම බලන්න tap කරන්න', style: t.bodyMedium?.copyWith(color: scheme.onSurfaceVariant)),
                ]),
              ),
            ),
          ),
          const SizedBox(height: 12),
          Row(children: [
            Expanded(child: OutlinedButton(onPressed: () => setState(() { idx++; flipped = false; }), child: const Text('ආයෙත් බලන්න'))),
            const SizedBox(width: 8),
            Expanded(
              child: FilledButton(
                onPressed: () {
                  final cur = order[idx % order.length];
                  setState(() {
                    order.removeAt(idx % order.length);
                    flipped = false;
                    if (order.isEmpty) _buildOrder();
                  });
                  s.markKnown(cur);
                },
                child: const Text('මට තේරෙනවා'),
              ),
            ),
          ]),
          const SizedBox(height: 12),
          Card(
            child: ExpansionTile(
              title: const Text('ඔක්කොම වචන — list එක'),
              children: [
                for (var j = 0; j < s.content.words.length; j++)
                  ListTile(
                    dense: true,
                    leading: s.known.contains(j)
                        ? Icon(Icons.check, color: goodColor(context))
                        : const Icon(Icons.circle_outlined, size: 18),
                    title: Text(s.content.words[j][0], style: const TextStyle(fontWeight: FontWeight.w600)),
                    subtitle: Text(s.content.words[j][1]),
                  ),
              ],
            ),
          ),
        ]);
      },
    );
  }
}

/* ---------------- PRACTICE ---------------- */

Future<bool> confirmRestart(BuildContext context, AppState s, QSet set) async {
  final ok = await showDialog<bool>(
    context: context,
    builder: (ctx) => AlertDialog(
      title: const Text('Restart this set?'),
      content: Text('${set.title}: answers ඔක්කොම මැකිලා මුල ඉඳන් පටන් ගන්නවා.'),
      actions: [
        TextButton(onPressed: () => Navigator.pop(ctx, false), child: const Text('Cancel')),
        FilledButton(onPressed: () => Navigator.pop(ctx, true), child: const Text('Restart')),
      ],
    ),
  );
  if (ok == true) s.resetSet(set.id);
  return ok == true;
}

class PracticePage extends StatelessWidget {
  const PracticePage({super.key, required this.state});
  final AppState state;

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    return ListenableBuilder(
      listenable: state,
      builder: (context, _) => ListView(padding: const EdgeInsets.all(16), children: [
        Text('${state.totalCorrect} / ${state.content.totalQuestions} questions correct', style: t.titleMedium),
        const SizedBox(height: 8),
        for (final q in state.content.sets)
          Card(
            child: InkWell(
              borderRadius: BorderRadius.circular(12),
              onTap: () => openSet(context, state, q),
              child: Padding(
                padding: const EdgeInsets.all(14),
                child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                  Row(children: [
                    Expanded(child: Text(q.title, style: t.titleMedium?.copyWith(fontWeight: FontWeight.w700))),
                    Text('${state.correctOf(q.id)} / ${q.qs.length}', style: const TextStyle(fontWeight: FontWeight.w700)),
                    if (state.answersOf(q.id).isNotEmpty)
                      IconButton(
                        tooltip: 'Restart set',
                        visualDensity: VisualDensity.compact,
                        icon: const Icon(Icons.restart_alt),
                        onPressed: () => confirmRestart(context, state, q),
                      ),
                  ]),
                  if (q.sub.isNotEmpty) Padding(padding: const EdgeInsets.only(top: 2), child: Text(q.sub, style: t.bodySmall)),
                  const SizedBox(height: 10),
                  Bar(state.correctOf(q.id) / q.qs.length),
                  const SizedBox(height: 4),
                  Text('Answered ${state.answersOf(q.id).length} · Correct ${state.correctOf(q.id)}', style: t.bodySmall),
                ]),
              ),
            ),
          ),
      ]),
    );
  }
}

class QuizPage extends StatefulWidget {
  const QuizPage({super.key, required this.state, required this.set});
  final AppState state;
  final QSet set;

  @override
  State<QuizPage> createState() => _QuizPageState();
}

class _QuizPageState extends State<QuizPage> {
  int qi = 0;
  List<int> sel = [];
  final _scroll = ScrollController();

  AppState get s => widget.state;
  QSet get set => widget.set;

  @override
  void initState() {
    super.initState();
    _jumpToFirstOpen();
  }

  @override
  void dispose() {
    _scroll.dispose();
    super.dispose();
  }

  void _jumpToFirstOpen() {
    final a = s.answersOf(set.id);
    qi = 0;
    for (var i = 0; i < set.qs.length; i++) {
      if (!a.containsKey(i)) {
        qi = i;
        break;
      }
    }
  }

  void _go(int i) {
    setState(() {
      qi = i;
      sel = [];
    });
    if (_scroll.hasClients) _scroll.jumpTo(0);
  }

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    final scheme = Theme.of(context).colorScheme;
    return ListenableBuilder(
      listenable: s,
      builder: (context, _) {
        final q = set.qs[qi];
        final done = s.answersOf(set.id)[qi];
        final help = set.bridge ? s.mode : 2;
        const letters = 'ABCDE';
        return Scaffold(
          appBar: AppBar(
            title: Text(set.title),
            actions: [
              Center(child: Text('${s.correctOf(set.id)} / ${set.qs.length}', style: const TextStyle(fontWeight: FontWeight.w700))),
              IconButton(
                tooltip: 'Restart set',
                icon: const Icon(Icons.restart_alt),
                onPressed: () async {
                  if (await confirmRestart(context, s, set)) {
                    setState(() {
                      sel = [];
                      qi = 0;
                    });
                  }
                },
              ),
            ],
          ),
          body: ListView(controller: _scroll, padding: const EdgeInsets.all(16), children: [
            if (set.bridge) ...[
              SegmentedButton<int>(
                showSelectedIcon: false,
                segments: const [
                  ButtonSegment(value: 0, label: Text('සිංහල')),
                  ButtonSegment(value: 1, label: Text('Keywords')),
                  ButtonSegment(value: 2, label: Text('English')),
                ],
                selected: {s.mode},
                onSelectionChanged: (v) => s.setMode(v.first),
              ),
              const SizedBox(height: 12),
            ],
            Wrap(spacing: 4, runSpacing: 4, children: [
              for (var i = 0; i < set.qs.length; i++) _dot(context, i),
            ]),
            const SizedBox(height: 12),
            Card(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                  Row(children: [
                    Expanded(child: Label('Question ${qi + 1} / ${set.qs.length}')),
                    if (q.d.isNotEmpty) Chip(label: Text(q.d), visualDensity: VisualDensity.compact),
                  ]),
                  const SizedBox(height: 8),
                  Rich(q.q, showMarks: help < 2, style: t.titleMedium?.copyWith(height: 1.5)),
                  if (set.bridge && help == 0 && q.t != null) ...[
                    const SizedBox(height: 10),
                    Container(
                      padding: const EdgeInsets.only(left: 12),
                      decoration: BoxDecoration(border: Border(left: BorderSide(color: scheme.primary, width: 3))),
                      child: Text(q.t!, style: t.bodyLarge),
                    ),
                  ],
                  if (set.bridge && help < 2 && q.h.isNotEmpty) ...[
                    const SizedBox(height: 10),
                    Wrap(spacing: 6, runSpacing: 6, children: [
                      for (final h in q.h)
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                          decoration: BoxDecoration(color: scheme.surfaceContainerHighest, borderRadius: BorderRadius.circular(8)),
                          child: Rich('**${h[0]}** = ${h[1]}', style: t.bodySmall),
                        ),
                    ]),
                  ],
                  const SizedBox(height: 14),
                  for (var i = 0; i < q.o.length; i++) _option(context, q, i, done),
                  if (q.multi && done == null)
                    Padding(
                      padding: const EdgeInsets.only(top: 6),
                      child: FilledButton(
                        onPressed: sel.isEmpty ? null : () => s.answer(set, qi, sel),
                        child: Text('Check (${sel.length} / ${q.a.length})'),
                      ),
                    ),
                  if (done != null) ...[
                    const SizedBox(height: 10),
                    Container(
                      padding: const EdgeInsets.all(12),
                      decoration: BoxDecoration(color: scheme.surfaceContainerHighest, borderRadius: BorderRadius.circular(10)),
                      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                        Rich('**${done.ok ? 'හරි!' : 'වැරදියි.'}** Answer: **${q.a.map((i) => letters[i]).join(', ')}**. ${q.e}', style: t.bodyLarge),
                        const SizedBox(height: 6),
                        Text('ඇයි කියලා සිංහලෙන් ශබ්ද නඟලා කියන්න.', style: t.bodySmall),
                      ]),
                    ),
                  ],
                ]),
              ),
            ),
            const SizedBox(height: 12),
            Row(children: [
              OutlinedButton(onPressed: qi == 0 ? null : () => _go(qi - 1), child: const Text('Back')),
              const Spacer(),
              TextButton(
                onPressed: () {
                  s.retryWrong(set.id);
                  setState(() {
                    sel = [];
                    _jumpToFirstOpen();
                  });
                },
                child: const Text('වැරදුණු ඒවා ආයෙත්'),
              ),
              const Spacer(),
              FilledButton(
                onPressed: qi < set.qs.length - 1 ? () => _go(qi + 1) : () => Navigator.pop(context),
                child: Text(qi < set.qs.length - 1 ? 'Next' : 'Finish'),
              ),
            ]),
            const SizedBox(height: 24),
          ]),
        );
      },
    );
  }

  Widget _dot(BuildContext context, int i) {
    final a = s.answersOf(set.id)[i];
    final scheme = Theme.of(context).colorScheme;
    final color = a == null ? scheme.outlineVariant : (a.ok ? goodColor(context) : badColor(context));
    return InkWell(
      onTap: () => _go(i),
      borderRadius: BorderRadius.circular(6),
      child: Container(
        width: 30,
        height: 30,
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: a == null ? null : color.withAlpha(40),
          border: Border.all(color: i == qi ? scheme.primary : color, width: i == qi ? 2.5 : 1),
          borderRadius: BorderRadius.circular(6),
        ),
        child: Text('${i + 1}', style: TextStyle(fontSize: 11, fontWeight: FontWeight.w600, color: a == null ? scheme.onSurfaceVariant : color)),
      ),
    );
  }

  Widget _option(BuildContext context, Question q, int i, Ans? done) {
    final scheme = Theme.of(context).colorScheme;
    Color border = scheme.outlineVariant;
    Color? fill;
    if (done != null) {
      if (q.a.contains(i)) {
        border = goodColor(context);
        fill = border.withAlpha(35);
      } else if (done.sel.contains(i)) {
        border = badColor(context);
        fill = border.withAlpha(35);
      }
    } else if (sel.contains(i)) {
      border = scheme.primary;
    }
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: InkWell(
        borderRadius: BorderRadius.circular(10),
        onTap: done != null
            ? null
            : () {
                if (q.multi) {
                  setState(() {
                    if (sel.contains(i)) {
                      sel.remove(i);
                    } else {
                      sel.add(i);
                    }
                  });
                } else {
                  sel = [i];
                  s.answer(set, qi, sel);
                }
              },
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
          decoration: BoxDecoration(
            color: fill,
            border: Border.all(color: border, width: 1.5),
            borderRadius: BorderRadius.circular(10),
          ),
          child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text('ABCDE'[i], style: TextStyle(fontWeight: FontWeight.w700, color: scheme.onSurfaceVariant)),
            const SizedBox(width: 12),
            Expanded(child: Text(q.o[i], style: Theme.of(context).textTheme.bodyLarge)),
          ]),
        ),
      ),
    );
  }
}

/* ---------------- GAME ---------------- */

class GamePage extends StatefulWidget {
  const GamePage({super.key, required this.state});
  final AppState state;

  @override
  State<GamePage> createState() => _GamePageState();
}

class _GamePageState extends State<GamePage> {
  final _rnd = Random();
  late List<String> cur;
  List<String> opts = [];
  String? picked;
  int streak = 0;

  @override
  void initState() {
    super.initState();
    _newRound();
  }

  void _newRound() {
    final pairs = widget.state.content.pairs;
    cur = pairs[_rnd.nextInt(pairs.length)];
    final others = pairs.where((p) => p[1] != cur[1]).toList()..shuffle(_rnd);
    opts = [...others.take(3).map((p) => p[1]), cur[1]]..shuffle(_rnd);
    picked = null;
  }

  void _pick(String o) {
    setState(() {
      picked = o;
      streak = o == cur[1] ? streak + 1 : 0;
    });
    widget.state.gameScore(streak);
  }

  @override
  Widget build(BuildContext context) {
    final t = Theme.of(context).textTheme;
    final scheme = Theme.of(context).colorScheme;
    return ListenableBuilder(
      listenable: widget.state,
      builder: (context, _) => ListView(padding: const EdgeInsets.all(16), children: [
        Row(children: [
          const Expanded(child: Label('Keyword → Service')),
          Text('Streak $streak · Best ${widget.state.gameBest}', style: const TextStyle(fontWeight: FontWeight.w700)),
        ]),
        const SizedBox(height: 6),
        const Text('Keyword එක දැක්කම service එක තත්පර 2කින් මතක් වෙන්න ඕන.'),
        const SizedBox(height: 16),
        Card(
          child: Padding(
            padding: const EdgeInsets.symmetric(vertical: 28, horizontal: 16),
            child: Text(cur[0], textAlign: TextAlign.center, style: t.headlineSmall?.copyWith(fontWeight: FontWeight.w800)),
          ),
        ),
        const SizedBox(height: 12),
        for (final o in opts)
          Padding(
            padding: const EdgeInsets.only(bottom: 8),
            child: OutlinedButton(
              style: OutlinedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 14),
                side: BorderSide(
                  width: 1.5,
                  color: picked == null
                      ? scheme.outlineVariant
                      : o == cur[1]
                          ? goodColor(context)
                          : (o == picked ? badColor(context) : scheme.outlineVariant),
                ),
                backgroundColor: picked != null && o == cur[1] ? goodColor(context).withAlpha(35) : null,
              ),
              onPressed: picked == null ? () => _pick(o) : null,
              child: Text(o, style: t.titleMedium),
            ),
          ),
        if (picked != null) ...[
          const SizedBox(height: 4),
          Rich(picked == cur[1] ? '**හරි!**' : '**වැරදියි.** "${cur[0]}" → **${cur[1]}**', style: t.bodyLarge),
          const SizedBox(height: 10),
          FilledButton(onPressed: () => setState(_newRound), child: const Text('Next')),
        ],
      ]),
    );
  }
}
