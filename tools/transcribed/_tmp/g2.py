import json
D=json.load(open('D:/DevOps/aws-clf-c02-bridge/tools/ict-lessons-images.json',encoding='utf-8'))
S=[x for x in D['sets'] if x['id']=='ictl-db-mcq'][0]['qs'][35:69]
RES="""Results table:
StudentNo | NIC | FirstName | SubjectID | Grade
S1234 | 986888457V | Nilam | ENG | B
S1447 | 992562321V | Praveena | PHY | C
S1234 | 986888457V | Nilam | ACC | A
S1323 | 900251452V | Thilan | ENG | S
S1323 | 900251452V | Thilan | ACC | B

Subjects table:
SubjectID | SubjectName
ENG | English
PHY | Physics
ECO | Economics
ACC | Accountancy"""
SHOP="""Customer table:
CusId | Fname | Lname | Location
C001 | Saman | Perera | Dehiwala
C002 | Kalum | Gamage | Galle
C003 | Shiromi | Silva | Galle
C004 | Kalum | Perera | Kandy

Product table:
ProId | Name
PR001 | Refrigerator
PB401 | Blender
PM025 | Mobile Phone
PP009 | Inkjet Printer

Order table:
OrderId | CusId | OrderDate | SellerId
A001 | C001 | 2022-07-14 | S001
A002 | C002 | 2022-07-14 | S001
A003 | C003 | 2022-07-18 | S002
A004 | C004 | 2022-07-20 | S002

Order_Product table:
OrderId | ProId
A003 | PR001
A001 | PR001
A002 | PB401
A003 | PM025
A004 | PP009"""
ADM="""A principal of a National school wants to develop a database to maintain Admission Number, Student Name, Address, National Identity Card number (NIC) and the Date of Birth (DOB) of Advanced Level students. The principal also wants to know the marks obtained for each subject by the students. In addition to the above requirements, the principal needs to know the subjects assigned to the teachers.

Relations:
A - Student(admissionNo, studentName, address, DOB, NIC)
B - Subject(subjectCode, subjectName)
C - Mark(admissionNo, subjectCode, marksObtained)
D - Teacher(teacherNo, subjectCode, teacherName, subjectName, class)
"""
SUBJ="""Assume that a subject has only one paper for an examination.

subject table:
subjectId | title
SUB001 | Information and Technology
SUB002 | Chemistry
SUB003 | Physics

examSubject table:
examId | subjectId | examDate
EXAM001 | SUB001 | 2014.12.12
EXAM002 | SUB001 | 2014.8.21
EXAM002 | SUB002 | 2014.8.21
EXAM002 | SUB003 | 2014.8.21

exam table:
examId | name
EXAM001 | GCE OL
EXAM002 | GCE AL"""
OPT3=["A only.","B only.","A and C only.","B and C only.","All of the above."]
OPT3S=["A පමණි.","B පමණි.","A හා C පමණි.","B හා C පමණි.","ඉහත සියල්ලම."]
OPT3b=["A only.","A and B only.","A and C only.","B and C only.","All of the above."]
OPT3bS=["A පමණි.","A හා B පමණි.","A හා C පමණි.","B හා C පමණි.","ඉහත සියල්ලම."]
Q=[]
def add(q,o,qs=None,os=None): Q.append(dict(q=q,o=o,qs=qs,os=os))

add("Consider the following Results and Subjects tables.\n"+RES+"\n\nWhich of the following is the correct statement about the Results table?",
 ["All the non-key attributes are fully functionally dependent on the primary key.","It has one candidate key.","It is in the First Normal Form (1NF).","It is in the Second Normal Form (2NF).","The cardinality of the table is four."],
 "Results වගුව සම්බන්ධයෙන් පහත කවර වගන්තියක් නිවැරදි වේ ද?")
add("Consider the Results and Subjects tables:\n"+RES+"\n\nWhich dependency is removed when converting the Results table to next normal form?",
 ["foreign key dependency","fully functional dependency of non-key attributes on the primary key","multivalued dependency","partial dependencies of non-key attributes on the primary key","transitive dependency of non-key attributes"],
 "Results වගුව ඊලඟ ප්‍රමතකරණයට පත්කරන විට පහත කුමන පරායත්තතාව ඉවත් වේ ද?")
