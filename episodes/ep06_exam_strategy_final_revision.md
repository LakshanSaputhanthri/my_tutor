# Episode 6 — Exam Strategy + Rapid Revision + Mock Exam (30 Questions)

**Hosts:** **නදී** (AWS engineer) · **කසුන්** (දැන් ලෑස්ති developer)

**මේ episode එකෙන්:**
- Exam එකට කලින් සතියේ කරන්න ඕන දේ
- Question එකක් විසඳන 7-step ක්‍රමය
- Rapid fire revision
- **Mock exam — questions 30** (exam එකේ domain weights අනුව)

---

## 1. Exam එකට කලින් සතිය

**කසුන්:** කවදද exam එක book කරන්න ලෑස්ති?

**නදී:** Practice exams **දෙකක් පිටිපස්සට 85%+** ගත්තොත්.

**අන්තිම සතියේ plan එක:**
1. දවසකට **full practice exam** එකක් — විනාඩි 90, timed
2. හැම question එකකම **explanation** එක කියවන්න — හරි ගියත්, වැරදුණත්
3. **Mistakes notebook** — "Inspector කිව්වා, හරි GuardDuty. ඇයි: threat vs vulnerability"
4. මේ episodes 6 එකේ **tables** ආයෙත් බලන්න
5. කලින් රෑ **හොඳට නිදාගන්න** — නිදි මරාගෙන පාඩම් කරන්න එපා

**Free official practice (AWS Skill Builder):**
- **Official Practice Question Set** (free)
- **Official Pretest**
- **Official Practice Exam**

**Online exam නම්:** කලින් දවසේ **Pearson VUE system test** · මේසය හිස් · ID ළඟ · කාමරයේ වෙන කවුරුවත් එපා · **ESL +30** request කළාද?

---

## 2. Question එකක් විසඳන 7-step ක්‍රමය

**නදී:** Question එකකට තත්පර **80**ක් විතර.

1. **අන්තිම වාක්‍යය මුලින්** කියවන්න — ඇත්තටම අහන්නේ මොකක්ද?
2. **Qualifier** එක අල්ලගන්න — **MOST cost-effective · LEAST operational overhead · MOST secure**
3. **Keyword** එක හොයන්න — serverless, who, alarm, interrupt, PII, DDoS...
4. පැහැදිලිවම **වැරදි දෙක** අයින් කරන්න
5. ඉතුරු දෙකෙන් qualifier එකට ගැලපෙන එක තෝරන්න
6. **Select TWO** නම් — දෙකක් තෝරලාද ගණන් කරන්න
7. සැක නම් — answer එකක් දාලා **flag** කරලා ඉස්සරහට

> **Golden rules (සැක නම්):**
> - **Managed / serverless** option එක > "EC2 එකේ තනියම install" (full control ඉල්ලන්නේ නැත්නම්)
> - High availability → **multiple AZs** · Disaster recovery → **multiple Regions**
> - Security → **least privilege · MFA · IAM roles · encryption**
> - Root user → **MFA දාලා, පාවිච්චි නොකර තියන්න**

**කසුන්:** කාලය බෙදන්නේ කොහොමද?

**නදී:** පළවෙනි round එක විනාඩි **60**කින්. ඉතුරු කාලය **flagged** questions වලට. එක question එකක හිරවෙන්න එපා.

---

## 3. Rapid Fire — Keyword → Service

**නදී:** මම keyword එක කියනවා, ඔයා service එක කියන්න — තත්පර 2!

| Keyword | Service |
| --- | --- |
| Who made this API call? | CloudTrail |
| CPU alarm | CloudWatch |
| Configuration history / compliance rules | Config |
| Download SOC / PCI reports | Artifact |
| DDoS | Shield |
| SQL injection | WAF |
| Threats | GuardDuty |
| Vulnerabilities | Inspector |
| PII in S3 | Macie |
| Encryption keys | KMS |
| Rotate passwords | Secrets Manager |
| One login, many accounts | IAM Identity Center |
| Object storage | S3 |
| Disk for one EC2 | EBS |
| Shared Linux files | EFS |
| Cheapest archive | Glacier Deep Archive |
| Unknown access pattern | Intelligent-Tiering |
| Huge data, slow internet | Snowball Edge |
| Managed SQL DB | RDS / Aurora |
| NoSQL | DynamoDB |
| Data warehouse | Redshift |
| Cache | ElastiCache |
| Serverless code | Lambda |
| Serverless containers | Fargate |
| Kubernetes | EKS |
| Infrastructure as Code | CloudFormation |
| Just deploy my web app | Elastic Beanstalk |
| CDN | CloudFront |
| DNS | Route 53 |
| Private line to AWS | Direct Connect |
| Queue / decouple | SQS |
| Notifications | SNS |
| SQL on S3 | Athena |
| Streaming | Kinesis |
| Dashboards | Quick Sight |
| Build ML models | SageMaker AI |
| GenAI foundation models | Bedrock |
| Chatbot | Lex |
| Text → speech | Polly |
| Speech → text | Transcribe |
| Estimate before building | Pricing Calculator |
| Analyze past costs | Cost Explorer |
| Cost alert | Budgets |
| Interruptible = cheapest | Spot |
| Server-bound licenses | Dedicated Hosts |
| Designated TAM | Enterprise Support |

