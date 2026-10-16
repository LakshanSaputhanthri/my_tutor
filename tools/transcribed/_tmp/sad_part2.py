import json
idx=json.load(open('D:/DevOps/aws-clf-c02-bridge/tools/ict-lessons-images.json',encoding='utf-8'))
s=[x for x in idx['sets'] if x['id']=='ictl-sad-mcq'][0]['qs'][38:75]
data={}
def m(i,q,qs,o,os=None):
    r={"q":q}
    if qs: r["qs"]=qs
    r["o"]=o
    if os: r["os"]=os
    data[i]=r

def split(pairs):
    return [p[0] for p in pairs],[p[1] for p in pairs]

ALLS="ඉහත සියල්ලම"

m(39,"Which of the following shows the correct order of software testing?",
 "පහත කවරකින් මෘදුකාංග පරීක්ෂාවෙහි (software testing) නිවැරදි අනුපිළිවෙළ දැක්වෙයි ද?",
 ["acceptance testing → system testing → integration testing → unit testing",
  "unit testing → acceptance testing → system testing → integration testing",
  "unit testing → integration testing → acceptance testing → system testing",
  "unit testing → integration testing → system testing → acceptance testing",
  "white-box testing → black-box testing → system testing → unit testing"],
 ["ප්‍රතිග්‍රහණ පරීක්ෂාව → පද්ධති පරීක්ෂාව → ඒකාබද්ධ පරීක්ෂාව → ඒකක පරීක්ෂාව",
  "ඒකක පරීක්ෂාව → ප්‍රතිග්‍රහණ පරීක්ෂාව → පද්ධති පරීක්ෂාව → ඒකාබද්ධ පරීක්ෂාව",
  "ඒකක පරීක්ෂාව → ඒකාබද්ධ පරීක්ෂාව → ප්‍රතිග්‍රහණ පරීක්ෂාව → පද්ධති පරීක්ෂාව",
  "ඒකක පරීක්ෂාව → ඒකාබද්ධ පරීක්ෂාව → පද්ධති පරීක්ෂාව → ප්‍රතිග්‍රහණ පරීක්ෂාව",
  "ශ්වේත මංජුසා පරීක්ෂාව → කාළ මංජුසා පරීක්ෂාව → පද්ධති පරීක්ෂාව → ඒකක පරීක්ෂාව"])

e,si=split([("agile","සුචල"),("prototyping","මූලාකෘතිකරණය"),("rapid application development","ශීඝ්‍ර යෙදවුම් සංවර්ධනය"),("spiral","සර්පිල"),("waterfall","දියඇලි")])
m(40,"A software development company identifies that their new system development project has complex requirements and has a medium to high risk level. Further, an evaluation is needed to clear the requirements and significant changes are expected during system development. What is the most suitable software development process model for this project?",
 "මෘදුකාංග සංවර්ධන සමාගමක් තම නව ව්‍යාපෘතිය සංකීර්ණ අවශ්‍යතාවලින් සමන්විත බව, මධ්‍යම (medium) සිට ඉහළ (high) දක්වා අවදානම් (risk) මට්ටමක් ඇති බව හඳුනාගනියි. තවද අවශ්‍යතා පැහැදිලි කර ගැනීමට ඇගයීමක් (evaluation) අවශ්‍ය බවත් පද්ධති සංවර්ධන ක්‍රියාවලියේ දී සැලකිය යුතු වෙනස්කම් අපේක්ෂා කරන බවත් හඳුනාගනියි. මෙම ව්‍යාපෘතිය සඳහා වඩාත්ම සුදුසු මෘදුකාංග සංවර්ධන ක්‍රියාවලි ආකෘතිය (software development process model) කුමක් ද?",e,si)

m(41,"Which of the following indicates a non-functional requirement?\nA - A user shall be allowed to upload an image to the system to be used as his/her profile picture.\nB - The correct invoice value should be calculated including applicable tax rates at the check-out.\nC - The system must satisfy 99.9% availability of service.",
 "පහත කුමකින් කාර්යබද්ධ නොවන (non functional) අවශ්‍යතාවක්/අවශ්‍යතා දැක්වෙයි ද?\nA - රූපයක් තමන්ගේ පැතිකඩ ඡායාරූපය (profile picture) ලෙස පද්ධතියට උඩුගත කිරීමට පරිශීලකයෙකුට අවස්ථාව තිබිය යුතු ය.\nB - පිටවීම පරීක්ෂාවේදී (check-out) අදාළ බදු අනුපාත ඇතුළත්ව නිවැරදි ඉන්වොයිස් (invoice) අගය ගණනය කළ යුතු ය.\nC - පද්ධතියෙහි සේවා පැවැත්ම (service availability) 99.9% ක් සපුරාලිය යුතු වේ.",
 ["A only.","B only.","C only.","A and B only.","All of the above"],
 ["A පමණි.","B පමණි.","C පමණි.","A හා B පමණි.",ALLS])

m(42,"What is the correct statement related to system deployment?",
 "පද්ධති ස්ථාපනය කිරීම (system deployment) පිළිබඳ නිවැරදි ප්‍රකාශය කුමක් ද?",
 ["Direct deployment is the most complex and the slowest form of deployment.",
  "In pilot deployment, all the users have the ability to use the system at the beginning.",
  "In parallel deployment old and new systems are used at the same time.",
  "Phased deployment do not allow users to develop skills required for new system gradually.",
  "Phased deployment means the entire system is used in one location."],
 ["සෘජු ස්ථාපනය වඩාත් ම සංකීර්ණ මෙන්ම සෙමෙන් ක්‍රියාත්මක වන ස්ථාපන ක්‍රමයකි.",
  "නියමු ස්ථාපනයේ දී, සියලු පරිශීලකයන්ට ආරම්භයේ දී පද්ධති භාවිත කිරීමට හැකියාව ලැබේ.",
  "සමාන්තර ස්ථාපනයේ දී, පැරණි සහ නව පද්ධති එකවර භාවිත කෙරේ.",
  "අවධි ස්ථාපනය මගින් පරිශීලකයන්ට නව පද්ධතිය පිළිබඳ අවශ්‍ය වන ශිල්පක්‍රම ක්‍රමානුකූලව වර්ධනය කර ගැනීමට අවස්ථාව ලබා නොදේ.",
  "අවධි ස්ථාපනය යනු මුළු පද්ධතියම එක් ස්ථානයක පමණක් භාවිත කිරීම ය."])

