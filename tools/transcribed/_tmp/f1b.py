import json,sys,os as _os
sys.path.insert(0,_os.path.dirname(__file__))
from f1a import R,add
idx=json.load(open('tools/ict-lessons-images.json',encoding='utf8'))
S=[x for x in idx['sets'] if x['id']=='ictl-db-mcq'][0]['qs'][:35]
ctx20=("Consider the following four relational database tables to answer questions.\nitem table: item | product\nT001 | Laptop\nT002 | TV\nT003 | Camera\nsupplier table: supplier | name\nS001 | BeLap Company Ltd.\nS002 | DigiTV trading company\nitemSupplier table: item | supplier\nT001 | S001\nT002 | S001\nT002 | S002\ndelivery table: item | supplier | batch | quantity | date\nT001 | S001 | B01 | 450 | 1.5.2015\nT002 | S001 | AB1 | 45 | 1.5.2015\nT001 | S001 | B02 | 500 | 2.5.2015\nT001 | S002 | C01 | 75 | 5.5.2015\n")
add(19,ctx20+"Which of the following is correct with respect to the above tables?","ප්‍රශ්න සඳහා පිළිතුරු සැපයීමට පහත පෙන්වා ඇති දත්ත සමුදා වගු හතර සලකන්න. (වගු: item, supplier, itemSupplier, delivery - ඉහත දැක්වෙන පරිදි)\nඉහත වගු සම්බන්ධයෙන් කුමක් නිවැරදි වන්නේ ද?",
 ["All the tables are in third normal form.","Normalization has been applied to these tables.","Integrity constraints are correctly applied to these tables.","There is no evidence to say that integrity constraints are properly applied.","Normalization and integrity constraints are properly applied."],
 ["සියලු වගු තෙවැනි ප්‍රමත අවස්ථාවේ පවතී.","මෙම වගුවලට ප්‍රමතකරණය කර ඇත.","මෙම වගුවලට ඒකාබද්ධ සංරෝධක (integrity constraints) නිවැරදි ව යොදා ඇත.","ඒකාබද්ධ සංරෝධක නියමානුකූලව යොදාගෙන ඇති බව පැවසීමට කිසිදු සාධකයක් මෙහි නොමැත.","ප්‍රමතකරණය හා ඒකාබද්ධ සංරෝධක නියමානුකූලව ආදේශ කර ඇත."])
ctx21="Consider the following relation to answer questions 21 and 22:\nbook (BN, title, publisher, version, author1, author2, author3)\nwhere BN is a unique code.\n"
ctx21s="අංක 21 සහ 22 ප්‍රශ්නවලට පිළිතුරු දීම සඳහා පහත දක්වා ඇති සම්බන්ධතාව සලකන්න.\nbook (BN, title, publisher, version, author1, author2, author3)\nමෙහි BN යනු අනන්‍ය කේතයකි.\n"
add(20,ctx21+"Which of the following statements is correct with respect to the above relation?",ctx21s+"ඉහත සම්බන්ධතාවයේ ප්‍රමත අවස්ථාව සම්බන්ධයෙන් නිවැරදි ප්‍රකාශය කුමක් ද?",
 ["It is in zero normal form.","It is in the 1st normal form.","It is in the 2nd normal form.","It is in the 3rd normal form.","Its normal form cannot be decided."],
 ["එය ශුන්‍ය ප්‍රමත අවස්ථාවේ පවතී.","එය පළමු ප්‍රමත අවස්ථාවේ පවතී.","එය දෙවන ප්‍රමත අවස්ථාවේ පවතී.","එය තෙවන ප්‍රමත අවස්ථාවේ පවතී.","එහි ප්‍රමත අවස්ථාව තීරණය කළ නොහැකි ය."])
add(21,ctx21+"Which of the followings can be a candidate key of the above relation?",ctx21s+"කවරක් ඉහත සම්බන්ධතාවයේ අපේක්ෂක යතුරක් (candidate key) විය හැකි ද?",["BN","publisher","version","author1","author2"])
add(22,"Which of the followings is correct with respect to the term \"domain\" in relational database?","සම්බන්ධිත දත්ත සමුදායකට (relational database) අනුබද්ධව \"වසම\" (domain) යන වදන සඳහා නිවැරදි වන්නේ පහත කවරක් ද?",
 ["It is a set of possible names for a table.","It is a set of possible names for an attribute.","It is the collection of all possible primary keys.","It is the set of all possible values of an attribute.","It is the collection of foreign keys."],
 ["එය වගුවක් සඳහා ගත හැකි නාමවල කුලකයකි.","එය උපලැකියක් (attribute) සඳහා ගත හැකි නාමවල කුලකයයි.","එය පැවතිය හැකි ප්‍රාථමික යතුරු සියල්ලේ එකතුවයි.","එය උපලැකියකට පැවතිය හැකි සියලු අගයන්ගේ කුලකයයි.","එය ආගන්තුක යතුරුවල එකතුවයි."])
