# Episode 3 — Global Infrastructure, Compute, Storage, Databases (Domain 3, 34% — Part 1)

**Hosts:** **නදී** (AWS engineer) · **කසුන්** (තර්ක කරන developer)

**මේ episode එකෙන් ඉගෙන ගන්නේ:**
- AWS වලට access වෙන ක්‍රම
- Regions, AZs, Edge locations
- EC2, Lambda, containers
- S3, EBS, EFS
- RDS, DynamoDB සහ අනෙක් databases

---

## Opening

**කසුන්:** AWS එකේ services 200කට වඩා තියෙනවා. ඔක්කොම කටපාඩම් කරන්න ඕනද?

**නදී:** නෑ. හැම service එකකටම **එක line එකක්** දැනගත්තම ඇති. Questions වල **keyword** එක අල්ලගන්න පුරුදු වෙන්න. අද ඒක තමයි කරන්නේ.

---

## 1. AWS වලට access වෙන ක්‍රම

| ක්‍රමය | සරලව |
| --- | --- |
| **Management Console** | Web browser එකෙන් click කරලා |
| **AWS CLI** | Command line එකෙන් |
| **SDKs** | Code එකෙන් (Python, Java...) |
| **CloudFormation** | **Infrastructure as Code** — template එකකින් ඔක්කොම හදනවා |

**කසුන්:** කවදද Console එක, කවදද CloudFormation?

**නදී:** **එක පාරක්** කරන පොඩි වැඩක් → **Console**. **නැවත නැවත** කරන්න ඕන (environments 10ක් එකම විදිහට) → **CloudFormation**.

- **Elastic Beanstalk** — code එක දෙන්න, servers, load balancer, scaling ඔක්කොම AWS හදනවා.

---

## 2. Global Infrastructure

**නදී:** ගමක් හිතන්න:

- **Region** = **දිස්ත්‍රික්කයක්** (Mumbai, Singapore)
- **Availability Zone (AZ)** = දිස්ත්‍රික්කේ **වෙන වෙනම නගර** — data centers එකක් හෝ කිහිපයක්. Region එකක **අවම 3**ක්. එකක ගින්නක් ගියත් අනිකට බලපාන්නේ නෑ (**no single point of failure**).
- **Edge location** = පාරවල් අයිනේ **පොඩි කඩ** — users ලට ළඟින් content **cache** කරනවා (CloudFront, Route 53).

**කසුන්:** High availability ගන්නේ කොහොමද?

**නදී:** "**බිත්තර සේරම එක කූඩයට දාන්න එපා.**" → **Multiple AZs** වලට deploy කරන්න.

> **Region එකක් තෝරන්න කරුණු 4:**
> 1. **Compliance / data residency** (නීතිය)
> 2. **Latency** (customers ලට ළඟද)
> 3. **Service availability** (service එක එතන තියෙනවද)
> 4. **Pricing** (මිල)
>
> **Multiple Regions** ඕන ඇයි? → **Disaster recovery** · business continuity · ලෝකය පුරා users ට low latency · data sovereignty

**අනෙක් infrastructure:**
- **Local Zones** — ලොකු නගරවලට ළඟින්, ඉතා low latency
- **Wavelength** — 5G network ඇතුළේ
- **Outposts** — AWS hardware **ඔයාගේ data center** එකේ

---

## 3. Compute

### EC2 — Virtual servers

**නදී:** **EC2** = cloud එකේ virtual computer. **IaaS**. OS එක ඔයා බලාගන්නවා.

| Instance type | මතක trick එක | Use |
| --- | --- | --- |
| **General purpose** (T, M) | සාමාන්‍ය | Web servers |
| **Compute optimized** (C) | **C** = **C**PU | Gaming, scientific, batch |
| **Memory optimized** (R, X) | **R** = **R**AM | In-memory databases |
| **Storage optimized** (I, D) | **I** = **I**/O | High disk read/write |
| **Accelerated** (P, G) | **G** = **G**PU | Machine learning |

### Scaling සහ Load Balancing

- **Auto Scaling** — demand අනුව instances එකතු / අයින් කරනවා → **Elasticity**
- **Elastic Load Balancing** — traffic instances අතර **බෙදනවා**
  - **ALB** — HTTP/HTTPS (layer 7)
  - **NLB** — TCP/UDP, ඉතා වේගවත් (layer 4)