**කසුන්:** *(හිනාවෙලා)* Episode 1 එකේ මට IaaS කියන එකවත් තේරුණේ නෑ. දැන් මේ ඔක්කොම කියන්න පුළුවන්!

---

## 4. Mock Exam — 30 Questions

**නදී:** දැන් සැබෑ exam එක වගේ. Timer එක **විනාඩි 40**කට දාන්න. Notes බලන්න එපා. උත්තර අන්තිමට.

### Domain 1 — Cloud Concepts

**Q1.** Which benefit of AWS lets a company deploy an application in multiple countries in a few minutes?
A. Economies of scale
B. Go global in minutes
C. Stop guessing capacity
D. Fault tolerance

**Q2.** Which costs does a company NO LONGER pay when it moves from on-premises to AWS? (Select TWO)
A. Data center electricity and cooling
B. IAM user management
C. Buying and replacing physical servers
D. Application code updates
E. Data encryption decisions

**Q3.** Which Well-Architected pillar includes using infrastructure as code and automating operations?
A. Operational Excellence
B. Reliability
C. Sustainability
D. Security

**Q4.** Which Well-Architected pillar focuses on using only the resources you need and avoiding waste?
A. Performance Efficiency
B. Cost Optimization
C. Reliability
D. Security

**Q5.** A company replaces its on-premises CRM with a SaaS CRM product. Which migration strategy is this?
A. Rehost
B. Replatform
C. Repurchase
D. Retain

**Q6.** Which is an example of moving from CapEx to OpEx?
A. Buying servers for a new data center
B. Paying monthly for EC2 usage instead of buying servers
C. Signing a 10-year building lease
D. Hiring more data center staff

**Q7.** Which AWS CAF perspective focuses on risk management and portfolio management?
A. People
B. Governance
C. Platform
D. Operations

### Domain 2 — Security and Compliance

**Q8.** Under the shared responsibility model, which task is the customer's responsibility for AWS Lambda?
A. Patching the operating system
B. Managing the function code and IAM permissions
C. Maintaining physical servers
D. Scaling the underlying infrastructure

**Q9.** Which actions follow AWS best practices for the root user? (Select TWO)
A. Enable MFA
B. Use the root user for daily administration
C. Create root access keys for applications
D. Create IAM users or use IAM Identity Center for daily work
E. Share the root password with all developers

**Q10.** Which service gives a central view of security findings from GuardDuty, Inspector, and Macie?
A. AWS Security Hub
B. AWS Config
C. AWS Artifact
D. Amazon CloudWatch

**Q11.** A security team wants to know which IAM user terminated an EC2 instance last night. Which service?
A. Amazon CloudWatch
B. AWS CloudTrail
C. Amazon Inspector
D. AWS Trusted Advisor

**Q12.** Which encryption protects data while it moves between a user's browser and a web server?
A. Encryption at rest
B. Encryption in transit (TLS)
C. AWS KMS key rotation
D. S3 versioning

**Q13.** Which service provides free SSL/TLS certificates for websites?
A. AWS Certificate Manager
B. AWS KMS
C. AWS CloudHSM
D. Amazon Cognito

**Q14.** A company must restrict what member accounts in AWS Organizations can do. What should it use?
A. Security groups
B. Service control policies (SCPs)
C. Network ACLs
D. AWS Budgets

**Q15.** Which service adds user sign-up and sign-in to a mobile app?
A. AWS IAM Identity Center
B. Amazon Cognito
C. AWS Directory Service
D. AWS Secrets Manager

**Q16.** Which service checks an AWS account for security issues like open ports and missing MFA on the root user?
A. AWS Trusted Advisor
B. Amazon Polly
C. AWS Cost Explorer
D. Amazon Kinesis

### Domain 3 — Cloud Technology and Services

**Q17.** Which is TRUE about Availability Zones?
A. They share a single power source
B. They are isolated so they do not share single points of failure
C. There is only one per Region
D. They are the same as edge locations

**Q18.** A company needs a database that requires full control of the operating system. What should it use?
A. Amazon RDS
B. Database installed on Amazon EC2
C. Amazon DynamoDB
D. Amazon Aurora Serverless

**Q19.** Which service stores Docker container images?
A. Amazon ECS
B. Amazon ECR
C. Amazon EKS
D. AWS Fargate

**Q20.** Which storage option attaches to a single EC2 instance as a persistent block device?
A. Amazon S3
B. Amazon EBS
C. Amazon EFS
D. AWS Storage Gateway

**Q21.** Which service gives on-premises applications access to cloud storage with local caching?
A. AWS Storage Gateway
B. Amazon EFS
C. AWS Snowcone
D. Amazon S3 Glacier

**Q22.** Which service centrally manages and automates backups across EBS, RDS, and DynamoDB?
A. AWS Backup
B. Amazon S3 Lifecycle
C. AWS DataSync
D. AWS Config