ctx24="Consider the following relation to answer questions 24 and 25:\nStudent (index_no, national_id_no, name, date_of_birth, gender, blood_group)\nwhere index_no is a unique attribute and the name attribute fully depends on the index_no attribute.\n"
ctx24s="අංක 24 සහ 25 ප්‍රශ්නවලට පිළිතුරු දීම සඳහා පහත දක්වා ඇති සම්බන්ධතාව සලකන්න.\nStudent (index_no, national_id_no, name, date_of_birth, gender, blood_group)\nමෙහි index_no යනු අනන්‍ය උපලක්ෂණයක් වන අතර name උපලක්ෂණය index_no උපලක්ෂණය මත මුළුමනින් ආයත්ත (depend) වේ.\n"
add(23,ctx24+"Which of the following statements is correct with respect to normal form of above relation?",ctx24s+"ඉහත සම්බන්ධතාවයේ ප්‍රමත අවස්ථාව සම්බන්ධයෙන් දැක්වෙන වගන්ති අතුරෙන් කුමක් නිවැරදි වේද?",
 ["It is in the zero normal form.","It is in the first normal form.","It is in the second normal form.","It is in the third normal form.","Its normal form cannot be decided."],
 ["එය ශුන්‍ය ප්‍රමත අවස්ථාවේ පවතියි.","එය පළමු ප්‍රමත අවස්ථාවේ පවතියි.","එය දෙවන ප්‍රමත අවස්ථාවේ පවතියි.","එය තෙවන ප්‍රමත අවස්ථාවේ පවතියි.","එහි ප්‍රමත අවස්ථාව තීරණය කළ නොහැකි ය."])
add(24,ctx24+"Which of the followings can be a candidate key of the above relation?",ctx24s+"කවරක් ඉහත සම්බන්ධතාවයේ අපේක්ෂක යතුරක් (candidate key) විය හැකි ද?",["national_id_no","name","date_of_birth","gender","blood_group"])
ctx26="Consider the following relation to answer questions 26 and 27:\nbook (book_no, title, publisher, edition)\nauthor (author_id, name, email_address)\nbookAuthor (book_no, author_id)\nwhere book_no and author_id are unique attributes in the relations book and author respectively.\n"
ctx26s="අංක 26 සිට 27 ප්‍රශ්නවලට පිළිතුරු දීම සඳහා පහත දක්වා ඇති සම්බන්ධතා සලකන්න.\nbook (book_no, title, publisher, edition)\nauthor (author_id, name, email_address)\nbookAuthor (book_no, author_id)\nමෙහි book_no සහ author_id පිළිවෙළින් book සහ author සම්බන්ධතාවල අනන්‍ය උපලක්ෂණ වේ.\n"
add(25,ctx26+"Which of the following statements is correct with respect to the relation bookAuthor?",ctx26s+"ඉහත bookAuthor සම්බන්ධතාව පිළිබඳ නිවැරදි ප්‍රකාශය පහත දැක්වෙන ඒවා අතුරෙන් කුමක් ද?",
 ["book_no is the primary key.","author_id is the primary key.","Any single attribute can be a candidate key.","author_id is a candidate key.","book_no is a part of the primary key."],
 ["book_no ප්‍රාථමික යතුර වේ.","author_id ප්‍රාථමික යතුර වේ.","ඕනෑම තනි උපලක්ෂණයක් අපේක්ෂක යතුරක් විය හැකි ය.","author_id අපේක්ෂක යතුරක් වේ.","book_no යනු ප්‍රාථමික යතුරෙහි කොටසක් වේ."])
add(26,ctx26+"Which of the following Entity Relationship (ER) diagrams correctly represents the relationship between the entities represented by the above relations?\n[Figure: entity 'book' -- diamond 'write' -- entity 'author', with cardinalities:]\nOption 1: book 1 -- write -- m author.\nOption 2: book 1 -- write -- 1 author.\nOption 3: book m -- write -- 1 author.\nOption 4: book m -- write -- n author.\nOption 5: book m -- write -- m author.",
 ctx26s+"ඉහත සම්බන්ධතා මගින් නිරූපණය කෙරෙන භූතාර්ථ අතර සම්බන්ධය නිවැරදි ව නිරූපණය කෙරෙන්නේ පහත කුමන භූතාර්ථ සම්බන්ධතා (ER) රූප සටහනින් ද?",
 ["book 1 : m author","book 1 : 1 author","book m : 1 author","book m : n author","book m : m author"])
