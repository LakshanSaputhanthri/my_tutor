import json
E=[]
def add(d,q,qs=None):
    o={"d":d,"q":q}
    if qs:o["qs"]=qs
    E.append(o)

# ---------- 2013
c2013="""<html>
<head>
   <........> Test Cricket<........>
</head>
<body>
   <........>Sri Lankan Test cricket records<........>
   <........>
   <p>The<..................................................................>
      Sri Lankan national cricket team <........>
      played their first Test match on 17 February 1982 against England.
   </p>
   <p><........>Record Groups<........></p>
   <........>
      <li>Team records</li>
      <li>Individual records</li>
      <li>Partnership records</li>
   <........>
   <........>
   <........>Partnership records<........>
   <p><...........................................................>Sri Lanka holds the most
      number of partnership records in Test cricket,with the records for
      the second, third, fourth, and sixth wickets.South Africa and
      Pakistan are ranked second with two records each.
   </p>
   <...............................................>
      <........>Highest wicket partnerships<........>
      <tr>
         <th>Runs</th>
         <th>Wicket</th>
         <th colspan = "2">Partners</th>
      </tr>
      <tr>
         <td>335</td>
         <td>1st wicket</td>
         <td>Marvan Atapattu</td>
         <td>Sanath Jayasuriya</td>
      </tr>
      <tr>
         <td>576</td>
         <td>2nd wicket</td>
         <td>Sanath Jayasuriya</td>
         <td>Roshan Mahanama</td>
      </tr>
   </table>
</body>
</html>"""
fig13="""[Figure: A web page titled "Sri Lankan Test cricket records" (heading), a horizontal rule, then the paragraph "The Sri Lankan national cricket team played their first Test match on 17 February 1982 against England." where "Sri Lankan national cricket team" is a hyperlink. Below it a bold "Record Groups" paragraph followed by a bulleted list: Team records, Individual records, Partnership records. Then a heading "Partnership records", an image (two cricketers) with the text "Sri Lanka holds the most number of partnership records in Test cricket, with the records for the second, third, fourth, and sixth wickets. South Africa and Pakistan are ranked second with two records each." wrapped beside it. Finally a bordered table with caption "Highest wicket partnerships":
Runs | Wicket | Partners
335 | 1st wicket | Marvan Atapattu | Sanath Jayasuriya
576 | 2nd wicket | Sanath Jayasuriya | Roshan Mahanama
(the "Partners" header spans two columns)]"""
add("2013 ESSAY01","""1. Consider the section of a web page on the Sri Lankan Test Cricket team, given in the Figure:
"""+fig13+"""
A partial HTML document of the file "cricket.html" which generates the above web page is given below. Fill in the blanks of the HTML document with the appropriate tags to render the web page.
Notes :
1. When the user clicks on the phrase "Sri Lankan national cricket team" it should display the document named "team.html".
2. Name of the source file of the image displayed on the above webpage is "cricket.jpg".
3. The link to the image "cricket.jpg" should have an alternative description "cricket".

"""+c2013,
"""1. රූපයේ දී ඇති ශ්‍රී ලංකා ටෙස්ට් ක්‍රිකට් කණ්ඩායමේ වෙබ් පිටුවක කොටස සලකන්න:
"""+fig13+"""
ඉහත වෙබ් පිටුව ජනනය කරන "cricket.html" ගොනුවේ ආංශික HTML ලේඛනයක් පහත දී ඇත. වෙබ් පිටුව විදැහු කිරීමට අදාළ ඇමිණුම් (tags) යොදා ගනිමින් HTML ලේඛනයේ හිස්තැන් පුරවන්න.
සටහන් :
1. "Sri Lankan national cricket team" යන වාක්‍ය ඛණ්ඩය මත පරිශීලකයා ක්ලික් (click) කළ විට "team.html" නම් වූ ලේඛනය දර්ශනය විය යුතුය.
2. ඉහත වෙබ් පිටුවේ ඇති රූපයෙහි ප්‍රභව ගොනුවෙහි නම "cricket.jpg" වේ.
3. "cricket.jpg" යන රූපයේ සන්ධානය (link) සඳහා "cricket" නම් වූ විකල්ප විස්තරයක් තිබිය යුතුය.

"""+c2013)

# ---------- 2014
add("2014 ESSAY01","""2.(a) Consider the definition list given below rendered by a web browser:
CPU
    Central Processing Unit
ROM
    Read Only Memory
Complete the following HTML code segment to display the above list.
<dl>
   <..........................>CPU<..........................>
   <..........................>Central Processing Unit<..........................>
   <..........................>ROM<..........................>
   <..........................>Read Only Memory<..........................>
</dl>
(b) Write the outputs of following HTML code segments when rendered by a web browser.
(i) <abc>Greetings!</abc>
........
(ii) </u>Greetings!<u>
........
(c) Consider the following Output with check boxes rendered by a web browser:
Programming Languages Used:
C [ ] Java [ ] Python [ ]
Complete the following HTML code segment to render the above output.
<form method = "get" action = "">
   ........
   ........
   ........
   ........
</form>""",
"""2.(a) වෙබ් අතරික්සුවක් මගින් විදහු කරන ලද පහත පෙන්වා ඇති අර්ථ දැක්වීම් ලැයිස්තුව සලකා බලන්න:
CPU
    Central Processing Unit
ROM
    Read Only Memory
ඉහත ලැයිස්තුව සංදර්ශනය කිරීම සඳහා පහත දක්වන HTML කේත ඛණ්ඩය සම්පූර්ණ කරන්න.
<dl>
   <..........................>CPU<..........................>
   <..........................>Central Processing Unit<..........................>
   <..........................>ROM<..........................>
   <..........................>Read Only Memory<..........................>
</dl>
(b) වෙබ් අතරික්සුවක් මගින් පහත දක්වා ඇති HTML කේත ඛණ්ඩ විදහා කරන ආකාරය ලියා දක්වන්න.
(i) <abc>Greetings!</abc>
........
(ii) </u>Greetings!<u>
........
(c) වෙබ් අතරික්සුවක් මගින් විදහු කරන ලද පහත පෙන්වා ඇති ආවේක්ෂණ කොටු (check boxes) සහිත ප්‍රතිදානය සලකා බලන්න:
Programming Languages Used:
C [ ] Java [ ] Python [ ]
ඉහත දක්වා ඇති ප්‍රතිදානය විදහු කිරීම සඳහා පහත දක්වා ඇති HTML කේත ඛණ්ඩය සම්පූර්ණ කරන්න.
<form method = "get" action = "">
   ........
   ........
   ........
   ........
</form>""")

