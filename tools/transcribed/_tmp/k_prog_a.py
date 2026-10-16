Q = []
def add(d, q, qs=None):
    Q.append((d, q, qs))

add("2012 ESSAY3[a], 2012 ESSAY5", r"""1. (a) Explain the necessity of program translators in computer programming.
(b) Give two main features for each of the First-Generation and Second-Generation programming languages.
(c) Give three main flow control structures used in a structured programming language. Show how these flow control structures can be represented in a flow chart.
(d) The following Python program is intended to convert user given positive integers to their equivalent binary representations. The program should halt when the user inputs the value 0. The program has both syntactic and logical errors. The line numbers are not part of the program, but they are used to reference the lines.
1 x = int (input ("Enter an integer ->)
2 while x!=0:
3 bn = ""
4   while x > 1:
5      quotient = int(x/2)
6      remainder == x % 2
7      bn = bn + str(remainder);
8         x = quotient
9      bn = str(x) + bn
10   print ("Binary Number", bn)
11   x = int (input("Enter an integer ->)
(i) State the lines with syntactic errors and state the error.
(ii) Which lines of the program should be changed and state how they should be changed to obtain the desired results. (You are not allowed to add new lines or to delete existing lines.)
(2011 - Essay [5])

2. (a) (i) Describe how you would determine whether a given positive integer is odd or even.
(ii) Develop a flowchart to represent an algorithm, based on the method suggested in (i) above, to decide whether a given positive integer is odd or even.
(iii) Convert the flowchart you have obtained for the above (ii) into a pseudo code.
(2012 - S.Essay 3[a])

Consider the following Python program named example.py.
datasummary = {}
datakeys = []
def readdata():
   global datakeys, datasummary
   f1 = open('input.txt','r')
   line = f1.readline()
   while (line):
      data = line.strip().split(",")
      for dataitem in data:
        if dataitem in datasummary:
          datasummary [dataitem] += 1
        else:
          datasummary[dataitem] = 1
          datakeys = datakeys + [dataitem]
      line = f1.readline()
   f1.close()

def processdata():
   global datakeys
   for i in range(len(datakeys) - 1):
      for j in range(i+1, len(datakeys)):
         if(datakeys[i] > datakeys[j]):
           datakeys[i], datakeys[j] = datakeys[j], datakeys [i]

def printdata():
   global datakeys, datasummary
   f2 = open('output.txt', 'w')
   for key in datakeys:
      f2.write('{}-{}\n'.format(key,datasummary[key]))
   f2.close()

readdata()
processdata()
printdata()

(a) What are the data types of the variables datasummary and datakeys in the above program?
(b) Write a Python statement required to insert the program name as a comment at the beginning of the above program.
(c) What is the result of execution of the command open('input.txt','r') in the above program?
(d) Describe the main task of each of the functions readdata(), printdata() and processdata() in the above program.
(e) If the content of the file input.txt is as given below, what would be the content of the file output.txt after the execution of this program?
a,d,b,a,n
d,b,n,x,a
(2012 - Essay 5)""",
r"""1. (a) පරිගණක ක්‍රමලේඛයේදී පරිවර්තකවල (Translators) අවශ්‍යතාව පැහැදිලි කරන්න.
(b) පළමුවන පරම්පරාවේ (First-Generation) සහ දෙවන පරම්පරාවේ (Second-Generation) ක්‍රමලේඛ භාෂා එක එකක් සඳහා ප්‍රධාන ලක්ෂණ දෙකක් බැගින් දක්වන්න.
(c) ව්‍යුහගත ක්‍රමලේඛ භාෂාවක භාවිත වන ප්‍රධාන ගැලීම් පාලක ව්‍යුහ (Flow control structures) තුනක් දක්වන්න. මෙම ගැලීම් පාලක ව්‍යුහ, ගැලීම් සටහනක නිරූපණය කරන ලබන්නේ කෙසේදැයි දක්වන්න.
(d) පහත දැක්වෙන පයිතන් ක්‍රමලේඛය (Python program) පරිශීලක විසින් දෙනු ලබන ධන නිබිල, ඒවාට තුල්‍ය ද්වීමය නියෝජනවලට හැරවීම සඳහා නිර්මාණය කර ඇත. පරිශීලක විසින් 0 අගය ඇතුළත් කළ විට ක්‍රමලේඛය නැවතිය යුතුය. ක්‍රමලේඛයේ වාග්විති දෝෂ (Syntax errors) සහ තාර්කික දෝෂ (Logical errors) යන දෝෂවර්ග දෙකම ඇත. පේළි අංක, ක්‍රමලේඛයේ කොටසක් නොවන අතර ඒවා අදාළ පේළි යොමුව දක්වයි.
(i) වාග්විති දෝෂ සහිත පේළි නම් කර, ඒ එක් එකෙහි දෝෂ ද දක්වන්න.
(ii) අපේක්ෂිත ප්‍රතිඵලය ලබාගැනීම සඳහා, ක්‍රමලේඛයේ වෙනස් කළ යුතු පේළි සහ ඒවා වෙනස් කළ යුත්තේ කෙසේදැයි දක්වන්න. (ක්‍රමලේඛයට අලුතින් පේළි එකතුකිරීමට හෝ එහි පේළි ඉවත් කිරීමට හෝ ඔබට අවසර නැත.)

2. (a) (i) ඔබ, දී ඇති ධන නිබිලයක්, ඔත්තේ ද ඉරට්ටට ද යන්න තීරණය කරන්නේ කෙසේදැයි විස්තර කරන්න.
(ii) ඉහත (i) කොටසෙහි යෝජිත ක්‍රමය පාදක කර, දී ඇති ධන නිබිලයක්, ඔත්තේ ද ඉරට්ටට ද යන්න තීරණය කිරීම සඳහා වන ඇල්ගොරිතමයක් නිරූපණය කරන ගැලීම් සටහනක් ගොඩනගන්න.
(iii) ඉහත (ii) කොටසෙහි ගැලීම් සටහන ව්‍යාජ කේතයකට (pseudo code) හරවන්න.

පහත දැක්වෙන example.py පයිතන් ක්‍රමලේඛය සලකා බලන්න. (ක්‍රමලේඛය ඉහත පරිදි වේ.)
(a) ඉහත ක්‍රමලේඛයෙහි datasummary සහ datakeys යන විචල්‍යවල දත්ත ප්‍රරූප මොනවා ද?
(b) ඉහත ක්‍රමලේඛය ආරම්භයේදී, එහි නම, සටහනක් (comment) ලෙස ඇතුළත්කිරීම සඳහා පයිතන් ප්‍රකාශයක් ලියන්න.
(c) ඉහත ක්‍රමලේඛයෙහි open('input.txt','r') යන විධානය ක්‍රියාත්මක කිරීමෙන් ඇතිවන ප්‍රතිඵලය කුමක් ද?
(d) ඉහත ක්‍රමලේඛයෙහි readdata(), printdata() සහ processdata() යන එක් එක් ශ්‍රිතයෙහි (each of the functions) ප්‍රධාන කාර්යය විස්තර කරන්න.
(e) input.txt ගොනුවෙහි අන්තර්ගතය පහත දී ඇති පරිදි වේ නම්, මෙම ක්‍රමලේඛය ක්‍රියාත්මක වීමෙන් පසු output.txt ගොනුවෙහි අන්තර්ගතය කුමක් වේ ද?
a,d,b,a,n
d,b,n,x,a""")