m(43,"Which of the following statement/s regarding the testing of a system are correct?\nA - Black-box testing involves detailed checking of each line in the code.\nB - Unit-testing helps to uncover errors in the codes.\nC - System testing should not be performed prior to unit-testing.",
 "පද්ධතියක හරි වැරදි බැලීම (පරීක්ෂා කිරීම) (testing) සම්බන්ධයෙන් පහත කවර වගන්තිය/ය නිවැරදි වේ ද?\nA - කාල මංජුසා පරීක්ෂාවට (black box testing) කේතයෙහි සෑම පේළියක්ම විස්තරාත්මකව පරීක්ෂා කිරීම අඩංගු වේ.\nB - ඒකක පරීක්ෂාව (unit testing) කේතවල දෝෂ අනාවරණය කිරීමට උපකාරී වේ.\nC - ඒකක පරීක්ෂාවට පෙර පද්ධති පරීක්ෂාව සිදු නොකළ යුතු ය.",
 ["A only.","B only.","C only.","A and C only.","B and C only"],
 ["A පමණි.","B පමණි.","C පමණි.","A හා C පමණි.","B හා C පමණි."])

m(44,"Which of the following indicate functional requirements?\nA - The users should be allowed to update their contact addresses and phone numbers.\nB - Any user request must be responded within 2 ms.\nC - The system must be easy to change.",
 "පහත කවරක් කාර්යබද්ධ අවශ්‍යතා (functional requirements) දක්වයි ද?\nA - පරිශීලකයන්ට තමන්ගේ ලිපින හා දුරකතන අංක යාවත්කාලීන කිරීමට අවස්ථාව ලබා දිය යුතු ය.\nB - ඕනෑම පරිශීලක ඉල්ලීමකටම 2 ms ක කාලයක් තුළ ප්‍රතිචාර දැක්විය යුතු ය.\nC - පද්ධතිය පහසුවෙන් වෙනස් කිරීමට හැකි විය යුතු ය.",
 ["A only.","B only.","C only.","A and C only.","All of the above"],
 ["A පමණි.","B පමණි.","C පමණි.","A හා C පමණි.",ALLS])

m(45,"The following details are given about a software project:\nA - requirements are fixed (not allowed to change throughout the complete project).\nB - must deliver the complete software product at once\nC - detailed descriptions and specifications must be prepared for each activity within the project\nWhat is the most suitable software process model for this project?",
 "මෘදුකාංග ව්‍යාපෘතියකට අදාල ව පහත විස්තර ලබා දී ඇත.\nA - අවශ්‍යතාවයන් ස්ථිර වේ (මුළු ව්‍යාපෘතිය පුරාවට වෙනස්කම් සඳහා ඉඩ නොලැබේ).\nB - සම්පූර්ණ මෘදුකාංග නිෂ්පාදිතය එකවර ලබා දිය යුතු ය.\nC - ව්‍යාපෘතිය තුළ එක් එක් ක්‍රියාකාරකම් (activity) සඳහා සියලු විස්තර සහ පිරිවිතර ව්‍යාපෘති අතරතුර සූදානම් කළ යුතු ය.\nමෙම ව්‍යාපෘතිය සඳහා වඩාත් ම සුදුසු මෘදුකාංග ක්‍රියායන ආකෘතිය (software process model) කුමක් ද?",e,si)

m(46,"Which of the following statements on Data Flow Diagrams (DFD) is incorrect?",
 "දත්ත ගැලීම් සටහන් (Data Flow Diagram-DFD) පිළිබඳ පහත කවර වගන්තිය සාවද්‍ය වේ ද?",
 ["Context diagram is a DFD with the highest level of abstraction.",
  "All data stores in a system must be represented in the context diagram.",
  "Data flows are used to link the other components in DFDs.",
  "Elementary processes are not decomposed further.",
  "External entities in DFDs act as sources or recipients of data."],
 ["සන්දර්භ (context) සටහන යනු ඉහළම මට්ටමේ වියුක්තකරණය (abstraction) ඇති දත්ත ගැලීම් සටහනකි.",
  "පද්ධතියේ ඇති සියලු ම දත්ත ගබඩා (data stores) සන්දර්භ සටහනෙහි නිරූපණය කළ යුතු ය.",
  "DFD හි අනෙකුත් සංරචක සම්බන්ධ කිරීම සඳහා දත්ත ගැලීම් භාවිත කෙරේ.",
  "මූලික ක්‍රියායන (elementary processes) තවදුරටත් විඛණ්ඩනය (decompose) නොකෙරේ.",
  "DFD හි බාහිර ආයතන (external entities) දත්ත ප්‍රභව (sources) හෝ දත්ත ලබාගන්නන් (recepients) අංග ලෙස ක්‍රියා කෙරේ."])

m(47,"Which of the following is incorrect about the Agile Method?",
 "සුචල ක්‍රමය (agile method) සම්බන්ධයෙන් වැරදි වන්නේ පහත කුමක් ද?",
 ["It cannot be used when the project has a fixed set of requirements.",
  "It recommends a time sliced schedule for task completion.",
  "It delivers gradual builds of the working product in an iterative manner.",
  "It facilitates stakeholders (e.g., buyer, user) to review progress and provide feedback at every phase.",
  "The product of each build is tested independently."],
 ["ව්‍යාපෘතියට නිශ්චිත අවශ්‍යතා කුලකයක් ඇති විට මෙය යොදාගත නොහැකි ය.",
  "කාර්ය නිම කිරීම සඳහා කාණ්ඩවලට බෙදූ කාලසටහනක් නිර්දේශ කරයි.",
  "ක්‍රමිකව, ක්‍රියාත්මක මට්ටමේ නිෂ්පාදිතයක් පුනරාවර්තන ආකාරයෙන් ලබා දේ.",
  "සෑම අදියරකදීම අදාළ පුද්ගලයින්ට (උදා: ගැනුම්කරු, පරිශීලකයා) ප්‍රගතිය සමාලෝචනය කර ප්‍රතිපෝෂණ ලබාදීමට පහසුකම් ලබා දේ.",
  "සෑම අදියරේදීම නිමවුම ස්වාධීනව පරීක්ෂා (test) කෙරේ."])