# ---------- 2015
f15="""<h2>Send Text Message</h2>
<p>Fill in all the fields and click Send Message</p>
<form action="" method="POST">
   <div class = "a">
      <div class="l"> Phone No.:</div>
      <div class="r"><input type=.................. name="phone" size="20"></div>
   </div>
   <div class = "a">
      <div class="l">Message:</div>
      <div class="r"><............................name="message" rows="7" cols="30">
         </...................></div>
   </div>
   <div class = "a">
      <div class="r"><input type="submit" value=...........................></div>
   </div>
</form>"""
fig15="""[Figure: A web form titled "Send Text Message" with the text "Fill in all the fields and click Send Message", a "Phone No.:" single-line text box, a "Message:" multi-line text area, and a button labelled "Send your message".]"""
add("2015 ESSAY01","""3.(a) Consider the web form given in the figure which has been developed for sending text messages from a web application.
"""+fig15+"""
The partial HTML code segment given below is prepared to generate the above form. Complete the code segment to render the above form.
"""+f15+"""
(b) A well-formed syntactically correct HTML code has been developed to render a web page which includes an image of a school. However, the browser does not display the image. Instead, it only displays the text "School" which is given as the 'text' attribute of alt. Give two possible reasons for this behaviour.
(c) Indicate whether the following CSS rules are syntactically correct or incorrect. If a rule is incorrect write the correct version.
(i) p {color: red}
    p {font-type: Arial;}
(ii) body{color: red;}
     {background-color: yellow;}
(iii) h1, h3{color: blue;}
Answer lines for each: ........""",
"""3.(a) වෙබ් යෙදුමක් මගින් පාඨ පණිවුඩ (text messages) යැවීම සඳහා සංවර්ධනය කරන ලද, පහත රූපයෙන් පෙන්වා ඇති වෙබ් පෝරමය (web form) සලකා බලන්න:
"""+fig15+"""
ඉහත පෝරමය ජනනය කිරීම සඳහා අර්ධ HTML කේත ඛණ්ඩයක් (partial code) පහත දී ඇත. ඉහත පෝරමය විදහු කිරීමට එම කේත ඛණ්ඩය සම්පූර්ණ කරන්න.
"""+f15+"""
(b) පාසලක ඡායාරූපයක් අඩංගු වෙබ් පිටුවක් විදහු කිරීමට නිවැරදි කාරක රීති භාවිත කරමින් සුනිර්මාණ (well formed) HTML කේතයක් සංවර්ධනය කර ඇත. එහෙත් වෙබ් අතරික්සුව (web browser) මගින් පාසලේ පිංතූරය විදහු නොවන අතර alt උපලක්ෂණය "text" ලෙස ලබා තිබූ "School" පමණක් විදහු විය. මෙම වර්යාව පැවතීමට හේතු දෙකක් දක්වන්න.
(c) පහත දක්වා ඇති නීති, කාරක රීතිවලට අනුකූලව නිවැරදි ද නැතහොත් වැරදි ද යන්න දක්වන්න, යම් නීතියක් වැරදි නම් එහි නිවැරදි ආකාරය ද ලියා දක්වන්න.
(i) p {color: red}
    p {font-type: Arial;}
(ii) body{color: red;}
     {background-color: yellow;}
(iii) h1, h3{color: blue;}
එක් එක් සඳහා පිළිතුරු පේළි: ........""")

# ---------- 2016
add("2016 ESSAY01","""4.(a) State the Operation of each HTML code segments given below. Assume that all images and HTML documents are in the same folder.
(i) <a href="coverPage.jpg" target = "_blank">Cover Page</a>
........
(ii) <a href="content.html">Content</a>
........
(iii) <a href="figures.html" target = "_self"> <img src = "figures.jpg"/></a>
........
(b) Which of the three mechanisms used to apply styles to HTML elements increases the maintainability of a web site?
........
(c) Consider the following HTML code segment:
<body>
   <h2>How web search engines work</h2>
   <p>A search engine maintains three processes.
   </p>
</body>
Write the internal styles required to apply the following styles for the elements in the above code segment.
Element | Property | Style
h2 | Colour | Red
 | Text | Centre aligned
P | Font | Courier New, 14 points high
........""",
"""4.(a) පහත දෙන එක් එක් HTML කේත ඛණ්ඩයන්හි ක්‍රියාකාරිත්වය ලියා දක්වන්න. සියලු HTML ලේඛන සහ අනුරූ (images) එකම ෆෝල්ඩරයෙහි අඩංගු යැයි උපකල්පනය කරන්න.
(i) <a href="coverPage.jpg" target = "_blank">Cover Page</a>
........
(ii) <a href="content.html">Content</a>
........
(iii) <a href="figures.html" target = "_self"> <img src = "figures.jpg"/></a>
........
(b) HTML මූලාංග රටා යෙදීමට භාවිත කරන යාන්ත්‍රණ තුනෙන් කුමක් වෙබ් අඩවියක් නඩත්තු කිරීමේ හැකියාව වැඩි කරයි ද?
........
(c) පහත සඳහන් HTML කේත ඛණ්ඩය සලකන්න:
<body>
   <h2>How web search engines work</h2>
   <p>A search engine maintains three processes.
   </p>
</body>
ඉහත දී ඇති කේත ඛණ්ඩයෙහි ඇති මූලාංග සඳහා පහත සඳහන් රටා යෙදීමට අවශ්‍ය අභ්‍යන්තර රටා (Internal styles) ලියා දක්වන්න.
මූලාංගය | ගුණාංගය | රටාව
h2 | වර්ණය (Colour) | Red
 | පාඨ (Text) | Centre aligned
P | අක්ෂර රූපය (Font) | Courier New, 14 points high
........""")

# ---------- 2018
add("2018 ESSAY01","""5.(a)(i) State two benefits of using Cascading Style Sheets (CSS).
........
(ii) Write the output of following HTML code segment when rendered by a web browser.
<html>
<body>
<u> Important Sites </u>
<ul>
   <li>
   <a href="www.nie.lk/index.html"> National Institute of Education </a>
   </li>
   <li>
   <a href="www.doenets.lk/exam/index.html"> Department of Examinations </a>
   </li>
</ul>
</body>
</html>
........
(iii) Write the output of following HTML code segment when rendered by a web browser.
<html>
<body>
<p><center> Department of Examinations <br> Pelawatta
<br> Battaramulla </center></p><hr>
</body>
</html>
........
(b) Consider the following HTML code segment:
<body>
   <h1> Introduction to Web Technologies </h1>
   <h3> HTML </h3>
   <p> HTML is the standard markup language for creating web pages </p>
</body>
Write down the internal Styles required to apply the styles mentioned in the following table for the elements h1 and p in the above code segment.
Element Name | Attribute | Attribute Value
h1 | color | blue
h1 | text-align | centre
h1 | font-family | Arial
p | background-color | Yellow
p | font-size | 12px
........
(c) Consider the HTML form given below rendered by a web browser:
[Figure: A form titled "Student Registration" with a text box labelled "Studnet Name", Gender radio buttons "Male" (selected) and "Female", a "Selected District:" drop-down list showing Colombo, Jaffna, Matara, and a Submit button.]
This is a registration form used for registering students. It is required to enter Student Name as a text input, select Gender, select District and then click Submit button. Complete following HTML code segment by filling the spaces to display the form.
<html>
<body>
<h3>Student Registration </h3>
<....................... action="register.php" method="post">
<div>
   Student Name  <input ....................... = ....................... ....................... = "name">
</div>
<br>
<div>
Gender
   <input .............. = ..........................="gtype" .................="male" checked> Male
   <input ............. = ......................="gtype" ...............="female" checked> Female
</div>
<br>
<div>
Selected District :
<..................... .....................= "city">
   <option .......................="Colombo"> ....................... </option>
   <option .......................="Jaffna"> ....................... </option>
   <option .......................="Matara"> ....................... </option>
</.......................>
</div>
<br>
   <input ..................... = ..................... name="submit" .....................="Submit">
</.......................>
</body>
</html>""",
"""5.(a)(i) පුගමන රටා පත්‍රිකා (CSS) භාවිත කිරීමේ ප්‍රයෝජන දෙකක් සඳහන් කරන්න.
........
(ii) පහත දැක්වෙන HTML කේත ඛණ්ඩය වෙබ් අතරික්සුවක් මගින් විදහා දක්වන විට ලැබෙන ප්‍රතිදානය ලියා දක්වන්න.
<html>
<body>
<u> Important Sites </u>
<ul>
   <li>
   <a href="www.nie.lk/index.html"> National Institute of Education </a>
   </li>
   <li>
   <a href="www.doenets.lk/exam/index.html"> Department of Examinations </a>
   </li>
</ul>
</body>
</html>
........
(iii) පහත දැක්වෙන HTML කේත ඛණ්ඩය වෙබ් අතරික්සුවක් මගින් විදහා දක්වන විට ලැබෙන ප්‍රතිදානය ලියා දක්වන්න.
<html>
<body>
<p><center> Department of Examinations <br> Pelawatta
<br> Battaramulla </center></p><hr>
</body>
</html>
........
(b) පහත දැක්වෙන HTML කේත ඛණ්ඩය සලකන්න:
<body>
   <h1> Introduction to Web Technologies </h1>
   <h3> HTML </h3>
   <p> HTML is the standard markup language for creating web pages </p>
</body>
ඉහත කේත ඛණ්ඩයෙහි ඇති h1 සහ p මූලාංග සඳහා, පහත වගුවේ සඳහන් රටා යෙදීමට අවශ්‍ය අභ්‍යන්තර රටා (internal styles) ලියා දක්වන්න.
මූලාංගයේ නම | උපලක්ෂණය | උපලක්ෂණයේ අගය
h1 | color | blue
h1 | text-align | centre
h1 | font-family | Arial
p | background-color | Yellow
p | font-size | 12px
........
(c) වෙබ් අතරික්සුවක් මගින් විදහා දක්වන පහත දැක්වෙන HTML පෝරමය සලකන්න.
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට "Student Registration" පෝරමය]
මෙහි දැක්වෙන්නේ සිසුන් ලියාපදිංචි කිරීමට භාවිත කරන ලියාපදිංචි පත්‍රයකි. සිසුවාගේ නම, පාඨ ආදානයක් ලෙස ඇතුළත් කර, ගැහැනු පිරිමි බව තෝරා, දිස්ත්‍රික්කය තෝරා ඉන් පසුව Submit බොත්තම එබීම අවශ්‍ය වේ. ආකෘති පත්‍රය සංදර්ශනය කිරීම සඳහා පහත දැක්වෙන කේත ඛණ්ඩයෙහි ඇති හිස්තැන් පුරවන්න.
(HTML කේත ඛණ්ඩය ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට)""")