add("2013 ESSAY4", r"""3. (a) Explain what is done by the Python interpreter when executing the following program. Your explanation should include the types assigned to variables and type conversions.
a = 4
b = 4.7
c = a + b
(b) Explain what will happen when the statements of following Python program are executed.
total = 0.0
x = float(input("Enter a number:"))
while x > 0:
   total = total + x
   x = float(input("Enter a number:"))
print(total)
(c) You are requested to write a Python program to find and display the maximum value of given 10 integers. The program should read integers one at a time.
(i) Propose an algorithm to solve the problem using a flow chart.
(ii) Write a Python program to implement your flow chart proposed in section c (i).
(2013 - Essay 4)""",
r"""3. (a) පහත සඳහන් ක්‍රමලේඛය ක්‍රියාත්මක වන විට පයිතන් අර්ථ වින්‍යාසකය (interpreter) මගින් කරනු ලබන කාර්යය පැහැදිලි කරන්න. විචල්‍ය (variables) සඳහා පවරනු ලැබූ ප්‍රරූප (types) හා ප්‍රරූප පරිවර්තනයන් ඔබේ පැහැදිලි කිරීම තුළ අඩංගු විය යුතුය.
a = 4
b = 4.7
c = a + b
(b) පහත සඳහන් පයිතන් ක්‍රමලේඛයේ ඇති වගන්ති ක්‍රියාත්මක කිරීමේ දී කුමක් සිදුවේ දැයි විස්තර කරන්න.
(ක්‍රමලේඛය ඉහත පරිදි වේ.)
(c) දෙන ලද නිබිල (integers) සංඛ්‍යා දහයක උපරිම අගය සොයා එය ප්‍රදර්ශනය කිරීම සඳහා පයිතන් ක්‍රමලේඛයක් ලිවීමට ඔබෙන් ඉල්ලීමක් කරනු ලැබේ. ක්‍රමලේඛයෙන් වරකට එක බැගින් නිබිලයන් කියවිය යුතු වේ.
(i) ඉහත ගැටළුව විසඳීම සඳහා ඇල්ගොරිතමයක් ගැලීම් සටහනක් භාවිත කරමින් යෝජනා කරන්න.
(ii) ඉහත c (i) මගින් යෝජනා කරනු ලැබූ ඔබේ ගැලීම් සටහන ස්ථාපිත කිරීම සඳහා පයිතන් ක්‍රමලේඛයක් ලියන්න.""")

add("2014 ESSAY4", r"""4. (a) Explain what is done by the Python interpreter when executing the following statements. You should state the types of the variables involved.
(i) x = input("Enter a number")
(ii) infile = open("myfile.txt","r")
(iii) a = "a,b,c".split(",")
(b) Factorial of a positive integer n is defined as n x (n-1) x (n-2) x ....... x 3 x 2 x 1.
(i) Propose an algorithm by using a flowchart to print the factorial of a given positive_integer n.
(ii) Write a Python function to implement your flowchart.
(2014 - Essay 4)""",
r"""4. (a) පයිතන් අර්ථවින්‍යාසකයක් (interpreter) මගින් පහත වගන්ති ක්‍රියාත්මක (execute) කරන විට සිදුවන්නේ කුමක්දැයි පැහැදිලි කරන්න. මේ සඳහා සම්බන්ධ විචල්‍යවල ප්‍රරූප (variable types) දැක්විය යුතු වේ.
(i) x = input("Enter a number")
(ii) infile = open("myfile.txt","r")
(iii) a = "a,b,c".split(",")
(b) n නම් ධන නිබිලයක ක්‍රමාරෝපිතය (factorial) අර්ථ දක්වනු ලබන්නේ n x (n-1) x (n-2) x ....... x 3 x 2 x 1 ලෙස ය.
(i) දී ඇති n නම් ධන නිබිලයක ක්‍රමාරෝපිතය මුද්‍රණය කිරීම සඳහා සුදුසු ඇල්ගොරිතමයක් ගැලීම් සටහනක් ඇසුරෙන් යෝජනා කරන්න.
(ii) ඔබේ ගැලීම් සටහන ස්ථාපනය කිරීම සඳහා පයිතන් ශ්‍රිතයක් (function) ලියා දක්වන්න.""")

add("2015 ESSAY4", r"""5. (a) Explain why compilers or interpreters are needed when using high level programming languages.
(b) Your teacher has requested you to write a Python program to record the marks obtained by students at the term test. Each student has sat for the same three papers and each mark was given as an integer value out of 100 marks. Each student is identified by a unique index member which is also an integer. You should record the marks of student in a text file named 'marks.txt' in the following format.
Index_no_1,mark_11,mark_12,mark_13
Index_no_2,mark_21,mark_22,mark_23
........................................
Where
Index_no_X : Index number of the Xth student; X = 1, ..., n
mark_XY : Marks obtained by the Xth student for the Yth paper; Y = 1,2,3
Index numbers and marks of the students should be entered through the keyboard, one item at a time and the program should be terminated when -1 is entered as the index number.
(i) Propose an algorithm by using a flowchart for the program.
(ii) Write a Python program to implement your flowchart.
(2015 - Essay 4)""",
r"""5. (a) ඉහළ මට්ටමේ ක්‍රමලේඛන භාෂා භාවිතයේ දී සම්පාදකයන් (compilers) හෝ අර්ථවින්‍යාසකයන් (interpreters) අවශ්‍ය වන්නේ ඇයි දැයි පැහැදිලි කරන්න.
(b) වාර විභාගයක දී ළමුන් ලබාගන්නා ලද ලකුණු වාර්තා කිරීම සඳහා පයිතන් ක්‍රමලේඛයක් ලියන ලෙස ඔබගේ ගුරුතුමා විසින් ඔබෙන් ඉල්ලීමක් කර තිබේ. සෑම සිසුවෙක්ම එකම ප්‍රශ්න පත්‍ර තුනකට පෙනී සිටි ඇති අතර සෑම ලකුණකම දී ඇත්තේ 100 න් වන අතර එය නිබිල අගයක් (integer value) වේ. සෑම සිසුවකුම අනන්‍ය සුචි අංකයක් (index number) මගින් හඳුනා ගන්නා අතර සුචි අංකය ද නිබිලයක් වේ. ඔබ විසින් පහත පෙන්වා දී ඇති ආකාරයට සිසුන්ගේ ලකුණු 'marks.txt' නමැති පාඨ ගොනුවේ (text file) වාර්තා කළ යුතු වේ.
Index_no_1,mark_11,mark_12,mark_13
Index_no_2,mark_21,mark_22,mark_23
........................................
මෙහි
Index_no_X : X වැනි සිසුවාගේ සුචි අංකය X = 1, ..., n
mark_XY : X වැනි සිසුවා Y ප්‍රශ්න පත්‍රයට ගත් ලකුණු සංඛ්‍යාව Y = 1, 2, 3
වරකට එක අයිතමය බැගින් යතුරු පුවරුව තුළින් සිසුන්ගේ සුචි අංක සහ ලකුණු ඇතුළත් කළ යුතු වේ. සුචි අංකය -1 ලෙස ඇතුළත් කළ විට ක්‍රමලේඛය නැවතිය යුතුය.
(i) ගැලීම් සටහනක් භාවිතයෙන් මෙම ක්‍රමලේඛය සඳහා ඇල්ගොරිතමයක් යෝජනා කරන්න.
(ii) ඔබගේ ගැලීම් සටහන ක්‍රියාත්මක කිරීම සඳහා පයිතන් ක්‍රමලේඛයක් ලියන්න.""")

