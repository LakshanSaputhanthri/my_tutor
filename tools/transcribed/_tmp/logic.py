import json,re
E=[]
def ob(s):
    return re.sub(r'!([A-Za-z])', lambda m:m.group(1)+'\u0304', s) if s else s
def add(d,q,qs=None):
    o={"d":d,"q":ob(q)}
    if qs:o["qs"]=ob(qs)
    E.append(o)

add("2022 ESSAY04[d]","""1.(d) (i) Complete the truth table for the given logic circuit.
[Figure: logic circuit with two inverting gates (bubble at output) fed by inputs A (top gate, output X) and B (bottom gate, output Y); X and Y feed a third inverting gate (bubble at output) producing Q.]
A | B | X | Y | Q
0 | 0 | ........ | ........ | ........
0 | 1 | ........ | ........ | ........
1 | 0 | ........ | ........ | ........
1 | 1 | ........ | ........ | ........
(ii) What is the basic logic gate that has the above truth table (with inputs A, B and the output Q)?""",
"""1.(d) (i) පහත දී ඇති තාර්කික පරිපථය සඳහා සත්‍යතා වගුව සම්පූර්ණ කරන්න.
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන තාර්කික පරිපථය]
A | B | X | Y | Q
0 | 0 | ........ | ........ | ........
0 | 1 | ........ | ........ | ........
1 | 0 | ........ | ........ | ........
1 | 1 | ........ | ........ | ........
(ii) ඉහත සත්‍යතා වගුව (A, B ආදාන සහ Q ප්‍රතිදානය වන) සහිත මූලික තාර්කික ද්වාරය කුමක් ද?""")

add("2011 ESSAY01[d]","""1. (d) A digital circuit takes four binary digits as an input, and produces 1 as its output if the decimal value represented by the four binary digits is a prime number (number which can only be divided by itself and 1), and 0 otherwise. Assume that all four binary digits represent positive decimal values (No bit is allocated for the sign).
(i) The following truth table is designed to describe the above circuit, in which A, B, C and D represents the four binary inputs from the most significant bit to the least significant bit and F(A,B,C,D) as the output of the circuit. Copy the following truth table onto your answer sheet as it is and complete the output column.
A | B | C | D | F(A,B,C,D)
0 | 0 | 0 | 0 |
0 | 0 | 0 | 1 |
0 | 0 | 1 | 0 |
0 | 0 | 1 | 1 |
0 | 1 | 0 | 0 |
0 | 1 | 0 | 1 |
0 | 1 | 1 | 0 |
0 | 1 | 1 | 1 |
1 | 0 | 0 | 0 |
1 | 0 | 0 | 1 |
1 | 0 | 1 | 0 |
1 | 0 | 1 | 1 |
1 | 1 | 0 | 0 |
1 | 1 | 0 | 1 |
1 | 1 | 1 | 0 |
1 | 1 | 1 | 1 |
(ii) Write a Boolean expression to represent the logic function of the above circuit in the sum of products form.
(iii) Design a logic circuit for the Boolean expression you have obtained for the above part (ii).""",
"""1. (d) අංකිත පරිපථයක් ආදානය ලෙස ද්විමය සංඛ්‍යාංක හතරක් ගෙන, එම ද්විමය සංඛ්‍යාංක හතරෙන් නිරූපිත දශමය අගය ප්‍රථම සංඛ්‍යාවක් නම් (1න් හා එම සංඛ්‍යාවෙන් පමණක් බෙදෙන සංඛ්‍යා) ප්‍රතිදානය ලෙස 1 ලබා දෙන අතර, අන් සෑම විටම 0 ලබා දේ. සෑම ද්විමය සංඛ්‍යාංක හතරකින්ම ධන දශමය අගයක් නිරූපණය වන බව උපකල්පනය කරන්න. (ලකුණ සඳහා කිසිදු බිටුවක් වෙන් නොමැත.)
(i) ඉහත පරිපථය විස්තර කිරීම සඳහා පහත දක්වා ඇති සත්‍යතා වගුව නිර්මාණය කර ඇත, මෙහි A, B, C හා D මගින් ද්විමය ආදාන හතර වැඩිම වෙසෙසි බිටුවේ සිට අඩුම වෙසෙසි බිටුව තෙක් නිරූපණය වන අතර, F(A,B,C,D) මගින් පරිපථයේ ප්‍රතිදානය නිරූපණය කෙරේ. පහත දැක්වෙන සත්‍යතා වගුව, එම ආකාරයටම පිටපත් කරගෙන ප්‍රතිදාන තීරුව සම්පූර්ණ කරන්න.
A | B | C | D | F(A,B,C,D)
0 | 0 | 0 | 0 |
0 | 0 | 0 | 1 |
0 | 0 | 1 | 0 |
0 | 0 | 1 | 1 |
0 | 1 | 0 | 0 |
0 | 1 | 0 | 1 |
0 | 1 | 1 | 0 |
0 | 1 | 1 | 1 |
1 | 0 | 0 | 0 |
1 | 0 | 0 | 1 |
1 | 0 | 1 | 0 |
1 | 0 | 1 | 1 |
1 | 1 | 0 | 0 |
1 | 1 | 0 | 1 |
1 | 1 | 1 | 0 |
1 | 1 | 1 | 1 |
(ii) ඉහත පරිපථයේ බූලීය ප්‍රකාශනය, ගුණිතවල එකතුවක් ලෙස නිරූපණය කිරීමට බූලීය ප්‍රකාශනයක් ලියන්න.
(iii) ඉහත (ii) කොටස සඳහා ඔබ ලබා ගත් බූලීය ප්‍රකාශනය සඳහා තාර්කික පරිපථයක් අඳින්න.""")