o=['A only.','B only.','A and B only.','A and C only.','All of the above.']
os=['A පමණි.','B පමණි.','A හා B පමණි.','A හා C පමණි.','ඉහත සියල්ලම.']
add(27,"Consider the following statements regarding databases.\nA. Candidate key is column, or a set of columns that can uniquely identify a row in a table.\nB. Alternate key is any candidate key that has not been selected as the primary key.\nC. Primary key can have a NULL value.\nWhich of the above statements is/are correct?",
 "දත්ත සමුදා සම්බන්ධයෙන් පහත දැක්වෙන වගන්ති සලකන්න.\nA. නිරුපය යතුර (candidate key) යනු, වගුවක ඇති පේළියක් අනන්‍යව හඳුනා ගැනීමට උපකාරී වන තීරුවක් හෝ තීරු කිහිපයකි.\nB. විකල්ප යතුර (alternate key) යනු ප්‍රාථමික යතුර (primary key) ලෙස තෝරා නොගත් නිරුපය යතුරකි.\nC. ප්‍රාථමික යතුරට අභිශූන්‍ය (NULL) අගයක් තිබිය හැකි ය.\nඉහත කවර වගන්තියක්/වගන්ති නිවැරදි වේ ද?",o,os)
add(28,"Consider the following relational schema in a database.\nSubject (SubjectID, TermID, SubjectDescription)\nHere the SubjectID, TermID, and SubjectDescription are ................... and Subject is ...................\nWhich of the following are most suitable to fill the blanks, respectively?",
 "දත්ත සමුදා පද්ධතියක පහත දැක්වෙන සම්බන්ධතා පරිකල්පනය (relational schema) සලකන්න.\nSubject (SubjectID, TermID, SubjectDescription)\nමෙහි SubjectID, TermID හා SubjectDescription යන දෑ .......... වන අතර Subject යන්න ........ වේ.\nඉහත හිස්තැන් පිරවීම සඳහා වඩාත් ම සුදුසු පිළිවෙළින් පහත කවරක් ද?",
 ["attributes, relation","relation, attributes","tuples, relation","tuples, attributes","relation, tuples"],
 ["උපලක්ෂණ (attributes), සම්බන්ධයක් (relation)","සම්බන්ධ (relation), උපලක්ෂණයක් (attributes)","උපලැකියාන (tuples), සම්බන්ධයක් (relation)","උපලැකියාන (tuples), උපලක්ෂණයක් (attributes)","සම්බන්ධ (relation), උපලැකියානයක් (tuples)"])
o=['A only.','A and B only.','A and C only.','B and C only.','All of the above.']
os=['A පමණි.','A හා B පමණි.','A හා C පමණි.','B හා C පමණි.','ඉහත සියල්ලම.']
add(29,"Consider the following statements regarding databases.\nA. For each attribute of a relation, there is a set of permitted values, called the domain of that attribute.\nB. The tuples (records) of the relations are always in sorted order.\nC. Database schema shows the organization of data as a blueprint of how the database is constructed.\nWhich of the above statements is/are correct?",
 "දත්ත සමුදායක් පිළිබඳ පහත ප්‍රකාශ සලකන්න.\nA. සම්බන්ධයක ඇති සෑම උපලක්ෂණයක් (attribute) සඳහාම එම උපලක්ෂණයෙහි වසම (domain) ලෙස හැඳින්වෙන අනුමත අගයන් කුලකයක් පවතී.\nB. සම්බන්ධතාවක ඇති උපලැකියාන (tuples) සෑම විටම අනුපිළිවෙළකට පවතී (sorted).\nC. දත්ත සමුදා පරිකල්පනය (database schema), දත්ත සමුදායක් ගොඩනැගීමට අදාළ දත්ත නිශ්චිත සැලසුමක් (blueprint) අනුව සංවිධානය වී ඇති අයුරු පෙන්වයි.\nඉහත ප්‍රකාශවලින් කවරක් නිවැරදි වේ ද?",o,os)