add("2016 ESSAY4", r"""6. (a) Consider the following Python program:
#Print the sum of integers from 1 to 5 (including 1 and 5)
total = 0
i = 1
while (i <= 5):
        total = total + i
i = i + 1
print (total)
(i) What would be the output of the above program when executed? Justify your answer.
(ii) Modify and rewrite the above program, without increasing the number of statements, to compute the sum of integers from 1 to 10 (including 1 and 10).
(2016 - S.Essay [4(a)])

7. (a) A canteen of a school sells 10 different types of foods. These food types are placed in a shelf. Students can select foods while walking alongside the shelf and keep them on a tray. These trays are available at the entrance of the canteen. A student, after selecting the food, should proceed to the cashier with the food tray for the payment.
You are asked to develop a computer program to calculate the payment due for a food tray. For this purpose, each food type is given a unique integer from 1 to 10.
The integer value assigned for each food type and its unit price is shown in the following table.
Food type | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
Unit price (Rs) | 10.00 | 12.00 | 15.00 | 10.00 | 25.00 | 45.00 | 50.00 | 25.00 | 10.00 | 12.00
(i) State all the inputs required for the computer program and its expected output.
(ii) Draw a flowchart to represent the algorithm required to compute the payment due for a food tray.
(iii) Transform the above flowchart into a Python program.
(2016 - Essay 4)""",
r"""6. (a) පහත දැක්වෙන පයිතන් ක්‍රමලේඛය සලකන්න:
(ක්‍රමලේඛය ඉහත පරිදි වේ.)
(i) ඉහත ක්‍රමලේඛය ක්‍රියාත්මක කිරීමෙන් ලැබෙන ප්‍රතිදානය කුමක් විය හැකි දැයි ඔබගේ පිළිතුර සත්‍යාපනය කරන්න.
(ii) ඉහත ක්‍රමලේඛයේ ඇති ප්‍රකාශන සංඛ්‍යාව වැඩි නොකරමින් 1 සිට 10 දක්වා (1 සහ 10 ඇතුළුව) ඇති නිබිලවල (integers) එකතුව ගණනය කිරීමට හැකි වන පරිදි එම ක්‍රමලේඛය වෙනස් කොට ලියා දක්වන්න.

7. (a) පාසලක ආපනශාලාවක් විවිධ ආහාර වර්ග 10ක් අලෙවි කරයි. මෙම ආහාර වර්ග රාක්කයක අසුරා ඇත. සිසුන්ට රාක්කය අසලින් ඇවිදින ගමන් ආහාර වර්ග තෝරාගෙන බන්දේසියක තබා ගත හැකි ය. මෙම බන්දේසි ආපනශාලාවට ඇතුළුවන ස්ථානයේ තබා ඇත. ආහාර තෝරා ගැනීමෙන් පසු සිසුවකු මුදල් ගෙවීම සඳහා ආහාර බන්දේසියද රැගෙන මුදල් අයකැමි වෙත ළඟා විය යුතු ය.
ආහාර බන්දේසියකට ගෙවිය යුතු මුදල ගණනය කිරීම සඳහා පරිගණක ක්‍රමලේඛයක් සකස් කිරීමට ඔබට භාර කොට ඇත. මේ අරමුණ සඳහා සෑම ආහාර වර්ගයකටම 1 සිට 10 දක්වා වූ අනන්‍ය නිබිලයක් ලබා දී ඇත.
පහත දැක්වෙන වගුවෙහි එක් එක් ආහාර වර්ගයක් සඳහා ලබා දී ඇති අනන්‍ය නිබිලය සහ එහි ඒකක මිල දක්වා ඇත.
Food type | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10
Unit price (Rs) | 10.00 | 12.00 | 15.00 | 10.00 | 25.00 | 45.00 | 50.00 | 25.00 | 10.00 | 12.00
(i) පරිගණක ක්‍රමලේඛයකට අවශ්‍ය වන ආදාන හා එයින් බලාපොරොත්තු වන ප්‍රතිදානයන් සඳහන් කරන්න.
(ii) ආහාර බන්දේසියකට ගෙවිය යුතු මුදල ගණනය කිරීම සඳහා අවශ්‍ය වන ඇල්ගොරිතමය නිරූපණය කිරීම සඳහා ගැලීම් සටහනක් අඳින්න.
(iii) ඉහත ගැලීම් සටහන පයිතන් ක්‍රමලේඛයකට පරිවර්තනය කරන්න.""")

add("2017 ESSAY4", r"""8. The consumption of electricity at houses is charged based on the number of units consumed. The first 64 units are charged at Rs.5.00 per unit, and the rest at Rs.10.00 per unit.
(a) Draw a flowchart to represent an algorithm that can be used to compute the total amount to be charged from a householder when the household number and present and the previous readings of the electricity meter are given.
(b) Encode the algorithm given in the (a) above in Python programming language. State all valid assumptions, if any.
(c) Develop a function in Python to write household number, meter readings and the total amount to be charged at the end of an existing text file named "deb.txt".
(2017 - Essay 4)""",
r"""8. ගෘහස්ථ විදුලි පරිභෝජනය සඳහා ගෙවිය යුතු මුදල පරිභෝජනය කරන ලද විදුලි ඒකක ගණන මත පදනම් වේ. පළමු ඒකක 64 සඳහා ඒකකයකට රු. 5.00 බැගින් දල ඉතිරි ඒකක සඳහා ඒකකයකට රු. 10.00 බැගින් ද අයකරනු ලැබේ.
(a) ගෘහස්ථයේ අංකය, පෙර හා වර්තමාන විදුලි මනු කියවීම් දුන් විට ගෘහස්ථ, හිමිකරුගෙන් අයවිය යුතු මුළු මුදල ගණනය කිරීමට භාවිත කළ හැකි ඇල්ගොරිතමයක් නිරූපණය කිරීම සඳහා ගැලීම් සටහනක් අඳින්න.
(b) ඉහත (a) හි ඉදිරිපත් කරන ලද ඇල්ගොරිතමය Python ක්‍රමලේඛන භාෂාවෙන් කේතනය කරන්න. වලංගු උපකල්පන ඇත්නම්, ඒවා සියල්ල සඳහන් කරන්න.
(c) ගෘහස්ථ අංකය, විදුලි මනු කියවීම් සහ අය කළ යුතු මුළු මුදලද, පවතින "deb.txt" නම් වූ පාඨ ගොනුවක අගට ලිවීමට අවශ්‍ය Python ශ්‍රිතයක් ගොඩනගන්න.""")