add("2012 ESSAY01[b]","""2. (b) A fan in a room can be on (1) or off (0). A control system is required to operate the fan efficiently with the following conditions / functionalities.
1. The fan can manually be switched on or off.
2. The timer will be either on or off.
3. The sensor will detect whether the environment is cold or hot.
4. The fan will automatically be switched on when the timer is on and the sensor indicates. environment is hot.
The following table assigns Boolean values for the above conditions/functionalities.
Condition/functionality | Boolean value
Fan switched on manually | 1
Fan switched off manually | 0
Timer is on | 1
Timer is off | 0
Sensor detects cold environment | 1
Sensor detects hot environment | 0
(i) Draw a logic circuit by using a combination of only AND, OR and NOT gates to implement the above control system.
(ii) Construct a truth table to represent the functionality of the above system.
(iii) Write a Boolean expression (not simplified) to represent the truth table constructed in the (b) (ii) above.""",
"""2. (b) කාමරයක ඇති විදුලි පංකාවක් ක්‍රියාත්මකව (on - 1) හෝ අක්‍රියව (off - 0) පැවතිය හැකිය. එම විදුලි පංකාව කාර්යක්ෂමව ක්‍රියාත්මක කිරීම සඳහා පහත දැක්වෙන තත්ත්ව/ක්‍රියාවලි සහිත පාලන පද්ධතියක් අවශ්‍ය වේ.
1. විදුලි පංකාව අත්හුරුවෙන් ක්‍රියාත්මක හෝ අක්‍රිය කළ හැක වීම.
2. කාලගණකය ක්‍රියාත්මකව හෝ අක්‍රියව පැවතිය හැකිය.
3. පරිසරය සීතල ද උණුසුම් ද යන්න සංවේදකයක් අනාවරණය කරගනියි.
4. කාලගණකය ක්‍රියාත්මකව ඇතිවිට සහ පරිසරය උණුසුම් යැයි සංවේදකය පෙන්නුම් කරන අවස්ථාවකදී විදුලි පංකාව ස්වයංක්‍රීයව ක්‍රියාත්මක විය හැකිය.
පහත දැක්වෙන වගුවෙන් ඉහත පෙන්වා ඇති කොන්දේසිවලට/ක්‍රියාවලිවලට අදාළ බූලීය අගයන් දැක්වේ.
කොන්දේසිය/ක්‍රියාවලිය | බූලියානු අගය
පංකාව අත්හුරුවෙන් ක්‍රියාත්මක කරනු ලබයි. | 1
පංකාව අත්හුරුවෙන් වසා දමනු ලබයි. | 0
කාලගණකය ක්‍රියාත්මක වී ඇත. | 1
කාලගණකය ක්‍රියාත්මක වී නැත. | 0
පරිසරය සීතල බව සංවේදකය හඳුනාගනියි. | 1
පරිසරය උණුසුම් බව සංවේදකය හඳුනාගනියි. | 0
(i) ඉහත පාලන පද්ධතිය ක්‍රියාත්මක කිරීම සඳහා AND, OR සහ NOT ද්වාර සංයෝජන පමණක් අඩංගු තර්කපථයක් අඳින්න.
(ii) ඉහත පද්ධතියෙහි ක්‍රියාකිරීම දැක්වෙන සත්‍යතා වගුවක් ගොඩනගන්න.
(iii) ඉහත (b) (ii) කොටසෙහි ගොඩනගන ලද සත්‍යතා වගුව නිරූපණය කරෙන බූලියන් ප්‍රකාශනයක් (සුළු නොකරන ලද) ලියන්න.""")

add("2013 ESSAY01","""3. (a) A fire alarm system consists of three sensors S1, S2 and S3 to detect smoke, flame and heat respectively. A sensor can either be active (sends the logical value 1) or inactive (Sends the logical value 0). The system automatically triggers the fire alarm when at least two of the sensors are active.
(i) Construct the truth table to represent the functionality of the above fire alarm system.
(ii) Derive the Boolean expression to represent the above truth table.
(b) Consider the logic circuit shown here to answer the sections (i) and (ii) below:
[Figure: inputs A, B, C feed three AND gates whose outputs go to a single OR gate with output Q. One NOT gate is on an input of the middle AND gate and another on an input of the bottom AND gate.]
(i) Write and simplify the Boolean expression for the above circuit using Boolean algebra. Show all the workings and algebraic rules used for the simplification.
(ii) Construct the logic circuit using a combination of only AND, OR and NOT gates for the simplified Boolean expression obtained in section b(i) above.""",
"""3. (a) ගිනි අනතුරු ඇඟවීමේ සංඥා පද්ධතියක් සඳහා දුම, ගිනි දැල්ල හා තාපය පිරිසිඳීම සඳහා සමන්විත වන අතර ඒවා පිළිවෙළින් ඇත්තේ S1, S2 හා S3 නම් සංවේදක තුනකින් සමන්විත වේ. සංවේදකයක් එක්කෝ සක්‍රීයව (තාර්කික අගය 1 ප්‍රතිදානය කරයි.) හෝ අක්‍රීයව (තාර්කික අගය 0 ප්‍රතිදානය කරයි.) පැවතිය හැකිය. අවම වශයෙන් සංවේදක දෙකක් සක්‍රීය වන විට මෙම පද්ධතිය ස්වයංක්‍රීයව ගිනි අනතුරු සංඥාව නිකුත් කරයි.
(i) ඉහත ගිනි අනතුරු ඇඟවීමේ සංඥා පද්ධතියේ ක්‍රියාකාරිත්වය නිරූපණය කරනු ලබන සත්‍යතා වගුව ගොඩනගන්න.
(ii) ඉහත සත්‍යතා වගුව නිරූපණය කරනු ලබන බූලියානු ප්‍රකාශනය ලබා ගන්න.
(b) පහත දැක්වෙන (i) හා (ii) කොටස්වලට පිළිතුරු සැපයීම සඳහා මෙහි පෙන්වා ඇති තාර්කික පරිපථය සලකන්න:
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන තාර්කික පරිපථය]
(i) බූලියානු වීජ ගණිතය භාවිත කරමින් ඉහත පරිපථය සඳහා බූලියානු ප්‍රකාශනයක් ලියා එය සරල කර දක්වන්න. සරල කිරීම සඳහා භාවිත කරනු ලැබූ සියළු ම ක්‍රියාවන් හා වීජීය රීති ලියා දක්වන්න.
(ii) ඉහත b (i) කොටසෙහි සරල කිරීම අවසානයේ දී ලබා ගත් ප්‍රකාශනය සඳහා AND, OR සහ NOT යන ද්වාර සංයෝජනයක් පමණක් භාවිත කරමින් තාර්කික පරිපථය ගොඩනගන්න.""")