# ---------- 2019
php19="""<?php
  $conn = new mysqli('locathost', ....................... , ....................... , .......................);
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  $sql = "......................... into ......................... (......................... , .........................)
  values ('Piyal', '12-B')";

  if ($conn->query(.........................) ==true) {
    echo "New record created successfully";
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }

  $conn->close();
?>"""
add("2019 ESSAY01","""6.(a)(i) Draw the expected output of the following HTML code segment when rendered by a web browser.
<html>
<body>
<!--Effects of Social Networking -->
<p>Social networking has <br> <u>advantages</u> and disadvantages </p>
</body>
</html>
[Answer box]
(ii) Draw the expected output of the following HTML code segment when rendered by a web browser.
<html>
<body>
<table border="1">
<caption>Schedule</caption>
<tr><th>Time</th><th>Event</th></tr>
<tr><td>8 am</td><td>Drama</td></tr>
<tr><td>10 am</td><td>News</td></tr>
<tr><td colspan =2> Lunch</td></tr>
</table>
</body>
</html>
[Answer box]
(b)(i) Write two advantages of using external style sheets when creating a web page.
........
(ii) Consider the following HTML elements require the styles as given in the table.
Element Name | Attribute | Attribute Value
P | color | red
P | font-family | Calibri
P | text-align | justify
h1 | color | red
h1 | font-family | Calibri
h2 | color | red
h2 | font-family | Calibri
h2 | text-align | justify
Write an external style sheet in the most efficient way to fulfil the above requirements using only the CSS group selector concept.
(c) The following PHP code is intended to add data into 'name' and 'class' fields of the table named 'student' in the MYSQL database called 'school_db'. User name and password to login to 'school_db' are 'admin' and 'A!2t*' respectively. Complete the PHP code segment by filling the blanks.

"""+php19,
"""6.(a)(i) වෙබ් අතරික්සුවක් මගින් විදහු විට පහත දැක්වෙන HTML කේත ඛණ්ඩයෙන් බලාපොරොත්තු වන ප්‍රතිදානය අඳින්න.
<html>
<body>
<!--Effects of Social Networking -->
<p>Social networking has <br> <u>advantages</u> and disadvantages </p>
</body>
</html>
[පිළිතුරු කොටුව]
(ii) වෙබ් අතරික්සුවක් මගින් විදහු විට පහත දැක්වෙන HTML කේත ඛණ්ඩයෙන් බලාපොරොත්තු වන ප්‍රතිදානය අඳින්න.
<html>
<body>
<table border="1">
<caption>Schedule</caption>
<tr><th>Time</th><th>Event</th></tr>
<tr><td>8 am</td><td>Drama</td></tr>
<tr><td>10 am</td><td>News</td></tr>
<tr><td colspan =2> Lunch</td></tr>
</table>
</body>
</html>
[පිළිතුරු කොටුව]
(b)(i) වෙබ් පිටුවක් නිර්මාණය කිරීමේදී බාහිර විලාස පත් භාවිත කිරීමේ වාසි දෙකක් ලියන්න.
........
(ii) පහත දැක්වෙන HTML මූලාංගවලට වගුවේ දී ඇති පරිදි විලාසයන් අවශ්‍ය යැයි සලකන්න.
මූලාංගයේ නම | උපලක්ෂණය | උපලක්ෂණයේ අගය
P | color | red
P | font-family | Calibri
P | text-align | justify
h1 | color | red
h1 | font-family | Calibri
h2 | color | red
h2 | font-family | Calibri
h2 | text-align | justify
විලාස කාණ්ඩ (CSS group selector) සංකල්පය පමණක් යොදා ගනිමින් ඉහත අවශ්‍යතා සපුරාලීම සඳහා වඩාත්ම කාර්යක්ෂම ක්‍රමයකින් බාහිර විලාස පතක් ලියන්න.
(c) පහත දී ඇති PHP කේතයෙන් 'school_db' නම් MYSQL දත්ත සමුදායෙහි 'student' නම් වගුවෙහි 'name' සහ 'class' ක්ෂේත්‍රවලට දත්ත එකතු කිරීමට බලාපොරොත්තු වේ. 'school_db' වලට පිරීම (login) සඳහා වන පරිශීලක නම සහ මුර පදය පිළිවෙළින් 'admin' සහ 'A!2t*' වේ. හිස්තැන් පුරවා, PHP කේත ඛණ්ඩය සම්පූර්ණ කරන්න.

"""+php19)