add("Following are the steps involved in creating an Entity Relationship (ER) Diagram:\nI. Determine the ..... A ..... in your diagram.\nII. Add .... B .... to each .... C ....\nIII. Include the .... D .... between the .... A ....\nIV. Add .... E .... to every relationship.\n\nWhich of the following gives suitable choices for the A, B, C, D and E blanks in above steps?",
 ["A - attributes, B - entities, C - attribute, D - cardinality, E - entities","A - attributes, B - cardinality, C - attribute, D - entities, E - entity","A - entities, B - attributes, C - entity, D - relationships, E - cardinality","A - entities, B - relationships, C - entity, D - attributes, E - cardinality","A - relationships, B - cardinality, C - relationships, D - attributes, E - entities"])
add("Which of the following can be modelled with an Extended Entity Relationship diagram?\nA - subclasses of an entity\nB - inheritance of attributes\nC - specialization of entities",
 ["A only.","B only.","C only.","A and C only.","All of the above."],
 "විස්තෘත භූතාර්ථ සම්බන්ධතා (Extended Entity Relationship) රූප සටහනකින් පහත කවරක් නිරූපණය කළ හැකි ද?",
 ["A පමණි.","B පමණි.","C පමණි.","A හා C පමණි.","ඉහත සියල්ලම."])
add("Consider the following relational schema:\n\nStudent (StudentId, StudentName, Address, Gender, DateOfBirth)\nStudy (StudentId, SubjectId, Grade)   [StudentId references Student; SubjectId references Subject]\nSubject (SubjectId, SubjectName)\n\nWhich of the following is the most suitable Entity Relationship (ER) diagram to correctly represent the relationship between Student and Subject entities?\nNote: In the ER diagrams, the entities are drawn without attributes. 'study' means learning.\n\nEach option is an ER diagram: entity - relationship diamond - entity, with cardinality labels.",
 ["[Figure: Student (1) -- studies -- (1) Subject]","[Figure: Student (1) -- studies -- (m) Subject]","[Figure: Student (m) -- subject -- (1) Study]","[Figure: Student (n) -- subject -- (m) Study]","[Figure: Student (n) -- studies -- (m) Subject]"])
add("The tables which are partially extracted from a database used in an information system developed for a shop are shown below. Answer the question using those tables.\n"+SHOP+"\n\nWhich of the following shows the most suitable primary keys for Order and Order_Product relations?",
 ["Order: CusId; Order_Product: OrderId","Order: OrderId; Order_Product: OrderId","Order: OrderId; Order_Product: OrderId + ProdId","Order: CusId + SellerId; Order Product: ProdId","Order: OrderId + CusId; Order_Product: OrderId"],
 "Order සහ Order_Product වගු සඳහා වඩාත් සුදුසු ප්‍රාථමික යතුරු පිළිවෙළින් දැක්වෙන්නේ පහත කවරක් ද?")
add("Which of the following statements is/are correct regarding Entity Relationship (ER) modelling?\nA. A weak entity is dependent on another entity.\nB. A derived attribute is represented as an attribute in a relation.\nC. An entity can contain a multi-value attribute and a composite attribute at the same time.",OPT3,
 None,None)
add("The following ER diagram represents a scenario of students borrowing books from a library. Which of the following gives the most suitable relation list for the given ER diagram?\nNote: author, book, student, write, borrow\n\n[Figure: ER diagram. Entity AUTHOR with attributes Aut_Id (key), Aut_Name, Qualifications (multivalued). Entity BOOK with attributes Book_Id (key), Book_Name, ISBN. Entity STUDENT with attributes Stu_Id (key), Stu_Name (composite: Stu_FName, Stu_LName), DOB. Relationships: AUTHOR (1) -- writes -- (m) BOOK; BOOK (m) -- borrows -- (1) STUDENT.]",
 ["BOOK (Book_Id, Book_Name, ISBN, Stu_Id, Aut_Id); STUDENT (Stu_Id, Stu_FName, Stu_LName, DOB); AUTHOR (Aut_Id, Aut_Name); AUTHOR_QUALIFICATION (Aut_Id, Qualifications)  [key of last: Aut_Id + Qualifications]",
  "BOOK (Book_Id, Book_Name, ISBN); STUDENT (Stu_Id, Stu_FName, Stu_LName, DOB); AUTHOR (Aut_Id, Aut_Name); AUTHOR_QUALIFICATION (Aut_Id, Qualifications)",
  "BOOK (Book_Id, Book_Name, ISBN, Stu_Id, Aut_Id); STUDENT (Stu_Id, Stu_FName, Stu_LName, DOB); AUTHOR (Aut_Id, Aut_Name, Qualifications)",
  "BOOK (Book_Id, Book_Name, ISBN, Stu_Id, Aut_Id); STUDENT (Stu_Id, Stu_Name, DOB); AUTHOR (Aut_Id, Aut_Name); AUTHOR_QUALIFICATION (Aut_Id, Qualifications)",
  "BOOK (Book_Id, Book_Name, ISBN, Stu_Id, Aut_Id); STUDENT (Stu_Id, Stu_Name, DOB); AUTHOR (Aut_Id, Aut_Name); AUTHOR_QUALIFICATION (Aut_Id, Qualifications); BORROW (Aut_Id, Book_Id); WRITE (Aut_Id, Book_Id)"])
