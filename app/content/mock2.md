# Mock Exam 2 — 65 Questions (Full exam size)

Real exam එක වගේම: questions 65, විනාඩි 90. Domain split: Cloud Concepts 16 · Security 20 · Technology 22 · Billing 7.

## Questions

**Q1.** Which actions follow the "design for failure" principle? (Select TWO)
A. Deploy instances across multiple Availability Zones
B. Use one larger EC2 instance instead of several small ones
C. Put an Elastic Load Balancer in front of several instances
D. Turn on MFA for all IAM users
E. Run penetration tests every month

**Q2.** A startup wants to try a new idea quickly and shut it down cheaply if it fails. Which AWS Cloud benefit does this show?
A. Economies of scale
B. Agility
C. High availability
D. Fault tolerance

**Q3.** Which cost is part of running an on-premises data center but NOT a direct cost when using AWS?
A. Data transfer out to the internet
B. Physical server replacement
C. Amazon S3 storage
D. AWS Support plan fees

**Q4.** A company already owns Microsoft SQL Server licenses and wants to use them on AWS. Which licensing model is this?
A. License included
B. Bring Your Own License (BYOL)
C. Pay-as-you-go licensing
D. Free Tier licensing

**Q5.** Which Well-Architected pillar recommends selecting the right resource types and sizes for a workload?
A. Performance Efficiency
B. Security
C. Reliability
D. Sustainability

**Q6.** Which Well-Architected pillar includes the ability to protect data, systems, and assets?
A. Operational Excellence
B. Security
C. Cost Optimization
D. Performance Efficiency

**Q7.** Which statement BEST describes elasticity?
A. Running workloads in several Regions
B. Automatically adding and removing resources to match demand
C. Keeping a backup copy of data
D. Encrypting data at rest

**Q8.** A company decides to keep some applications on-premises because they will be retired in 2 years. Which migration strategy is this?
A. Rehost
B. Retain
C. Refactor
D. Repurchase

**Q9.** A company rewrites a monolithic application into microservices using AWS Lambda. Which migration strategy is this?
A. Rehost
B. Replatform
C. Refactor
D. Retire

**Q10.** Which are benefits of using automation in the AWS Cloud? (Select TWO)
A. Fewer human errors
B. Unlimited free compute
C. Faster, repeatable deployments
D. No need for security
E. No AWS bill

**Q11.** Which AWS Cloud Adoption Framework perspective helps make sure cloud investments support business goals?
A. Business
B. Platform
C. Operations
D. Security

**Q12.** Which AWS CAF perspective focuses on building and running cloud infrastructure, like architecture and engineering?
A. People
B. Governance
C. Platform
D. Business

**Q13.** Which resource can help a company understand the best practices for designing workloads on AWS?
A. AWS Well-Architected Framework
B. AWS Artifact
C. AWS Marketplace
D. Amazon Inspector

**Q14.** Which describes horizontal scaling?
A. Changing an instance from t3.small to t3.2xlarge
B. Adding more instances to share the load
C. Adding more memory to a database
D. Moving to a different Region

**Q15.** Why can AWS offer lower variable costs than a company running its own data center?
A. AWS uses only Spot Instances
B. AWS benefits from economies of scale
C. AWS does not charge for data transfer
D. AWS has no hardware costs

**Q16.** A company wants to reduce costs by matching instance size to actual usage. What is this called?
A. Rightsizing
B. Rehosting
C. Decoupling
D. Replatforming

**Q17.** Under the shared responsibility model, which is a responsibility of AWS for Amazon DynamoDB?
A. Managing access with IAM policies
B. Classifying the data stored in tables
C. Patching the underlying servers and software
D. Deciding who can read the data

**Q18.** Which responsibility changes between AWS and the customer depending on the service used?
A. Physical data center security
B. Operating system patching
C. Hardware disposal
D. Global network maintenance

**Q19.** What is the BEST way to give a group of developers the same permissions?
A. Attach the same policy to each user one by one
B. Create an IAM group, attach the policy, and add the users
C. Share one IAM user between all developers
D. Give them the root user password

**Q20.** A user from another AWS account needs temporary access to resources in your account. What should you use?
A. Share your access keys
B. A cross-account IAM role
C. The root user
D. A security group

**Q21.** Employees want to sign in to AWS using their existing company (Active Directory) credentials. What is this called?
A. Federation
B. Encryption
C. Replication
D. Rightsizing

**Q22.** Which IAM feature can force users to create strong passwords?
A. IAM password policy
B. Security groups
C. AWS Shield
D. S3 bucket policy

**Q23.** Which service can find S3 buckets and IAM roles that are shared with an external entity?
A. IAM Access Analyzer
B. AWS Shield
C. Amazon Polly
D. AWS Budgets