# ---------- 2020
add("2020 ESSAY01","""7.(a) Draw the expected output of following code segment when rendered by a web browser.
<html>
<body>
<table border=1>
      <tr><th>No</th><th>Type</th><th>City</th></tr>
      <tr><td>1</td><td rowspan=2>High</td><td>Galle</td></tr>
      <tr><td>2</td><td>Jaffna</td></tr>
</table>
</body>
</html>
Note : Please consider edges of the following dotted line box as display area of web browser.
[Answer box]
(b) Consider the following html code in which the lines are numbered to answer the questions in this part.
1.    <html>
2.    <head>
3.          <style type="text/css">
4.                h1,h2{color:blue;}
5.          </style>
6.    </head>
7.    <body>
8.          <h1 style="color:green;">Title One</h1>
9.          <h2>Title Two</h2>
10.   </body>
11.   </html>
(i) What are the colours of the text in line numbers 8 and 9 when the above code is rendered by the browser?
Line number | Text | Colour
8 | Title One | ........
9 | Title Two | ........
(ii) Write one advantage of defining styles as in line numbers 3, 4 and 5 over that of line number 8.
........
(iii) Write only the content of an external style sheet to include the following:
a) the style defined in line number 8 and
b) a CSS Id named 'appear' to define the style of the font as 'Arial'
........
(c) The following four PHP code blocks which are labeled as A,B,C and D are taken from a code intended to retrieve data from a database to display on the screen. However, the code blocks are not in correct order.
Label | Code Block
A | $sql = "SELECT itemcode, name FROM Product";
  | $result = $conn->query($sql);
B | if ($conn->connect_error) {
  |       die("Connection failed: " . $conn->connect_error);
  | }
C | if ($result->num_rows > 0) {
  |     while($row = $result->fetch_assoc()) {
  |     echo "Code:".$row["itemcode"]."/Item:".$row["name"]."<br>";
  |     }
  | } else {
  |     echo "0 results";
  | }
D | $conn = new mysqli("localhost", "admin", "C#a8t", "StoreDB");
(i) Write the labels of the four code blocks in the correct order inside four blanks of the following PHP script.
<?php
........
........
........
........
$conn->close();
?>
(ii) If the above code blocks are in the correct order, what is the expected output if the 'Product' table has only the following values?
Product
itemcode | name
P1 | Pen
P3 | Book""",
"""7.(a) වෙබ් අතරික්සුවක් මගින් විදහු විට පහත කේත ඛණ්ඩයෙන් අපේක්ෂා කෙරෙන ප්‍රතිදානය අඳින්න.
<html>
<body>
<table border=1>
      <tr><th>No</th><th>Type</th><th>City</th></tr>
      <tr><td>1</td><td rowspan=2>High</td><td>Galle</td></tr>
      <tr><td>2</td><td>Jaffna</td></tr>
</table>
</body>
</html>
සටහන : පහත දැක්වෙන තිත්ඉරි සහිත කොටුවේ දාර වෙබ් අතරික්සුවේ දර්ශනය වන කොටස ලෙස සලකන්න.
[පිළිතුරු කොටුව]
(b) මෙම කොටස සඳහා පිළිතුරු සැපයීමට පේළි අංකනය කර ඇති පහත දැක්වෙන html කේතය සලකන්න.
1.    <html>
2.    <head>
3.          <style type="text/css">
4.                h1,h2{color:blue;}
5.          </style>
6.    </head>
7.    <body>
8.          <h1 style="color:green;">Title One</h1>
9.          <h2>Title Two</h2>
10.   </body>
11.   </html>
(i) වෙබ් අතරික්සුවක් මගින් ඉහත කේතය විදහු විට අංක 8 සහ 9 වන පේළිවල පාඨ දිස්වෙන වර්ණයන් මොනවාද?
පේළි අංකය | පාඨය | වර්ණය
8 | Title One | ........
9 | Title Two | ........
(ii) පේළි අංක 8 හි දක්වා ඇති ලෙස විලාස (style) අර්ථ දැක්වීමට වඩා පේළි අංක 3, 4, 5 හි දක්වා ඇති ලෙස විලාස අර්ථ දැක්වීමේ ඇති එක් වාසියක් ලියා දක්වන්න.
........
(iii) පහත දැක්වෙන දෑ අඩංගු කිරීම සඳහා බාහිර විලාස පතක තිබිය හැකි අන්තර්ගතය පමණක් ලියන්න.
a) පේළි අංක 8 හි ඇති විලාසිතාව සහ
b) අකුරු විලාසය (font style) 'Arial' ලෙස දැක්වීමට 'appear' නම් වූ CSS Id එකක්
........
(c) A,B,C සහ D ලෙස ලේබල් කර ඇති පහත දැක්වෙන PHP කේත ඛණ්ඩ හතර දත්ත සමුදායකින් දත්ත (retrieve) කර තිරය මත ප්‍රදර්ශනය කිරීමේ කේතයකින් ලබාගෙන ඇත. එහෙත් මෙම කේත ඛණ්ඩ නිවැරදි අනුපිළිවෙළට නොමැත.
ලේබලය | කේත ඛණ්ඩය
A | $sql = "SELECT itemcode, name FROM Product";
  | $result = $conn->query($sql);
B | if ($conn->connect_error) {
  |       die("Connection failed: " . $conn->connect_error);
  | }
C | if ($result->num_rows > 0) {
  |     while($row = $result->fetch_assoc()) {
  |     echo "Code:".$row["itemcode"]."/Item:".$row["name"]."<br>";
  |     }
  | } else {
  |     echo "0 results";
  | }
D | $conn = new mysqli("localhost", "admin", "C#a8t", "StoreDB");
(i) ඉහත කේත ඛණ්ඩවල දක්වා ඇති ලේබල හතර පහත PHP කේතයේ හිස්තැන් හතර තුළ නිවැරදි අනුපිළිවෙළට ලියා දක්වන්න.
<?php
........
........
........
........
$conn->close();
?>
(ii) 'Product' වගුවේ පහත දැක්වෙන අගයන් පමණක් තිබේ නම්, සහ ඉහත කේත නිවැරදි අනුපිළිවෙළට ඇති විට අපේක්ෂිත ප්‍රතිදානය කුමක් ද?
Product
itemcode | name
P1 | Pen
P3 | Book""")

# ---------- 2021
add("2021 ESSAY01","""8.(a)(i) In the following HTML code, underline the parts containing errors. (Please ignore line numbering.)
1.    <html>
2.    <body background-color="green">
3.    <hl> Welcome all of you to online ICT Seminar </h1>
4.    <a url="#one" >A/L Student Section</a>
5.    <p> O/L ICT is not available</a>
6.    < -- Section 1 -- >
7.    <h4> A/L ICT </h4>
8.    <hr><p>Good Morning</p><hr>
9.    <br><p> This section is for students </p>
10.   </body></html>
(ii) Write the relevant correct code lines to make "A/L Student Section" (in line number 4) a hyperlink to "A/L ICT" (in line number 7).
Code for Line 4 : ........
Code for Line 7 : ........
(b) Consider the styles in Table 1, to answer the given questions.
Table 1
Selector | Description of the Style
Class with a class name "art" | Size of the font 14px, Text should be centered
Header 1 | Text color is yellow
(i) It is expected to use above styles in several web pages on a web site. Write a suitable cascading style sheet to define the styles given in Table 1 to satisfy this requirement.
........
(ii) Write the relevant HTML code lines to include the style sheet defined in part (b) (i) into a web page. [Assume that the style sheet created in part (b)(i) is saved with name neat.]
........
(c) An output of an HTML code rendered by a browser is shown below.
[Figure: A web page with heading "Chess Tournament"; a definition list: "Category I" followed by a bulleted list (Team A, Team C); "Category II" followed by Team B and Team D (indented, no bullets); a heading "Registration Form"; a bordered form containing "Select the team:" with a drop-down showing "Team A", "Your Comments:" with a multi-line text box, two check boxes "Food Required" and "Accommodation Required", and a "Submit" button.]
(i) The relevant HTML code (incomplete) is given below. Fill the blanks in it in order to get the required output.
<html><body>
<h2>Chess Tournament</h2>
<.......>
       <dt>Category I <.......><li>Team A</li><li>Team C</li></.......></dt>
       <dt>Category II<.......>Team B</.......><.......>Team D</.......></dt>
</.......>
<h3>Registration Form</h3>
<form method="get">
       <...............>
              <label for="Team">Select the team:</label>
               <............ name="team">
                     <option value="a">Team A</option>
                     <option value="b">Team B</option>
                     <option value="c">Team C</option>
                     <option value="d">Team D</option>
               </........><br><br>
              <label for="comment">Your Comments:</label>
              <......... name="comment" rows="3" cols="30"></..........><br><br>
              <input type=................ name="food">
              <label for="fr">Food Required</label>
              <input type=................ name="accom">
              <label for="ar">Accommodation Required</label><br><br>
              <............ type="submit" value="Submit">
       </...............>
</form>
</body></html>
(ii) Write the relevant HTML code line to show "Team B" as the default selection for "Select the team".
........""",
"""8.(a)(i) පහත HTML කේතයේ දෝෂ කොටස් යටින් ඉරි අඳින්න. (කරුණාකර පේළි අංක නොසලකන්න.)
1.    <html>
2.    <body background-color="green">
3.    <hl> Welcome all of you to online ICT Seminar </h1>
4.    <a url="#one" >A/L Student Section</a>
5.    <p> O/L ICT is not available</a>
6.    < -- Section 1 -- >
7.    <h4> A/L ICT </h4>
8.    <hr><p>Good Morning</p><hr>
9.    <br><p> This section is for students </p>
10.   </body></html>
(ii) ඉහත "A/L Student Section" යන්න (4 වන පේළියේ ඇති) "A/L ICT" (7 වන පේළියේ ඇති) යන්නට අධිසම්බන්ධකයක් (hyperlink) කිරීමට අදාළ කේත පේළි ලියන්න.
4 වන පේළිය සඳහා කේතය : ........
7 වන පේළිය සඳහා කේතය : ........
(b) අසා ඇති ප්‍රශ්නවලට පිළිතුරු දීමේදී, 1 වගුවේ ඇති විලාස (styles) සලකන්න.
1 වගුව
වරකය | විලාස විස්තරය
"art" නමින් යුත් පන්තියක් | අක්ෂර වල විශාලත්වය 14px සහ පාඨ මධ්‍යගතව
1 ශීර්ෂය | පාඨවල වර්ණය : කහ
(i) ඉහත විලාස, වෙබ් අඩවියක වෙබ් පිටු කිහිපයකම භාවිතයට ගැනීමට අපේක්ෂා කෙරේ. මෙම අවශ්‍යතාව සපුරාගැනීමට, ඉහත 1 වගුවේ ඇති විලාස අර්ථ දැක්වීමට සුදුසු කැස්කේඩින් විලාස පතක් (CSS) ලියන්න.
........
(ii) ඉහත (b) (i) හි අර්ථ දක්වන ලද විලාස පත, වෙබ් පිටුවකට ඇතුළත් කිරීමට අදාළ HTML කේත පේළි ලියන්න. [ඉහත (b)(i) සඳහා නිමැවුණු විලාස පත neat නමින් සුරැකී බව උපකල්පනය කරන්න.]
........
(c) HTML කේතයක් වෙබ් අතරික්සුවක් මගින් විදහු විට පහත පරිදි වේ.
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට "Chess Tournament" වෙබ් පිටුව]
(i) අදාළ HTML කේතය (අසම්පූර්ණ) පහත දක්වේ. අවශ්‍ය ප්‍රතිදානය ලබාගත හැකිවන පරිදි එහි ඇති හිස්තැන් සම්පූර්ණ කරන්න.
(HTML කේත ඛණ්ඩය ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට)
(ii) "Select the team" සඳහා පෙරනිමි තේරීම (default selection) ලෙස "Team B" දැක්වීමට අදාළ HTML කේත පේළිය ලියන්න.
........""")