ctx31="Consider the following relational schema consisting of text fields in answering questions 31 and 32.\nStudents (admission_number, surname_with_initials, house_number, street_name, village, postal_town, postal_code)\nAssume that for a given postal_town only one postal_code exists.\n"
ctx31s="අංක 31 සහ 32 යන ප්‍රශ්නවලට පිළිතුරු දීමට, පාඨ ක්ෂේත්‍රවලින් සමන්විත පහත දැක්වෙන සම්බන්ධක පරිකල්පනය (relational schema) සලකන්න.\nStudents (admission_number, surname_with_initials, house_number, street_name, village, postal_town, postal_code)\nදෙන ලද තැපැල් නගරයකට එක් තැපැල් කේතයක් පමණක් පවතින බව සලකන්න.\n"
o=['A only.','B only.','A and C only.','B and C only.','All of the above.']
os=['A පමණි.','B පමණි.','A හා C පමණි.','B හා C පමණි.','ඉහත සියල්ලම.']
add(30,ctx31+"Consider the following statements.\nA. Students relation is not normalised.\nB. Students is a relation in First Normal Form (1NF) only.\nC. In normalization terms, Students is a relation in Second Normal Form (2NF) and hence also in 1NF.\nWhich of the above statements is/are correct?",
 ctx31s+"පහත ප්‍රකාශ සලකන්න.\nA. Students සම්බන්ධය ප්‍රමතකරණය (normalized) කර නැත.\nB. Students යනු පළමු ප්‍රමතකරණයෙහි (First Normal Form - 1NF) පමණක් ඇති සම්බන්ධයකි.\nC. ප්‍රමතකරණ අර්ථවලට අනුව Students යනු දෙවන ප්‍රමතකරණයෙහි (Second Normal Form - 2NF) හි ඇති එනයින් 1NF හි ද ඇති සම්බන්ධයකි.\nඉහත ප්‍රකාශවලින් කවරක් නිවැරදි වේ ද?",o,os)
o=['A only.','A and B only.','A and C only.','B and C only.','All of the above.']
os=['A පමණි.','A හා B පමණි.','A හා C පමණි.','B හා C පමණි.','ඉහත සියල්ලම.']
add(31,ctx31+"Consider the following statements relating to Entity Relationship (ER) modelling.\nA. Cardinality specifies how many instances of an entity relates to one instance of another entity.\nB. An entity is a 'thing' or 'object' in the real world that can be identified separately (distinguishable) from all other objects.\nC. Cardinality specifies primary key attributes of an entity.\nWhich of the above is/are correct?",
 ctx31s+"භූතාර්ථ සම්බන්ධතා (ER) ආකෘතිකරණය පිළිබඳ පහත දැක්වෙන ප්‍රකාශ සලකන්න.\nA. ගණනීයතාව (cardinality) මගින් එක් භූතාර්ථයක දෘෂ්ටාන්ත (instances) කොපමණ සංඛ්‍යාවක් වෙනත් භූතාර්ථයක එක් දෘෂ්ටාන්තයකට සම්බන්ධ වේ දැයි විශේෂයෙන් සඳහන් කරනු ලැබේ.\nB. භූතාර්ථයක් යනු තථ්‍ය ලෝකයෙහි (real world) ඇති අනෙක් සියලු වස්තූන්ගෙන් වෙන්කර හඳුනා ගත හැකි යම් 'දෙයක්' හෝ 'වස්තුවක්' හෝ වේ.\nC. ගණනීයතාව මගින් භූතාර්ථයක ප්‍රාථමික යතුරු උපලක්ෂණ විශේෂිතව දැක්වේ.\nඉහත කවරක් නිවැරදි වේ ද?",o,os)
ctxss="Consider the following database table to answer the questions 33 to 34.\nStudent_Sport: Student_Id | Event_Id | Event_Name\n10012 | S-02 | Carrom\n10022 | S-01 | Basketball\n10018 | S-02 | Carrom\n10012 | S-03 | Volleyball\n10025 | S-04 | Chess\n10018 | S-01 | Basketball\n"
ctxsss="අංක 33 සිට 34 ප්‍රශ්නවලට පිළිතුරු සැපයීම සඳහා පහත දැක්වෙන දත්ත සමුදා වගුව සලකන්න. (වගුව Student_Sport - ඉහත දැක්වෙන පරිදි)\n"
o=['A only.','B only.','A and B only.','A and C only.','All of the above.']
os=['A පමණි.','B පමණි.','A හා B පමණි.','A හා C පමණි.','ඉහත සියල්ලම.']
add(32,ctxss+"Consider the following statements regarding the above table:\nA. It has a composite primary key.\nB. Event_Name attribute is fully dependent on the primary key of Student_Sport table.\nC. Event_Id is a candidate key.\nWhich of the above statements is/are true?",
 ctxsss+"ඉහත වගුව පිළිබඳ පහත ප්‍රකාශ සලකන්න.\nA. එයට සංයුක්ත ප්‍රාථමික යතුරක් පවතී.\nB. Event_Name උපලක්ෂණය Student_Sport වගුවෙහි ප්‍රාථමික යතුර මත පූර්ණ පරායත්ත වේ.\nC. Event_Id යනු නිරුපය (candidate) යතුරකි.\nඉහත කුමන වගන්තියක්/වගන්ති සත්‍ය වේ ද?",o,os)