**Q24.** Which service provides a central place to manage AWS WAF rules across many accounts in AWS Organizations?
A. AWS Firewall Manager
B. AWS Config
C. Amazon Detective
D. AWS Artifact

**Q25.** A company needs DDoS protection with 24/7 access to the AWS Shield Response Team. Which should it use?
A. AWS Shield Standard
B. AWS Shield Advanced
C. AWS WAF only
D. Security groups

**Q26.** Which service helps investigate the root cause of a security finding by analyzing logs and showing relationships?
A. Amazon Detective
B. Amazon Inspector
C. AWS Artifact
D. Amazon Macie

**Q27.** A company must store encryption keys in single-tenant hardware that only it controls, to meet compliance rules. Which service?
A. AWS KMS
B. AWS CloudHSM
C. AWS Secrets Manager
D. AWS Certificate Manager

**Q28.** Which service checks resource configurations against rules, such as "all EBS volumes must be encrypted"?
A. AWS Config
B. Amazon CloudWatch
C. AWS CloudTrail
D. AWS Shield

**Q29.** Where should a company look for logs that show API activity in its AWS account?
A. AWS CloudTrail
B. Amazon Inspector
C. AWS Trusted Advisor
D. AWS Marketplace

**Q30.** Which are examples of encryption in transit? (Select TWO)
A. Using HTTPS for a website
B. Encrypting an EBS volume with KMS
C. Using TLS between an application and a database
D. Enabling S3 default encryption
E. Using S3 Glacier

**Q31.** A healthcare company needs to check whether AWS services can be used for HIPAA workloads. Where can it find this compliance information?
A. AWS Compliance programs and AWS Artifact
B. Amazon CloudWatch
C. AWS Cost Explorer
D. Amazon Route 53

**Q32.** Which service continuously collects evidence to help a company prepare for its own audits?
A. AWS Audit Manager
B. AWS Artifact
C. Amazon GuardDuty
D. AWS Health Dashboard

**Q33.** Which services help detect security issues in an AWS account? (Select TWO)
A. Amazon GuardDuty
B. Amazon Inspector
C. Amazon Polly
D. AWS Amplify
E. Amazon WorkSpaces

**Q34.** Where can a company find official AWS security best-practice articles and announcements?
A. AWS Security Blog and AWS Security Center
B. AWS Marketplace
C. Amazon Connect
D. AWS Pricing Calculator

**Q35.** Which service gives single sign-on access to multiple AWS accounts and business applications?
A. AWS IAM Identity Center
B. Amazon Cognito
C. AWS KMS
D. AWS WAF

**Q36.** A company wants to make sure no account in its organization can turn off AWS CloudTrail. What should it use?
A. A service control policy (SCP) in AWS Organizations
B. An S3 lifecycle policy
C. A security group
D. AWS Budgets

**Q37.** Which statement about Availability Zones is TRUE?
A. Each Availability Zone is a single data center shared by all Regions
B. Availability Zones in a Region are connected with low-latency links
C. An Availability Zone can be in two Regions
D. Availability Zones share the same power supply

**Q38.** A company must keep customer data inside one country because of local law. What should it do?
A. Choose an AWS Region in that country
B. Use more edge locations
C. Use Amazon CloudFront
D. Use AWS Global Accelerator

**Q39.** Which compute service is BEST for a simple website with a predictable monthly price for a beginner?
A. Amazon Lightsail
B. Amazon EKS
C. AWS Batch
D. Amazon EMR

**Q40.** Which service runs large numbers of batch computing jobs without managing the scheduling software?
A. AWS Batch
B. Amazon Lightsail
C. Amazon Route 53
D. AWS Amplify

**Q41.** Which EC2 instance family is BEST for a workload that needs high, sequential read and write access to large datasets on local storage?
A. Storage optimized
B. Compute optimized
C. Memory optimized
D. General purpose

**Q42.** Which load balancer is BEST for routing HTTP requests based on the URL path?
A. Application Load Balancer
B. Network Load Balancer
C. Gateway Load Balancer
D. Amazon Route 53

**Q43.** How can a company back up an Amazon EBS volume?
A. Create an EBS snapshot
B. Use an S3 lifecycle policy
C. Use Amazon CloudFront
D. Use AWS Shield

**Q44.** Which storage service provides a fully managed Windows file system?
A. Amazon FSx for Windows File Server
B. Amazon EFS
C. Amazon EBS
D. Amazon S3 Glacier

**Q45.** Which S3 storage class stores data in only one Availability Zone at a lower cost?
A. S3 One Zone-Infrequent Access
B. S3 Standard
C. S3 Intelligent-Tiering
D. S3 Glacier Deep Archive

**Q46.** A company needs archived data back within milliseconds, but it accesses the data only once a quarter. Which S3 class is BEST?
A. S3 Glacier Instant Retrieval
B. S3 Glacier Deep Archive
C. S3 Glacier Flexible Retrieval
D. S3 Standard