# ---------- 2022
add("2022 ESSAY01","""9.(a) Draw the expected output of the following- HTML code segment when rendered by a web browser.
<html>
<body>
<table border=1>
      <tr><th>Designation</th><th>Contact Telephone Numbers</th> </tr>
      <tr><td rowspan=2> Principal</td><td> 061-2223211 </td> </tr>
      <tr><td> 067-5557772</td> </tr>
      <tr> <td> Vice Principal</td> <td> 061-5557771 </td> </tr>
      <tr> <td colspan=2> Common Phone Number: 019-2233445</td> </tr>
</table>
</body>
</html>
Note : Please consider edges of the following dotted line box as display area of web browser.
[Answer box]
(b) Rewrite the following HTML code by applying internal CSS with grouping selectors.
<html>
<head> <title>Cascading Style Sheets</title> </head>
<body>
<h1 style="color:blue;text-align:center"> Introduction to Cascading Style Sheets</h1>
<h2 style="color:blue"> CSS can be applied to html documents in three different ways. </h2>
</body>
</html>
(c) Consider the HTML form given in Figure 1 rendered by a web browser.
[Figure 1: A form with heading "Registration for Examination"; a text box labelled "Studnet Name"; "Select Examination Module:" with three check boxes ICT, English, IQ; "Prefered Medium:" with radio buttons Sinhala (selected), Tamil, English; "Select Test Center:" drop-down showing Colombo (options Colombo, Matara, Jaffna); and a Submit button.]
The relevant HTML code (incomplete) is given below. Fill the blanks in it in order to get the output shown in Figure 1.
<html>
<head>Registration Form</head>
<body>
<h3>Registration for Examination</h3>
<form ................="process.php" ................="post">
<div> ................ <input ................=................ ................="name"></div>
<p>
  <div>
    Select Examination Module: <p>
    <input ...........=........... ..........="module[]" ..........="ICT"/>..........<br>
    <input ...........=........... ..........="module[]" ..........="English"/>....<br>
    <input ...........=........... ..........="module[]" ..........="IQ"/>..........<br>
  </div>
    <br>
  <div>
    Prefered Medium:
    <input ...........=........ .........="language" .......="Sinhala" ......./>Sinhala
    <input ...........=........... ..........="language" ..........="Tamil"/>Tamil
    <input ...........=........... ..........="language" ..........="English"/>English
  </div>
  <div>
    <br>
    Select Test Center:
    <.......... name="Center">
        <.......... ..........="Colombo" selected>..........</..........>
        <.......... ..........="Matara">..........</..........>
        <.......... ..........="Jaffna">..........</..........>
    </..........>
  </div>
    <br>
    <input type="submit" name="submit" value="Submit">
</form>
</body>
</html>
(d) The process.php script is invoked after submitting the above form in part (c). After submitting the form, it is required to display the name, medium and test center. Complete the following PHP code segment (process.php) to fulfil this requirement.
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
   $name = $_........["........"];
   $medium = $_........["........"];
   $center = $_........["........"];}
echo "<h2> Your Input:</h2>";
echo $........; echo "<br>";
echo $........; echo "<br>";
echo $........; echo "<br>";
?>""",
"""9.(a) වෙබ් අතරික්සුවක් (web browser) මගින් විදහු (render) විට පහත සඳහන් HTML කේත ඛණ්ඩයෙන් අපේක්ෂිත ප්‍රතිදානය අඳින්න.
<html>
<body>
<table border=1>
      <tr><th>Designation</th><th>Contact Telephone Numbers</th> </tr>
      <tr><td rowspan=2> Principal</td><td> 061-2223211 </td> </tr>
      <tr><td> 067-5557772</td> </tr>
      <tr> <td> Vice Principal</td> <td> 061-5557771 </td> </tr>
      <tr> <td colspan=2> Common Phone Number: 019-2233445</td> </tr>
</table>
</body>
</html>
සටහන : පහත දැක්වෙන තිත්ඉරි සහිත කොටුවේ දාර වෙබ් අතරික්සුවේ දර්ශනය වන කොටස ලෙස සලකන්න.
[පිළිතුරු කොටුව]
(b) අභ්‍යන්තර (internal) CSS සමඟ සමූහ වරණ (group selectors) යොදාගනිමින් පහත සඳහන් HTML කේතය නැවත ලියන්න.
<html>
<head> <title>Cascading Style Sheets</title> </head>
<body>
<h1 style="color:blue;text-align:center"> Introduction to Cascading Style Sheets</h1>
<h2 style="color:blue"> CSS can be applied to html documents in three different ways. </h2>
</body>
</html>
(c) වෙබ් අතරික්සුවක් මගින් විදහු (render) රූපය 1 හි දැක්වෙන HTML ආකෘති පත්‍රය (form) සලකන්න.
[රූපය 1: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන "Registration for Examination" පෝරමය]
අදාළ HTML කේතය (අසම්පූර්ණ) පහත දැක්වේ. රූපය 1 හි ඇතුළත් පරිදි ප්‍රතිදානය ලබාගැනීමට හැකිවන පරිදි එහි ඇති හිස්තැන් සම්පූර්ණ කරන්න.
(HTML කේත ඛණ්ඩය ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට)
(d) ඉහත (c) කොටසේ සඳහන් ආකෘති පත්‍රය යොමු කිරීමෙන් (submit) අනතුරුව process.php උපදේශාවලිය (script) ක්‍රියාත්මක කෙරේ. ආකෘති පත්‍රය යොමු කිරීමෙන් පසුව නම (name), මාධ්‍ය (medium) සහ විභාග මධ්‍යස්ථානය (test center) ප්‍රදර්ශනය කිරීම අවශ්‍ය වේ. මෙම අවශ්‍යතාව සපුරාලීම සඳහා පහත PHP කේත ඛණ්ඩය (process.php) සම්පූර්ණ කරන්න.
(PHP කේත ඛණ්ඩය ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට)""")