add("2014 ESSAY01","""4. An alarm system has been designed to detect break ins by using three detectors. They are a motion detector, a glass break detector and a blackout detector. A detector can either be active (sends the logical value 1) or inactive (sends the logical value 0).
The system automatically detects a break in and triggers the alarm (sends the logical value 1) only when all the three detectors are simultaneously active, or the blackout detector and anyone of the remaining detectors are active.
(a) Construct a truth table to represent the functionality of the above alarm system.
(b) (i) Derive the Boolean expression to represent the truth table constructed in section (a) above.
(ii) Simplify the Boolean expression obtained in section (b) (i) above, using Boolean algebra. Clearly show all the workings and Boolean algebraic rules used for this simplification.
(iii) Construct the logic circuit for the simplified Boolean expression obtained in section (b) (ii) above.
(c) The analysis of the past incidents where the alarm triggered reveals that break in attempts have been made only during blackouts. Do you agree with the above statement? Justify your answer.""",
"""4. සංවේදක තුනක් භාවිත කර බලහත්කාරයෙන් ඇතුළුවීම් හඳුනා ගැනීම සඳහා අනතුරු ඇඟවීමේ සංඥා පද්ධතියක් සැලසුම් කර ඇත. මෙම සංවේදක චලන සංවේදකයක්, වීදුරු බිඳුම් සංවේදකයක් හා අන්ධකාර සංවේදකයක් වේ. සංවේදකයක් එක්කෝ සක්‍රීය (තාර්කික අගය 1 ලබා දීම) හෝ අක්‍රීය (තාර්කික අගය 0 ලබාදීම) හෝ වේ.
මෙම පද්ධතිය බලහත්කාරයෙන් ඇතුළුවීම් ස්වයංක්‍රීයව හඳුනාගෙන සංඥා පද්ධතිය ක්‍රියාත්මක (තාර්කික අගය 1 ලබාදීම) වන්නේ, එක ම අවස්ථාවේ දී සංවේදක තුනම සක්‍රීය වන්නේ නම් හෝ අන්ධකාර සංවේදකය හා ඉතිරි සංවේදක දෙකෙන් ඕනෑම එකක් සක්‍රීය වන්නේ නම් පමණි.
(a) ඉහත සංඥා පද්ධතියේ කාර්යබද්ධතාවය නිරූපණය කිරීමට සත්‍යතා වගුවක් ගොඩනගන්න.
(b) (i) ඉහත (a) කොටසේ ලබාගත් සත්‍යතා වගුව නිරූපණය කිරීම සඳහා බූලියානු ප්‍රකාශනය ලබා දෙන්න.
(ii) ඉහත b (i) කොටසෙන්ද ලබාගත් බූලියානු ප්‍රකාශනය බූලියානු වීජ ගණිතය භාවිත කර සරල කොට දක්වන්න. මෙම සරල කිරීම සඳහා භාවිත කළ ගණනය කිරීම් හා බූලියානු වීජ ගණිත නීති පැහැදිලි ව ලියා දක්වන්න.
(iii) ඉහත b (ii) කොටසෙන් ලබාගත් සරල කළ බූලියානු ප්‍රකාශනය සඳහා තාර්කික පරිපථයක් ගොඩනගන්න.
(c) මෙම සංඥා පද්ධතිය සක්‍රීය වීම සම්බන්ධව පසුගිය සිදුවීම් විශ්ලේෂණය කිරීමේ දී අනාවරණය වන්නේ බලහත්කාරයෙන් ඇතුළුවීමේ උත්සාහයන් සිදු වී ඇත්තේ අන්ධකාර අවස්ථාවල දී පමණක් බව ය. ඔබ ඉහත ප්‍රකාශය හා එකඟ වන්නේ ද? ඔබේ පිළිතුර තහවුරු කරන්න.""")

add("2015 ESSAY01","""5. (a) Explain how to derive a Boolean expression from a given truth table.
(b) In residential electrical wiring, the following circuit has been used to operate a light in a staircase.
[Figure: Circuit with Power Source P and Lamp L in a loop with two two-way switches, Switch S1 and Switch S2. Each switch has two positions X (top) and Y (bottom); the X and Y terminals of S1 are wired to the X and Y terminals of S2 respectively.]
As in the above circuit, two switches S1 and S2 are installed at the bottom and the top of the staircase to operate the lamp L. The lamp turned on by using the switch S1 at the bottom of the staircase can be turned off by using the switch S2 at the top of the staircase. Further, the lamp turned on by using switch S2 at the top of the staircase can also be turned off by using the switch S1 at the bottom of the staircase. Moreover, the lamp L turned on by a switch can be turned off by the same switch.
Assume that the connections to positions X and Y of a switch in the above circuit are represented by the truth values 1 and 0 respectively and the turned on and turned off states of the lamp L are represented by the truth values 1 and 0 respectively.
(i) Construct a truth table to represent the functionality of the above circuit.
(ii) Derive a Boolean expression to represent the truth table obtained in section (i) above.
(iii) What is the logic gate which is equivalent to the functionality of the Boolean expression obtained in section (ii) above?
(iv) Construct a logic circuit for the Boolean expression obtained in section (ii) above with NOT, AND and OR gates only.""",
"""5. (a) දී ඇති සත්‍යතා වගුවකින් බූලියානු ප්‍රකාශනයක් ව්‍යුත්පන්න කරන අයුරු පැහැදිලි කරන්න.
(b) ගෘහස්ථ විදුලි රැහැන් ඇද්දීමේ දී පඩිපෙළක සවි කරනු ලබන විදුලි පහනක් ක්‍රියාත්මක කිරීම සඳහා පහත දැක්වෙන පරිපථය යොදා ගන්නා ලදී.
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන පරිපථය]
ඉහත පරිපථයේ දැක්වෙන ලෙසට L විදුලි පහන ක්‍රියාත්මක කිරීම සඳහා පඩිපෙළේ පහළ සහ ඉහළ S1 සහ S2 ස්විච දෙකක් සවිකර ඇත. පඩිපෙළ පහළ දී S1 ස්විචය මගින් දල්වන ලද විදුලි පහන පඩිපෙළ ඉහළ දී S2 ස්විචය මගින් නිවා දැමීමට ද පඩිපෙළ ඉහළ දී S2 ස්විචය මගින් දල්වන ලද විදුලි පහන පඩිපෙළ පහළ දී S1 ස්විචය මගින් නිවා දැමීමට ද හැකි වේ. තව ද යම් ස්විචයක් මගින් දල්වන ලද L විදුලි පහන එම ස්විචය මගින් ම නිවා දැමීමට ද හැකි වේ.
ඉහත පරිපථයේ ස්විචයක් X ස්ථානයට සහ Y ස්ථානයට සම්බන්ධ වී ඇති අවස්ථා සත්‍යතා අගයන් 1 සහ 0 මගින් පිළිවෙළින් නිරූපණය වන බව ද, L පහන දල්වා ඇති හා නිවා ඇති අවස්ථා සත්‍යතා අගයන් 1 සහ 0 මගින් පිළිවෙළින් නිරූපණය වන බව ද උපකල්පනය කරන්න.
(i) ඉහත පරිපථයේ ක්‍රියාකාරිත්වය නිරූපණය කිරීම සඳහා සත්‍යතා වගුවක් ගොඩනගන්න.
(ii) ඉහත (i) කොටසේ දී ඔබ ලබාගත් සත්‍යතා වගුව නිරූපණය කිරීමට බූලියානු ප්‍රකාශනයක් ව්‍යුත්පන්න කරන්න.
(iii) ඉහත (ii) දී ලබා ගත් බූලියානු ප්‍රකාශනයේ කාර්යයට සමතුල්‍ය වන තාර්කික ද්වාරය කුමක් ද?
(iv) ඉහත (ii) කොටසේ දී ලබාගත් බූලියානු ප්‍රකාශනය සඳහා NOT, AND සහ OR ද්වාර පමණක් භාවිත කරමින් තාර්කික පරිපථයක් ගොඩනගන්න.""")