add("Match the given entity attributes labelled from A to D to the corresponding descriptions labelled from 1 to 4.\n\nEntity attribute: A Composite attribute; B Simple attribute; C Multivalued attribute; D Derived attribute\n\nDescription:\n1 - an attribute that cannot be broken down into smaller components\n2 - an attribute that can be broken down into component parts\n3 - an attribute whose values can be calculated from related attribute values\n4 - an attribute that may take more than one value",
 ["A-2, B-1, C-3, D-4","A-2, B-1, C-4, D-3","A-3, B-4, C-2, D-1","A-4, B-2, C-3, D-1","A-4, B-3, C-1, D-2"])
add("When the Employee entity of the following diagram is represented in a database which of the following should not be included?\n\n[Figure: ER diagram. Entity Employee with attributes: Date_of_Birth, Employee_Number, Employee_Name, Designation, Qualifications (double ellipse, multivalued), Age (dashed ellipse, derived).]",
 ["Date_of_Birth","Designation","Employee_Name","Employee_Number","Qualifications"])
add("Which of the listed relations will be obtained if the following ER diagram is correctly mapped into the relational model?\n\n[Figure: ER diagram. Entity Lecturer with attributes LecturerName, Address, DOB, NIC. Entity Course with attributes CourseName, CourseId. Relationship Teaches (with attribute Hours) between Lecturer (1) and Course (M).]\n\nA - Lecturer(NIC, LecturerName, DOB, Address)\nB - Lecturer(NIC, LecturerName, DOB, Address, CourseId)\nC - Teaches(NIC, CourseId, Hours)\nD - Course(CourseId, CourseName, Hours, NIC)",
 ["A and B only.","A and C only.","A and D only.","B and C only.","A, C and D only."],
 None,None)
add("Which of the following gives a correct matching between ER diagram components and the relational model?",
 ["Entity -> Field, Attribute -> Table, Unique attribute -> Primary key, Multivalued attribute -> Table","Entity -> Table, Attribute -> Field, Unique attribute -> Primary key, Multivalued attribute -> Table","Entity -> Table, Attribute -> Field, Unique attribute -> Table, Multivalued attribute -> Primary key","Entity -> Table, Attribute -> Primary key, Unique attribute -> Primary key, Multivalued attribute -> Table","Entity -> Table, Attribute -> Table, Unique attribute -> Primary key, Multivalued attribute -> Primary key"])
REL="""Consider the following relations:
adviser (adId, adName, adGender, adNIC, adPhone)
farmer (farmerId, farmerName, farmerAddress, farmerPhone)
task (taskId, taskName, farmerId, startDate, endDate)
advises (adId, taskId, startDate, endDate)
(Primary keys: adviser.adId, farmer.farmerId, task.taskId, advises.adId + taskId.)
Note: adNIC - The National Identity Card number of an adviser."""
add(REL+"\n\nWhich of the following statements are correct?\nA - One farmer can have many tasks.\nB - One adviser can advise many tasks.\nC - For one task, a farmer can have many advisers.",OPT3b,
 "පහත කවර ප්‍රකාශ නිවැරදි වේ ද?",OPT3bS)
add(REL+"\n\nWhich of the following statements are correct with respect to the given relations?\nA - All relations are in 3rd normal form.\nB - The startDate attribute in the task relation is a derived attribute.\nC - adNIC is a candidate key in the adviser relation.",OPT3b,
 None,None)