# ---------- 2023
add("2023 ESSAY01","""10.(a) Draw the expected output of the following HTML code segment when rendered by a web browser.
<html>
<body>
 <ul  style="list-style-type:none;">
  <li>Cricket</li>
  <li>Football</li>
  <li>Hockey</li>
 </ul>
<html>
<body>
Note : Please consider edges of the following dotted line box as display area of web browser.
[Answer box]
(b) A registration form for a speech competition and its labeled HTML source are given in Figures 1.1 and 1.2 respectively.
[Figure 1.1: A web page with heading "Back to the nature!", sub-heading "Speech Competition", heading "Registration form", a form with: Name: text box; Gender: radio buttons Male, Female; District: drop-down showing Colombo; Email: text box; check box "Subscribe for newsletter?"; Submit button; below the form an image (a tree) with the link text "Western Province Environment".]
Figure 1.2 (HTML source):
<html>
<...A...>Back to the nature!</...A...>
<...B...>Speech Competition</...B...>
<h3>Registration form</h3>
<form method="...C..." ...D...="./action_page.php">
       <label for="name">Name:</label>
       <input type="...E..." name="name"><br><br>
       <label for="gender">Gender:</label>
       <input type="...F..." name="gender" id="male" value="male">
       <label for="male">Male</label>
       <input type="...F..." name="gender" id="female" value="female">
       <label for="female">Female</label> <br><br>
       <label for=" G ">District: </label>
       <...H... name="district" id="district">
              <option value="colombo">Colombo</option>
              <option value="gampaha">Gampaha</option>
              <option value="kalutara">Kalutara</option>
       </...H...><br><br>
       <label for="email">Email:</label>
       <input type="email" name="email"><br><br>
       <input type="...I..." name="newsletter" id="newsletter">
       <label for="newsletter">Subscribe for newsletter?</label><br><br>
       <input type="...J..." value="Submit">
</form
<br>
   <...K...="wpeLogo.jpg" alt="...L..." width="50" height="60">
   <...M...="https://www.wpe.lk" title="...N...">Western Province Environment</a>
</html>
For each of the labels A to N in the HTML code in Figure 1.2, choose a suitable replacement from the given list. In the answer table, write down the number of the replacement for each label.
List:
1: action | 2: a href | 3: caption | 4: checkbox | 5: district
6: font | 7: h1 | 8: h2 | 9: h3 | 10: head
11: img src | 12: More details | 13: name | 14: post | 15: radio
16: select | 17: submit | 18: text | 19: th | 20: WPE logo
Answer table:
A: ... B: ... C: ... D: ... E: ... F: ... G: ...
H: ... I: ... J: ... K: ... L: ... M: ... N: ...
(b) The action_page.php file mentioned in the given code of Figure 1.2 is shown below.
<?php
$servername = "localhost"; $username = "root";  $password = "";
$dbname = "environment";
// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Section P
$name = $_POST['name']; $gender = $_POST['gender']); $district = $_POST['district']; $email = $_POST[‘email’]; $newsletter = $_POST(['news-letter'];
// section P end
// Section Q
$sql = "INSERT INTO applicants (name, gender, district, email, newsletter) VALUES ('$name', '$gender', '$district', '$email', '$newsletter')";
// section Q end

if ($conn->query($sql) === TRUE) {
      echo "Data inserted successfully!";
} else {
      echo "Error: " . $sql . "<br>" . $conn->error;
}
// Close the connection
mysqli_close($conn);
?>
Write down the purpose of section P and the purpose of section Q.
P : ........
Q : ........""",
"""10.(a) වෙබ් අතරික්සුවක් මගින් විදහු විට පහත සඳහන් HTML කේත ඛණ්ඩයෙන් අපේක්ෂිත ප්‍රතිදානය අඳින්න.
<html>
<body>
 <ul  style="list-style-type:none;">
  <li>Cricket</li>
  <li>Football</li>
  <li>Hockey</li>
 </ul>
<html>
<body>
සටහන : පහත දැක්වෙන තිත්ඉරි සහිත කොටුවේ දාර වෙබ් අතරික්සුවේ දර්ශනය වන කොටස ලෙස සලකන්න.
[පිළිතුරු කොටුව]
(b) කථික තරඟයක් සඳහා ලියාපදිංචිවීමේ පෝරමයක් (registration form) සහ එහි ලේබල් කරන ලද HTML ප්‍රභවය රූපය 1.1 සහ රූපය 1.2 මගින් පිළිවෙළින් දක්වා ඇත.
[රූපය 1.1 සහ රූපය 1.2: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට]
1.2 රූපයෙන් දැක්වෙන HTML කේතයේ A සිට N තෙක් වූ එක් එක් ලේබලය සඳහා සුදුසු ආදේශකය, දී ඇති ලැයිස්තුවෙන් තෝරාගන්න. එක් එක් ලේබලයට අදාළ ආදේශකයේ අංකය පිළිතුරු වගුවේ ලියා දක්වන්න.
ලැයිස්තුව සහ පිළිතුරු වගුව ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට
(b) කේතයේ (1.2 රූපයේ) සඳහන් action_page.php ගොනුව පහත දක්වා ඇත.
(PHP කේතය ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට)
P කොටසේ අරමුණ සහ Q කොටසේ අරමුණ ලියා දක්වන්න.
P : ........
Q : ........""")