add(33,ctxss+"In which normal form does the above table exist?",ctxsss+"ඉහත වගුව පවතින්නේ කුමන ප්‍රමත ආකාරයට ද?",
 ["BCNF","First normal form","Second normal form","Third normal form","Zero normal form"])
add(34,"Consider the following statements regarding the Extended Entity Relationship (EER) model.\nA. EER model includes all the concepts of the original ER model.\nB. EER model has additional concepts of specialization/generalization.\nC. EER model includes a new concept to model the weak entities.\nWhich of the above statements is/are correct?",
 "විස්තෘත භූතාර්ථ සම්බන්ධතා (EER) ආකෘතිය පිළිබඳව පහත දැක්වෙන වගන්ති සලකන්න.\nA. EER ආකෘතියට මුල් ER ආකෘතියෙහි ඇති සියලු ම සංකල්ප ඇතුළත් වේ.\nB. විශේෂකරණය/සාමාන්‍යකරණය පිළිබඳව අමතර සංකල්ප EER හි පවතී.\nC. දුර්වල භූතාර්ථ ආකෘතිකරණය සඳහා නව සංකල්පයක් EER හි ඇතුළත් වේ.\nඉහත කුමන වගන්තියක්/වගන්ති සත්‍ය වේ ද?",o,os)
o=['B only.','C only.','A and B only.','B and C only.','All of the above.']
os=['B පමණි.','C පමණි.','A හා B පමණි.','B හා C පමණි.','ඉහත සියල්ලම.']
add(35,"Which of the following statement/s about a relation in the Second Normal Form (2NF) are true?\nA. It can have a composite key.\nB. It should be in the First Normal Form (1NF) as well.\nC. All non-key attributes are fully functionally dependent on the primary key.\n(Note: the source images also contain several following questions from the same paper; only the first is transcribed.)",
 "දෙවන ප්‍රමතකරණයක් (2NF) ඇති සම්බන්ධතාවක් පිළිබඳ පහත කවර වගන්ති/ය සත්‍ය වේ ද?\nA. එයට සංයුක්ත යතුරක් තිබිය හැක.\nB. එය පළමු ප්‍රමතකරණයෙහි (1NF) ද පැවතිය යුතු ය.\nC. යතුරු නොවන සියලු උපලක්ෂණ ප්‍රාථමික යතුර මත මුළුමනින්ම කාර්යාත්මකව පරායත්ත වේ.",o,os)
add(36,"Consider the following Results and Subjects tables to answer questions 41 to 42:\nResults: StudentNo | NIC | FirstName | SubjectID | Grade\nS1234 | 986888457V | Nilam | ENG | B\nS1447 | 992562321V | Praveena | PHY | C\nS1234 | 986888457V | Nilam | ACC | A\nS1323 | 900251452V | Thilan | ENG | S\nS1323 | 900251452V | Thilan | ACC | B\nSubjects: SubjectID | SubjectName\nENG | English\nPHY | Physics\nECO | Economics\nACC | Accountancy\nWhich of the following is most suited to be selected as the primary key of the Results table with respect to the given details?",
 "ප්‍රශ්න අංක 41 සිට 42 තෙක් පිළිතුරු දීමට පහත Results සහ Subjects වගු සලකන්න. (වගු ඉහත දැක්වෙන පරිදි)\nදී ඇති විස්තර අනුව, Results වගුවේ ප්‍රාථමික යතුර ලෙස තෝරා ගැනීමට වඩාත්ම සුදුසු වන්නේ කුමක් ද?",
 ["NIC","SubjectID","StudentNo","StudentNo and NIC","StudentNo and SubjectID"])
M={i:i for i in range(1,7)}; M[7]=9; M[8]=8
for i in range(9,35): M[i]=i+1
M[35]=36
out=[]
for i,q in enumerate(S,1):
    r=R[M[i]]; d={'n':q['n'],'d':q['d'],'q':r['q'],'qs':r['qs'],'o':r['o']}
    if 'os' in r: d['os']=r['os']
    out.append(d)
assert len(out)==35 and all(4<=len(x['o'])<=5 and all(x['o']) for x in out)
assert all(len(x['os'])==len(x['o']) for x in out if 'os' in x)
json.dump(out,open('tools/transcribed/ictl-db-mcq.part1.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
print(len(out))
