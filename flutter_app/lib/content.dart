import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';
import 'package:flutter/foundation.dart';

class Question {
  Question({
    required this.d,
    required this.q,
    required this.o,
    required this.a,
    required this.e,
    this.t,
    this.h = const [],
    this.im = const [],
    this.img = false,
    this.qs,
    this.os,
    this.es,
  });

  final String d;
  final String q;
  final List<String> o;
  final List<int> a;
  final String e;
  final String? t;
  final List<List<String>> h;
  final List<String> im; // page-crop images (assets/…) for figure / bilingual questions
  final bool img; // the picture is the question; hide the text
  final String? qs, es; // Sinhala question / explanation
  final List<String>? os; // Sinhala options

  bool get multi => a.length > 1;
  bool get pending => a.isEmpty; // answer key not added yet

  factory Question.fromJson(Map<String, dynamic> j) => Question(
        d: (j['d'] ?? '') as String,
        q: j['q'] as String,
        o: (j['o'] as List).map((x) => x as String).toList(),
        a: (j['a'] as List).map((x) => (x as num).toInt()).toList(),
        e: (j['e'] ?? '') as String,
        t: j['t'] as String?,
        h: ((j['h'] ?? const []) as List)
            .map((p) => (p as List).map((x) => x as String).toList())
            .toList(),
        im: ((j['im'] ?? const []) as List).map((x) => x as String).toList(),
        img: j['img'] != null,
        qs: j['qs'] as String?,
        es: j['es'] as String?,
        os: j['os'] == null ? null : (j['os'] as List).map((x) => x as String).toList(),
      );
}

class QSet {
  QSet(this.id, this.title, this.sub, this.qs, {this.bridge = false, this.exam = 'clf', this.essay = false, this.numbered = false});
  final String id;
  final String exam;
  final bool numbered; // options labelled 1–5 like the printed papers
  final bool essay; // read-only written questions, marked "done" instead of answered
  final String title;
  final String sub;
  final List<Question> qs;
  final bool bridge;
}

class Lesson {
  Lesson(this.id, this.title, this.short, this.blocks, {this.patterns = false});
  final String id;
  final String title;
  final String short;
  final List<dynamic> blocks;
  final bool patterns;
}

class Exam {
  const Exam(this.id, this.code, this.name, this.blurb);
  final String id;
  final String code;
  final String name;
  final String blurb;
}

const kExams = [
  Exam('clf', 'CLF-C02', 'AWS Certified Cloud Practitioner',
      'Foundational · Sinhala bridge, lessons, words, keyword game and mock exams.'),
  Exam('saa', 'SAA-C03', 'AWS Certified Solutions Architect – Associate',
      'Associate · scenario-based practice questions by exam domain.'),
  Exam('ict', 'AL ICT', 'G.C.E. Advanced Level ICT',
      'Lessons with past-paper questions · English and Sinhala.'),
];

class Content {
  Content(this.lessons, this.sets, this.words, this.patterns, this.pairs);

  final List<Lesson> lessons;
  final List<QSet> sets;
  final List<List<String>> words;
  final List<List<String>> patterns;
  final List<List<String>> pairs;

  List<QSet> setsFor(String exam) => sets.where((s) => s.exam == exam).toList();
  int questionsFor(String exam) => setsFor(exam).fold(0, (n, s) => n + s.qs.length);

  QSet? setById(String id) {
    for (final s in sets) {
      if (s.id == id) return s;
    }
    return null;
  }

  factory Content.fromJson(Map<String, dynamic> j) {
    List<List<String>> strLists(dynamic v) =>
        (v as List).map((r) => (r as List).map((x) => x as String).toList()).toList();

    Lesson toLesson(Map<String, dynamic> l) => Lesson(
          l['id'] as String,
          l['title'] as String,
          (l['short'] ?? '') as String,
          l['blocks'] as List<dynamic>,
        );

    final raw = (j['lessons'] as List).map((e) => e as Map<String, dynamic>).toList();
    final lessons = <Lesson>[
      ...raw.where((l) => l['id'] != 'cheat').map(toLesson),
      Lesson('patterns', 'Question Patterns', '12 patterns', const [], patterns: true),
      ...raw.where((l) => l['id'] == 'cheat').map(toLesson),
    ];

    String subFor(String id) {
      if (id == 'ep6') return 'Exam එක වගේ — විනාඩි 40';
      if (id == 'mock2') return 'සම්පූර්ණ exam එක — questions 65, විනාඩි 90';
      if (id == 'mock3') return 'කෙටි සරල questions — "මේ service එක මොකටද?"';
      return '';
    }

    final bridge = (j['bridge'] as List)
        .map((q) => Question.fromJson(q as Map<String, dynamic>))
        .toList();

    final sets = <QSet>[
      QSet('bridge', 'Sinhala bridge (20)', 'සිංහල උදව් එක්ක — මෙතනින් පටන් ගන්න', bridge,
          bridge: true),
      ...(j['sets'] as List).map((s) {
        final m = s as Map<String, dynamic>;
        final id = m['id'] as String;
        final exam = (m['exam'] ?? 'clf') as String;
        return QSet(
          id,
          m['title'] as String,
          exam != 'clf' ? ((m['sub'] ?? '') as String) : subFor(id),
          (m['qs'] as List).map((q) => Question.fromJson(q as Map<String, dynamic>)).toList(),
          exam: exam,
          essay: m['kind'] == 'essay',
          numbered: false,
        );
      }),
    ];

    return Content(lessons, sets, strLists(j['words']), strLists(j['patterns']), strLists(j['pairs']));
  }
}

class Ans {
  Ans(this.sel, this.ok);
  final List<int> sel;
  final bool ok;