add("2016 ESSAY01","""6. The top secret recipe for making milk rice at the restaurant chain SLFC is kept in an electronic safe at their head office. The lock (L) of the safe can either be in locked or unlocked states represented by logical truth values 0 and 1 respectively. This lock has three different key holes K1, K2 and K3 each with a unique key. These three keys are in the custody of three directors of SLFC. The lock opens when at least two keys are properly inserted into the corresponding key holes. The situation where the corresponding key is properly inserted into any key hole is represented by the logical truth value 1 and all the other situations are represented by the logical truth value 0.
Assuming that only the following Integrated Circuits (ICs) are available, construct a logic circuit to operate the lock (L) of the safe, by using the truth tables and Boolean algebra. Clearly show the truth tables, Boolean expressions and the Boolean algebraic rules used to construct your circuit.
[Figure: two ICs. Left IC (20 pins: 1-10 along the bottom, 11-20 along the top) contains four 2-input AND gates. Right IC (8 pins: 1-4 along the bottom, 5-8 along the top) contains a 2-input OR gate.]""",
"""6. SLFC නමැති ආපන ශාලා දාමයේ කිරිබත් පිළියෙල කිරීම සඳහා භාවිත කරන ඉතා රහසිගත වට්ටෝරුව ප්‍රධාන කාර්යාලයේ ඇති ආරක්ෂිත විද්‍යුත් සේප්පුවක තැන්පත් කර ඇත. මෙම සේප්පුවෙහි අගුල (L) අගුලු ලා හෝ අගුළු ඇර හෝ අවස්ථා දෙකෙන් එකක පැවතිය හැකි අතර, එම අවස්ථා පිළිවෙළින් 0 සහ 1 යන තාර්කික සත්‍යතා අගයන් මගින් නිරූපණය කරයි. මෙම අගුලට K1, K2 සහ K3 යන එකිනෙකට වෙනස් වූ යතුරු සිදුරු තුනක් ඇති අතර සෑම යතුරු සිදුරකට ම අනන්‍ය වූ යතුරක් ඇත. මෙම යතුරු තුන SLFC ආයතනයේ අධ්‍යක්ෂකවරුන් තිදෙනෙකුගේ භාරයේ පවතී. යතුරු සිදුරුවලට අවම වශයෙන් අදාළ යතුරු දෙකකවත් ඇතුළත් කර ඇති විට අගුල විවෘත වේ. ඒනයින් යතුරු සිදුරකට අදාළ යතුර නිසි ලෙස ඇතුළත් කර ඇති අවස්ථාව සත්‍යතා අගය 1 මගින් ද අනික් සියලු ම අවස්ථාවන් සත්‍යතා අගය 0 මගින් ද නිරූපණය වේ.
පහත දක්වා ඇති සංගෘහිත පරිපථ පමණක් ඇති බව උපකල්පනය කරමින් සත්‍යතා වගු සහ බූලියානු වීජගණිතය භාවිත කරමින් ඉහත අගුල (L) ක්‍රියාත්මක කිරීම සඳහා පරිපථයක් ගොඩනගන්න. ඔබේ පරිපථය ගොඩනගන්න සඳහා භාවිත කළ සත්‍යතා වගු, බූලියානු ප්‍රකාශන සහ සරල කිරීමට යොදාගත් බූලියානු වීජගණිත නීති පැහැදිලි ව සඳහන් කරන්න.
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන සංගෘහිත පරිපථ (IC) දෙක]""")

add("2017 ESSAY01","""7. A switch (A), a temperature sensor (B) and a timer (C) of an air conditioner determine turned on and turned off states of the air conditioner. Turned on and turned off states of the air conditioner as well as the 'ON' and 'OFF' states of the switch, temperature sensor and the timer are represented by the logical values 1 and 0, respectively.
The air conditioner can be turned on or off manually by setting the switch to its 'ON' or 'OFF' states, respectively. The temperature sensor detects the temperature in the room. The temperature sensor sets its state as 'ON' or 'OFF' when the detected temperature is respectively higher or lower than a pre defined temperature value. The air conditioner is automatically turned on or off when the detected temperature is respectively higher or lower than the pre defined temperature value. The timer sets its state as 'OFF' until it reaches a preset time value and sets the state as 'ON' once it reached. The air conditioner is automatically turned off when the timer reaches the preset time value.
(a) Construct a logic circuit using only NOR gates to control the air conditioner. Clearly show truth table, Boolean expression and Boolean algebraic rules used for simplification. Assume that the electricity is always supplied to the air conditioner.
(b) The user of the air conditioner says that the switch is not required for the operation of the air conditioner. Do you agree with this statement? Justify your answer.""",
"""7. ස්විචයක් (A), උෂ්ණත්ව සංවේදකයක් (B) සහ කාලගණකයක් (C) මගින් වායුසමීකරණ යන්ත්‍රයක ක්‍රියාත්මක සහ ක්‍රියා විරහිත තත්ත්ව තීරණය කරනු ලබයි. වායුසමීකරණ යන්ත්‍රයේ ක්‍රියාත්මක සහ ක්‍රියා විරහිත අවස්ථා ද, ස්විචයේ, උෂ්ණත්ව සංවේදකයේ සහ කාලගණකයේ, 'ON' සහ 'OFF' අවස්ථා ද පිළිවෙළින් තාර්කික අගයන් 1 සහ 0 මගින් නිරූපණය කරනු ලැබේ.
ස්විචය එහි 'ON' හෝ 'OFF' අවස්ථාවට පිහිටුවීම මගින් වායුසමීකරණ යන්ත්‍රය අත්හුරුවෙන් ක්‍රියාත්මක හෝ ක්‍රියා විරහිත කළ හැකි ය. උෂ්ණත්ව සංවේදකය කාමරයේ අනාවරණය කරනු ලබන උෂ්ණත්වය පෙර අර්ථ දක්වන ලද උෂ්ණත්ව අගයකට වඩා ඉහළ හෝ පහළ හෝ විට උෂ්ණත්ව සංවේදකයේ එහි අවස්ථාව පිළිවෙළින් 'ON' හෝ 'OFF' හෝ ලෙස පිහිටුවයි. අනාවරණය කරනු ලැබූ උෂ්ණත්වය පෙර අර්ථ දක්වන ලද උෂ්ණත්ව අගයට වඩා ඉහළ හෝ පහළ හෝ විට වායුසමීකරණ යන්ත්‍රය පිළිවෙළින් ස්වයංක්‍රීයව ක්‍රියාත්මක හෝ ක්‍රියා විරහිත වේ. කාලගණකය පෙර නිරූපණය කළ කාල අගයකට පැමිණෙන තෙක් එහි අවස්ථාව 'OFF' ලෙස ද පැමිණි විට එහි අවස්ථාව 'ON' ලෙස ද පිහිටුවයි. කාලගණකය පෙර තීරණය කළ කාල අගයට පැමිණි විට වායුසමීකරණ යන්ත්‍රය ස්වයංක්‍රීයව ක්‍රියා විරහිත වේ.
(a) වායුසමීකරණ යන්ත්‍රය පාලනය කිරීමට NOR ද්වාර පමණක් යොදා ගනිමින් තාර්කික පරිපථයක් ගොඩනගන්න. සත්‍යතා වගුව, බූලියානු ප්‍රකාශනය සහ සරල කිරීමට යොදාගත් බූලියානු වීජ ගණිත නීති පැහැදිලිව දක්වන්න. සැමවිටම වායුසමීකරණ යන්ත්‍රයට විදුලිය සපයා දී ඇති බව උපකල්පනය කරන්න.
(b) ස්විචය වායුසමීකරණ යන්ත්‍රයේ ක්‍රියාකරීත්වයට අවශ්‍ය නොවන බව වායුසමීකරණ යන්ත්‍රයේ පරිශීලකයා කියයි. මෙම කියමනට ඔබ එකඟ වන්නේ ද? ඔබේ පිළිතුර සාධාරණීකරණය කරන්න.""")