### Serverless

**නදී:** **AWS Lambda** — code එක දෙනවා. **Event** එකක් ආවම run වෙනවා. Run වෙන වෙලාවට විතරක් ගෙවනවා. උපරිම **15 minutes**.

**කසුන්:** "Serverless" බොරුවක්! Servers නැතුව code run වෙන්නේ නෑ.

**නදී:** *(හිනාවෙලා)* ඇත්ත! Servers තියෙනවා. ඒත් **ඔයාට ඒවා බලාගන්න ඕන නෑ**. Taxi එකක් වගේ — වාහනයක් තියෙනවා, ඒත් service කරන්න ඕන නෑ, ගමනට විතරයි ගෙවන්නේ.

**කසුන්:** එහෙනම් හැම දේම Lambda වලින්!

**නදී:** නෑ. පැය ගාණක් run වෙන වැඩකට Lambda හරියන්නේ නෑ — 15 minute limit එක.

### Containers

| Keyword | Service |
| --- | --- |
| Containers (AWS ගේ ක්‍රමය) | **Amazon ECS** |
| **Kubernetes** | **Amazon EKS** |
| Containers, **servers manage නොකර** | **AWS Fargate** |
| Container **images** store | **Amazon ECR** |

**අනෙක්:** **Lightsail** — ආරම්භකයින්ට සරල server එකක්, **මාසික fixed price** · **AWS Batch** — batch jobs

---

## 4. Storage

**කසුන්:** Storage storage තමයි. ඇයි වර්ග තුනක්?

**නදී:** "**All that glitters is not gold.**" හැම storage එකම එක වගේ නෙවෙයි.

| Service | Type | සරලව |
| --- | --- | --- |
| **Amazon S3** | **Object** | **Google Drive** වගේ — files URL එකෙන්. Unlimited. **11 nines** durability |
| **Amazon EBS** | **Block** | Laptop එකේ **hard disk** — **එක EC2** එකකට, **එකම AZ** එකේ |
| **Instance Store** | Block (temporary) | EC2 **stop** කළොත් data **නැති** වෙනවා |
| **Amazon EFS** | **File** | Office එකේ **shared drive** — **Linux** EC2 ගොඩකට එකපාර |
| **Amazon FSx** | File | **Windows** file server / Lustre (HPC) |
| **Storage Gateway** | Hybrid | On-prem servers ට cloud storage (cache එකක් එක්ක) |
| **AWS Backup** | Backup | Services ගොඩකට **central** backup |

**කසුන්:** S3 එකේ OS එක install කරන්න පුළුවන්ද?

**නදී:** නෑ. OS එකට ඕන **block storage** — **EBS**.

### S3 Storage Classes

**නදී:** "**ඇඳේ දිගට කකුල් දිගහරින්න.**" Data එක පාවිච්චි කරන වාර ගණන අනුව class එක තෝරන්න.

| Class | කවදද? |
| --- | --- |
| **S3 Standard** | නිතර පාවිච්චි කරනවා |
| **S3 Intelligent-Tiering** | Access pattern එක **දන්නේ නෑ** |
| **S3 Standard-IA** | කලාතුරකින්, ඒත් ඉක්මනින් ඕන |
| **S3 One Zone-IA** | කලාතුරකින්, ආයෙ හදන්න පුළුවන් data (**එක AZ** එකයි) |
| **Glacier Instant Retrieval** | Archive, ඒත් **milliseconds** වලින් ඕන |
| **Glacier Flexible Retrieval** | Archive, **minutes–hours** |
| **Glacier Deep Archive** | **ලාභම**, **පැය 12–48**. අවුරුදු ගාණක් තියන records |

> **Lifecycle policy** = "දවස් 30කට පස්සේ IA එකට, දවස් 365කට පස්සේ Deep Archive එකට" — **ඉබේම** move කරනවා.

---

## 5. Databases

**කසුන්:** මම EC2 එකේ MySQL install කරගන්නවා. RDS ට ගෙවන්නේ ඇයි?

**නදී:** පුළුවන්. ඒත් එතකොට patching, backups, failover — **ඔක්කොම ඔයාගේ වැඩ**. රෑ 2ට DB එක crash වුණොත් call එක ඔයාට. **RDS** නම් ඒවා **AWS** බලාගන්නවා.

