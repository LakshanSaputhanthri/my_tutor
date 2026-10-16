import json
def M(n,d,q,o,os=None):
    r={"n":n,"d":d,"q":q,"o":o}
    if os:r["os"]=os
    return r
SI=["I පමණි","II පමණි","III පමණි","I හා II පමණි","I හා III පමණි"]
items=[
M(1,"2011 Q27","Which of the following would be the result if the Boolean expression F(x,y) = (x+y)' . (x'+y')' is simplified by using De Morgan's Law?  [as printed: overbar over (x+y) and overbar over (x' + y')]",["x","y","0","1","x, y"]),
M(2,"2011 Q28","Which of the following Boolean expressions represents the given logic circuit?\n[Figure: inputs A, B, C. A and B feed a gate with an output bubble in the first stage (OR with bubble); B and C feed an AND gate; the outputs of these gates feed a final OR gate. Wiring partly unclear in the image.]",["(A+B)' + (B+C)","(A + B) + (B.C)","(A+B)' + (B+C)' [overbar over (B+C)]","(A.B) + (B.C)","(A+B)' + (B.C)"]),
M(3,"2012 Q26","What would be the result if the following Boolean expression is simplified?\nF(x,y) = x'y'(x'+y)(y+y')",["x'","y'","x","y","xy"]),
M(4,"2012 Q27","Which of the following Boolean expressions represents the output of the given logic circuit?\n[Figure: inputs A, B feed an OR gate; inputs B, C feed an AND gate; the two outputs feed a final gate with an output bubble (NOR)]",["(A+B)' + (B.C)'","(A+B)' . (B.C)'","((A+B) + (B.C))' [overbar over the whole expression]","(A.B)' + (B.C)'","((A.B) + (B+C))' [overbar over the whole expression]"]),
M(5,"2013 Q01","The Boolean expression (x + y) . (x + z) simplifies to ........",["x","x . (y + z)","x . y . z","x + y . z","x + y + z"]),
M(6,"2013 Q02","Which of the following Boolean expressions represents the output (Q) of the circuit shown below? A and B are inputs.\n[Figure: A passes through a NOT gate into an AND gate (the other AND input is from B); B also feeds an OR gate together with the AND output; the OR output passes through a NOT gate to Q]",["A'.B' + A.B'","A'.B' + A.B","A.B + A'.B'","A'.B + A.B'","A'.B + A.B'"]),
M(7,"2013 Q09","Which of the following is an incorrect Karnaugh Map layout to represent a Boolean function of four (4) Boolean variables a, b, c and d?",[
"ab\\cd | 01 | 00 | 10 | 11  (rows: 01, 00, 10, 11)",
"ac\\bd | 01 | 00 | 10 | 11  (rows: 01, 00, 10, 11)",
"ab\\cd | 01 | 00 | 11 | 10  (rows: 01, 00, 11, 10)",
"ad\\bc | 11 | 10 | 00 | 01  (rows: 11, 10, 00, 01)",
"ac\\bd | 00 | 10 | 11 | 01  (rows: 00, 10, 11, 01)"]),
M(8,"2014 Q12","Consider the following logic circuit.\n[Figure: inputs X, Y, Z; two OR gates whose outputs feed an AND gate giving Q]\nWhich of the following circuit diagrams represents a simplified version of the above circuit?",["[Figure 1: an AND gate and then an OR gate -> Q]","[Figure 2: an OR gate whose output goes to an AND gate -> Q]","[Figure 3: a single AND gate with inputs from X, Y, Z -> Q]","[Figure 4: an AND gate whose output goes to an OR gate -> Q]","[Figure 5: a single OR gate with inputs from X, Y, Z -> Q]"]),
M(9,"2014 Q13","Consider the following circuit with four push button switches namely: S1, S2, S3, and S4. These four switches can either be in pushed or released states which are represented by 1 and 0 respectively. (Note: In the circuit given below, all the switches are in released state having value 0.)\n[Figure: a battery, switch S1 in series, then a parallel pair of branches (S2 on top, S3 on bottom), then S4 in series, then a bulb]\nWhich of the following Boolean expressions represents the function of the bulb, if the on state of the bulb is represented by the value 1?",["S1 + (S2 . S3) + S4","(S1 + S2) . (S3 + S4)","(S1 . S2) + (S3 . S4)","S1 . S4 . (S2 + S3)","S2 + (S1 . S4) + S3"]),
M(10,"2015 Q11","Consider the following combinatory circuit implemented using universal gates:\n[Figure: two NAND gates, each with its inputs tied to the same input; their outputs feed a third NAND gate producing the Output]\nThe above circuit is equivalent to a/an,",["AND Gate","OR Gate","NAND Gate","NOR Gate","NOT Gate"]),
M(11,"2016 Q11","Consider the following logic circuit implemented using universal gates:\n[Figure: two NOR gates, each with its inputs tied to the same input; their outputs feed a third NOR gate]\nThe above circuit is equivalent to a/an,",["NOT Gate","AND Gate","OR Gate","NAND Gate","NOR Gate"]),
M(12,"2017 Q47","Consider the following statements on using NAND, NOR gates over NOT, AND, OR gates when constructing logic circuits:\nA - They make logic circuit design simpler.\nB - They help to construct logic circuits that consume less electricity.\nC - They make logic circuit construction more economical.\nWhich of the above statements is/are correct?",["A only","B only","A and B only","A and C only","B and C only"],["A පමණි","B පමණි","A හා B පමණි","A හා C පමණි","B හා C පමණි"]),
M(13,"2018 Q21","Consider the following Boolean expression.\n(A' + B.C')'  [as printed: overbar over the whole of A' + B . C' ]\nWhich of the following is/are equivalent to the above expression?\nI - A' + B' . C   [as printed: Ā + B̄ · C]\nII - A' . (B . C')'   [as printed: Ā · overline(B·C̄)]\nIII - A' . B' + A' . C   [as printed: Ā·B̄ + Ā·C]",["I only","II only","III only","I and II only","II and III only"],["I පමණි","II පමණි","III පමණි","I හා II පමණි","II හා III පමණි"]),
M(14,"2018 Q22","Consider the following logic circuit.\n[Figure: A and B each pass through a NOT gate; the two NOT outputs feed an OR gate; the OR output and A feed a NAND-type gate (output bubble) giving X]\nWhich of the following circuit/s is/are equivalent to the above circuit?\n[Figures I, II, III: three alternative circuits of AND, OR, NOT gates with inputs A and B and output X]",["I only","II only","III only","I and II only","All I, II and III"],["I පමණි","II පමණි","III පමණි","I හා II පමණි","I, II සහ III සියල්ලම"]),
M(15,"2019 Q39","Consider the Karnaugh map shown below.\nAB:  00 | 01 | 11 | 10\nC=0:  0 | 0 | 0 | 1\nC=1:  1 | 1 | 0 | 1\n[Two marked groups of 0s: the pair at AB=00 and 01 in row C=0 (horizontal), and the pair at AB=11 in rows C=0 and C=1 (vertical)]\nWhich of the following is the correct logic expression that corresponds to the two marked segments on the Karnaugh map?",["AB' + BC'","A'C' + AB","(A' + C')(A + B)","(A + C)(A' + B')","AC + A'B'"]),
M(16,"2019 Q37","Consider the following logic circuit diagram to answer the questions 37 and 38.\n[Figure: Inputs A and B go into the first dotted box: an XOR gate and an AND gate. The second dotted box has input Cin and the XOR output: an XOR gate (output S) and an AND gate. The two AND gate outputs go to an OR gate giving Cout.]\nWhich of the following statements is/are correct about the above circuit?\nI - It implements a full adder.\nII - The logic function of S can be stated as S = A ⊕ B ⊕ Cin.\nIII - The logic function of Cout can be stated as Cout = AB + BCin + ACin.",["I only","II only","I and II only","I and III only","All I, II and III"],["I පමණි","II පමණි","I හා II පමණි","II හා III පමණි","I, II සහ III සියල්ලම"]),
M(17,"2019 Q38","Which of the following statements is/are correct about the part of the circuit within the area surrounded by the dotted line?\nI - It implements a half adder.\nII - It can be implemented using only AND and OR gates.\nIII - It can be implemented using only NAND gates.",["I only","II only","III only","I and III only","All I, II and III"],["I පමණි","II පමණි","III පමණි","I හා III පමණි","I, II සහ III සියල්ලම"]),
M(18,"2020 Q11","Consider the following logic circuit consisting of NAND gates.\n[Figure: NAND gate 1 takes inputs A and B; NAND gate 2 takes inputs A' and X; their outputs and the input Y feed a three-input NAND gate producing F]\nIf the required output of the above circuit is AB + A'B' + C', then what should the inputs X and Y be?",["X = B and Y = C","X = B and Y = C'","X = B' and Y = C","X = B' and Y = C'","X = C' and Y = B"]),
M(19,"2020 Q09","Which of the following is the most simplified expression equivalent to ABC' + BC' + A'BC + BC ?",["ABC' + A'BC + B","B(AC' + A'C) + B","C'(AB + B) + B(A'C + B)","AC' + A'C + B","A'C + B"]),
M(20,"2020 Q10","A block diagram of a sequential logic circuit is shown below, with one block labelled as \"A\" and the other labelled as \"B\".\n[Figure: a large block A whose output returns (feedback) through the smaller block B back to an input of A]\nWhich of the following statements about the above block diagram are correct?\nI - The block A is a combinational logic circuit.\nII - The block B is a memory element.\nIII - Only the block A can be implemented using logic gates.",["I only","II only","I and II only","I and III only","All I, II and III"],["I පමණි","II පමණි","I හා II පමණි","I හා III පමණි","I, II සහ III සියල්ලම"]),
M(21,"2021 Q09","Consider the following Karnaugh map and the logic circuit implemented based on it where A, B and C are the inputs and Z is the output:\n(a) Karnaugh map\nAB:  00 | 01 | 11 | 10\nC=0:  0 | e | f | 0\nC=1:  1 | g | h | 1\n(b) Logic circuit based on Karnaugh map: [Figure: A and B go to an AND gate; its output and C go to an OR gate giving Z]\nFor the logic circuit to correctly implement the logic function represented in the Karnaugh map, what should be the values of e, f, g, h ?",["e=0, f=0, g=1, h=1","e=0, f=1, g=1, h=1","e=1, f=0, g=1, h=1","e=1, f=1, g=0, h=0","e=1, f=1, g=0, h=1"]),
M(22,"2022 Q09","Consider the following logic circuit:\n[Figure: A and B go to an AND gate; B goes through a NOT gate; the AND output and the NOT output feed a NOR gate (OR with output bubble) giving Q]\nWhen B=1, what would definitely be the output at Q?",["A","A'","B","B'","0"]),
M(23,"2022 Q10","Simplified Boolean expressions help to obtain simpler circuits.\nWhich of the following is a simplified form of X + X'Y ?",["X","Y","XY","X'Y","X + Y"]),
M(24,"2022 Q11","Consider the following truth table:\nA | B | C | Z\n0 | 0 | 0 | 0\n0 | 0 | 1 | 0\n0 | 1 | 0 | 1\n0 | 1 | 1 | 1\n1 | 0 | 0 | 1\n1 | 0 | 1 | 1\n1 | 1 | 0 | 0\n1 | 1 | 1 | 0\nWhat is the correct Karnaugh map for the above truth table?",[
"BC: 00 | 01 | 10 | 11\nA=0: 0 | 0 | 1 | 1\nA=1: 1 | 1 | 0 | 0",
"BC: 00 | 01 | 11 | 10\nA=0: 0 | 0 | 1 | 1\nA=1: 1 | 1 | 0 | 0",
"BC: 00 | 10 | 01 | 11\nA=0: 0 | 1 | 0 | 1\nA=1: 1 | 0 | 1 | 0",
"BC: 00 | 10 | 11 | 01\nA=0: 0 | 1 | 1 | 0\nA=1: 1 | 0 | 0 | 1",
"BC: 00 | 11 | 10 | 01\nA=0: 0 | 1 | 1 | 0\nA=1: 1 | 0 | 0 | 1"]),
M(25,"2023 Q12","Consider the following logic circuit in which X indicates a two-input logic gate.\n[Figure: inputs A and B go to a NAND gate; its output goes into the two-input gate X (both X inputs from the same line); output of X is C]\nWhich of the following should X be so that when A = 0 and B = 1, the output C would be 0 ?\nI - a NAND gate\nII - a NOR gate\nIII - an XOR gate",["I only","I and II only","I and III only","II and III only","All I, II and III"],["I පමණි","I හා II පමණි","I හා III පමණි","II හා III පමණි","I, II සහ III සියල්ලම"]),
M(26,"2023 Q13","Which of the following is the simplified form of the Boolean expression X(X' + Y) ?",["X","Y","XY","X'Y","X + Y"]),
M(27,"2024 Q12","Which of the following expresses the output (F) of the given circuit?\n[Figure: X and Y (Y through a NOT gate) go to a NAND gate; its output and Z go to an OR gate giving F]",["(X + Y')Z","(X + Y')' + Z  [overbar over (X + Y') only]","((X + Y')Z)'  [overbar over (X + Y')]·Z as printed","XY' + Z","(XY)' + Z  [overbar over XY]"]),
M(28,"2024 Q13","Applying Double complement and De Morgan's laws to x' + yz results in,",["xy + z'","xy' + z","x'yz","(x(yz)')'  [overbar over the whole expression x(yz)']","x'y' + yz"]),
M(29,"2024 Q14","What is the most simple Boolean expression that can be obtained through the given Karnaugh map?\nxy:  00 | 01 | 11 | 10\nz=0:  0 | 1 | 1 | 1\nz=1:  0 | 1 | 1 | 0",["y","xz","xz'","x'z","y + xz'"]),
M(30,"2025 Q14","What is the most simple Boolean expression that can be obtained through the given Karnaugh map?\nxy:  00 | 01 | 11 | 10\nz=0:  1 | 0 | 0 | 1\nz=1:  1 | 0 | 1 | 1",["y'","y + x'z'","y' + xz","y' + xyz","yz + x'y"]),
M(31,"2025 Q13","Consider the following flip-flop:\n[Figure: two cross-coupled NOR gates. Input i1 goes to the upper NOR gate whose output is Q = 0; input i2 goes to the lower NOR gate whose output is Q' = 1; each output is fed back to an input of the other gate]\nWhich of the following statements will be true when i1 = 0 and i2 = 1?",[
"Q output will remain at 0 and Q' output will remain at 1.",
"Q output will change to 1 and Q' output will change to 0.",
"Q output will change to 1 and then to 0.",
"Q' output will change to 0 and then to 1.",
"Q output will remain at 0 while Q' output will also change to 0."],[
"Q ප්‍රතිදානය 0 ලෙසම පවතින අතර Q' ප්‍රතිදානය 1 ලෙසම පවතී.",
"Q ප්‍රතිදානය 1 ලෙස වෙනස්වන අතර Q' ප්‍රතිදානය 0 ලෙස වෙනස් වේ.",
"Q ප්‍රතිදානය 1 ලෙස වෙනස් වී ඉන්පසු 0 ලෙස වෙනස් වේ.",
"Q' ප්‍රතිදානය 0 ලෙස වෙනස් වී ඉන්පසු 1 ලෙස වෙනස් වේ.",
"Q ප්‍රතිදානය 0 ලෙසම පවතින අතර, Q' ප්‍රතිදානය ද 0 ලෙස වෙනස් වේ."]),
M(32,"2026 Q10","The diagram shows a two-input X-OR gate.\n[Figure: XOR gate with inputs A and B and output F]\nIf A=1, the output F is,",["1","0","A","B","B'"]),
M(33,"2026 Q11","The boolean expression AB + AB' + AC is equal to,",["A","B","C","A'","A + C"]),
]
note="(NOT/complement is written with a prime ', e.g. A' means A-bar.)\n"
for it in items:
    if any("'" in x for x in [it["q"]]+it["o"]): it["q"]=note+it["q"]
assert len(items)==33
for it in items: assert 4<=len(it["o"])<=5 and all(it["o"])
json.dump(items,open("D:/DevOps/aws-clf-c02-bridge/tools/transcribed/ictl-logic-mcq.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(len(items))