add("2018 ESSAY01","""8. Suppose a logic circuit needs to be implemented for a digital system that has three inputs A, B and C and one output Z. Its behaviour is as follows:
If the input C=1, the output Z has the value of A.
If the input C=0, then output Z has the value of B.
(a) Obtain the truth table for the output Z.
(b) Write down either a sum of products (SOP) or a product of sums (POS) Boolean expression for Z.
(c) Simplify the Boolean expression for Z obtained in (b) above.
(d) Using the simplified expression in (c) above, construct a logic circuit for the system using either 2-input NAND gates only or 2-input NOR gates only.""",
"""8. A, B සහ C නම් ආදාන තුනක් සහ Z නම් එක් ප්‍රතිදානයක් සහිත සංඛ්‍යාංක පද්ධතියක් සඳහා තර්කන පරිපථයක් ස්ථාපනය කිරීමට අවශ්‍ය යැයි සිතන්න. එහි හැසිරීම පහත පරිදි වේ.
ආදානය C=1 නම් Z ප්‍රතිදානය A හි අගයන් ගනී.
ආදානය C=0 නම් Z ප්‍රතිදානය B හි අගයන් ගනී.
(a) Z ප්‍රතිදානය සඳහා සත්‍යතා වගුව ලබා ගන්න.
(b) Z සඳහා ගුණිතයන්ගේ එකතුව හෝ එකතුවල ගුණිතය හෝ ආකාරයට බූලියානු ප්‍රකාශනයක් ලියන්න.
(c) ඉහත (b) හි Z සඳහා ඔබ ලබාගත් ප්‍රකාශනය සුළු කරන්න.
(d) ඉහත (c) හි සුළු කරන ලද ප්‍රකාශනය සහ්‍ය භාවිත කර පද්ධතිය සඳහා ආදාන දෙකක් සහිත NAND ද්වාර පමණක් හෝ ආදාන දෙකක් සහිත NOR ද්වාර පමණක් හෝ භාවිත කර තර්කික පරිපථයක් ගොඩනගන්න.""")

add("2019 ESSAY01","""9. The Boolean function known as the majority function takes n binary inputs and outputs 1 if a majority (at least half) of the inputs are 1, otherwise it outputs 0. Let us consider the case when n=3, which is the 3-input majority function, whose inputs are A, B and C and the output is Z.
(a) Give the truth table for the 3-input majority function.
(b) Using Karnaugh maps, derive a simplified Boolean expression for the output Z in the 3-input majority function.
(c) Construct a logic circuit for the 3-input majority function using NAND gates only.""",
"""9. බහුතර ශ්‍රිතය ලෙස හැඳින්වෙන බූලියානු ශ්‍රිතය ද්විමය ආදාන n ලබාගෙන, ආදානයෙන් බහුතරයක් (අඩු තරමින් අඩක්වත්) 1 වේ නම්, 1 ප්‍රතිදානය කරයි, නැතහොත් 0 ප්‍රතිදානය කරයි. ආදාන A, B හා C ද Z ප්‍රතිදානය වන n = 3 අවස්ථාව එනම් ආදාන 3 හි බහුතර ශ්‍රිතය සලකමු.
(a) ආදාන 3 හි බහුතර ශ්‍රිතය සඳහා සත්‍යතා වගුව ඉදිරිපත් කරන්න.
(b) ආදාන 3 හි බහුතර ශ්‍රිතයේ Z සඳහා සුළු කරන ලද බූලියානු ප්‍රකාශනයක්, කානෝ සිතියම් භාවිත කරමින් ව්‍යුත්පන්න කරන්න.
(c) ආදාන 3 හි බහුතර ශ්‍රිතය සඳහා NAND ද්වාර පමණක් භාවිත කර තර්කණ පරිපථයක් ගොඩනගන්න.""")

add("2020 ESSAY05","""10. Consider the logic circuit shown in the figure, in which A, B and C are the inputs and Z is the output.
[Figure: Inputs A, B, C. Two OR gates and a final AND gate producing Z. (Wiring as shown in the original image.)]
(a) Give the complete truth table for the given circuit.
(b) Using a Karnaugh map, derive a simplified sum-of-products (SOP) expression for the output Z.
(c) Using a Karnaugh map, derive a simplified product-of-sums (POS) expression for the output Z.
(d) Of the two expressions (SOP and POS) you obtained in (b) and (c) above, which one is better to implement a more simplified logic circuit than the given logic circuit above? Explain your answer.""",
"""10. ආදාන A, B සහ C සහ ප්‍රතිදානය Z වන පහත රූපයෙහි දී ඇති තර්කන පරිපථය සලකන්න.
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන පරිපථය]
(a) ඉහත දී ඇති පරිපථය සඳහා සම්පූර්ණ සත්‍යතා වගුව ගොඩනගන්න.
(b) කානෝ සිතියමක් භාවිතයෙන් Z ප්‍රතිදානය සඳහා, සුළු කරන ලද, ගුණිතවල එකතුවෙහි (SOP) ප්‍රකාශයක් ව්‍යුත්පන්න කරන්න.
(c) කානෝ සිතියමක් භාවිතයෙන් Z ප්‍රතිදානය සඳහා, සුළු කරන ලද, එකතුවල ගුණිතයෙහි (POS) ප්‍රකාශයක් ව්‍යුත්පන්න කරන්න.
(d) ඉහත දෙන ලද තර්කන පරිපථයට වඩා සරල තර්කන පරිපථයක් ක්‍රියාත්මක කිරීමට, ඉහත (b) සහ (c) හි ඔබ විසින් ලබා ගන්නා ලද ප්‍රකාශ (SOP සහ POS) දෙක අතුරෙන් කවර එකක් වඩා හොඳ ද? ඔබේ පිළිතුර පැහැදිලි කරන්න.""")