# ---------- 2024
f24="""<html>
   <h1>Central Province</h1>
   <h2>Public concerns form</h2>
   <hr style="width:30%;text-align:left;margin-left:0">
    <form method="post" ------------------- ="./action_page.php">
    <h3>Concern</h3>
    <label for="district">District: </label>
    < ------------------- name="district" id="district">
        <option value="kandy">Kandy</option>
        <option value="matale">Matale</option>
        <option value="nuwaraeliya">Nuwara Eliya</option>
    < ------------------- ><br><br>
    <label for="ctype">Type:</label>
    <input type=" ------------------- " name="ctype" id="goods"
    value="goods">
    <label for="goods">Goods</label>
    <input type=" ------------------- " name="ctype" id="services"
    value="services">
    <label for="services">Services</label><br><br>
    <label for="description">Description:</label>
    <input type="text" name="description" size="25"><br><br>
   <hr style="width:30%;text-align:left;margin-left:0">
    <h3>Complainant details</h3>
    <label for="name">Name:</label>
    <input type="text" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" name="email">
    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone" size="10" pattern="[0-9]{10}"
    title="Invalid telephone number"required><br><br>
    <input type=" ------------------- " value=" ------------------- ">
</form>
<br>
<img src="flag.jpg" alt="Central province flag" width="50" height="40">
<a href="http://www.cpca.lk" title="10, Hill street, Kandy">Central Province
Consumer Affairs</a>
</html>"""
p24="""<?php
  $host = "localhost";
  $db_user = "student_user";
  $db_password = "student_pass";
  $db_name = "studentDB";
  $conn = mysqli_connect ($host, $db_user, $db_password, $db_name);
  if (!$conn) {
    die("<tr><td colspan='3'>Connection failed:" .
    mysqli_connect_error () . "</td></tr>");
    }
  $sql = "SELECT student_id, first_name, last_name FROM stu-dents";
  $result = mysqli_query ($conn, $sql) ;
  if (mysqli_num_rows ($result) > 0) {
    while ($row = mysqli_fetch_assoc ($result) ) {
      echo "<tr>
            <td>" . $row["student_id"] . "</td>
            <td>" . $row["first_name"] . "</td>
            <td>" . $row["last_name"] . "</td>
            </tr>";
    }
  } else {
    echo "<tr><td colspan='3'>No students found .</td></tr>";
  }
  mysqli_close ($conn);
?>"""
add("2024 ESSAY01","""11.(a) A form that a user can use to enter a complaint regarding a good or a service that he/she received is shown in Figure 1.1. The HTML source that was used to make the form is shown in Figure 1.2 with seven blanks (-----------).
[Figure 1.1: A web page with heading "Central Province", sub-heading "Public concerns form", a horizontal rule, a section "Concern" with a "District:" drop-down showing Kandy, "Type:" radio buttons Goods and Services, a "Description:" text box; a horizontal rule; a section "Complainant details" with "Name:" text box, "Email:" text box, "Phone:" text box, a Submit button; and an image (flag) with the link "Central Province Consumer Affairs".]
(i) Fill the seven blanks of Figure 1.2 to make the code complete.
Figure 1.2:
"""+f24+"""
(ii) What happens when the user presses the 'Submit' button on the form?
........
(iii) What is the benefit of using input type="email" for the email address entry field instead of input type="text"?
........
(iv) What can you guess about the purpose of pattern="[0-9]{10}" with respect to the Phone entry field?
........
(v) What is the purpose of the use of title="10, Hill street, Kandy" in the <img src code line?
........
(b) Explain the main purpose of the HTML code extract shown in Figure 1.3.
Figure 1.3:
"""+p24+"""
........""",
"""11.(a) පරිශීලකයකුට ඔහු/ඇය ලද යම් භාණ්ඩයක් හෝ සේවාවක් හෝ ගැන පැමිණිල්ලක් කිරීමට භාවිත කළ හැකි පෝරමයක් රූපය 1.1 හි දැක්වේ. එම පෝරමය සෑදීමට භාවිත කළ HTML ප්‍රභවය හිස්තැන් (-----------) හතක් ද සමඟින් රූපය 1.2 හි ඇත.
[රූපය 1.1: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට]
(i) රූපය 1.2 හි කේතය සම්පූර්ණ කිරීමට එහි ඇති හිස්තැන් හත පුරවන්න.
රූපය 1.2:
"""+f24+"""
(ii) පරිශීලකයා පෝරමයේ Submit බොත්තම එබූ විට කුමක් සිදු වේද?
........
(iii) ඊ-තැපැල් ලිපිනය ඇතුළත් කරන ක්ෂේත්‍රය සඳහා input type="text" වෙනුවට input type="email" භාවිත කිරීමේ වාසිය කුමක්ද?
........
(iv) Phone ඇතුළත් කිරීමේ ක්ෂේත්‍රයට අදාළව pattern="[0-9]{10}" හි අරමුණ පිළිබඳව ඔබට කුමක් අනුමාන කළ හැකි ද?
........
(v) <img src කේත පේළියේ title="10, Hill street, Kandy" භාවිතයේ අරමුණ කුමක්ද?
........
(b) රූපය 1.3 න් පෙන්වන කේත කොටසේ මූලික අරමුණ කුමක්ද?
රූපය 1.3:
"""+p24+"""
........""")

# ---------- 2011 ESSAY02
add("2011 ESSAY02","""1.(a) Describe the terms "elements" and "attributes" with respect to an HTML document.
(b) Identify each of the following as either an element or an attribute and describe their functionality.
(i) br    (ii) href    (iii) src    (iv) html
(c) Consider the following figure which shows a section of a web page of a tour operating company in Sri Lanka.
[Figure: A web page with heading "Wildlife Tours to Sri Lanka"; the paragraph "Sri Lanka is famous for its wildlife. There are many National parks and Sanctuaries where one can see animals in their natural habit."; a sub-heading "Highlights"; an image of elephants beside the text "Why visit Sri Lanka?" and three radio buttons labelled Blue Whale, Leopard, Elephant.]
Answer the following questions using the above figure.
(i) It is required to format all the paragraphs of the above HTML document in "arial" font, 14 font size and in blue color. Write the required CSS code segment for the paragraph.
(ii) Explain the effect of having the following tag in the above HTML document.
<a href = "elephants.jpg"><img src = "elephants_tnl.jpg" ALT = "Tour to Yala" width = "288cm" height = "156cm" style = "border:none"/></a>
(iii) Write HTML code segment to create the collection of three radio buttons labelled as 'Blue Whale', 'Leopard' and 'Elephant' as appeared in the above HTML document.
(iv) The company wants to add a table showing the rates as given below with the caption 'Wild Sri Lanka', to the above HTML Document.
Days | Price
7 | US$910
10 | US$1220
Write HTML code segment to create the table.""",
"""1.(a) HTML ලේඛනයක් සම්බන්ධයෙන් "මූලාංග" සහ "උපලක්ෂණ" යන පද විස්තර කරන්න.
(b) පහත දක්වා ඇති එක් එකක් මූලාංගයක් හෝ උපලක්ෂණයක් හෝ ලෙස හඳුනාගෙන ඒවායේ කාර්යයන් විස්තර කරන්න.
(i) br    (ii) href    (iii) src    (iv) html
(c) පහත රූප සටහනෙන් දැක්වෙන, ශ්‍රී ලංකාවේ ඇති සංචාර මෙහෙයුම් සමාගමක වෙබ් පිටුවක කොටස සලකන්න.
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට "Wildlife Tours to Sri Lanka" වෙබ් පිටුව]
ඉහත රූප සටහන භාවිත කරමින් පහත දක්වා ඇති ප්‍රශ්නවලට පිළිතුරු සපයන්න.
(i) ඉහත HTML ලේඛනයේ සියලුම ඡේද විරාම් අක්ෂර වර්ගය, අක්ෂර ප්‍රමාණය 14 සහ නිල් පැහැයෙන් හැඳින්වීමට අවශ්‍යතාව තිබේ. ඡේදය සඳහා අවශ්‍ය CSS කේත ඛණ්ඩය ලියා දක්වන්න.
(ii) ඉහත HTML ලේඛනය තුළ පහත දැක්වෙන ලේබලය (Tag) මගින් ඇතිකෙරෙන බලපෑම විස්තර කරන්න.
<a href = "elephants.jpg"><img src = "elephants_tnl.jpg" ALT = "Tour to Yala" width = "288cm" height = "156cm" style = "border:none"/></a>
(iii) ඉහත HTML ලේඛනයේ ඇති ආකාරයට 'Blue Whale', 'Leopard' සහ 'Elephant' ලෙස ලේබල් කර ඇති රේඩියෝ බොත්තම් තුනේ එකතුව ඉහත HTML ලේඛනයේ නිර්මාණය කිරීම සඳහා අවශ්‍ය HTML කේත ඛණ්ඩය ලියන්න.
(iv) 'Wild Sri Lanka' යන ශීර්ෂය (Caption) සහිතව පහත පෙන්වා ඇති ආකාරයේ මිල ගණන් දැක්වෙන වගුවක් ඉහත HTML ලේඛනයට ඇතුළත් කිරීමට සමාගමට අවශ්‍ය වී ඇත.
දින | මිල
7 | US$910
10 | US$1220
මෙම වගුව නිර්මාණය කිරීමට අවශ්‍ය HTML කේත ඛණ්ඩය ලියන්න.""")