m(48,"Consider the information system types in List A and some examples in List B:\nList A: A1 - Enterprise Resource Planning System; A2 - Expert system; A3 - Transaction processing system\nList B: B1 - A customer account system in a bank; B2 - A system that facilitates manufacturing, marketing and sales of a garment business; B3 - A system that prescribes ayurvedic medicines using a knowledge base\nA good matching between lists A and B is:",
 "A ලැයිස්තුවේ දක්වා ඇති තොරතුරු පද්ධති වර්ග කිහිපය හා B ලැයිස්තුවේ ඇති නිදසුන් කිහිපය සලකන්න:\nA ලැයිස්තුව: A1 - ව්‍යවසාය සම්පත් සැලසුම් පද්ධතිය; A2 - විශේෂඥ පද්ධතිය; A3 - ගනුදෙනු සැකසුම් පද්ධතිය\nB ලැයිස්තුව: B1 - බැංකුවක පවතින පාරිභෝගික ගිණුම් පද්ධතියකි; B2 - නිමි ඇඳුම් ව්‍යාපාරයක නිෂ්පාදනය, අලෙවිකරණය හා වෙළෙඳාම පහසු කරන පද්ධතියකි; B3 - දැනුම් ගබඩාවක් භාවිත කරමින් ආයුර්වේද ඖෂධ නියම කරන පද්ධතියකි\nA සහ B ලැයිස්තු අතර නිවැරදි ගැලපීම වන්නේ:",
 ["A1 – B1, A2 – B2, A3 – B3","A1 – B2, A2 – B3, A3 – B1","A1 – B3, A2 – B1, A3 – B2","A1 – B2, A2 – B1, A3 – B3","A1 – B3, A2 – B2, A3 – B1"])

m(49,"Which of the following statements is/are correct with respect to Object Oriented Programming?\nA - System output is determined by the object behaviour and their interactions.\nB - System is modelled as a collection of objects.\nC - Writing a program in this method is different from writing one according to the structured programming method.",
 "වස්තු නැඹුරු ක්‍රමලේඛනය (Object Oriented Programming) සම්බන්ධයෙන් පහත කවර ප්‍රකාශය/ප්‍රකාශ නිවැරදි වේ ද?\nA - පද්ධති ප්‍රතිදානය තීරණය වන්නේ වස්තු හැසිරීම හා ඒවායේ අන්තර්ක්‍රියා මගිනි.\nB - පද්ධතිය වස්තූන්ගේ එකතුවක් ලෙස ආකෘතිගත කෙරේ.\nC - මෙලෙස ක්‍රමලේඛයක් ලිවීම, ව්‍යුහගත (structured) ක්‍රමයට ක්‍රමලේඛයක් ලිවීමට වඩා වෙනස් වේ.",
 ["A only.","B only.","C only.","A and C only.","All of the above"],
 ["A පමණි.","B පමණි.","C පමණි.","A හා C පමණි.",ALLS])

m(50,"Which of the following lists the activities of Structured System Analysis and Design Methodology (SSADM) in the correct order?",
 "ව්‍යුහගත පද්ධති විශ්ලේෂණ සහ නිර්මාණ ක්‍රමවේදයේ (SSADM) ක්‍රියාකාරකම් නිවැරදිව පෙළගස්වා ඇත්තේ පහත කවරක ද?",
 ["Feasibility study, Physical design, Requirement analysis, Requirement specification, System development",
  "Feasibility study, Requirements analysis, Requirement specification, Logical system specification, Physical design",
  "Feasibility study, Requirement specification, Requirements analysis, Logical system specification, Physical design",
  "Requirements analysis, Logical system specification, Feasibility study, Requirement specification, Physical design",
  "Requirements analysis, Requirement specification, Feasibility study, Physical design, System development"],
 ["ශක්‍යතා අධ්‍යයනය, භෞතික නිර්මාණය, අවශ්‍යතා විශ්ලේෂණය, අවශ්‍යතා පිරිවිතර සැකසීම, පද්ධති සංවර්ධනය",
  "ශක්‍යතා අධ්‍යයනය, අවශ්‍යතා විශ්ලේෂණය, අවශ්‍යතා පිරිවිතර සැකසීම, තාර්කික පද්ධති පිරිවිතර සැකසීම, භෞතික නිර්මාණය",
  "ශක්‍යතා අධ්‍යයනය, අවශ්‍යතා පිරිවිතර සැකසීම, අවශ්‍යතා විශ්ලේෂණය, තාර්කික පද්ධති පිරිවිතර සැකසීම, භෞතික නිර්මාණය",
  "අවශ්‍යතා විශ්ලේෂණය, තාර්කික පද්ධති පිරිවිතර සැකසීම, ශක්‍යතා අධ්‍යයනය, අවශ්‍යතා පිරිවිතර සැකසීම, භෞතික නිර්මාණය",
  "අවශ්‍යතා විශ්ලේෂණය, අවශ්‍යතා පිරිවිතර සැකසීම, ශක්‍යතා අධ්‍යයනය, භෞතික නිර්මාණය, පද්ධති සංවර්ධනය"])