def sel(s,w): return "SELECT "+s+"\nFROM Student, Mark\nWHERE "+w
add(ADM+"\nWhich of the following SQL statements would produce an output with admission number, name of the student, subject code and marks obtained?",
 [sel("studentName, subjectCode, marksObtained","Student.admissionNo = Mark.admissionNo"),
  sel("Student.admissionNo, studentName, subjectCode, Student.marksObtained","Student.admissionNo = Mark.admissionNo"),
  sel("Student.admissionNo, studentName, subjectCode, marksObtained","Student.admissionNo = Mark.admissionNo"),
  sel("Student.admissionNo, studentName, subjectCode, marksObtained","Student.admissionNo = admissionNo"),
  sel("Student.admissionNo, studentName, subjectCode, marksObtained","admissionNo = Mark.admissionNo")])
add("Consider the following relation:\nstudent(stdNo, name, address, nicNo, date_of_birth)\n\nWhich of the following SQL (Structured Query Language) statements on the student relation is syntactically correct?",
 ["select *.* from student","select all from student","select * from student","select stdNo.name from student","select stdNo; name from student"])
add("Consider the following database operations:\nA - Remove records from a table\nB - Add new data to a table\nC - Modify the existing data in a table\nD - Retrieve data from a table\n\n\"The SQL statements ..................... should be used to perform the database operations A, B, C and D respectively.\"\n\nWhich of the following is most appropriate to fill the blank in the above statement?",
 ["delete, select, update and insert","delete, insert, select and update","select, delete, insert and update","insert, select, delete and update","delete, insert, update and select"])
add("Consider the following two relations:\nStudent(stdNo, name)\ncourseMarks(courseId, stdNo, marks)\n\nWhich of the following SQL (Structured Query Language) statements on the above relations is syntactically correct?",
 ["select stdNo, marks from student, courseMarks","select * from student and courseMarks","select s.stdNo and c.marks from student s, courseMarks c","select student.stdNo, courseMarks.marks from student, courseMarks\nwhere student.stdNo = courseMarks.stdNo","select student.stdNo and courseMarks.marks from student and courseMarks\nwhere student.stdNo = courseMarks.stdNo"])
add("Consider the following three tables in a relational database.\n"+SUBJ+"\n\nWhich of the following is the correct SQL statement to retrieve examId, name, and examDate of all examinations?",
 ["select examSubject.examId, name, examDate from exam, examSubject\nwhere exam.examId=examSubject.examId",
  "select examId, name, examDate from exam and examSubject\nwhere exam.examId=examSubject.examId",
  "select examId and name and examDate from exam and examSubject\nwhere exam.examId=examSubject.examId",
  "select * from exam and examSubject:\nwhere exam.examId=examSubject.examId",
  "select * from exam, examSubject\nwhere exam.examId=examSubject.examId"])
U="update examSubject set examDate='2014.08.25'\nwhere "
add("Consider the following three tables in a relational database.\n"+SUBJ+"\n\nWhich of the following SQL statements changes only the date of examination of Physics paper of GCE AL examination to 2014.08.25?",
 [U+"subjectId='SUB003' or 'sub003'",U+"examId='EXAM002' or subjectId='SUB003'",U+"examId='EXAM002' and subjectId='SUB003'",U+"examDate='2014.08 21'",U+"examId='EXAM002' or subjectId='SUB003' or examDate='2014.08.23'"])
add("Consider the following four relational database tables.\n\nitem table:\nitem | product\nT001 | Laptop\nT002 | TV\nT003 | Camera\n\nsupplier table:\nsupplier | name\nS001 | BeLap Company Ltd.\nS002 | DigiTV trading company\n\nitemSupplier table:\nitem | supplier\nT001 | S001\nT002 | S001\nT002 | S002\n\ndelivery table:\nitem | supplier | batch | quantity | date\nT001 | S001 | B01 | 450 | 1.5.2015\nT002 | S001 | AB1 | 45 | 1.5.2015\nT001 | S001 | B02 | 500 | 2.5.2015\nT001 | S002 | C01 | 75 | 5.5.2015\n\nWhich of the following actions is taken by a database management system when the SQL statement \"delete from item\" is executed?",
 ["It will ask the user to select records for deletion.","It may delete all the records from the 'item' table.","It will drop the 'item' table.","It will not delete any record from the 'item' table.","The SQL statement will not be executed since it has errors."])