add("2018 ESSAY4", r"""9. (a) Assume an input which contains a sequence of positive numbers. The sequence has at most 100 numbers. If the input sequence has n numbers where n < 100, then the end of the sequence is marked by making (n+1)th number -1.
For e.g., the following input sequence has 8 positive numbers, where the 9th input which is -1 marks the end.
23  12  54  76  89  22  44  65  -1
Draw a flowchart that represents an algorithm to output the largest number in a given sequence of n positive numbers as described above.
(b) Consider the flowchart given below. The algorithm in the flowchart takes two inputs, the first input L is a list of numbers, the second input K is a given number.
[Figure: flowchart] Start -> Input List L, Input K -> n = Length of L, i = 0 -> decision "is L[i]=K ?": Yes -> Output "True" -> Stop; No -> i = i + 1 -> decision "is i < n ?": Yes -> back to the decision "is L[i]=K ?"; No -> Output "False" -> Stop.
(i) What would be the output if the first input L was 23, 45, 32, 11, 67, 39, 92, 51, 74, 89 and the second input K was 38?
(ii) Briefly explain the aim of this algorithm.
(iii) Develop a Python program to implement the algorithm in the flowchart.
(2018 - Essay 4)""",
r"""9. (a) ධන සංඛ්‍යා අනුක්‍රමයක් ඇති ආදානයක් සලකන්න. අනුක්‍රමයට උපරිම වශයෙන් සංඛ්‍යා 100ක් තිබිය හැකි ය. n < 100 ලෙස අනුක්‍රමයට සංඛ්‍යා n තිබේ නම්, (n+1) වන සංඛ්‍යාව -1 ලෙස සලකුණු කිරීමෙන් අනුක්‍රමයේ අවසානය දැක්වේ.
උදාහරණයක් ලෙස පහත දැක්වෙන ආදාන අනුක්‍රමයට ධන සංඛ්‍යා 8ක් ඇති අතර 9 වන ආදානය වන -1 මගින් අවසානය සනිටුහන් කෙරේ.
23  12  54  76  89  22  44  65  -1
ඉහත විස්තර කරන ආකාරයේ ධන සංඛ්‍යා n ඇති අනුක්‍රමයක විශාලතම සංඛ්‍යාව ප්‍රතිදානය කිරීම සඳහා ඇල්ගොරිතමයක් ගැලීම් සටහනක් මගින් නිරූපණය කරන්න.
(b) දී ඇති ගැලීම් සටහන සලකන්න. ගැලීම් සටහනෙහි දැක්වෙන ඇල්ගොරිතමය ආදාන දෙකක් ලබාගන්නා අතර පළමු ආදානය වන L, සංඛ්‍යා ලැයිස්තුවක් ද, දෙවන ආදානය K, දෙන ලද සංඛ්‍යාවක් ද වේ.
(i) පළමු ආදානය (L) 23, 45, 32, 11, 67, 39, 92, 51, 74, 89 සහ දෙවන ආදානය (K) 38 ද වූයේ නම්, ප්‍රතිදානය කුමක් ද?
(ii) මෙම ඇල්ගොරිතමයෙහි අරමුණ කෙටියෙන් පැහැදිලි කරන්න.
(iii) ගැලීම් සටහනේ ඇති ඇල්ගොරිතමය ක්‍රියාත්මක කිරීම සඳහා පයිතන් කේතයක් ගොඩනගන්න.""")

add("2019 ESSAY2[b]", r"""10. Consider the following Python program:
x = 0
n = int (input ())
while (n>0):
      if n>x:
            x = n
      n = int (input ())
print (x)
(i) Write the output of the program if the input is 4 6 3 2 8 -1.
(ii) What is the purpose of this program?
(2019 - S.Essay 2 [b])""",
r"""10. පහත දැක්වෙන පයිතන් ක්‍රමලේඛය සලකන්න.
(ක්‍රමලේඛය ඉහත පරිදි වේ.)
(i) ආදානය 4 6 3 2 8 -1 වන්නේ නම් ක්‍රමලේඛයෙහි ප්‍රතිදානය ලියා දක්වන්න.
(ii) මෙම ක්‍රමලේඛයෙහි අරමුණ කුමක් ද?""")

add("2019 ESSAY4", r"""11. (a) The ICT teacher in a school needs to process the marks obtained by all the students in a class for the ICT subject and compute the average mark for the class. Construct a flow chart to express an algorithm for this purpose. Assume that the first input is the number of students in the class, n. Next, the marks of n students will be input one-by-one.
(b) Consider the flow chart given below. Note that x%2 represents (x mod 2).
[Figure: flowchart] Start -> input n -> a = 0 -> decision "Is n <= 0 ?": Yes -> Output a -> Stop; No -> input x -> decision "Is x%2 = 0 ?": Yes -> a = a + 1 -> n = n - 1; No -> n = n - 1 -> back to the decision "Is n <= 0 ?".
(i) What would be the output if the first input (n) was 6 and the next inputs were 3, 6, 4, 12, 11, 9?
(ii) What is the purpose of this algorithm?
(iii) Develop a Python program to implement the algorithm expressed by the flow chart
(2019 - Essay 4)""",
r"""11. (a) පාසලක තොරතුරු හා සන්නිවේදන තාක්ෂණය (ICT) භාර ආචාර්‍යවරයා පංතියේ සියලු ම සිසුන් ICT විෂයට ලබාගත් ලකුණු සැකසීමට අවශ්‍යව ඇති අතර පංතියේ සාමාන්‍ය ලකුණු ගණනය කළ යුතුව ඇත. මෙම කාර්යයට අදාළ ඇල්ගොරිතමයක් ප්‍රකාශන වන ගැලීම් සටහනක් ගොඩනගන්න. පළමු ආදානය පංතියේ සිටින මුළු සිසුන් සංඛ්‍යාව බව උපකල්පනය කරන්න. ඉන්පසු n සිසුන්ගේ ලකුණු එකින් එක ආදානය කරනු ලැබේ.
(b) පහත දක්වා ඇති ගැලීම් සටහන සලකන්න. එහි x % 2 මගින් x mod 2 නිරූපණය කෙරේ.
(i) පළමු ආදානය (n) 6 නම් සහ ඉන්පසු ආදාන 3, 6, 4, 12, 11, 9 නම් ප්‍රතිදානය කුමක් වන්නේ ද?
(ii) මෙම ඇල්ගොරිතමයෙහි අරමුණ කුමක් ද?
(iii) ගැලීම් සටහන මගින් ප්‍රකාශවන ඇල්ගොරිතමය ක්‍රියාත්මක කිරීම සඳහා පයිතන් ක්‍රමලේඛයක් ගොඩනගන්න.""")