fig51="[Figure: Level 1 DFD. External entity 'Passenger' sends flow P to process box R. External entity 'Taxi driver' sends flow Q to process box R. Process R sends flow S down to the process 'Make closest taxi driver list'. That process sends 'Closest taxi driver list' back to the entity 'Passenger'.]"
m(51,"A system that gives the list of closest taxi drivers to a passenger is to be developed. Answer questions 51 and 52 with respect to it.\nAssume that the following is the Level 1 DFD for this system:\n"+fig51+"\nWhich of the following contains the suitable replacements for P, Q, R and S in the above diagram?",
 "මගියෙකුට ආසන්නතම ටැක්සි රියදුරන්ගේ ලැයිස්තුවක් ලබාදෙන පද්ධතියක් සැදීමට අවශ්‍ය ය. එයට අදාළව ඇති 51 සහ 52 ප්‍රශ්නවලට පිළිතුරු සපයන්න.\nපහතින් දක්වා ඇත්තේ පද්ධතියට අදාළ පළමු මට්ටමේ DFD රූ සටහන යැයි සලකන්න.\nඉහත රූපයේ P, Q, R සහ S සඳහා නිවැරදි ආදේශ කිරීම් දක්වන්නේ පහත කවරක් ද?",
 ["P - Location, Q - Driver code, R - Get passenger and driver locations, S - Passenger and driver locations",
  "P - Location, Q - Driver code and location, R - Get passenger and driver details, S - Passenger and driver details",
  "P - NIC number, Q - NIC number, R - Get passenger and driver NIC numbers, S - Passenger and driver NIC numbers",
  "P - Passenger code, Q - Driver code, R - Get passenger and driver codes, S - Passenger and driver codes",
  "P - Passenger code, Q - Location, R - Get passenger and driver locations, S - Passenger and driver locations"],
 ["P - ස්ථානය, Q - රියැදුරු කේතය, R - මගියාගේ සහ රියදුරුන්ගේ ස්ථානයන් ලබාගන්න, S - මගියාගේ සහ රියදුරුන්ගේ ස්ථාන",
  "P - ස්ථානය, Q - රියැදුරු කේතය සහ ස්ථානය, R - මගියාගේ සහ රියදුරුන්ගේ විස්තර ලබාගන්න, S - මගියාගේ සහ රියදුරුන්ගේ විස්තර",
  "P - NIC අංකය, Q - NIC අංකය, R - මගියාගේ සහ රියදුරුන්ගේ NIC අංක ලබාගන්න, S - මගියාගේ සහ රියදුරුන්ගේ NIC අංක",
  "P - මගියාගේ කේතය, Q - රියැදුරු කේතය, R - මගියාගේ සහ රියදුරුන්ගේ කේත ලබාගන්න, S - මගියාගේ සහ රියදුරුන්ගේ කේත",
  "P - මගියාගේ කේතය, Q - ස්ථානය, R - මගියාගේ සහ රියදුරුන්ගේ ස්ථානයන් ලබාගන්න, S - මගියාගේ සහ රියදුරුන්ගේ ස්ථාන"])

e,si=split([("NIC data","NIC දත්ත"),("Passenger details","මගීන්ගේ විස්තර"),("Taxi driver details","ටැක්සි රියදුරුන්ගේ විස්තර"),("Travel cost details","ගමන් වියදම් විස්තර"),("Weather records","කාලගුණ වාර්තා")])
m(52,"(Context from Q51: a system that gives the list of closest taxi drivers to a passenger.)\nAbove Level-1 DFD was later improved so that a data store (D1) was connected to the process labelled R. What could be this data store?",
 "ඉහත පළමු මට්ටමේ DFD රූ සටහන පසුව දියුණු කරනු ලදුව, දත්ත ගබඩාවක් (D1), R ක්‍රියාවලියට සම්බන්ධ කරන ලදි. එම දත්ත ගබඩාව කුමක් විය හැකි ද?",e,si)

m(53,"Which of the following gives a suitable order of activities to follow when developing a system that involves a database?",
 "දත්ත සමුදායක් භාවිතයට ගෙන්නා පද්ධතියක් නිර්මාණය කිරීමට අනුගමනය කළ යුතු ක්‍රියාකාරකම් නිවැරදි අනුපිළිවෙලින් දක්වන්නේ පහත කවරක් ද?",
 ["Design the database, Draw the DFD, Draw the ER diagrams, Do the coding, Write the pseudo-code",
  "Design the database, Write the pseudo-code, Draw the ER diagrams, Draw the DFD, Do the coding",
  "Do the coding, Write the pseudo-code, Design the database, Draw the ER diagrams, Draw the DFD",
  "Draw the DFD, Draw the ER diagrams, Design the database, Write the pseudo-code, Do the coding",
  "Draw the ER diagrams, Do the coding, Write the pseudo-code, Design the database, Draw the DFD"],
 ["දත්ත සමුදාය නිර්මාණය කිරීම, DFD රූ සටහන ඇඳීම, භූතාර්ථ සම්බන්ධතා (ER) රූ සටහන ඇඳීම, කේතනය කිරීම, ව්‍යාජ කේතය ලිවීම",
  "දත්ත සමුදාය නිර්මාණය කිරීම, ව්‍යාජ කේතය ලිවීම, ER රූ සටහන ඇඳීම, DFD රූ සටහන ඇඳීම, කේතනය කිරීම",
  "කේතනය කිරීම, ව්‍යාජ කේතය ලිවීම, දත්ත සමුදාය නිර්මාණය කිරීම, ER රූ සටහන ඇඳීම, DFD රූ සටහන ඇඳීම",
  "DFD රූ සටහන ඇඳීම, ER රූ සටහන ඇඳීම, දත්ත සමුදාය නිර්මාණය කිරීම, ව්‍යාජ කේතය ලිවීම, කේතනය කිරීම",
  "ER රූ සටහන ඇඳීම, කේතනය කිරීම, ව්‍යාජ කේතය ලිවීම, දත්ත සමුදාය නිර්මාණය කිරීම, DFD රූ සටහන ඇඳීම"])

m(54,"Which of the following statements is/are correct about acceptance testing?\nA - Acceptance testing is done when the user requirements of the software are analysed.\nB - An essential activity in acceptance testing is checking through the conditional statements and loops in the code.\nC - Users may refuse to accept the software after the Acceptance Test.",
 "ප්‍රතිග්‍රහණ පරීක්ෂාව (acceptance testing) සම්බන්ධයෙන් පහත කවර වගන්තිය/ වගන්ති නිවැරදි වේ ද?\nA - මෘදුකාංගයෙන් පරිශීලකයා අපේක්ෂා කරන දෙය විශ්ලේෂණය කරන අතරතුර ප්‍රතිග්‍රහණ පරීක්ෂාව සිදු කෙරේ.\nB - කේතයේ කොන්දේසි සහිත වගන්ති (conditional statements) සහ ලූප (loops) පරීක්ෂා කිරීම ප්‍රතිග්‍රහණ පරීක්ෂාවේ අත්‍යවශ්‍ය කාර්යයකි.\nC - ප්‍රතිග්‍රහණ පරීක්ෂාවට පසුව පරිශීලකයන් මෘදුකාංගය භාර නොගැනීමට ඉඩ ඇත.",
 ["A only.","B only.","C only.","A and C only.","All of the above"],
 ["A පමණි.","B පමණි.","C පමණි.","A හා C පමණි.",ALLS])