**Q47.** Which database service is compatible with MySQL and PostgreSQL and built by AWS for high performance?
A. Amazon Aurora
B. Amazon DynamoDB
C. Amazon Neptune
D. Amazon Redshift

**Q48.** Which service reduces database load by keeping frequently read data in memory?
A. Amazon ElastiCache
B. Amazon S3
C. AWS Backup
D. Amazon EBS

**Q49.** A company stores social network data showing how users are connected. Which database is BEST?
A. Amazon Neptune
B. Amazon RDS for MySQL
C. Amazon Redshift
D. Amazon Timestream

**Q50.** Which VPC component is a stateless firewall at the subnet level?
A. Network ACL
B. Security group
C. Internet gateway
D. Route table

**Q51.** Which service connects many VPCs and on-premises networks through a central hub?
A. AWS Transit Gateway
B. VPC peering
C. Amazon CloudFront
D. AWS Client VPN

**Q52.** Which Route 53 feature can send users to a healthy backup site if the main site fails?
A. Failover routing with health checks
B. S3 lifecycle rules
C. AWS Shield Advanced
D. Security groups

**Q53.** Which service improves global application performance by routing traffic over the AWS network using static IP addresses?
A. AWS Global Accelerator
B. Amazon CloudFront
C. Amazon Route 53
D. AWS Direct Connect

**Q54.** A company wants to send a message to many subscribers (email, SMS, and SQS queues) at the same time. Which service?
A. Amazon SNS
B. Amazon SQS
C. Amazon SES
D. AWS Step Functions

**Q55.** Which service can trigger a Lambda function every day at 6 AM?
A. Amazon EventBridge
B. Amazon SQS
C. Amazon Route 53
D. AWS Glue

**Q56.** Which service detects the sentiment (positive or negative) of customer reviews?
A. Amazon Comprehend
B. Amazon Rekognition
C. Amazon Polly
D. Amazon Translate

**Q57.** A company wants to build a data lake and run SQL queries on S3 data without managing servers. Which services should it use? (Select TWO)
A. AWS Glue
B. Amazon Athena
C. Amazon EC2
D. Amazon EBS
E. AWS Direct Connect

**Q58.** Which service gives employees secure, persistent virtual Windows or Linux desktops in the cloud?
A. Amazon WorkSpaces
B. Amazon AppStream 2.0
C. AWS Amplify
D. Amazon Lightsail

**Q59.** A company has a steady workload but wants a discount that also applies to AWS Fargate and AWS Lambda. Which option?
A. Compute Savings Plans
B. Standard Reserved Instances
C. Spot Instances
D. Dedicated Hosts

**Q60.** How are Reserved Instance discounts handled in AWS Organizations with consolidated billing?
A. They can apply to matching usage in other accounts of the organization
B. They apply only to the management account
C. They are lost when accounts are combined
D. They apply only to Spot Instances

**Q61.** Which data transfer usually costs the MOST?
A. Data transfer into AWS from the internet
B. Data transfer out from AWS to the internet
C. Data transfer within the same Availability Zone using private IPs
D. Uploading data to Amazon S3

**Q62.** Which tool can show a company how much it spent last month on each service and forecast next month's costs?
A. AWS Cost Explorer
B. AWS Pricing Calculator
C. AWS Artifact
D. AWS CloudTrail

**Q63.** A company wants to tag resources by department and see each department's costs in billing reports. What must it do?
A. Activate cost allocation tags
B. Create a new AWS account for each user
C. Use AWS Shield
D. Enable S3 versioning

**Q64.** Which are benefits of joining the AWS Partner Network (APN)? (Select TWO)
A. Partner training and certification
B. Free EC2 instances forever
C. Access to partner events and programs
D. Automatic Enterprise Support
E. No need for AWS accounts

**Q65.** Which AWS resource gives personalized information about AWS events that affect your account's resources?
A. AWS Health Dashboard
B. AWS Marketplace
C. AWS re:Post
D. AWS Pricing Calculator

### Answers