add("2021 ESSAY05","""11. Consider the logic circuit shown in the figure, in which A, B and C are the inputs and X is the output.
[Figure: Inputs A, B, C feed three AND gates whose outputs feed an OR gate producing X. Some inputs pass through NOT gates before the AND gates. (Wiring as shown in the original image.)]
(a) Show the complete truth table for the given circuit.
(b) Complete the Karnaugh map, according to the following format.
AB columns: 00 | 01 | 11 | 10 ; C rows: 0, 1 (empty cells)
(c) Using the Karnaugh map, derive an optimal (most simplified) sum-of-products (SOP) expression for the output X. Show the loops clearly on the Karnaugh map.
(d) Using the Karnaugh map, derive an optimal (most simplified) product-of-sums. (POS) expression for the output X. Show the loops clearly on the Karnaugh map.
(e) Of the optimal SOP and POS expressions you obtained in (c) and (d) above, which is better (or more suitable) to implement a simplified logic circuit? Explain your answer.""",
"""11. ආදාන A, B හා C සහ ප්‍රතිදානය X වන පහත රූපයෙහි දී ඇති තර්කන පරිපථය සලකන්න.
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන පරිපථය]
(a) ඉහත දී ඇති පරිපථය සඳහා සම්පූර්ණ සත්‍යතා වගුව ගොඩනගන්න.
(b) කානෝ සිතියම, පහත ආකෘතිය පරිදි සම්පූර්ණ කරන්න.
AB තීරු: 00 | 01 | 11 | 10 ; C පේළි: 0, 1 (හිස් කොටු)
(c) කානෝ සිතියම භාවිතයෙන්, X ප්‍රතිදානය සඳහා, ගුණිතවල එකතුවෙහි සරලතම ප්‍රකාශය ව්‍යුත්පන්න කරන්න. ලූප පැහැදිලි ලෙස ඔබගේ කානෝ සිතියමේ පෙන්වන්න.
(d) කානෝ සිතියම භාවිතයෙන්, X ප්‍රතිදානය සඳහා, එකතුවල ගුණිතයෙහි සරලතම ප්‍රකාශය ව්‍යුත්පන්න කරන්න. ලූප පැහැදිලි ලෙස ඔබගේ කානෝ සිතියමේ පෙන්වන්න.
(e) ඉහත (c) සහ (d) හි ඔබ විසින් ලබා ගන්නා ලද සරල SOP සහ POS ප්‍රකාශ දෙක අතුරෙන්, වඩාත් සරල තර්කන පරිපථයක් ක්‍රියාත්මක කිරීමට වඩා උචිත (සුදුසු) වන්නේ කවරක් ද? ඔබේ පිළිතුර පැහැදිලි කරන්න.""")

add("2022 ESSAY05","""12. (a) Consider the logic circuit shown in the following figure in which P, Q and R are the inputs and Z is the output.:
[Figure: Inputs P, Q, R feed four 3-input AND gates, some inputs inverted through NOT gates; the outputs of the four AND gates feed a single OR gate producing Z. (Wiring as shown in the original image.)]
(i) Draw the complete truth table for the above circuit.
(ii) Complete the Karnaugh map relevant to the above circuit according to the following format.
PQ columns: 00 | 01 | 11 | 10 ; R rows: 0, 1 (empty cells)
(iii) Using the Karnaugh map, derive the most simplified sum-of-products expression for the output Z. Show the loops clearly on the Karnaugh map.
(d) (i) Using Boolean algebra, show that the Boolean expression !ABC + A!BC + AB!C + ABC is equivalent to BC + AC + AB.
(ii) Draw a logic circuit for the above simplified expression in (b)(i) by only using OR and AND gates.
(iii) Draw a logic circuit for the above simplified expression in (b)(i) by only using NAND gates.""",
"""12. (a) ආදාන P, Q හා R සහ ප්‍රතිදානය Z වන පහත රූපයේ දී ඇති තර්කන පරිපථය සලකන්න.
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන පරිපථය]
(i) ඉහත පරිපථය සඳහා සම්පූර්ණ සත්‍යතා වගුව අඳින්න.
(ii) ඉහත පරිපථයට අදාළ කානෝ සිතියම පහත ආකෘතිය පරිදි සම්පූර්ණ කරන්න.
PQ තීරු: 00 | 01 | 11 | 10 ; R පේළි: 0, 1 (හිස් කොටු)
(iii) Z ප්‍රතිදානය සඳහා ගුණිතවල එකතුවෙහි වඩාත් සරලතම ප්‍රකාශය කානෝ සිතියම භාවිතයෙන් ව්‍යුත්පන්න කරන්න. ලූප පැහැදිලි ලෙස කානෝ සිතියමේ පෙන්වන්න.
(d) (i) බූලීය වීජ ගණිතය භාවිතයෙන් !ABC + A!BC + AB!C + ABC බූලීය ප්‍රකාශය BC + AC + AB ට සමාන වන බව පෙන්වන්න.
(ii) ඉහත b(i) හි දැක්වෙන සරලතම ප්‍රකාශය සඳහා OR සහ AND ද්වාර පමණක් භාවිතයෙන් තර්කන පරිපථයක් අඳ දක්වන්න.
(iii) ඉහත b(i) හි දැක්වෙන සරලතම ප්‍රකාශය සඳහා NAND ද්වාර පමණක් භාවිතයෙන් තර්කන පරිපථයක් අඳ දක්වන්න.""")