add("2020 ESSAY2[b]", r"""12. Consider the following Python program:
L1 = [int(x) for x in input().split()]
L2 = [int(x) for x in input().split()]
L3 = [ ]
for i in L1:
   for j in L2:
      if (i= =j) and (i not in L3):
            L3.append(i)
L3.sort()
print(L3)
(i) Write the output of the program if the first input (that creates L1) is "7 4 1 2 2 8" and the second input (that creates L2) is "8 2 4 5 6"?
(ii) What is the purpose of this program?
(2020 - S.Essay 2[b])""",
r"""12. පහත දැක්වෙන පයිතන් ක්‍රමලේඛය සලකන්න.
(ක්‍රමලේඛය ඉහත පරිදි වේ.)
(i) (L1 නිර්මාණය කෙරෙන) පළමු ආදානය "7 4 1 2 2 8" සහ (L2 නිර්මාණය කෙරෙන) දෙවන ආදානය "8 2 4 5 6" නම් ක්‍රමලේඛයෙහි ප්‍රතිදානය ලියා දක්වන්න.
(ii) මෙම ක්‍රමලේඛයෙහි අරමුණ කුමක් ද?""")

add("2020 ESSAY4", r"""13. (a) You are given two positive integers N1 and N2 as inputs (assume NI < N2) and you have to output the list of even numbers between N1 and N2. Construct a flowchart or a pseudo code to express an algorithm for this purpose.
(b) Consider the flowchart given below. Assume that L is a list of positive integers, K is a positive integer and every element in L is less than M, which is a large integer.
[Figure: flowchart] Start -> input L, K -> N = length of L -> X = M -> a = 0 -> decision "Is a < N ?": No -> output X -> Stop; Yes -> decision "Is L[a] > K ?": No -> a = a + 1; Yes -> decision "Is L[a] < X ?": No -> a = a + 1; Yes -> X = L[a] -> a = a + 1 -> back to the decision "Is a < N ?".
(i) What would be the output if the first input L was 2,4,7,9,3,5 and the next input K was 5?
(ii) What is the purpose of this algorithm?
(iii) Develop a Python program to implement the algorithm expressed by the flowchart.
(2020 - Essay 4)""",
r"""13. (a) ඔබට N1 සහ N2 නම් ධන නිබිල සංඛ්‍යා දෙකක් ආදාන ලෙස ලබා දී ඇති අතර (N1 < N2 යැයි උපකල්පනය කරන්න) ඔබ විසින් N1 සහ N2 අතර ඇති ඉරට්ටේ සංඛ්‍යා ලැයිස්තුවක් ප්‍රතිදානය කළ යුතු වේ. මෙම කාර්යයට, අදාළ ඇල්ගොරිතමයක් ප්‍රකාශ වන ගැලීම් සටහනක් හෝ ව්‍යාජ කේතයක් හෝ ගොඩනගන්න.
(b) පහත දැක්වෙන ගැලීම් සටහන සලකන්න. L යනු ධන නිබිල ලැයිස්තුවක් බවත්, K යනු ධන නිබිලයක් බවත්, L හි සෑම සංඛ්‍යාවක්ම M නම් වන විශාල නිබිලයකට වඩා අඩු බවත් උපකල්පනය කරන්න.
(i) පළමු ආදානය වන L හි අගයන් 2, 4, 7, 9, 3, 5 සහ දෙවන ආදානය වන K හි අගය 5 වූයේ නම්, ප්‍රතිදානය කුමක් වන්නේ ද?
(ii) මෙම ඇල්ගොරිතමයෙහි අරමුණ කුමක් ද?
(iii) ගැලීම් සටහනෙහි ප්‍රකාශ වන ඇල්ගොරිතමය ක්‍රියාත්මක කිරීම සඳහා පයිතන් ක්‍රමලේඛයක් ගොඩනගන්න.""")

add("2021 ESSAY3", r"""14. (a) A flowchart is to be drawn for an algorithm to calculate and output the areas of triangles. The base and height of each triangle are given as inputs.
Note: Area of triangle = 1/2 x base x height
The algorithm should stop when an input is less than or equal to zero.
Complete the flowchart by writing the required content for the four components left blank.
[Figure: flowchart with four blank components] Start -> (blank input/output parallelogram) -> decision (blank diamond): Yes -> (blank process box) -> (blank parallelogram) -> loops back to the decision/first parallelogram; No -> Stop.
(b) Complete the four (4) blanks (indicated by ......) in the following Python program to calculate the factorial of an integer.
Note: The factorial of a positive integer is defined as the product of that integer and all the integers below it. e.g., factorial of 4 is equal to 1 x 2 x 3 x 4 = 24. The factorial of 0 is defined as 1.
# Get input from user
.................... = int(input("Enter a number:"))
factorial = 1
if num < 0:
      print("Factorial is not defined for negative numbers!")
elif ................................... :
      print("The factorial of 0 is 1")
else:
      for i in range(1,num + 1):
            ...............................
print ("The factorial of ",num,"is",...............................)
(c) Consider the following Python program:
lower = 2
upper = 5

for num in range(lower, upper + 1):
      flag = 1
      if num > 1:
            for i in range(2, num):
                  if (num % i) == 0:
                        flag = 0
                        break
      if flag == 1:
            print(num)
Write the output of the above program.
(2021 - S.Essay 3)""",
r"""14. (a) ත්‍රිකෝණවල වර්ගඵල ගණනය කර ප්‍රතිදානය කරන ඇල්ගොරිතමයක් සඳහා ගැලීම් සටහනක් ඇඳීමට අවශ්‍ය ය. එක් එක් ත්‍රිකෝණයේ ආධාරකයේ දිග සහ උස ආදාන ලෙස ලැබේ.
සටහන: ත්‍රිකෝණයක වර්ගඵලය = 1/2 x ආධාරකයේ දිග x උස
යම් ආදානයක් 0 ට සමාන හෝ අඩු වූ විට හෝ ඇල්ගොරිතමය නතර විය යුතු ය.
හිස්ව දක්වා ඇති සංරචක හතර සඳහා අවශ්‍ය අන්තර්ගතයන් ලියා, ගැලීම් සටහන සම්පූර්ණ කරන්න.
(b) නිබිලයක ක්‍රමාරෝපිතය (factorial) ගණනය කිරීමට අදාළ පහත පයිතන් කේතයේ හිස්තැන් හතර (...... වලින් දැක්වෙන) සම්පූර්ණ කරන්න.
සටහන: ධන නිබිලයක ක්‍රමාරෝපිතය යනු එම නිබිලයේ හා ඊට අඩු සියලු නිබිලවල ගුණිතයයි. උදා: 4 හි ක්‍රමාරෝපිතය 1 x 2 x 3 x 4 = 24 ට සමාන වේ. ඊට අමතරව 0 හි ක්‍රමාරෝපිතය 1 ලෙස අර්ථ දැක්වේ.
(කේතය ඉහත පරිදි වේ.)
(c) පහත පයිතන් ක්‍රමලේඛය සලකන්න.
(ක්‍රමලේඛය ඉහත පරිදි වේ.)
ඉහත ක්‍රමලේඛයේ ප්‍රතිදානය ලියා දක්වන්න.""")