- **Q1 — A, C.** Multiple AZs + Load Balancer = එකක් කැඩුණත් අනික වැඩ. MFA, pen testing = security.
- **Q2 — B.** ඉක්මනින්, ලාභෙට try කරනවා → **Agility**.
- **Q3 — B.** Hardware replace කිරීම AWS කරනවා. අනෙක් ඒවා AWS bill එකේ එනවා.
- **Q4 — B.** තියෙන license එක ගෙනියනවා → **BYOL**.
- **Q5 — A.** හරි type, හරි size → **Performance Efficiency**.
- **Q6 — B.** Protect → **Security**.
- **Q7 — B.** Demand අනුව ඉබේම වැඩි/අඩු → **Elasticity**.
- **Q8 — B.** දැනට තියාගන්නවා → **Retain**.
- **Q9 — C.** අලුතෙන් ලියනවා (serverless) → **Refactor**.
- **Q10 — A, C.** Automation = වැරදි අඩුයි + වේගවත්, නැවත නැවත කරන්න පුළුවන්.
- **Q11 — A.** Business goals → **Business** perspective.
- **Q12 — C.** Infrastructure, architecture → **Platform**.
- **Q13 — A.** Best practices → **Well-Architected Framework**.
- **Q14 — B.** Instances ගණන වැඩි කිරීම → horizontal (scale out).
- **Q15 — B.** Customers ගොඩක් → **economies of scale**.
- **Q16 — A.** Usage එකට ගැලපෙන size → **Rightsizing**.
- **Q17 — C.** DynamoDB managed → servers patch කරන්නේ **AWS**. Data, access = customer.
- **Q18 — B.** EC2 නම් customer, RDS/Lambda නම් AWS → **OS patching**.
- **Q19 — B.** **IAM group** එකකට policy දාලා users එකතු කරන්න.
- **Q20 — B.** වෙන account එකකට temporary access → **cross-account role**.
- **Q21 — A.** Company login එකෙන් AWS → **Federation**.
- **Q22 — A.** Strong passwords → **password policy**.
- **Q23 — A.** External share හොයනවා → **IAM Access Analyzer**.
- **Q24 — A.** WAF rules accounts ගොඩකට → **Firewall Manager**.
- **Q25 — B.** 24/7 Shield Response Team → **Shield Advanced**.
- **Q26 — A.** Root cause investigate → **Detective**.
- **Q27 — B.** Single-tenant hardware keys → **CloudHSM**.
- **Q28 — A.** Configuration rules → **Config**.
- **Q29 — A.** API activity logs → **CloudTrail**.
- **Q30 — A, C.** Network එකේ යනකොට → **HTTPS, TLS**. EBS/S3 encryption = at rest.
- **Q31 — A.** Compliance info → **AWS Compliance programs + Artifact**.
- **Q32 — A.** ඔයාගේ audit evidence → **Audit Manager**.
- **Q33 — A, B.** GuardDuty (threats) + Inspector (vulnerabilities).
- **Q34 — A.** **Security Blog + Security Center**.
- **Q35 — A.** Accounts ගොඩකට SSO → **IAM Identity Center**.
- **Q36 — A.** Accounts වලට සීමා දානවා → **SCP**.
- **Q37 — B.** AZs **low-latency links** වලින් connect. Power share කරන්නේ නෑ.
- **Q38 — A.** Data රට ඇතුළේ → ඒ රටේ **Region** එක.
- **Q39 — A.** සරල, fixed price → **Lightsail**.
- **Q40 — A.** Batch jobs → **AWS Batch**.
- **Q41 — A.** Local storage read/write → **Storage optimized**.
- **Q42 — A.** HTTP + URL path → **ALB**.
- **Q43 — A.** EBS backup → **snapshot**.
- **Q44 — A.** Windows file system → **FSx for Windows**.
- **Q45 — A.** එක AZ, ලාභ → **One Zone-IA**.
- **Q46 — A.** Archive + milliseconds → **Glacier Instant Retrieval**.
- **Q47 — A.** MySQL/PostgreSQL compatible, AWS හදපු → **Aurora**.
- **Q48 — A.** Memory cache → **ElastiCache**.
- **Q49 — A.** Connections / relationships → graph → **Neptune**.
- **Q50 — A.** Subnet + stateless → **Network ACL**.
- **Q51 — A.** Central hub → **Transit Gateway**.
- **Q52 — A.** Backup site එකට යවනවා → **failover routing + health checks**.
- **Q53 — A.** Static IPs + AWS network → **Global Accelerator**.
- **Q54 — A.** එකපාර හැමෝටම → **SNS**.
- **Q55 — A.** Schedule → **EventBridge**.
- **Q56 — A.** Sentiment → **Comprehend**.
- **Q57 — A, B.** Glue (catalog, ETL) + Athena (SQL on S3).
- **Q58 — A.** Virtual desktops → **WorkSpaces**. (AppStream = apps විතරයි)
- **Q59 — A.** Lambda + Fargate ත් → **Compute Savings Plans**.
- **Q60 — A.** Organization එකේ accounts අතර **share** වෙනවා.
- **Q61 — B.** Internet එකට **එළියට** යන එක ගෙවන්න ඕන. ඇතුළට free.
- **Q62 — A.** පහුගිය වියදම + forecast → **Cost Explorer**.
- **Q63 — A.** Department අනුව cost → **cost allocation tags** activate කරන්න.
- **Q64 — A, C.** Partner training/certification + events.
- **Q65 — A.** ඔයාගේ resources වලට බලපාන events → **Health Dashboard**.