add("2023 ESSAY05","""13. (a) A circuit with three inputs (A, B, C) and one output (Z) is to be designed. The output should be equal to 1 when the binary value combination of the three inputs is either 1, 3 or 6. The output should be 0 for other cases.
(i) Draw the complete truth table for the above circuit.
(ii) Complete the Karnaugh map relevant to the above circuit according to the following format:
AB columns: 00 | 01 | 11 | 10 ; C rows: 0, 1 (empty cells)
(iii) Using the Karnaugh map, derive the most simplified product of sums (POS) expression for the output Z. Show the loops clearly on the Karnaugh map.
(iv) Draw a logic circuit for the simplified expression derived in (iii) by only using NOR gates assuming that the complemented inputs !A, !B and !C are also available.
(b) Using Boolean Algebra show that !AC + !AB + !ABC + BC is equivalent to C + !AB.
(c) Consider the flip flop circuit shown on the right:
[Figure: SR latch built from two cross-coupled NOR gates. Input R feeds the top NOR gate whose output is Q; input S feeds the bottom NOR gate whose output is !Q; each gate's output is fed back to the input of the other gate.]
(i) Assume that the S input is 1 and the R input is 0. What will be the output at Q?
(ii) What will be the output at Q if the S input is now made 0?
(iii) What will be the output at Q when the R input is now made 1?""",
"""13. (a) A, B, C නම් වූ ආදාන තුනකින් සහ Z නම් වූ එක් ප්‍රතිදානයකින් සමන්විත පරිපථයක් නිර්මාණය කළ යුතුව ඇත. ආදාන තුනේ ද්විමය අගයන්ගේ සංයෝජනය 1 හෝ 3 හෝ 6 හෝ වන විට, ප්‍රතිදානය 1 විය යුතු ය. අනෙකුත් අවස්ථා සඳහා ප්‍රතිදානය 0 විය යුතු ය.
(i) ඉහත පරිපථය සඳහා සම්පූර්ණ සත්‍යතා වගුව අඳින්න.
(ii) ඉහත පරිපථයට අදාළ කානෝ සිතියම පහත ආකෘතිය පරිදි සම්පූර්ණ කරන්න.
AB තීරු: 00 | 01 | 11 | 10 ; C පේළි: 0, 1 (හිස් කොටු)
(iii) Z ප්‍රතිදානය සඳහා එකතුවල ගුණිතයෙහි වඩාත් සරලතම ප්‍රකාශය කානෝ සිතියම භාවිතයෙන් ව්‍යුත්පන්න කරන්න. ලූප පැහැදිලි ලෙස කානෝ සිතියමේ පෙන්වන්න.
(iv) ඉහත (iii) හි ලබාගත් සරලතම ප්‍රකාශය සඳහා NOR ද්වාර පමණක් භාවිත කරන තාර්කික පරිපථයක් අඳ දක්වන්න. !A, !B සහ !C (අනුපූරක ආදාන) කෙලින්ම ලබාගත හැකි බව උපකල්පනය කරන්න.
(b) බූලීය වීජ ගණිතයෙන් !AC + !AB + !ABC + BC බූලීය ප්‍රකාශය C + !AB ට සමාන වන බව පෙන්වන්න.
(c) දක්ෂිණපස දැක්වෙන පිළිපොළ පරිපථය සලකන්න.
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන පරිපථය]
(i) S ආදානය 1 සහ R ආදානය 0 යැයි උපකල්පනය කරන්න. Q ප්‍රතිදානය කුමක් වේ ද?
(ii) S ආදානය දැන් 0 කළ විට, Q ප්‍රතිදානය කුමක් වේ ද?
(iii) R ආදානය දැන් 1 කළ විට, Q ප්‍රතිදානය කුමක් වේ ද?""")

add("2024 ESSAY05","""14.(a)(iii) A register is a group of binary cells suitable for holding binary information and is constituted by a collection of flip-flops. How many flip-flops are needed to make an n bit register?

15. (a) Draw the complete truth table for the following circuit:
[Figure: Inputs A, B, C. A NOT gate feeds an AND gate; the AND gate output and another input feed a final gate (with an inverting bubble at its output) producing Z. (Wiring as shown in the original image.)]
(b) Write down the following Boolean expression in the simplest form.
(A + B) . (A + !B) + A!B
(c) In a circuit with three inputs A, B and C the output (Z) should be 1 when each of two or three inputs is 1. If none or only one of the inputs are 1 then the output should be 0.
(i) Draw the complete truth table for the above circuit.
(ii) Complete the Karnaugh map relevant to the above circuit according to the following format:
AB columns: 00 | 01 | 11 | 10 ; C rows: 0, 1 (empty cells)
(iii) Using the Karnaugh map, derive the most simplified sum-of-products (SOP) expression for the output Z. Show the loops clearly on the Karnaugh map.
(iv) Draw a logic circuit for the most simplified expression derived in above (iii) by only using AND, NOT and OR gates.
(d) (i) Explain the use of half adder in digital circuits.
(ii) Describe how a flip-flop works as a memory element in digital circuits. Explain how it differs from combinational logic gates.
(iii) Draw the truth table for a full adder circuit""",
"""14.(a)(iii) රෙජිස්ටරයක් යනු ද්විමය තොරතුරු රඳවා තබා ගැනීමට සුදුසු ද්විමය කෝෂ සමූහයක් වන අතර එය පිළි-පොළ එකතුවකින් සමන්විත වේ. බිටු n සහිත රෙජිස්ටරයක් සෑදීම සඳහා අවශ්‍ය පිළි පොළ ගණන කොපමණ ද?

15. (a) පහත පරිපථය සඳහා සම්පූර්ණ සත්‍යතා වගුව අඳින්න:
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන පරිපථය]
(b) පහත බූලීය ප්‍රකාශය එහි සරලතම ආකාරයෙන් ලියා දක්වන්න.
(A + B) . (A + !B) + A!B
(c) A, B සහ C නම් ආදාන තුනකින් යුත් පරිපථයක, ආදාන දෙකක් හෝ තුනක් හෝ ඉන් එකක් 1 වීම, Z ප්‍රතිදානය 1 විය යුතුය. කිසිම ආදානයක් 1 නොවන විට සහ ආදාන එකක් පමණක් 1 වීම විට ප්‍රතිදානය 0 විය යුතු ය.
(i) ඉහත පරිපථය සඳහා සම්පූර්ණ සත්‍යතා වගුව අඳින්න.
(ii) ඉහත පරිපථයට අදාළ කානෝ සිතියම පහත ආකෘතිය පරිදි සම්පූර්ණ කරන්න.
AB තීරු: 00 | 01 | 11 | 10 ; C පේළි: 0, 1 (හිස් කොටු)
(iii) Z ප්‍රතිදානය සඳහා ගුණිතවල එකතුවෙහි (SOP) වඩාත් සරලතම ප්‍රකාශය කානෝ සිතියම භාවිතයෙන් ව්‍යුත්පන්න කරන්න. ලූප පැහැදිලි ලෙස කානෝ සිතියමේ පෙන්වන්න.
(iv) ඉහත (iii) හි ලබාගත් සරලතම ප්‍රකාශය සඳහා AND, NOT සහ OR ද්වාර පමණක් භාවිතා කරන තාර්කික පරිපථයක් අඳ දක්වන්න.
(d) (i) අංකිත පරිපථවල අර්ධ ආකලකයේ භාවිතය පහදන්න.
(ii) අංකිත පරිපථවල මතක මූලයක් ලෙස පිළිපොළක් ක්‍රියාකරන අයුරු විස්තර කරන්න. එය සංයෝජන තාර්කික ද්වාරවලින් වෙනස් අයුරු පහදන්න.
(iii) පූර්ණකලක පරිපථයක් සඳහා සත්‍යතා වගුව අඳින්න.""")