add("Which of the followings is correct with respect to the output of an SQL statement?",
 ["It generates an error if no data is available in the tables referred in the SQL statement.","It is always a table.","The order of the attributes in the output should be the same as the order of attributes in the table definition.","Outputs cannot be produced if the primary keys are not defined.","Names of attributes in the output should be the same as names in the table definition."])
add("The length of an attribute defined using a Data Definition Language (DDL) statement is a/an .......................... constraint.\n\nWhich of the followings is the most appropriate to fill the blank in the above statement?",
 ["primary key","foreign key","null value","domain","application"])
add("Consider the following table in a relational database:\n\nstudent | name | telephone | zscore\nS0001 | Dananjaya | 0711118337 | 1.8\nS0002 | Saluka | 0712227447 | 1.9\nS0003 | Upul | 0713333882 | 2.0\nS0004 | Priyankara | 0714445225 | 1.9\nS0005 | Supun | 0715556446 | 2.1\n\nWhat is the minimum number of SQL statements required to update all the values of the attribute zscore in the above table to 2.1?",
 ["1","2","3","4","5"])
add("Consider the following relational schema consisting of text fields:\n\nStudents (admission_number, surname_with_initials, house_number, street_name, village, postal_town, postal_code)\n\nAssume that for a given postal_town only one postal_code exists.\n\nWhich of the following is displayed as output if the query is executed?\n\nSelect * from Students\nwhere postal_code ='10120' and house_number ='30A';",
 ["postal_code of all records","postal_code and house_number of records having postal_code '10120' and house_number as '30A'","postal_code and house_number of all records","all fields of records having postal_code as '10120' and house_number as '30A'","all fields of all records"])
add("Consider the following database table.\n\nStudent_Sport table:\nStudent_Id | Event_Id | Event_Name\n10012 | S-02 | Carrom\n10022 | S-01 | Basketball\n10018 | S-02 | Carrom\n10012 | S-03 | Volleyball\n10025 | S-04 | Chess\n10018 | S-01 | Basketball\n\nIt is required to add a new field called Age to the Student_Sport table and the values of the new field must be greater than 10.\n\nWhich one is the correct SQL statement to implement the above requirement?",
 ["Alter table Student_Sport add check (Age> 10);","Alter table Sudent_Sport add where (Age> 10);","Alter table Student_Sport set check (Age> 10);","Update table Student_Sport add check (Age> 10);","Update table Student_Sport add where (Age> 10);"])
add("Which of the following SQL commands isn't available in the Data Manipulation Language (DML)?",
 ["CREATE","DELETE","INSERT","SELECT","UPDATE"])
add("Consider the following SQL statement:\n\nUpdate school set contact_person= 'Sripal W.' where school_id= '04';\n\nWhich of the following is true when the above SQL statement is executed?",
 ["It adds an additional field with the name contact_person and adds value into that new field as 'Sripal W.' only in the records having school_id = 04","It adds an additional value to the contact_person as 'Sripal W.' only in the records having school_id = 04","It changes the field name of contact_person as 'Sripal W.' when selecting the records with school_id = 04","It changes value of contact_person as 'Sripal W.' only in records having school_id = 04","It selects all the records having school_id = 04 and contact_person as 'Sripal W.'"])
add("Consider the following SQL statement:\n\nAlter table subject add primary key (Subject_Id);\n\nWhich of the following is incorrect about the above SQL statement?",
 ["It adds a primary key constraint to the table named subject.","The table named subject should already exist.","The field Subject_Id should not be null.","A table named subject is created with a primary key named Subject_Id.","The values of the field Subject_Id should not be repeated in subject table."])
add("What is the correct SQL statement to delete a database called 'ALdb'?",
 ["delete ALdb;","delete database ALdb;","drop ALdb;","drop database ALdb;","remove database ALdb;"])