m(55,"Which of the following statements is correct about software deployment?",
 "මෘදුකාංග ස්ථාපනය (deployment) සම්බන්ධයෙන් පහත සඳහන් කවර වගන්තිය නිවැරදි වේ ද?",
 ["Direct deployment has the highest risk of complete failure but may be the only suitable method for some cases.",
  "Direct deployment is the most expensive and offers slowest learning to the users.",
  "Parallel deployment is the least expensive deployment option.",
  "Phased deployment does not provide the freedom for the relevant organization to make any needed adjustments to the system.",
  "Pilot deployment always rolls out the new system to a test user group larger than 50% of the users."],
 ["සෘජු (direct) ස්ථාපනය පූර්ණ බිඳවැටීමක් සිදුවීමේ වැඩි ම අවදානමක් සහිත වුව ද සමහර අවස්ථා සඳහා එය එකම සුදුසු ක්‍රමය වේ.",
  "සෘජු ස්ථාපනය වැඩිම වියදම් සහිත ක්‍රමය වන අතර පරිශීලකයන්ට පද්ධතිය ගැන ඉගෙනීමට ඉඩදෙයි.",
  "සමාන්තර (parallel) ස්ථාපනය අඩුම වියදමක් සහිත ස්ථාපන ක්‍රමය වේ.",
  "අවධි (phased) ස්ථාපනය පද්ධතියට අවශ්‍ය යම් යම් වෙනස්කම් කිරීමට අදාළ සංවිධානයට නිදහස නොදේ.",
  "නියමු (pilot) ස්ථාපනය හැමවිටම පරිශීලකයන්ගෙන් 50% කට වැඩි පරිශීලක කණ්ඩායමකට නව පද්ධතිය පරීක්ෂාව සඳහා යොමු කරයි."])

m(56,"The following diagrams labelled (A), (B) and (C) illustrate three software deployment types.\n[Figure: three timeline diagrams with a time axis. (A): an 'Old System' arrow ends at a vertical dashed line and a 'New System' arrow starts right at that line (immediate switch). (B): an 'Old System' arrow followed by progressively smaller arrows, while below it small new-system arrows grow progressively larger into a final 'New System' arrow, with dashed lines at the start and end of the transition (gradual stages). (C): an 'Old System' arrow and a 'New System' arrow overlapping in time between two vertical dashed lines (run side by side).]\nWhich of the following correctly represents (A), (B) and (C) deployment types respectively?",
 "පරිගණක පද්ධති ස්ථාපනය කිරීමේ (deployment) ආකාර තුනක් පහත (A),(B) සහ (C) ලෙස සලකුණු කළ රූපවලින් දැක්වේ.\nපහත කවරක් (A), (B) සහ (C) පද්ධති ස්ථාපනය කිරීමේ ආකාර පිළිවෙලින් දක්වයි ද?",
 ["Direct, Phased and Parallel","Direct, Pilot and Parallel","Parallel, Phased and Direct","Parallel, Pilot and Phased","Phased, Direct and Pilot"],
 ["සෘජු, අවධි සහ සමාන්තර","සෘජු, නියමු සහ සමාන්තර","සමාන්තර, අවධි සහ සෘජු","සමාන්තර, නියමු සහ අවධි","අවධි, සෘජු සහ නියමු"])

m(57,"Consider the information system types in List A and the descriptive examples in List B. Identify the most suitable matching between the items in lists A and B.\nList A: A1 - Decision Support System (DSS); A2 - Content Management System (CMS); A3 - Transaction Processing System (TPS)\nList B: B1 - a system that allows to update, create, and manage the details in a news website; B2 - a system that handles electronic fund transfers; B3 - a system that combines data and analytical tools for sales forecasting based on historical data",
 None,
 ["A1 – B1, A2 – B2, A3 – B3","A1 – B2, A2 – B1, A3 – B3","A1 – B2, A2 – B3, A3 – B1","A1 – B3, A2 – B1, A3 – B2","A1 – B3, A2 – B2, A3 – B1"])

m(58,"Non-functional requirements specify quality attributes of a system. Which of the following is an example for a non-functional requirement?",
 "කාර්යබද්ධ නොවන (non-functional) අවශ්‍යතා පද්ධතියක ගුණාත්මක උපලක්ෂණ නිරූපණය කරයි. කාර්යබද්ධ නොවන අවශ්‍යතාවකට උදාහරණයක් වන්නේ පහත සඳහන් කවරක් ද?",
 ["the email system should allow users to attach file",
  "each page of the website must load within 4 seconds",
  "administrator of the E-commerce website should be able to view a list of customers",
  "a user of the online banking system should be able to view the last transactions",
  "the ATM machine should allow users to print a receipt"],
 ["විද්‍යුත් තැපැල් පද්ධතිය පරිශීලකයන්ට ගොනු ඇමිණීමට ඉඩ ලබාදිය යුතු ය.",
  "වෙබ් අඩවියේ සෑම පිටුවක්ම තත්පර 4 ක් ඇතුළත පූරණය (load) විය යුතු ය.",
  "ඊ-වාණිජ්‍ය වෙබ් අඩවියේ පරිපාලකයාට, ගනුදෙනුකරුවන්ගේ ලැයිස්තුව බැලීමට හැකි විය යුතු ය.",
  "මාර්ගගත බැංකු පද්ධතිය භාවිත කරන්නෙකුට අවසන් ගනුදෙනු බැලීමට හැකි විය යුතු ය.",
  "ATM යන්ත්‍රය භාවිත කරන්නන්ට රිසිට්පතක් මුද්‍රණය කිරීමට ඉඩ ලබාදිය යුතු ය."])