# ---------- 2012 ESSAY02
add("2012 ESSAY02","""2.(a) What would be the responses by a browser for a paragraph tag and for a break tag in an HTML document?
(b) What will be displayed when the following HTML code segment is rendered? Clearly indicate blank line(s) in the display, if any, with dotted lines (.......................................).
<p>Our evergreen school days<br/>will not come back again</p>
<p>From the nursery to high school we learnt the best</p>
(c) A company named "Agri Sri Lanka" requires a web page as given below.
[Figure: A web page with heading "Agriculture Sri Lanka"; an image containing the text "AGRI SRI LANKA"; the paragraph "Sri Lanka is an agricultural country. Agriculture is one of the main sectors of the Sri Lankan economy."; the paragraph "The main plantation crops are"; a bulleted list: tea, rubber, coconut; the text "Links to agricultural firms"; and two hyperlinks on separate lines: "Jay Agro Technologies" and "Lanka Agri Systems Pvt Ltd."]
Write an HTML code to produce the above web page. Assume that the name of the image file is "agriSL.jpg". The links, Jay Agro Technologies and Lanka Agri Systems Pvt Ltd. should link to the sites "http://www.jayagrotec.com" and "http://www.lkagrisys.com" respectively.""",
"""2.(a) HTML ලේඛනයක ඡේද උපලකුණක් (paragraph) සහ කැඩුම් උපලකුණක් (break tag) සඳහා අතිරික්සුවක් (browser) දක්වන ප්‍රතිචාර කුමක් ද?
(b) පහත දැක්වෙන HTML කේතය විදහු (render) විට, කුමක් සංදර්ශනය වනු ඇත් ද? එම සංදර්ශනයෙහි හිස් රේඛා (blank lines) ඇත්නම් ඒවා තිත් ඉරි (.......................................) මගින් පැහැදිලිව දක්වන්න.
<p>Our evergreen school days<br/>will not come back again</p>
<p>From the nursery to high school we learnt the best</p>
(c) "Agri Sri Lanka" නමැති සමාගමකට පහත දී ඇති ආකාරයේ වෙබ් පිටුවක් අවශ්‍ය වේ.
[රූපය: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට "Agriculture Sri Lanka" වෙබ් පිටුව]
ඉහත වෙබ් පිටුව නිර්මාණය කරගැනීම සඳහා HTML කේතයක් ලියන්න. අනුරූ ගොනුවෙහි නම "agriSL.jpg" ලෙස උපකල්පනය කරන්න. Jay Agro Technologies සහ Lanka Agri Systems Pvt Ltd යන සබැඳුම් පිළිවෙළින් "http://www.jayagrotec.com" සහ "http://www.lkagrisys.com" යන අඩවිවලට සබැඳි විය යුතු ය.""")

# ---------- 2017 ESSAY06
add("2017 ESSAY06","""7.(a) Environmental Institute of Colombo intends to develop website to provide information on art competition for students. A web page from this website and another web page with the entry form to register for the competition are shown in Figure 6.1 and Figure 6.2 respectively.
[Figure 6.1: A web page of the website: heading "Student Art Competition"; heading "Theme: Litter on the environment"; heading "PRIZES" with a bulleted list (square bullets): 1st place Rs. 10,000/=, 2nd place Rs. 7,500/=, 3rd place Rs. 5,000/=; heading "ENTRY FORM"; text "Please fill and submit this online entry form to enter the competition" where "online entry form" is a hyperlink.]
[Figure 6.2: Entry form: heading "Art Competition Online Entry Form 2017"; "Theme: Litter on the environment"; Name: text box; Gender: radio buttons Male, Female; Grade Category: drop-down (Grade 1 -2); Art media: check boxes Water Colours, Colour Pencils, Crayon, Chalk; buttons "Clear your Entries" and "Submit".]
Using appropriate HTML tags, create an HTML file required to render the web page as shown in Figure 6.1. Your code should satisfy the following requirements.
It is required to format the text of the list in 'Calibri' font, 14 points high, in red color. The list should be bulleted with squares. Format the list by using internal or external style sheets only.
Further, when a user clicks on the hypertext 'online entry form' on the web page, the entry form given in Figure 6.2 should be rendered on a new tab/page. Assume that the name of the HTML file of the web page with the entry form is 'form.html'.
(b) Using appropriate HTML tags, create an HTML file to render the entry form given in Figure 6.2. The options for 'Grade Category' are given in the Figure 6.3. Your code should satisfy the following requirements. When the 'Clear your Entries' button is clicked, all the entries of the form should be cleared. Similarly, when the 'Submit' button is clicked, the form should be submitted to the server.
[Figure 6.3: Options for Grade Category: Grade 1 -2, Grade 3 -6, Grade 7 -10, Grade 11 -13]""",
"""7.(a) සිසුන් සඳහා පවත්වන චිත්‍ර තරඟයක් පිළිබඳ තොරතුරු ලබා දීම සඳහා කොළඹ පරිසර ආයතනය වෙබ් අඩවියක් නිර්මාණය කිරීමට අදහස් කරයි. එහි එක් වෙබ් පිටුවක් සහ තරඟයට ලියාපදිංචි වීම සඳහා ඇතුළත් වීමේ පෝරමය සහිත තවත් වෙබ් පිටුවක් රූපය 6.1 සහ රූපය 6.2 මගින් පිළිවෙළින් දැක්වේ.
[රූපය 6.1 සහ රූපය 6.2: ඉහත ඉංග්‍රීසි පෙළෙහි දැක්වෙන ආකාරයට]
සුදුසු HTML උපලකුණු භාවිත කර, රූපය 6.1 හි දැක්වෙන වෙබ් පිටුව විදහා දැක්වීමට අවශ්‍ය HTML ගොනුවක් නිර්මාණය කරන්න. ඔබගේ කේතය පහත දැක්වෙන අවශ්‍යතා තෘප්ත කළ යුතු ය.
ලැයිස්තුවේ (list) ඇති පාඨ මුද්‍රණ අක්ෂර වර්ගය (font) 'Calibri', ලක්ෂ (point) 14 ක් උස හා රතු වර්ණයෙන් ආකෘති කරන්න. ලැයිස්තුව සඳහා පෙරනිමි (bullet) හතරැස් විය යුතුය. අභ්‍යන්තර හෝ බාහිර රටා පත්‍ර පමණක් භාවිතයෙන් ලැයිස්තුව ආකෘති කළ යුතුය.
තව ද, පරිශීලකයෙකු වෙබ් පිටුවේ ඇති 'online entry form' අධිපෙළ (hypertext) ක්ලික් කළ විට රූපය 6.2 හි දැක්වෙන ඇතුළත් වීමේ පෝරමය අලුත් පටිත්තක/පිටුවක විදහු විය යුතුය. ඇතුළත් වීමේ පෝරමය සහිත වෙබ් පිටුවේ HTML ගොනුවේ නම 'form.html' යැයි උපකල්පනය කරන්න.
(b) සුදුසු HTML උපලකුණු භාවිත කර, රූපය 6.2 හි ඇතුළත් වීමේ පෝරමය විදහු කිරීමට HTML ගොනුවක් නිර්මාණය කරන්න. රූපය 6.3 හි 'Grade Category' සඳහා විකල්ප දී ඇත. ඔබගේ කේතය පහත දැක්වෙන අවශ්‍යතා තෘප්ත කළ යුතු ය. 'Clear your Entries' බොත්තම ක්ලික් කළ විට, පෝරමයේ ඇති සියලු ම නිවේශික (entries) මැකී යා (Clear) යුතුයි. එලෙස ම 'Submit' බොත්තම ක්ලික් කළ විට, පෝරමය සේවාදායකයට යොමු විය (Submit) යුතුයි.
[රූපය 6.3: Grade Category සඳහා විකල්ප: Grade 1 -2, Grade 3 -6, Grade 7 -10, Grade 11 -13]""")

assert len(E)==14,len(E)
json.dump(E,open('D:/DevOps/aws-clf-c02-bridge/tools/transcribed/ictl-web-essay.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
print(len(E))