add("2021 ESSAY4", r"""15. (a) Suppose the ages (in years) of n(n > 1) students in a school are in a list L. Assuming the list L and an integer k are inputs, express an algorithm using either a flowchart or pseudo-code to compute & output the average age of students in L whose age is less than k years.
(b) Consider the algorithm expressed by the flowchart. L1 and L2 are non-empty lists of integers. Each of L1 and L2 has unique elements (no duplicates). But there can be elements that are in both L1 and L2. The notation L[x] denotes the element at Index x of a list L. If there are N elements in list L, then the indices are from 0, 1, 2, ... to (N-1).
[Figure: flowchart] Start -> Input lists L1,L2 -> N1 = number of items in L1; N2 = number of items in L2; count = 0; i1 = 0 -> i2 = 0 -> decision "Is L1[i1] = L2[i2]?": Yes -> count = count + 1 -> i2 = i2 + 1; No -> i2 = i2 + 1 -> decision "Is i2 < N2?": Yes -> back to the decision "Is L1[i1] = L2[i2]?"; No -> i1 = i1 + 1 -> decision "Is i1 < N1?": Yes -> back to "i2 = 0"; No -> Output count -> Stop.
(i) What would be the output if L1 = 2, 4, 7, 9, 3, 5 and L2=1, 3, 8, 9, 6, 5, 7?
(ii) What is the purpose of this algorithm?
(iii) Develop a Python program to implement the algorithm expressed by the flowchart.
(2021 - Essay 4)""",
r"""15. (a) පාසලක සිසුන් n දෙනෙකුගේ (n > 1) වයස් (අවුරුදු ගණනින්) L නම් වූ ලැයිස්තුවක ඇතැයි සිතන්න. L ලැයිස්තුව සහ k නම් නිබිලයක් ආදාන යැයි උපකල්පනය කර, L ලැයිස්තුවේ ඇති, අවුරුදු k ට අඩු වයස ඇති සිසුන්ගේ සාමාන්‍ය (average) වයස ගණනය කර ප්‍රතිදානය කිරීමට ඇල්ගොරිතමයක් ගැලීම් සටහනක් හෝ ව්‍යාජ කේතයක් හෝ මගින් ඉදිරිපත් කරන්න.
(b) පහත දැක්වෙන ගැලීම් සටහනෙන් ඉදිරිපත් කෙරෙන ඇල්ගොරිතමය සලකන්න. L1 සහ L2 යනු ශූන්‍ය නොවන නිබිල ලැයිස්තු වේ. එම එක් එක් ලැයිස්තුවේ ඇත්තේ අනන්‍ය (එක නිබිලයක් එකවරක් පමණක් ඇති) අයිතමය. එහෙත් L1 සහ L2 ලැයිස්තු දෙකේම යම් නිබිලයන් තිබිය හැක. L[x] සංකේතනය මගින් L ලැයිස්තුවේ x නම් වූ දර්ශකයේ (index) ඇති අයිතමය දක්වයි. L ලැයිස්තුවේ අයිතම N ගණනක් ඇතිනම්, දර්ශකයන් 0, 1, 2, ... සිට (N-1) තෙක් වේ.
(i) L1 = 2, 4, 7, 9, 3, 5 සහ L2 = 1, 3, 8, 9, 6, 5, 7 වේ නම්, ප්‍රතිදානය කුමක් වේ ද?
(ii) මෙම ඇල්ගොරිතමයෙහි අරමුණ කුමක් ද?
(iii) ගැලීම් සටහනෙහි ප්‍රකාශ වන ඇල්ගොරිතමය ක්‍රියාත්මක කිරීම සඳහා පයිතන් ක්‍රමලේඛයක් ගොඩනගන්න.""")

add("2022 ESSAY3", r"""16. (a) A flowchart is to be drawn for an algorithm to calculate and output the area of a circle. The radius of the circle is given as an input.
Note: Area of a circle = 3.14 x Radius x Radius
The algorithm should not calculate the area if the input is a negative number.
Complete the flowchart by writing the required content for the four (4) components left blank.
[Figure: flowchart with four blank components] Start -> (blank input parallelogram) -> (blank decision diamond): No -> End; Yes -> (blank process box) -> (blank output parallelogram) -> End.
(b) What is the output of the following Python code?
S = "Advanced level"
S1 = " "
for c in S:
     if c in ("a" , "e" , "i" , "o" , "u"):
         pass
     else:
         S1 = S1 + c
print (S1)
(c) What code line(s) in part (b) is/are to be removed to get 'aeee' as the output?
(d) Fill in the blank spaces of the following Python code assuming that the purpose of the code is to copy the content of a text file (A) to another text file (B).
A = input("Enter the name of text file A")
B = input("Enter the name of text file B")
f1 = ................... (A, ...................)
f2 = ................... (B, ...................)
for line in ................... :
    f2.write (...................)
f1. ...................
f2. ...................
(2022 - S.Essay 3)""",
r"""16. (a) වෘත්තයක වර්ගඵලය ගණනය කිරීමට සහ ප්‍රතිදානය කිරීම සඳහා වූ ඇල්ගොරිතමයක් (algorithm) වෙනුවෙන් ගැලීම් සටහනක් ඇඳීමට අවශ්‍ය වේ. වෘත්තයේ අරය (input) ලෙස ලබාදේ.
සටහන: වෘත්තයක වර්ගඵලය = 3.14 x අරය x අරය
ආදානය ඍණ සංඛ්‍යාවක් නම් ඇල්ගොරිතමය වර්ගඵලය ගණනය නොකළ යුතු ය.
හිස්ව ඇති අංග හතර සඳහා නියමිත අන්තර්ගතයන් ලියමින් ගැලීම් සටහන සම්පූර්ණ කරන්න.
(b) පහත පයිතන් කේතයේ ප්‍රතිදානය කුමක් ද?
(c) ප්‍රතිදානය ලෙස 'aeee' ලබාගැනීමට ඉහත (b) කොටසේ ඉවත් කළ යුතු කේත පේළි(ය) කුමක් ද?
(d) පාඨ ගොනුවක (text file) [A] අන්තර්ගතය තවත් පාඨ ගොනුවකට [B] පිටපත් කිරීම කේතයේ අරමුණු යැයි උපකල්පනය කරමින් පහත සඳහන් පයිතන් කේතයේ හිස්තැන් පුරවන්න.
(කේතය ඉහත පරිදි වේ.)""")