**Q23.** A read-heavy application slows down because of many database read requests. What can improve read performance? (Select TWO)
A. RDS Read Replicas
B. Amazon ElastiCache
C. RDS Multi-AZ only
D. AWS Shield
E. Amazon SNS

**Q24.** Which service sends marketing emails to many customers?
A. Amazon SES
B. Amazon SQS
C. Amazon Connect
D. Amazon Lex

**Q25.** Which service lets employees run desktop applications from a web browser without installing them?
A. Amazon AppStream 2.0
B. AWS Amplify
C. Amazon Lightsail
D. AWS Batch

**Q26.** Which service prepares and transforms data for analytics (ETL) without managing servers?
A. AWS Glue
B. Amazon Redshift
C. Amazon Kinesis
D. Amazon Athena

### Domain 4 — Billing, Pricing, and Support

**Q27.** A company's workload is steady but it may change instance families in the future. Which option gives a discount AND flexibility?
A. Standard Reserved Instances
B. Convertible Reserved Instances
C. Spot Instances
D. Dedicated Hosts

**Q28.** Which support plan offers the fastest response for mission-critical workloads?
A. Business Support+
B. Enterprise Support
C. Unified Operations
D. Basic

**Q29.** Which AWS resource gives step-by-step guidance and patterns for migrations and modernization?
A. AWS Prescriptive Guidance
B. AWS Artifact
C. AWS Marketplace
D. AWS Trust & Safety

**Q30.** In AWS Organizations, how do Reserved Instance discounts work by default?
A. They apply only to the account that bought them
B. They can be shared across accounts in the organization
C. They are cancelled when accounts are added
D. They only apply to Spot Instances

---

## Mock Exam Answers

| Q | Answer | ඇයි? (සරලව) |
| --- | --- | --- |
| 1 | **B** | රටවල් ගොඩකට විනාඩි කිහිපයකින් |
| 2 | **A, C** | Data center වියදම් + servers ගන්න වියදම් AWS බලාගන්නවා |
| 3 | **A** | Automate, IaC → Operational Excellence |
| 4 | **B** | Waste නැති කරනවා → Cost Optimization |
| 5 | **C** | SaaS එකකට → Repurchase (drop and shop) |
| 6 | **B** | Upfront ගන්නවා වෙනුවට use එකට ගෙවනවා |
| 7 | **B** | Risk, portfolio → Governance |
| 8 | **B** | Lambda managed — code + IAM විතරයි ඔයාට |
| 9 | **A, D** | MFA + daily වැඩට IAM users / Identity Center |
| 10 | **A** | Findings ඔක්කොම එක තැනක → Security Hub |
| 11 | **B** | "Which user" → CloudTrail |
| 12 | **B** | Move වෙද්දි → In transit (TLS) |
| 13 | **A** | Free certificates → ACM |
| 14 | **B** | Accounts සීමා කරනවා → SCPs |
| 15 | **B** | App users → Cognito |
| 16 | **A** | Security checks + MFA on root → Trusted Advisor |
| 17 | **B** | AZs isolated — single point of failure share කරන්නේ නෑ |
| 18 | **B** | Full OS control → EC2 එකේ DB |
| 19 | **B** | Images → ECR |
| 20 | **B** | Single EC2 block → EBS |
| 21 | **A** | On-prem + cloud storage + cache → Storage Gateway |
| 22 | **A** | Central backup → AWS Backup |
| 23 | **A, B** | Read Replicas + cache. Multi-AZ = availability, performance නෙවෙයි |
| 24 | **A** | Emails → SES |
| 25 | **A** | Apps browser එකට stream → AppStream 2.0 |
| 26 | **A** | Serverless ETL → Glue |
| 27 | **B** | Family වෙනස් කරන්න පුළුවන් → Convertible RI |
| 28 | **C** | Mission-critical, < 5 min → Unified Operations |
| 29 | **A** | Patterns, guidance → Prescriptive Guidance |
| 30 | **B** | Consolidated billing නිසා share වෙනවා |

**ලකුණු:**
- **27–30** — නියමයි! Exam එක book කරන්න.
- **22–26** — හොඳයි. වැරදුණු domain එකේ episode එක ආයෙත් කියවන්න.
- **22ට අඩු** — කලබල වෙන්න එපා. "**හෙමින් සීරුවේ ගියොත් හිමාලයටත් යන්න පුළුවන්.**" තව සතියක් practice කරන්න.

---

## Closing

**කසුන්:** නදී, fail වුණොත්?

**නදී:** "**Fall seven times, stand up eight.**" ඒත් මේ plan එක follow කළා නම් ඔයා ලෑස්තියි. Pass වුණාම ඊළඟ AWS exam එකට **50% discount** එකක් ලැබෙනවා.

**කසුන්:** ඊළඟට Solutions Architect – Associate!

**නදී:** *(හිනාවෙලා)* ඒකටත් podcast එකක් හදමු. ඔයාට ජය — **Good luck, and keep building!**

**කසුන්:** ආයෙත් හමුවෙමු!