m(59,"Which of the following statements is/are correct regarding System Development Life Cycle (SDLC) models?\nA - In the agile model, small portions of systematically developed working software are delivered to the client frequently.\nB - Late changes in the requirements can be easily accommodated in the waterfall model.\nC - Prototyping model can be practiced without client interactions.",
 "පද්ධති සංවර්ධන ජීවන චක්‍රයේ (SDLC) ආකෘති සම්බන්ධයෙන් පහත කුමන ප්‍රකාශය/ප්‍රකාශ නිවැරදි වේ ද?\nA - සුචල (agile) ආකෘතියේදී, ක්‍රමානුකූලව සංවර්ධනය කළ ක්‍රියාකාරී මෘදුකාංගවල කුඩා කොටස් නිරන්තරයෙන් සේවාදායකයාට ලබා දෙනු ලැබේ.\nB - අවසාන වෙලාවේ වෙනස්කම් දියඇලි ආකෘතියට පහසුවෙන් ඉඩ ලබාගත හැකිය.\nC - සේවාදායකයාගේ අන්තර් ක්‍රියාකාරීත්වයෙන් තොරව මූලාකෘති (prototyping) ආකෘතිය ක්‍රියාවට නැංවිය හැකිය.",
 ["A only.","B only.","C only.","A and B only.","A and C only"],
 ["A පමණි.","B පමණි.","C පමණි.","A හා B පමණි.","A හා C පමණි."])
del data[59]["qs"]

m(60,"Which of the following Data Flow Diagrams (DFDs) is correct with respect to the rules of data flow modelling? (Note: A - an external entity, B - a process (1.0 B), C - a data store)",
 "දත්ත ගැලීමේ ආකෘතිකරණය පිළිබඳ නීතිරීති අනුව පහත සඳහන් කුමන දත්ත ගැලීම් රූසටහන (DFD) නිවැරදි වන්නේ ද? (සටහන: A - බාහිර ආයතනයක්, B - ක්‍රියාවලියක්, C - දත්ත ගබඩාවක්)",
 ["[Figure: B -> A, A -> B (flows between process B and entity A in both directions); C -> B, B -> C (flows between data store C and process B in both directions)]",
  "[Figure: A -> B, and A -> C (entity A sends flows to process B and to data store C)]",
  "[Figure: A -> B, B -> C, C -> A (entity A to process B, process B to data store C, data store C back to entity A)]",
  "[Figure: B -> A, A -> C (process B to entity A, entity A to data store C)]",
  "[Figure: A -> C and C -> A (entity A and data store C exchange flows directly, no process)]"])

m(61,"Which of the following statements is correct regarding software testing?",
 "මෘදුකාංග පරීක්ෂාව සම්බන්ධයෙන් පහත සඳහන් ප්‍රකාශවලින් නිවැරදි වන්නේ කුමක් ද?",
 ["Integration testing is usually carried out before unit testing.",
  "Black-box testing techniques are usually used in acceptance testing.",
  "White box testing examines the behaviour of a software based only on the inputs to a system.",
  "Unit testing examines the entire system's functionality as a whole.",
  "System testing is usually carried out after the user acceptance testing."],
 ["ඒකාබද්ධ (integration) පරීක්ෂාව සාමාන්‍යයෙන් ඒකක (unit) පරීක්ෂාවට පෙර සිදු කෙරේ.",
  "කාළ මංජුසා (black-box) පරීක්ෂා ශිල්පීය ක්‍රම සාමාන්‍යයෙන් ප්‍රතිග්‍රහණ (acceptance) පරීක්ෂාවේදී භාවිත වේ.",
  "ශ්වේත මංජුසා (white-box) පරීක්ෂාවේ දී මෘදුකාංගයක හැසිරීම, පද්ධතියට ලබා දෙන ආදාන මත පමණක් පදනම්ව පරීක්ෂා කෙරේ.",
  "ඒකක පරීක්ෂාවේදී සම්පූර්ණ පද්ධතියේ ක්‍රියාකාරීත්වය, සමස්තයක් ලෙස පරීක්ෂා කෙරේ.",
  "පද්ධති (system) පරීක්ෂාව සාමාන්‍යයෙන් පරිශීලක ප්‍රතිග්‍රහණ (user acceptance) පරීක්ෂාවෙන් පසුව සිදු කෙරේ."])

m(62,"Choose the option containing most suitable deployment types for the following systems:\nA - A new system to replace an existing air traffic control system at an airport\nB - A system for the customers of an island-wide supermarket chain to order goods online\nC - A system for the public to enter comments regarding the service experienced by them at an office",
 "පහත පද්ධති සඳහා වඩාත් සුදුසු ස්ථාපන ආකාර සහිත වරණය තෝරන්න.\nA - ගුවන්තොටුපළක දැනට පවතින ගුවන් ගමනාගමන පාලන පද්ධතිය වෙනුවට නව පද්ධතියක්\nB - දිවයින පුරා සුපිරි වෙළඳසැල් දාමයක ගැනුම්කරුවන්ට මාර්ගගතව භාණ්ඩ ඇණවුම් කිරීමට පද්ධතියක්\nC - කාර්යාලයකදී තමන් ලද සේවා අත්දැකීම් පිළිබඳ මහජන අදහස් ඇතුළත් කිරීමේ පද්ධතියක්",
 ["A – direct, B – direct, C – parallel","A – direct, B – pilot, C – parallel","A – parallel, B – pilot, C – direct","A – parallel, B – parallel, C – parallel","A – parallel, B – parallel, C – pilot"],
 ["A – සෘජු, B – සෘජු, C – සමාන්තර","A – සෘජු, B – නියමු, C – සමාන්තර","A – සමාන්තර, B – නියමු, C – සෘජු","A – සමාන්තර, B – සමාන්තර, C – සමාන්තර","A – සමාන්තර, B – සමාන්තර, C – නියමු"])

m(63,"Which of the following is a non-functional requirement for an e-commerce site?",
 "පහත කවරක් ඊ-වාණිජ්‍ය වෙබ් අඩවියක කාර්යබද්ධ නොවන (non-functional) අවශ්‍යතාවක් වේද?",
 ["Being able to add items to the shopping cart","Being able to make payments online","Being able to view the items based on item category","Each item to be shown with a small image and a description","The e-commerce site to be accessible through popular web browsers"],
 ["සාප්පු ට්‍රොලියට (shopping cart) අයිතම එකතු කිරීමේ හැකියාව","මාර්ගගත ගෙවීම් කිරීමට හැකි වීම","ප්‍රවර්ගය අනුව අයිතම දැක බලා ගැනීමේ හැකියාව","සෑම අයිතමයක්ම කුඩා රූපයක් සහ විස්තරයක් සහිතව පෙන්විය යුතු වීම","ජනප්‍රිය වෙබ් අතරික්සු හරහා ඊ-වාණිජ්‍ය වෙබ් අඩවියට ප්‍රවේශවීමේ හැකියාව"])