> **Exam:** "**reduce management / operational overhead**" → **Managed database (RDS)**. "**Full control of the OS**" → **EC2 database**.

### Relational (SQL)

- **Amazon RDS** — managed **SQL** DB. MySQL, PostgreSQL, MariaDB, Oracle, SQL Server.
  - **Multi-AZ** → **High availability** (standby copy, auto failover)
  - **Read Replicas** → **Read performance** (read-only copies)
- **Amazon Aurora** — AWS ගේම SQL DB. MySQL/PostgreSQL compatible. වේගයි.

**කසුන්:** Multi-AZ සහ Read Replica දෙකම copies නේ?

**නදී:** **Multi-AZ = spare tyre** (කැඩුණොත් මාරු කරන්න). **Read Replica = තව cashiers ලා** (පෝලිම ඉක්මන් කරන්න).

### අනෙක් databases — keyword එකෙන්

| Keyword | Service |
| --- | --- |
| **NoSQL**, key-value, millisecond, serverless | **DynamoDB** |
| **In-memory cache** (Redis, Memcached) | **ElastiCache** |
| **Data warehouse**, analytics | **Redshift** |
| **Graph** (social networks) | **Neptune** |
| **MongoDB** | **DocumentDB** |
| **Cassandra** | **Keyspaces** |
| **Time-series** (IoT) | **Timestream** |

**කසුන්:** SQL ද NoSQL ද හොඳ?

**නදී:** "**මාළුවාව ගහට නගින හැටියෙන් මනින්න එපා.**" **Joins, complex queries** → **RDS/Aurora**. **Huge scale, simple lookups** → **DynamoDB**.

### Database migration

- **AWS DMS** — DB එක migrate කරනවා, migrate වෙද්දිත් DB එක වැඩ
- **AWS SCT** — DB engine එක **වෙනස්** කරනවා නම් (Oracle → Aurora) schema convert කරනවා

---

## Practice Questions (20)

**Q1.** Which describes an Availability Zone?
A. A single server in a data center
B. One or more data centers with separate power and networking in a Region
C. A location that caches content for CloudFront
D. A group of Regions

**Q2.** How can a company make an application highly available on AWS?
A. Deploy it in a single Availability Zone
B. Deploy it across multiple Availability Zones
C. Use a larger EC2 instance
D. Use edge locations only

**Q3.** Which factors should a company consider when choosing an AWS Region? (Select TWO)
A. Data residency requirements
B. Number of IAM users
C. Latency to end users
D. Size of the S3 bucket
E. The AWS account ID

**Q4.** Which AWS feature caches content close to end users?
A. Availability Zones
B. Edge locations
C. VPC subnets
D. AWS Outposts

**Q5.** A company wants to run AWS infrastructure in its own on-premises data center. Which service?
A. AWS Local Zones
B. AWS Wavelength
C. AWS Outposts
D. Amazon Lightsail

**Q6.** A company must create the same infrastructure in 10 environments, repeatedly. What is BEST?
A. AWS Management Console
B. AWS CloudFormation
C. Amazon CloudWatch
D. AWS Trusted Advisor

**Q7.** Which EC2 instance type is BEST for a high-performance scientific application that needs a lot of CPU?
A. Memory optimized
B. Storage optimized
C. Compute optimized
D. General purpose

**Q8.** Which service runs code in response to events without managing servers?
A. Amazon EC2
B. AWS Lambda
C. Amazon EBS
D. Amazon Lightsail

**Q9.** Which service runs containers without managing the underlying servers?
A. Amazon EC2
B. AWS Fargate
C. Amazon EBS
D. Amazon ECR

**Q10.** A company wants to run Kubernetes on AWS. Which service?
A. Amazon ECS
B. Amazon EKS
C. AWS Lambda
D. AWS Batch

**Q11.** Which provides elasticity for Amazon EC2?
A. Amazon EBS snapshots
B. EC2 Auto Scaling
C. AWS CloudTrail
D. Amazon Route 53

**Q12.** What does a load balancer do?
A. Encrypts data at rest
B. Distributes incoming traffic across multiple targets
C. Stores backups
D. Creates IAM users

**Q13.** Which storage service is object storage?
A. Amazon EBS
B. Amazon EFS
C. Amazon S3
D. Instance store

**Q14.** Which storage gives a shared file system to many Linux EC2 instances at the same time?
A. Amazon EBS
B. Amazon EFS
C. Instance store
D. S3 Glacier