  Map<String, dynamic> toJson() => {'sel': sel, 'ok': ok};

  factory Ans.fromJson(Map<String, dynamic> j) =>
      Ans((j['sel'] as List).map((x) => (x as num).toInt()).toList(), j['ok'] as bool);
}

/// Progress, saved on the phone. Uses the same keys as the web app so backup codes work in both.
class AppState extends ChangeNotifier {
  AppState(this.prefs, this.content) {
    _load(prefs.getString(_key));
  }

  static const _key = 'awsBridge2';
  final SharedPreferences prefs;
  final Content content;

  Set<int> known = {};
  Set<String> lessonsDone = {};
  Map<String, Map<int, Ans>> answers = {};
  int mockBest = 0;
  int gameBest = 0;
  int mode = 0;
  String wFilter = 'all';
  String? exam; // null until the user picks one on the first page

  void _load(String? raw) {
    known = {};
    lessonsDone = {};
    answers = {};
    mockBest = 0;
    gameBest = 0;
    mode = 0;
    wFilter = 'all';
    exam = null;
    if (raw == null || raw.isEmpty) return;
    final j = jsonDecode(raw) as Map<String, dynamic>;
    known = ((j['known'] ?? const []) as List).map((x) => (x as num).toInt()).toSet();
    lessonsDone = ((j['lessonsDone'] ?? const []) as List).map((x) => x as String).toSet();
    final a = (j['ans'] ?? const <String, dynamic>{}) as Map<String, dynamic>;
    answers = a.map((setId, v) => MapEntry(
          setId,
          (v as Map<String, dynamic>).map(
              (qi, x) => MapEntry(int.parse(qi), Ans.fromJson(x as Map<String, dynamic>))),
        ));
    mockBest = ((j['mockBest'] ?? 0) as num).toInt();
    gameBest = ((j['gBest'] ?? 0) as num).toInt();
    mode = ((j['mode'] ?? 0) as num).toInt();
    wFilter = (j['wFilter'] ?? 'all') as String;
    final e = j['exam'];
    exam = kExams.any((x) => x.id == e) ? e as String : null;
  }

  String _export() => jsonEncode({
        'known': known.toList(),
        'lessonsDone': lessonsDone.toList(),
        'ans': answers.map((k, v) => MapEntry(k, v.map((qi, x) => MapEntry('$qi', x.toJson())))),
        'mockBest': mockBest,
        'gBest': gameBest,
        'mode': mode,
        'wFilter': wFilter,
        'exam': exam,
      });

  void _save() {
    prefs.setString(_key, _export());
    notifyListeners();
  }

  String backupCode() => base64.encode(utf8.encode(_export()));

  bool restore(String code) {
    try {
      final raw = utf8.decode(base64.decode(code.trim()));
      jsonDecode(raw) as Map<String, dynamic>;
      _load(raw);
      _save();
      return true;
    } catch (_) {
      return false;
    }
  }

  void reset() {
    final keep = exam;
    _load(null);
    exam = keep;
    _save();
  }

  void setExam(String? id) {
    exam = id;
    _save();
  }

  List<QSet> get sets => content.setsFor(exam ?? 'clf');
  int get totalQuestions => content.questionsFor(exam ?? 'clf');

  Map<int, Ans> answersOf(String id) => answers[id] ?? const {};
  /// Essays count when marked done; MCQs whose answer key is still missing never count (re-checked when a key is added).
  int correctOf(String id) {
    final set = content.setById(id);
    if (set == null) return answersOf(id).values.where((x) => x.ok).length;
    return answersOf(id).entries.where((e) => effectiveOk(set, e.key, e.value)).length;
  }

  bool effectiveOk(QSet set, int qi, Ans a) {
    if (set.essay) return a.ok;
    final q = set.qs[qi];
    if (q.pending) return false;
    return a.sel.length == q.a.length && q.a.every(a.sel.contains);
  }
  int get totalCorrect => sets.fold(0, (n, s) => n + correctOf(s.id));

  double get overall {
    final q = totalCorrect / totalQuestions;
    if (exam != 'clf') return q;
    return lessonsDone.length / content.lessons.length * .25 +
        known.length / content.words.length * .25 +
        q * .5;
  }

  void toggleLesson(String id) {
    if (!lessonsDone.remove(id)) lessonsDone.add(id);
    _save();
  }

  void markKnown(int i) {
    known.add(i);
    _save();
  }

  void setMode(int m) {
    mode = m;
    _save();
  }

  void setFilter(String f) {
    wFilter = f;
    _save();
  }

  void answer(QSet s, int qi, List<int> sel) {
    final q = s.qs[qi];
    final ok = !q.pending && sel.length == q.a.length && q.a.every(sel.contains);
    answers.putIfAbsent(s.id, () => {})[qi] = Ans(List.of(sel), ok);
    if ((s.id == 'ep6' || s.id == 'mock2' || s.id == 'mock3') &&answersOf(s.id).length == s.qs.length) {
      final pct = (correctOf(s.id) / s.qs.length * 100).round();
      if (pct > mockBest) mockBest = pct;
    }
    _save();
  }

  void toggleEssay(QSet s, int qi) {
    final m = answers.putIfAbsent(s.id, () => {});
    if (m.remove(qi) == null) m[qi] = Ans(const [], true);
    _save();
  }

  void retryWrong(String id) {
    final set = content.setById(id);
    // keep picks that are only "wrong" because the answer key is missing
    answers[id]?.removeWhere((k, v) => !v.ok && !(set != null && set.qs[k].pending));
    _save();
  }

  void resetSet(String id) {
    answers.remove(id);
    _save();
  }

  void gameScore(int streak) {
    if (streak > gameBest) {
      gameBest = streak;
      _save();
    }
  }
}