add("2022 ESSAY8", r"""17. (a) (i) What is the output of the following python script if 1002 is given as the input?
A = int(input("Enter a number:"))
B = 0
while(A > 0):
      C = A % 10
      B = B + C
      A = A // 10 # // is integer division
print(B)
(ii) What would be the modification required to the B = B + C code line of the above code if the reverse of a given positive number is to be printed? (Example: if the input is 1234, the output should be 4321)
(b) Assume that your class is having a party, and each student is asked to bring one food item. The class teacher has decided to make the party interesting by introducing one rule: the first and last letters of the name of the food item must match with the first and last letters of the student name.
For example, percy is allowed to bring potato curry and prageeth is allowed to bring pepper fish.
Write a Python function called Party() that takes the student name and the name of the food item as parameters. The function should return True or False to indicate whether the student is allowed to bring the food item to the party or not.
Example:
Party ("percy", "potato curry") should return True
Party ("fareena", "fried rice") should return False
Note: You can assume that student name and food item name are always lowercase strings and have at least two letters. There may be hyphens and spaces in the names, but these will not appear at the beginning or end of the string. The names will not contain numerals.
(c) Write down the most suitable statements for labels to in the flowchart given below which is drawn to calculate the factorial of a given positive Integer.
[Figure: flowchart] (A) terminator (start) -> (B) input parallelogram -> (C) process box -> (D) decision diamond: one branch -> (E) process box -> (F) process box -> loops back to (D); other branch -> (G) output parallelogram -> (H) terminator (stop).
(i) The factorial of a positive integer is defined as the product of that integer and all the integers below it. E.g. factorial of 5 is 5x4x3x2x1 = 120. The factorial of 0 is defined as 1.
(ii) A process box in this flowchart may contain one or more statements.
(2022 - Essay 8)""",
r"""17. (a) (i) ආදානය ලෙස 1002 ලබා දුන් විට පහත දැක්වෙන පයිතන් කේතයේ ප්‍රතිදානය කුමක් වේ ද?
(කේතය ඉහත පරිදි වේ.)
(ii) දෙන ලද ධන සංඛ්‍යාවක ප්‍රතිවර්තනය (reverse) ප්‍රතිදානයක් කර ගැනීමට, ඉහත පයිතන් කේතයේ B = B + C පේළිය කෙලෙස වෙනස් විය යුද ද? (උදා: ආදානය 1234 වූ විට, ප්‍රතිදානය 4321 විය යුතු ය)
(b) ඔබගේ පන්තියේ සාදයක් පැවැත්වෙන බවත්, ඊට එක් එක් ශිෂ්‍යයාට එක් ආහාර වර්ගයක් බැගින් රැගෙන එන ලෙසට දන්වා ඇති බවත් සලකන්න. එය වඩාත් රසවත් කිරීමට ගුරුතුමිය නියමයක් හඳුන්වා දෙයි, එනම්, ශිෂ්‍යයා ගෙන එන ආහාර වර්ගයේ නමේ පළමු සහ අවසන් ඉංග්‍රීසි අක්ෂරවලට සමාන විය යුතු බවයි.
උදා: percy ශිෂ්‍යයාට potato curry ගෙන ආ හැකි අතර prageeth ශිෂ්‍යයාට pepper fish රැගෙන ඒමට අවසර ලැබේ.
ඉහත සන්දර්භය සඳහා භාවිත කළ ශිෂ්‍යයාගේ නම සහ ආහාර වර්ගයේ නම පරාමිතීන් (parameters) ලෙස ලබාගන්නා Party() නම් වූ Python ශ්‍රිතයක් ලියා දක්වන්න. ශිෂ්‍යයාට සාදයට ආහාර වර්ගය රැගෙන ඒමට අවසර තිබේද නැතිද යන්න පෙන්වීමට ශ්‍රිතය පිළිවෙළින් True හෝ False හෝ ප්‍රතිදානය කළ යුතු ය.
උදා:
Party("percy", "potato curry") විට True ප්‍රතිදානය විය යුතු ය.
Party("fareena", "fried rice") විට False ප්‍රතිදානය විය යුතු ය.
සටහන: ශිෂ්‍යයාගේ නම සහ ආහාර වර්ගයේ නම සැමවිටම කුඩා අකුරු (කැපිටල් නොවන), සහිත අක්ෂර වැල් (strings) වන බවත් ඒවායේ අවම වශයෙන් අක්ෂර දෙකක්වත් ඇති බවත් ඔබට උපකල්පනය කළ හැක. ඒවායේ කෙටිරා (-) සහ අන්තර (space) තිබිය හැකි නමුදු ඒවා අක්ෂර වැලේ පළමු සහ අවසන් අක්ෂර ලෙස නොපවතියි. නම්වල ඉලක්කම් අන්තර්ගත නොවේ.
(c) දෙන ලද ධන නිබිලයක ක්‍රමාරෝපිතය (factorial) ගණනය කිරීමට ඇඳ ඇති පහත දැක්වෙන ගැලීම් සටහනේ (A) සිට (H) දක්වා ඇති ලේබල සඳහා වඩාත්ම ගැළපෙන ප්‍රකාශන ලියා දක්වන්න.
(i) ධන නිබිලයක ක්‍රමාරෝපිතය යනු එම නිබිලයේ හා ඊට අඩු සියලු නිබිලවල ගුණිතයයි. උදා: 5 හි ක්‍රමාරෝපිතය 5x4x3x2x1 = 120 වේ. ඊට අමතරව, 0 හි ක්‍රමාරෝපිතය 1 ලෙස අර්ථ දැක්වේ.
(ii) මෙම ගැලීම් සටහනේ එක් ක්‍රියාවලි කොටුවක (process box) ප්‍රකාශන එකක් හෝ ඊට වැඩි ගණනක් හෝ තිබිය හැකි ය.""")