add("Consider the following Results and Subjects tables.\n"+RES+"\n\nWhat is the correct SQL statement to retrieve the values of attributes StudentNo, SubjectName and Grade?",
 ["SELECT Results.StudentNo, Subjects.SubjectName, Results.Grade FROM Results INNER JOIN ON Results.SubjectID = Subjects.SubjectID;","SELECT Results.StudentNo, Subjects.SubjectName, Results.Grade FROM Results INNER JOIN Results.SubjectID = Subjects.SubjectID;","SELECT Results.StudentNo, Subjects.SubjectName, Results.Grade FROM Results INNER JOIN Subjects IN Results.SubjectID = Subjects.SubjectID;","SELECT Results.StudentNo, Subjects.SubjectName, Results.Grade FROM Results INNER JOIN Subjects ON Results.SubjectID = Subjects.SubjectID;","SELECT Results.StudentNo, Subjects.SubjectName, Results.Grade INNER JOIN Results AND Subjects Results.SubjectID = Subjects.SubjectID;"])
add("The tables which are partially extracted from a database used in an information system developed for a shop are shown below. Answer the question using those tables.\n"+SHOP+"\n\nWhat will be the output after executing the following SQL statement?\n\nSELECT Customer.Fname, Customer.Lname, Order.OrderId\nFROM Customer INNER JOIN Order ON Customer.CusId = Order.CusId\nWHERE Customer.Location=\"Galle\";",
 ["Fname | Lname | OrderId\nKalum | Gamage | A001\nKalum | Gamage | A003\nShiromi | Silva | A002",
  "Fname | Lname | OrderId\nKalum | Gamage | A004\nKalum | Perera | A001\nKalum | Gamage | A003\nShiromi | Silva | A002",
  "Fname | Lname | OrderId\nKalum | Gamage | A001\nKalum | Perera | A003\nShiromi | Silva | A002",
  "Lname | Fname | OrderId\nGamage | Kalum | A001\nGamage | Kalum | A003\nSilva | Shiromi | A002",
  "Fname | Lname | OrderId\nKalum | Gamage | A001\nShiromi | Silva | A002"])
add("Consider the following Employee Relation:\n\nEmployee_ID | Employee_Name | Salary\n1001 | John | 60000\n1002 | Hari | 55000\n1003 | Mahas | 70000\n1004 | Sarath | 65000\n1005 | Rajah | 75000\n\nWhat would be the output of the following SQL query when it is applied on the Employee relation?\n\nSELECT COUNT(*) FROM Employee\nWHERE Salary > ANY (SELECT Salary FROM Emplyoee);",
 ["3","4","5","6","10"])
add("Consider the given SQL statements to create two database tables named LENDING and STUDENT:\n\nCREATE TABLE LENDING(\n  BOOK_NUMBER VARCHAR(10) NOTNULL,\n  BOOK_NAME VARCHAR(20) NOTNULL,\n  AUTHOR VARCHAR(25) NOTNULL,\n  DESCRIPTION VARCHAR(75) NOTNULL,\n  ISSUED_DATE DATE,\n  STUDENT_ID CHAR(5) NOTNULL,\n  PRIMARY KEY(BOOK_NUMBER));\n\nCREATE TABLE STUDENT(\n  STUDENT_ID CHAR(5) NOTNULL,\n  NAME VARCHAR(25) NOTNULL,\n  BIRTHDAY DATE NOTNULL,\n  ADDRESS VARCHAR(25) NOTNULL,\n  PROVINCE CHAR(10),\n  PRIMARY KEY(STUDENT_ID));\n\nWhich of the following statements are correct?\nA. STUDENT_ID is a foreign key in the LENDING table.\nB. It is compulsory to input data to the DATE data type fields in both tables.\nC. STUDENT_ID can contain only five English letters.",
 ["A only.","A and B only.","A and C only.","B and C only.","All of the above."],
 "පහත කවර වගන්ති නිවැරදි වේ ද?",OPT3bS)
assert len(Q)==len(S)==34,(len(Q),len(S))
out=[]
for it,q in zip(S,Q):
    o=dict(n=it['n'],d=it['d'],q=q['q'])
    if q['qs']: o['qs']=q['qs']
    o['o']=q['o']
    if q['os']: o['os']=q['os']
    assert 4<=len(o['o'])<=5 and all(x.strip() for x in o['o'])
    if 'os' in o: assert len(o['os'])==len(o['o'])
    out.append(o)
json.dump(out,open('D:/DevOps/aws-clf-c02-bridge/tools/transcribed/ictl-db-mcq.part2.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out))