add("2025 ESSAY05","""16. (a) Prove the following using Boolean algebra:
!A!BCD + !A!BCD + !ABC!D + !ABCD + AB!C!D + ABCD = !ACD + AB!D + BC
(b) A bank vault is secured by a logic circuit with four binary inputs. Three of these inputs come from the keys named k0, k1, and k2, and the fourth input comes from a timer. The four inputs together form a 4-bit binary number with the timer input as the Most Significant Bit (MSB) and k0 as the Least Significant Bit (LSB).
The vault unlocks only when the 4-bit binary input (from timer, k2, k1, and k0 respectively) represents a number that is a multiple of 3 (i.e., 3, 6, 9, 12, 15) or a multiple of 7 (i.e., 7, 14).
Design the most simplified logic circuit that takes these four inputs and gives an output Z which is equal to 1 for the valid input combinations to indicate the unlocking of the vault.
(c) Key k1 is held by the officer-in-charge, while k0, and k2 are held by two senior officers. The duration in which the time signal becomes 1 is decided by the bank. State whether the vault can be opened in the absence of the officer-in-charge. Justify your answer.""",
"""16. (a) බූලීය වීජ ගණිතය භාවිතයෙන් පහත සාධනය කරන්න.
!A!BCD + !A!BCD + !ABC!D + !ABCD + AB!C!D + ABCD = !ACD + AB!D + BC
(b) බැංකුවක ආරක්ෂිත කුටියක් ද්විමය ආදාන හතරකින් යුත් තාර්කික පරිපථයකින් සුරක්ෂිත කර ඇත. ඉන් ආදාන තුනක් k0, k1 සහ k2 ලෙස නම් කළ යතුරුවලින් ලැබෙන අතර සිව්වන ආදානය කාල පාලකයකින් ලැබේ. එම ආදාන හතරින් එක්ව, කාල පාලක ආදානය වැඩිම වෙසෙසි බිටුව ලෙස සහ k0 ආදානය අඩුම වෙසෙසි බිටුව ලෙස වන බිටු 4 ක ද්විමය සංඛ්‍යාවක් සාදයි.
කුටියේ අගුල ඇරෙන්නේ බිටු හතරේ ද්විමය ආදානය (අනුපිළිවෙලින් කාලපාලකය, k2, k1, සහ k0 වලින්) තුනේ ගුණාකාරයක් (එනම් 3, 6, 9, 12, 15) හෝ හතේ ගුණාකාරයක් (එනම් 7, 14) වන විට පමණි.
මෙම ආදාන හතර ලබාගෙන, වලංගු ආදාන සංයෝජනයන් සඳහා Z නම් වූ ප්‍රතිදානයක් 1 ලෙස දක්වමින් ඇරුළු කුටියේ අගුල ඇරීම පෙන්වා දැක්වීමට සරලතම තාර්කික පරිපථය නිර්මාණය කරන්න.
(c) යතුරු k1 කාර්යභාර නිලධාරියා භාරයේ ද, k0 සහ k2 ජ්‍යෙෂ්ඨ නිලධාරීන් දෙදෙනෙකු භාරයේ ද ඇත. කාල පාලකයේ සංඥාව 1 ලෙස පවතින කාලය බැංකුව විසින් තීරණය කෙරේ. කාර්යභාර නිලධාරියා නැති විට ඇරුළු කුටිය විවෘත කළ හැකි දැයි සඳහන් කරන්න. ඔබගේ පිළිතුර සාධාරණීකරණය කරන්න.""")

add("2026 ESSAY05","""17. (a) State and prove De Morgan's theorems.
(b) Show that by solving the left-hand side of the equation using Boolean algebra.
!A!BC + !AB!C + A!B!C + ABC = (!AB + A!B)!C + !(!AB + A!B)C
(c) The room containing a company's confidential documents is secured by a door controlled by a logic circuit. This logic circuit is equipped with two locks and a fingerprint scanner. The supervisor and a clerk each hold one key, with each key corresponding to one of the two locks. Under normal operation, the door opens only when both the supervisor's key and the clerk's key are inserted simultaneously. However, in the absence of the clerk, the supervisor is authorized to open the door by inserting his own key and providing his fingerprint at the same time. The circuit does not operate when all three inputs are provided simultaneously. Design a logic circuit, clearly showing all the necessary design steps, to implement this access control system using only NAND gates. State assumptions you make if any.""",
"""17. (a) ද මෝගන්ගේ නාහයන් සඳහන් කර ඒවා සාධනය කරන්න.
(b) සමීකරණයේ වම්පස ප්‍රකාශනය බූලීය වීජ ගණිතයෙන් විසඳා: බව පෙන්වන්න.
!A!BC + !AB!C + A!B!C + ABC = (!AB + A!B)!C + !(!AB + A!B)C
(c) සමාගමක රහසිගත ලේඛන අඩංගු කාමරය තාර්කික පරිපථයක් මගින් පාලනය කරනු ලබන දොරකින් ආරක්ෂා කර ඇත. මෙම තාර්කික පරිපථයට අගුළු දෙකකින් සහ ඇඟිලි සලකුණු ස්කෑනරයකින් සමන්විත වේ. අගුළු දෙක යතුරු වෙන වෙනම අධීක්ෂක නිලධාරියා සහ ලිපිකරුවෙකු සතුව එක් යතුරු බැගින් ඇති අතර, එම එක් යතුරක් අගුළු දෙකෙන් එක් අගුලකට අදාළ වේ. සාමාන්‍ය ක්‍රියාකාරිත්වයේ දී අධීක්ෂණ නිලධාරියාගේ යතුර සහ ලිපිකරුවාගේ යතුර එකවර ඇතුළු කළ විට පමණක් දොර විවෘත වේ. එසේ වුවද, ලිපිකරුවා නොමැතිව ඇති විට, අධීක්ෂක නිලධාරියාට තම ඇඟිලි සලකුණ ලබාදීමෙන් සමඟ යතුර පමණක් ඇතුළු කිරීමෙන් දොර විවෘත කිරීමට අධීක්ෂක නිලධාරියාට බලය ලබා දී ඇත. මෙම ආදාන තුනම එකවර ලබාදුන් විට පරිපථය ක්‍රියාත්මක නොවේ. මෙම ප්‍රවේශ පාලන පද්ධතිය ක්‍රියාත්මක කිරීම සඳහා, අවශ්‍ය සියලු සැලසුම් පියවර පැහැදිලිව පෙන්වමින්, NAND ද්වාර පමණක් භාවිත කර තාර්කික පරිපථයක් සැලසුම් කරන්න. ඔබ විසින් කරන ලද උපකල්පන (ඇත්නම්) ප්‍රකාශ කරන්න.""")

assert len(E)==17,len(E)
json.dump(E,open('D:/DevOps/aws-clf-c02-bridge/tools/transcribed/ictl-logic-essay.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
print(len(E))