add("2023 ESSAY3", r"""18. (a) Write down the most suitable replacements for labels to in the following flowchart which is drawn to calculate and display sum of first ten even numbers.
[Figure: flowchart] Start -> sum = 0 -> count = 0 -> decision "Is count even?": branch (A) [arrow back to the join/loop] and branch (B) -> process box (C) -> joins -> count = count +1 -> (D) loop-back arrow -> decision (E): (F) exit branch -> output (G) -> End.
(A): ................................................
(B): ................................................
(C): ................................................
(D): ................................................
(E): ................................................
(F): ................................................
(G): ................................................
(b) (i) What is the output of the following Python code?
def func(n):
   MyNumber=[ ]
   for i in range(4,n+1):
      if i%2==0:
         MyNumber.append(i)
   print (MyNumber)
func(30)
(ii) Write down the output in the above Python code when the condition if i%2==0: is changed to if i%2 != 0:
(b) Write down the replacements for the labels of the following Python code which has been written to find the Largest of a set of integers.
def findlargest(myList):
      largest = (A)
      for i in (B)  :
            if i> (C)
                  largest = (D)
      print("largest value is", (E)  )
list1=[4,6,24,12,8,94,22]
findlargest ( (F) )
(A): ................................................
(B): ................................................
(C): ................................................
(D): ................................................
(E): ................................................
(F): ................................................
(2023 - S.Essay 3)""",
r"""18. (a) පළමු ඉරට්ටේ සංඛ්‍යා දහයේ එකතුව ගණනය කර ප්‍රදර්ශනය කිරීම සඳහා ඇඳ ඇති පහත ගැලීම් සටහනේ (A) සිට (G) තෙක් ලේබල සඳහා වඩාත් සුදුසු ආදේශක ලියා දක්වන්න.
(A): ................................................
(B): ................................................
(C): ................................................
(D): ................................................
(E): ................................................
(F): ................................................
(G): ................................................
(b) (i) පහත පයිතන් කේතයේ ප්‍රතිදානය කුමක් ද?
(ii) ඉහත පයිතන් කේතයේ if i%2==0: කොන්දේසිය if i%2 != 0: ලෙස වෙනස් කළ විට ප්‍රතිදානය ලියා දක්වන්න.
(b) නිබිල සමූහයක විශාලතම නිබිලය සෙවීමට ලියා ඇති පහත පයිතන් කේතයේ ලේබල සඳහා ආදේශක ලියා දක්වන්න.
(A): ................................................
(B): ................................................
(C): ................................................
(D): ................................................
(E): ................................................
(F): ................................................""")

add("2023 ESSAY8", r"""19. (a) Write the output of the Python code given in Figure 8.1.
def function1(str):
    newstr=  ""
    for character in str:
        if character in 'aeiouAEIOU':
            newstr+='*'
        else:
            newstr+=character
    return newstr
str1="LibrAry"
str2=function1(str1)
print(str2)
Figure 8.1
(b) The function in Figure 8.2 uses the bubblesort algorithm to sort a given list of numbers into ascending order. Write down the suitable replacements for the labels P-U to complete the code.
def bubblesort(nList):
    for pnumber in range(P,Q,R):
    S:
            if nList[i] > nList[i+1]
                temp = nList[i]
                T
                U
Figure 8.2
(c) An estate owner wants a program to determine the minimum currency note combination needed to make the pay of each employee. (E.g., Rs. 40,000 should be paid using eight notes of Rs.5000 and not four hundred notes of Rs. 100). The program should also output the currency requirement for all employees. The program should use the employees.txt file which contains employee pay details. Each line in it contains an employee's name and net pay. A Python program written for this purpose is shown in Figure 8.3. A sample employees.txt file and the program's output for that file are shown in Figure 8.4.
(i) Write down the suitable replacements for the ten labels A-J in program given in Figure 8.3.
#currency notes used in Sri Lanka
notes = [5000,1000,500,100,50,20]
#total notes required from each currency note type
totals = [0,0,0,0,0,0]

file = A(employees.txt',r')

while True:
      required = [0,0,0,0,0,0]
      # notes required for employee
      line = file.readline()
      if B line:
         C

      empDetails = line.spli()
      netpay = int(foar(D))
      If netpay < 0:
         continue

      print("\n")
      print(empDetails[0],"Net pay =",netpay)
      topay = netpay
      i=0
      while topay > 0:
         required[i] = E
         totals[i] = totals[i] + F
         topay = G
         H
      #print employee netpay breakdown
      for i in range(0, len(required)):
         print("Rs.",notes[i],":",I)
      J
print("\nTOTAL REQUIREMENT:")
for i in range(0, len(totals)):
    print("Rs.",notes[i],":",totals[i])
Figure 8.3
Example 'employees.txt' file:
Raj 40120
Niranjala 51670
Program's output for that file:
Raj Net pay=40120
Rs. 5000 : 8
Rs. 1000 : 0
Rs. 500 : 0
Rs. 100 : 1
Rs. 50 : 0
Rs. 20 : 1

Niranjala Net pay=51670
Rs. 5000 : 10
Rs. 1000 : 1
Rs. 500 : 1
Rs. 100 : 1
Rs. 50 : 1
Rs. 20 : 1

TOTAL REQUIREMENT:
Rs. 5000 : 18
Rs. 1000 : 1
Rs. 500 : 1
Rs. 100 : 2
Rs. 50 : 1
Rs. 20 : 2
Figure 8.4
(ii) The net pay of employees in this estate, does not contain cents. However, what practical problem with respect to the net pay inputs exists in this code? What modifications will you do to fix that problem?
(2023 - Essay 8)""",
r"""19. (a) රූපය 8.1 හි දැක්වෙන පයිතන් කේතයේ ප්‍රතිදානය ලියා දක්වන්න.
(b) රූපය 8.2 හි දැක්වෙන පයිතන් ශ්‍රිතය, දෙන ලද අංක ලැයිස්තුවක් ආරෝහණ ක්‍රමයට සැකසීමට බුබුළු තේරීම් (bubble sort) ඇල්ගොරිතමය භාවිත කරයි. කේතය සම්පූර්ණ කිරීම සඳහා P - U ලේබලවලට සුදුසු ආදේශක ලියා දක්වන්න.
(c) එක් එක් සේවකයාගේ වැටුප සඳහා අවම මුදල් නෝට්ටු සංයෝජනය නිර්ණය කිරීමට ක්‍රමලේඛයක් වතු හිමිකරුවෙකුට අවශ්‍ය වේ. (උදා. රු. 40,000 ක මාසික වැටුප ගෙවිය යුත්තේ රු. පන්දහසේ නෝට්ටු අටකින් මිස රු. සියයේ නෝට්ටු 400 කින් නොවේ.) සියලු සේවකයන් සඳහා මුදල් අවශ්‍යතාවය ද ක්‍රමලේඛය ප්‍රතිදානය කළ යුතු ය. ක්‍රමලේඛය, සේවකයාගේ වැටුප් අඩංගු employees.txt ගොනුව භාවිත කළ යුතු ය. එහි එක් එක් පේළියේ සේවකයකුගේ නම සහ ශුද්ධ වැටුප අඩංගු වේ. මේ සඳහා ලියන ලද පයිතන් ක්‍රමලේඛය රූපය 8.3 හි දැක්වේ. සාම්පල employees.txt ගොනුවකුත්, එම ගොනුවට අදාළ ඉහත ක්‍රමලේඛයේ ප්‍රතිදානයත් රූපය 8.4 හි දැක්වේ.
(i) රූපය 8.3 හි දැක්වෙන පයිතන් ක්‍රමලේඛයේ A - J ලේබල සඳහා සුදුසු ආදේශක ලියා දක්වන්න.
(ii) මෙම වතුයායේ සේවකයන්ගේ ශුද්ධ වැටුප්වල ශත ගණන් අඩංගු නොවේ. එහෙත් ශුද්ධ වැටුප් ආදාන සම්බන්ධයෙන් කුමන ප්‍රායෝගික ගැටලුවක් මෙම කේතයේ පවතී ද? එම ගැටලුව විසඳීමට ඔබ කේතයට කරන වෙනස්කම් ලියා දක්වන්න.""")
