import json
P='D:/DevOps/aws-clf-c02-bridge/tools/'
src=json.load(open(P+'ict-lessons-images.json',encoding='utf8'))
ds=[q['d'] for s in src['sets'] if s['id']=='ictl-fund-essay' for q in s['qs']]
Q=[]
Q.append(("1. (b) Draw a diagram to depict the fetch-execute cycle used in program execution.",
"1. (b) ක්‍රමලේඛ ක්‍රියාත්මක වීමේදී භාවිත වන ආහරණ - ක්‍රියාකරවුම් චක්‍රය (Fetch-execute cycle) නිරූපණය කිරීමට රූපසටහනක් අඳින්න."))
Q.append(("""2. (a) Classify the following software as either "system software" or as "application software".
Software | Classification
Linux | ........
Word Processor | ........
Web Browser | ........
(b) Computer storage devices can be categorized into three types based on the medium used to store /retrieve data. State the three types of media and give an example for each type.
(c) The transaction file in a company's payroll system includes employee number, hours worked department code, and week number. Assume that the system maintains a Employee master table and a Department master table. Encircle the most appropriate validation check for each of the data elements given in the following table.
Data element | Validation checks
employee Number | Presence in Employee master table / Numerical check
hours worked | Presence in Employee master table / Range check
department code | Presence in Department master table / Range check
week number | Length / Range check
(d) Describe the terms "Video conferencing" and "Copyright".""",
"""2. (a) පහත දක්වා ඇති මෘදුකාංග "පද්ධති මෘදුකාංග" (System software) හෝ "යෙදුම් මෘදුකාංග" (Application software) ලෙස වර්ගීකරණ කරන්න.
(b) දත්ත ගබඩා කිරීම/සම්මුද්‍රණය (Retrieve) සඳහා භාවිත වන මාධ්‍යය (Medium) පාදක කරගෙන පරිගණක ආවයන (Storage) පද්ධති ආකාර තුනකට වර්ග කළ හැකිය. මෙම ආකාර තුන සඳහන් කර, එක් එක් ආකාරයට උදාහරණ බැගින් ලබා දෙන්න.
(c) සමාගමක වැටුප් ලැයිස්තු පද්ධතියේ ගනුදෙනු ගොනුවේ (Transaction file) සේවක අංකය, වැඩකළ පැය ගණන, දෙපාර්තමේන්තු කේතය හා සති අංකය අඩංගු වේ. පද්ධතියේ "Employee master" හා "Department master" යන වගු පවතී යැයි උපකල්පනය කරන්න. පහත වගුවේ එක් එක් දත්ත අයිතමය සඳහා වඩාත් ම සුදුසු සප්‍රමාණතා පිරික්සුම (Validation check) රවුම් කර දක්වන්න.
(d) "වීඩියෝ සම්මන්ත්‍රණ පැවැත්වීම" (Video conferencing) සහ "කර්තෘ හිමිකම" (Copyright) යන පද විස්තර කරන්න."""))
Q.append(("""3. (a) What do you mean by the terms "privacy" and "software piracy"?
(b) Describe the term "mobile computing".
(c) Consider the following scenario:
A semi conductor manufacturing company has branches in Japan and USA. At present, representatives of the development team should visit other branches of the company frequently to discuss their technical issues, Over the years, the company has realized this mechanism is costly and time consuming.
(i) As an ICT student, suggest an ICT based method to conduct these technical review meetings without visiting the other branches.
(ii) Name three essential ICT devices required for the method suggested in (i) above.""",
"""3. (a) "පෞද්ගලිකත්වය" (privacy) සහ "මෘදුකාංග කොල්ලය" (software piracy) යන පදවලින් ඔබ අදහස් කරන්නේ කුමක්ද?
(b) "ජංගම අංගනනය" (mobile computing) යන පදය විස්තර කරන්න.
(c) පහත දැක්වෙන සන්දර්භය සලකා බලන්න:
අර්ධ සන්නායක (semi conductor) නිෂ්පාදන සමාගමකට ජපානයෙහි සහ ඇමරිකා එක්සත් ජනපදයෙහි ශාඛා තිබේ. වර්තමානයේදී සංවර්ධන කණ්ඩායමේ නියෝජිතයන්ට ඔවුන්ගේ තාක්ෂණික ගැටලු සාකච්ඡා කිරීම සඳහා සමාගමේහි අනෙකුත් ශාඛාවලට නිරන්තරයෙන් යාමට සිදුවී තිබේ. මෙම යාන්ත්‍රණය බොහෝ වියදම් සහිත සහ කාලය වැයවන සුළු බව වසර ගණනාවක් තිස්සේ සමාගම හඳුනාගෙන ඇත.
(i) අනෙකුත් ශාඛාවලට ගමන් කිරීමෙන් තොරව මෙම තාක්ෂණ විමර්ශන රැස්වීම් පැවැත්වීම සඳහා තොරතුරු හා සන්නිවේදන (ICT) තාක්ෂණය පදනම් කරගත් ක්‍රමයක්, ICT විෂය හදාරන සිසුවකු ලෙස ඔබ යෝජනා කරන්න.
(ii) ඉහත (i) කොටසේ යෝජිත ක්‍රමය සඳහා අත්‍යවශ්‍ය "තොරතුරු හා සන්නිවේදන (ICT) උපාංග" තුනක් නම් කරන්න."""))
Q.append(("""4.(a) Consider the following diagram which shows how the abstract layers of a computer system are related.
[Figure: a row of boxes "user 1", "user 2", "user 3", ..., "user n" at the top, each with a double-headed arrow to a large rectangle below. The rectangle is divided into three horizontal bands. The top band contains the circled label A at its left and the entries "assembler", "word processor", ..., "database system". The second band is labelled B, the third band C and the bottom band D (the circled labels B, C, D sit at the left edge beside the bands, from top to bottom: B, C, D).]
Choose and write down the correct terms from the list given below for labels A, B, C and D.
List: {compiler, computer hardware, live-ware, operating system, system/application programs}""",
"""4.(a) පරිගණක පද්ධතියක අමූර්ත ස්තර (abstract layers) එකිනෙකට සම්බන්ධ වන ආකාරය පෙන්වන පහත දැක්වෙන රූපසටහන සලකන්න.
A, B, C හා D යන ලේබලවලට අදාළ නිවැරදි පද පහත ලැයිස්තුවෙන් තෝරා ලියන්න.
ලැයිස්තුව : {සම්පාදකය, පරිගණක දෘඩාංග, ජීවාංග, මෙහෙයුම් පද්ධතිය, පද්ධති/යෙදුම් ක්‍රමලේඛ}"""))
Q.append(("""5.(a) (i) State two service models in cloud computing.
(ii) What are the three steps in the FETCH-EXECUTION cycle of a computer?""",
"""5.(a) (i) වලාකුළු පරිගණනයෙහි (cloud computing) සේවා ආකෘති (service models) දෙකක් ලියන්න.
(ii) පරිගණකයක ආහරණ-ක්‍රියාකරවුම් (Fetch-Execution) චක්‍රයෙහි පියවර තුන මොනවා ද?"""))
Q.append(("""[Note: the images for this item contain several question parts in sequence; transcribed in order.]
6. (a) Cloud Computing allows us to obtain computing resources and capabilities as a service. The three main types of cloud computing services are: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).
From those three cloud computing service types, write down the suitable service type for each of the following scenarios.
(i) To obtain an environment for application deployment and execution from a cloud service provider ..........
(ii) To obtain hard disk space for data storage from a cloud service provider ..........
(iii) To obtain data file sharing, office applications and email services from a cloud service provider ..........
(b) Fill the blanks in the following statements with suitable words from the given list of words.
(i) ............... helps to ensure the confidentiality of our data and information.
(ii) ............... is the attempt to acquire sensitive information by pretending as a trustworthy entity in an electronic communication.
(iii) The illegal copying, distribution, or use of software is known as ............... and ............... helps us to protect our software from such illegal use.
List of words: { Encryption, Copyright, Phishing, Plagiarism, Software piracy }
(2021 S.ESSAY - 02[a],[b])
7. (b) Write the most appropriate word or phrase to answer the following questions based on the description given below.
Recently introduced National Fuel Pass system in Sri Lanka is an example of how ICT can be used to overcome national challenges successfully. It is observed that for a given week, the maximum server hardware resource utilization happens only for a short period (e.g., few hours) and the rest of the time the system operates at a very low resource demand.
(i) One of the views on resource provision is to purchase computer hardware permanently considering the maximum demand. What is the main disadvantage with this approach?
(ii) What is the alternative solution to overcome the disadvantage mentioned in (b)(i) above, while satisfying the maximum resource demand instances?
(c) The steps in the fetch-execute cycle are as follows:
1. The ..........(P).......... is loaded with the memory address of the relevant instruction of the program.
2. The instruction is loaded into the instruction register.
3. The instruction present in the instruction register is decoded.
4. The control unit of the CPU passes the decoded instruction as a sequence of control signals to the relevant ..........(Q).......... of the CPU.
5. The program counter is changed to point to the next instruction.
6. Steps from Step 2 are repeated.
Select the most suitable items to replace the labels P and Q from the following list.
List: {file, functional unit, instruction, memory, page, program counter}
(2022 S.ESSAY - 04[b],[c])
8. (a) A simple and high-level view of the data lifecycle consists of three steps. Write the 2nd and the 3rd steps of the data life cycle.
1st step is: the creation of data
2nd step is: ........
3rd step is: ........
(d) (i) Your friend thinks the digital divide is a tool used for arithmetic division. Briefly explain to your friend what the digital divide is.
(ii) E-waste is becoming a major environmental problem in Sri Lanka. Suggest a step that we can take to reduce the environmental impact of our e-waste.
(2023 S.ESSAY - 02[a],[d])
9.(a) (i) Following diagram shows the abstract model of information creation:
[Figure: three boxes in a row connected by right arrows: A → B → C]
Identify the A, B and C above.   A: ........  B: ........  C: ........
(ii) Write down the A, B and C components of the above model for each of the following online activities:
Activity 1: Successfully logging in to your favourite online bookshop to buy stationery.
Activity 2: Selecting the items to purchase and adding them to your shopping trolley.
Activity 3: Successfully paying for your order using your debit card.
Activity 1 - A: ........ B: ........ C: ........
Activity 2 - A: ........ B: ........ C: ........
Activity 3 - A: ........ B: ........ C: ........
(iii) At a later date, after successfully logging in to this system to purchase the same items, you decide to use the 'Repeat Previous Order' option given at the site. Write down any changes to your answer for Activity 2 of part (ii) above.
Activity 2 - A: ........ B: ........ C: ........
(b) Open source software require the users to be technically skilled in setting up and configuring them. Briefly explain how the setting up and configuration are usually done in proprietary software.
(c) While Information and Communication Technology (ICT) allows us to create and disseminate our intellectual ideas in more efficient and impactful ways, it also contributes to a higher level of plagiarism than in traditional (non-ICT) methods. Briefly explain the reason for this observation.
(d) Some argue that the increasing use of Information and Communication Technology as an indirect contributor to global warming. Briefly explain a major reason for this view.
(2024 S.ESSAY - 02)
1(a) (i) Describe the main difference between data and information by using a suitable system.
(ii) Give three drawbacks of manual methods in manipulating data in bulk.
(iii) Describe the terms hardware, software and firmware using examples.
(2011 ESSAY - 01[a])""",
"""9.(a) (i) පහත රූප සටහනින් පෙන්වන්නේ තොරතුරු නිර්මාණය කිරීමේ වියුක්ත ආකෘතියකි. ඉහත A, B සහ C හඳුනාගන්න.
(ii) පහත දැක්වෙන එක් එක් මාර්ගගත ක්‍රියාකාරකම් සඳහා, ඉහත ආකෘතියේ A, B සහ C සංරචක ලියා දක්වන්න.
1 ක්‍රියාකාරකම: ලිපිද්‍රව්‍ය මිලදී ගැනීමට ඔබගේ ප්‍රියතම මාර්ගගත පොත් සප්පුවට සාර්ථකව පුරන (login) වීම
2 ක්‍රියාකාරකම: මිලදී ගන්නා අයිතම තෝරා ඒවා ඔබගේ බඩු ට්‍රොලියට (shopping trolley) එකතු කිරීම
3 ක්‍රියාකාරකම: ඇනවුම සඳහා ගෙවීම ඔබගේ හරපත (debit card) භාවිතා කර සාර්ථකව සිදු කිරීම
(iii) පසු දිනයක සාර්ථකව මෙම පද්ධතියට පුරන වූවාට පසු එම අයිතම ම නැවත මිලදී ගැනීමට අඩවියේ ඇති Repeat Previous Order විකල්පය භාවිතා කිරීමට ඔබ තීරණය කරයි. ඉහත (ii) කොටස සඳහා ඔබ 2 ක්‍රියාකාරකම අදාළව දුන් පිළිතුරෙහි වෙනස්කම් ඇතොත් ඒවා ලියා දක්වන්න.
(b) විවෘත මූලාශ්‍ර (open source) මෘදුකාංග ස්ථාපනය (setup) සහ වින්‍යාස (configure) කිරීමට පරිශීලකයන්ට තාක්ෂණික කුසලතා තිබීම අවශ්‍ය වේ. හිමිකම් සහිත (proprietary) මෘදුකාංගවල ස්ථාපනය සහ වින්‍යාස කිරීම සාමාන්‍යයෙන් සිදු කෙරෙන ආකාරය කෙටියෙන් පහදන්න."""))
Q.append(("""1(a) (i) Describe the main difference between data and information by using a suitable system.
(ii) Give three drawbacks of manual methods in manipulating data in bulk.
(iii) Describe the terms hardware, software and firmware using examples.""",
"""1(a) (i) දත්ත සහ තොරතුරු අතර ප්‍රධාන වෙනස සුදුසු පද්ධතියක් අනුසාරයෙන් විස්තර කරන්න.
(ii) විශාල පරිමාණයෙන් දත්ත පරිහරණය කිරීමේදී අත්‍යවශ්‍ය (manual) ක්‍රම යොදාගැනීමේ අඩුපාඩු තුනක් දක්වන්න.
(iii) නිදසුන් යොදාගනිමින් දෘඩාංග (hardware), මෘදුකාංග (software) සහ ස්ටිරාංග (firmware) යන පද විස්තර කරන්න."""))
Q.append(("""2. (b) Computer storage devices can be categorized into three types based on the medium used to store /retrieve data. State the three types of media and give an example for each type.""",
"""2. (b) දත්ත ගබඩා කිරීම/සම්මුද්‍රණය (Retrieve) සඳහා භාවිත වන මාධ්‍යය (Medium) පාදක කරගෙන පරිගණක ආවයන (Storage) පද්ධති ආකාර තුනකට වර්ග කළ හැකිය. මෙම ආකාර තුන සඳහන් කර, එක් එක් ආකාරයට උදාහරණ බැගින් ලබා දෙන්න."""))
Q.append(("""1. (a) What are the three (3) main components of a Central Processing Unit (CPU) of a typical computer? List the main functions of these three components.""",
"""1. (a) ආකෘතික පරිගණකයක (Typical computer) මධ්‍ය සැකසුම් ඒකකයේ (CPU) ප්‍රධාන සංරචක තුන මොනවා ද? මෙම සංරචක තුනෙහි ප්‍රධාන කාර්යයන් ලැයිස්තුගත කරන්න."""))
Q.append(("""2.(a) (i) Explain one (1) way in which the bar code technology can be beneficial to a library management system.
(ii) Most modern computers have multiple processors in them. Explain one (1) way in which the multiple processors in such computers can be beneficial.
(iii) Explain what is meant by volatile memory and write down one (1) example for such selecting from the list below.
List: { Dynamic RAM (DRAM), Hard disk, L1 cache, Registers }""",
"""2.(a) (i) තීරු කේත (bar code) තාක්ෂණය, පුස්තකාල කළමනාකරණ පද්ධතියට ප්‍රයෝජනවත් විය හැකි ආකාරයක් (1) විස්තර කරන්න.
(ii) නූතන පරිගණක බොහොමයක සකසන (processor) කිහිපයක් ඇත. එවැනි පරිගණකවල එකකට වඩා වැඩි සකසන තිබීමෙන් ප්‍රයෝජනවත් වන ආකාරයක් (1) විස්තර කරන්න.
(iii) ගතික (volatile) මතකය යන්නෙන් කුමක් අදහස් වේදැයි පහදා එවැන්නකට උදාහරණයක් (1) පහත ලැයිස්තුවෙන් තෝරා ලියන්න.
ලැයිස්තුව : { ගතික සසම්භාවී ප්‍රවේශ මතකය (DRAM), දෘඩ ඩිස්කය, L1 නිහිත මතකය, රෙජිස්ටර් }"""))
assert len(Q)==len(ds)==10
out=[]
for d,(q,qs) in zip(ds,Q):
    out.append({"d":d,"q":q,"qs":qs})
json.dump(out,open(P+'transcribed/ictl-fund-essay.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
print(len(json.load(open(P+'transcribed/ictl-fund-essay.json',encoding='utf8'))))