m(64,"During which of the following is an application tested by its developers in a setting that closely resembles its intended deployment hardware, software, and network configuration environment?",
 None,
 ["Acceptance testing","Integration testing","Parallel testing","System testing","Unit testing"],
 ["ප්‍රතිග්‍රහණ පරීක්ෂාව","ඒකාබද්ධ පරීක්ෂාව","සමාන්තර පරීක්ෂාව","පද්ධති පරීක්ෂාව","ඒකක පරීක්ෂාව"])

m(65,"A company considers developing a new software application for its use. The application is expected to re-engineer internal processes, improve collaboration, and enhance productivity. However, during the feasibility analysis, it was identified that the new software may face some resistance from employees who are accustomed to the existing processes. Which component of the feasibility study would have helped to get that information?",
 None,
 ["economic feasibility","legal feasibility","operational feasibility","schedule feasibility","technical feasibility"],
 ["ආර්ථික ශක්‍යතාව","නීතිමය ශක්‍යතාව","මෙහෙයුම් ශක්‍යතාව","කාල ශක්‍යතාව","තාක්ෂණික ශක්‍යතාව"])

m(66,"Which of the following is incorrect about the waterfall model of software development?",
 "මෘදුකාංග සංවර්ධනයේ දියඇලි (waterfall) ආකෘතිය සම්බන්ධයෙන් අසත්‍ය වන්නේ පහත කවරක් ද?",
 ["It allows developers to collect and implement requirements throughout the project.","It is not an iterative model.","It is suitable for software with well defined requirements.","It is easy to estimate the resources needed for a project.","No working product is available until the latter stages of the project."],
 ["සංවර්ධකයන්ට ව්‍යාපෘතිය පුරාවටම අවශ්‍යතා එකතු කිරීමටත්, ක්‍රියාත්මක කිරීමටත් එය ඉඩ දෙයි.","එය පුනරාවර්තී (iterative) ආකෘතියක් නොවේ.","මනාව නිර්වචනය කරන ලද අවශ්‍යතා සහිත මෘදුකාංග සඳහා එය සුදුසු වේ.","ව්‍යාපෘතියක් සඳහා අවශ්‍ය සම්පත් ඇස්තමේන්තු කිරීම පහසු වේ.","ව්‍යාපෘතියේ අවසාන අදියර වන තෙක්, ක්‍රියාකරන නිෂ්පාදිතයක් (working product) ලබාගත නොහැක."])

m(67,"Select the option which includes most suitable replacements for the labels P to S in the following Data Flow Diagram of a library management system.\n[Figure: Level-1 DFD. External entity 'Member'. Processes: 1.0 Book Search, 2.0 Book lending, 3.0 Book return. Data stores: D1 BOOKS, D2 MEMBERS. Flows: Member -> 1.0 labelled P; 1.0 -> Member 'search results'; Member -> 2.0 labelled Q and R (two flows); 2.0 -> Member 'lending information'; Member -> 3.0 labelled S; 3.0 -> Member 'return information'; 1.0 <-> D1 BOOKS; 2.0 <-> D1 BOOKS; 2.0 <-> D2 MEMBERS; 3.0 <-> D1 BOOKS; 3.0 <-> D2 MEMBERS.]",
 None,
 ["P - keyword, Q - member ID, R - book details, S - book details","P - keyword, Q - keyword, R - book details, S - member ID","P - keyword, Q - keyword, R - book details, S - keyword","P - member ID, Q - keyword, R - member ID, S - member ID","P - member ID, Q - member ID, R - book details, S - book details"])

m(68,"In addition to the required features, which of the following should also be considered when a government institution selects a Commercial Off-The-Shelf (COTS) software to be implemented island wide?\nA - cost to deploy, maintain, upgrade and modify\nB - ease of integration with existing systems\nC - after sales service from the vendor",
 None,
 ["A only.","A and B only.","A and C only.","B and C only.","All of the above"],
 ["A පමණි.","A හා B පමණි.","A හා C පමණි.","B හා C පමණි.",ALLS+"."])

m(69,"A new system must be delivered completely to the client by a given date. There should not be any partial deliveries. Further, the system architecture and design must be fully defined before any coding began. Which of the following are suitable models to develop this system?\nA - waterfall; B - spiral; C - agile",
 None,
 ["A only.","A and B only.","A and C only.","B and C only.","All of the above"],
 ["A පමණි.","A හා B පමණි.","A හා C පමණි.","B හා C පමණි.",ALLS+"."])

m(70,"During the feasibility analysis of a software development project, it was discovered that the development team does not have the knowledge and the skills to develop the software. Which component of the feasibility study would have identified this issue?",
 None,
 ["economic feasibility","legal feasibility","operational feasibility","schedule feasibility","technical feasibility"],
 ["ආර්ථික ශක්‍යතාව","නීතිමය ශක්‍යතාව","මෙහෙයුම් ශක්‍යතාව","කාල ශක්‍යතාව","තාක්ෂණික ශක්‍යතාව"])

m(71,"Which of the following shows the correct order of stages in the System Development Life Cycle?",
 "පද්ධති සංවර්ධන ජීවන චක්‍රයේ (system development life cycle) අදියර නිවැරදිව පෙළගස්වා ඇත්තේ පහත කවරක ද?",
 ["Feasibility study → Requirements analysis → System design → Implementation → Testing → Deployment","Feasibility study → System design → Requirements analysis → Implementation → Testing → Deployment","Requirements analysis → Feasibility study → System design → Testing → Deployment → Implementation","Requirements analysis → System design → Feasibility study → Deployment → Testing → Implementation","System design → Requirements analysis → Feasibility study → Implementation → Testing → Deployment"],
 ["ශක්‍යතා අධ්‍යයනය → අවශ්‍යතා විශ්ලේෂණය → පද්ධති නිර්මාණය → ක්‍රියාත්මක කිරීම → පරීක්ෂාව → යෙදවීම","ශක්‍යතා අධ්‍යයනය → පද්ධති නිර්මාණය → අවශ්‍යතා විශ්ලේෂණය → ක්‍රියාත්මක කිරීම → පරීක්ෂාව → යෙදවීම","අවශ්‍යතා විශ්ලේෂණය → ශක්‍යතා අධ්‍යයනය → පද්ධති නිර්මාණය → පරීක්ෂාව → යෙදවීම → ක්‍රියාත්මක කිරීම","අවශ්‍යතා විශ්ලේෂණය → පද්ධති නිර්මාණය → ශක්‍යතා අධ්‍යයනය → යෙදවීම → පරීක්ෂාව → ක්‍රියාත්මක කිරීම","පද්ධති නිර්මාණය → අවශ්‍යතා විශ්ලේෂණය → ශක්‍යතා අධ්‍යයනය → ක්‍රියාත්මක කිරීම → පරීක්ෂාව → යෙදවීම"])