**Q15.** Which storage is lost when an EC2 instance is stopped?
A. Amazon EBS
B. Amazon S3
C. Instance store
D. Amazon EFS

**Q16.** Which S3 storage class is BEST when access patterns are unknown or change often?
A. S3 Standard
B. S3 Intelligent-Tiering
C. S3 Glacier Deep Archive
D. S3 One Zone-IA

**Q17.** Which is the LOWEST-cost S3 storage class for data that is rarely accessed and can wait 12+ hours?
A. S3 Standard-IA
B. S3 Glacier Instant Retrieval
C. S3 Glacier Deep Archive
D. S3 Intelligent-Tiering

**Q18.** A company wants to automatically move S3 objects to cheaper storage after 90 days. What should it use?
A. S3 Lifecycle policy
B. AWS Backup
C. Amazon EBS snapshots
D. AWS Storage Gateway

**Q19.** A relational database must keep running if an Availability Zone fails. What should the company use?
A. RDS Read Replicas
B. RDS Multi-AZ deployment
C. Amazon ElastiCache
D. Amazon S3

**Q20.** Which database is a NoSQL key-value database with single-digit millisecond performance at any scale?
A. Amazon RDS
B. Amazon Aurora
C. Amazon DynamoDB
D. Amazon Redshift

### Extra (5) — Database keywords

**Q21.** Which service is an in-memory cache? → A. Redshift B. ElastiCache C. Neptune D. DMS
**Q22.** Which is a data warehouse? → A. Redshift B. DynamoDB C. DocumentDB D. Aurora
**Q23.** Which is a graph database? → A. Keyspaces B. Neptune C. RDS D. Timestream
**Q24.** Which migrates a database to AWS with minimal downtime? → A. AWS SCT B. AWS DMS C. AWS Backup D. DataSync
**Q25.** Which converts an Oracle schema to Aurora PostgreSQL? → A. AWS DMS B. AWS SCT C. CloudFormation D. AWS Glue

### Answers

- **Q1 — B.** AZ = data centers **එකක් හෝ කිහිපයක්**, වෙනම power/network.
- **Q2 — B.** Multiple AZs = බිත්තර කූඩ කිහිපයක.
- **Q3 — A, C.** Data residency + latency.
- **Q4 — B.** Edge locations = පාර අයිනේ පොඩි කඩ.
- **Q5 — C.** ඔයාගේ data center එකේ AWS → **Outposts**.
- **Q6 — B.** Repeatable → **CloudFormation**.
- **Q7 — C.** CPU → **C**ompute optimized.
- **Q8 — B.** Events + no servers → **Lambda**.
- **Q9 — B.** Containers + no servers → **Fargate**.
- **Q10 — B.** Kubernetes → **EKS**.
- **Q11 — B.** Elasticity → **Auto Scaling**.
- **Q12 — B.** Traffic බෙදනවා.
- **Q13 — C.** Object → **S3**.
- **Q14 — B.** Shared Linux → **EFS**.
- **Q15 — C.** Stop කළොත් නැති වෙනවා → **Instance store**.
- **Q16 — B.** Unknown pattern → **Intelligent-Tiering**.
- **Q17 — C.** ලාභම, පැය 12+ → **Deep Archive**.
- **Q18 — A.** ඉබේම move → **Lifecycle policy**.
- **Q19 — B.** AZ failure → **Multi-AZ** (spare tyre).
- **Q20 — C.** NoSQL key-value → **DynamoDB**.
- **Q21 — B** ElastiCache · **Q22 — A** Redshift · **Q23 — B** Neptune · **Q24 — B** DMS · **Q25 — B** SCT

---

## Closing

**කසුන්:** "ලේසියි" කියලා හිතපු storage එකේ වර්ග ගොඩයි. ඒත් table එකෙන් බැලුවම පැහැදිලියි.

**නදී:** **Homework:** Free Tier එකේ **t3.micro** EC2 එකක් launch කරන්න. S3 bucket එකක් හදලා file එකක් upload කරන්න. වැඩේ ඉවර වුණාම EC2 එක **terminate** කරන්න අමතක කරන්න එපා!

**කසුන්:** ඊළඟට — Networking, AI, Analytics.

**නදී:** ආයෙත් හමුවෙමු!