m(72,"Which of the following is not true regarding the prototyping technique used in system development?",
 "පද්ධති සංවර්ධනයේ භාවිතා වන මූලාකෘතිකරණය (prototyping) සම්බන්ධයෙන් පහත කවරක් අසත්‍ය වේ ද?",
 ["Prototypes need to be approved by the users, during the 'system testing' phase.","Prototyping is neither necessary nor appropriate in every project.","Successful prototyping helps to develop a system that better addresses user needs and expectations.","Successful prototyping helps to eliminate costly late changes to a system.","To get the benefits of prototyping, user feedback on the prototypes is extremely important."],
 ["පද්ධති පරීක්ෂා (system testing) අදියරේදී මූලාකෘති, පරිශීලකයන්ගෙන් අනුමත විය යුතු ය.","මූලාකෘතිකරණය සෑම ව්‍යාපෘතියකටම අවශ්‍ය හෝ සුදුසු හෝ නොවේ.","සාර්ථක මූලාකෘතිකරණය පරිශීලක අවශ්‍යතා සහ බලාපොරොත්තු වඩා හොඳින් සපුරාලන පද්ධති සංවර්ධනයට ඉවහල් වේ.","සාර්ථක මූලාකෘතිකරණය පද්ධතියකට පසුව සිදුවන වියදම් සහිත වෙනස්කම් ඉවත් කිරීමට ඉවහල් වේ.","මූලාකෘතිකරණයේ වාසි ලබාගැනීමට මූලාකෘති පිළිබඳ පරිශීලක ප්‍රතිචාර අතිශයින් වැදගත් වේ."])

m(73,"Which of the following statements regarding software tests are correct?\nA - White-box tests involve testing the internal structures and workings of a software.\nB - Unit tests are usually performed after the system test.\nC - System developers should take every effort to make the acceptance test successful.",
 None,
 ["A only.","A and B only.","A and C only.","B and C only.","All of the above"],
 ["A පමණි.","A හා B පමණි.","A හා C පමණි.","B හා C පමණි.",ALLS+"."])

ctx74=("A playground reservation system is needed for students and others to reserve the school playground (which is adjoining the school) for team sports. Each reservation is for two hours. All non-students will need to pay for their reservations. The reservations are to be made using the National Identity Card (NIC) numbers. The NICs are to be verified at the playground gate before a team is let in.\n"
 "The algorithm that could be used for the reservation process is shown below with blanks labelled A - D.\nBEGIN\n  A\n  IF user interested to make a reservation THEN\n    B\n    C\n    IF user is not a student THEN\n      D\n    ENDIF\n    Confirm booking and update reservation database\n  ENDIF\nEND.")
m(74,ctx74+"\nWhich of the following contains the suitable replacements for the above blanks?",
 None,
 ["A - DISPLAY existing bookings; B - GET date/time; C - GET NIC number; D - Complete user's credit/debit card payment",
  "A - DISPLAY existing bookings; B - GET date/time; C - Complete user's credit/debit card payment; D - GET NIC number",
  "A - DISPLAY existing bookings; B - GET NIC number; C - Complete user's credit/debit card payment; D - GET date/time",
  "A - GET date/time; B - DISPLAY existing bookings; C - GET NIC number; D - Complete user's credit/debit card payment",
  "A - GET NIC number; B - DISPLAY existing bookings; C - GET date/time; D - Complete user's credit/debit card payment"])

m(75,"(Refer to the playground reservation system described below, shared with Q74.)\n"+ctx74+"\nWhich of the following suggestions about the above system is not suitable?",
 "ඉහත පද්ධතිය ගැන පහත කවර යෝජනාවක් නුසුදුසු වේ ද?",
 ["The list of reservations for a given date should be provided when needed.","Each time a student is making a reservation he/she should be required to enter his/her home address.","It is suitable to check the validity of the NIC number.","Reservations should not clash with school times.","For fairness, the number of reservations that a particular NIC number is allowed per day should be limited."],
 ["අවශ්‍ය විටක, දී ඇති දිනයකට අදාළ වෙන්කිරීම්වල ලැයිස්තුවක් ලබා දිය යුතු ය.","සිසුවෙකු වෙන් කිරීමක් සිදු කරන සෑම විටකම ඔහු/ඇය තම ගෙදර ලිපිනය ඇතුළත් කිරීම අවශ්‍ය කළ යුතු ය.","NIC අංකයේ වලංගුතාව පිරික්සීම සුදුසු වේ.","වෙන්කිරීම් පාසල් වේලාවන් සමඟ ගැටීම් නොවිය යුතු ය.","සාධාරණත්වය සඳහා, යම් NIC අංකයකට දිනකට ඉඩ දෙන වෙන් කිරීම් ගණන සීමා කළ යුතු ය."])

out=[]
for k,q in enumerate(s):
    pos=39+k
    r=data[pos]
    o={"n":q['n'],"d":q['d']}
    o.update(r)
    assert 4<=len(o['o'])<=5 and all(x.strip() for x in o['o']), pos
    if 'os' in o: assert len(o['os'])==len(o['o']),pos
    out.append(o)
assert len(out)==37
json.dump(out,open('D:/DevOps/aws-clf-c02-bridge/tools/transcribed/ictl-sad-mcq.part2.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out), [o['n'] for o in out][-3:], [o['d'] for o in out][:2])
