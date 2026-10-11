# Extra Practice — Episode 6 (40 Questions)

## Questions

**Q1.** A company uses Amazon RDS for its database. Under the AWS shared responsibility model, which task is AWS's responsibility?
A. Creating and managing database user accounts and their permissions
B. Configuring security group rules that allow access to the DB instance
C. Patching the database engine and the underlying operating system
D. Deciding which data to store and whether to enable encryption

**Q2.** A security team wants to scan Amazon EC2 instances and container images for known software vulnerabilities and unintended network exposure. Which service should they use?
A. Amazon Inspector
B. Amazon GuardDuty
C. Amazon Macie
D. AWS Shield

**Q3.** A company wants to automatically discover and protect personally identifiable information (PII) stored in Amazon S3 buckets. Which service meets this requirement?
A. Amazon GuardDuty
B. AWS Config
C. Amazon Inspector
D. Amazon Macie

**Q4.** Which statement about AWS Shield is correct?
A. Shield Advanced is enabled automatically for all customers at no cost
B. Shield Standard is automatically included at no additional cost for all AWS customers
C. Shield protects web applications from SQL injection attacks
D. Shield encrypts data at rest in Amazon S3

**Q5.** A company hosts a website behind Amazon CloudFront and wants to block requests that contain SQL injection patterns and requests from specific IP address ranges. Which service should it use?
A. AWS WAF
B. AWS Shield Standard
C. Amazon GuardDuty
D. AWS Config

**Q6.** Which tasks are the customer's responsibility when using Amazon EC2? (Select TWO)
A. Configuring security group rules
B. Maintaining the physical network equipment
C. Patching the guest operating system
D. Replacing failed host servers in the data center
E. Maintaining the AWS global fiber network

**Q7.** A compliance team needs to see how the configuration of a security group changed over the last six months and to be alerted when it becomes non-compliant with company rules. Which service should they use?
A. AWS CloudTrail
B. Amazon CloudWatch
C. AWS Config
D. AWS Artifact

**Q8.** A finance team wants an email alert when the forecasted monthly AWS spend is expected to exceed a set amount. Which service should they use?
A. AWS Cost Explorer
B. AWS Budgets
C. AWS Pricing Calculator
D. AWS Trusted Advisor

**Q9.** A company needs the most detailed and comprehensive AWS cost and usage data, delivered to an Amazon S3 bucket for analysis with Amazon Athena. Which option provides this?
A. AWS Cost and Usage Report
B. AWS Pricing Calculator
C. AWS Budgets
D. AWS Support Center

**Q10.** Which AWS Support plan includes a designated Technical Account Manager (TAM)?
A. Basic Support
B. Enterprise Support
C. Developer Support
D. AWS Free Tier

**Q11.** A company runs a fault-tolerant, flexible batch-processing job that can be interrupted at any time. Which Amazon EC2 purchasing option is the MOST cost-effective?
A. On-Demand Instances
B. Dedicated Hosts
C. Standard Reserved Instances
D. Spot Instances

**Q12.** A company wants a discount in exchange for a 1-year or 3-year spend commitment that also applies to AWS Fargate and AWS Lambda usage. Which option should it choose?
A. EC2 Instance Savings Plans
B. Standard Reserved Instances
C. Compute Savings Plans
D. Spot Instances

**Q13.** A company must use existing server-bound software licenses (per-socket and per-core) on AWS and needs visibility into the physical server. Which option should it use?
A. Amazon EC2 Dedicated Hosts
B. Amazon EC2 Spot Instances
C. Amazon EC2 On-Demand Capacity Reservations
D. AWS Lambda

**Q14.** Which factors should a company consider when choosing an AWS Region for its workload? (Select TWO)
A. Latency to the end users
B. The number of IAM users allowed in the Region
C. Data residency and compliance requirements
D. The colour theme of the AWS Management Console
E. The Region name length

**Q15.** A company needs its application to keep running even if an entire AWS Region becomes unavailable. Which design satisfies this requirement?
A. Deploy across multiple Availability Zones in one Region
B. Deploy across multiple AWS Regions
C. Deploy in a single Availability Zone with larger instances
D. Use Amazon EBS snapshots in the same Availability Zone

**Q16.** A company stores secondary copies of data that can be easily re-created. The data is accessed infrequently but must be available within milliseconds. Which Amazon S3 storage class is the MOST cost-effective?
A. S3 Standard
B. S3 Glacier Deep Archive
C. S3 Standard-IA
D. S3 One Zone-IA

**Q17.** Multiple Linux EC2 instances in different Availability Zones need to read and write to the same shared file system. Which service should be used?
A. Amazon EBS
B. Amazon S3 Glacier
C. Amazon EFS
D. EC2 instance store

**Q18.** A data processing job runs continuously for 3 hours in a container, and the team does not want to manage servers. Which service is MOST suitable?
A. AWS Lambda
B. AWS Fargate
C. Amazon EC2 Dedicated Hosts
D. AWS Snowball Edge

**Q19.** A company already runs its applications on Kubernetes and wants a managed Kubernetes control plane on AWS. Which service should it use?
A. Amazon EKS
B. Amazon ECS
C. Amazon ECR
D. AWS Elastic Beanstalk

**Q20.** An application needs a NoSQL database that provides single-digit millisecond performance at any scale with no servers to manage. Which service should be used?
A. Amazon RDS
B. Amazon Redshift
C. Amazon ElastiCache
D. Amazon DynamoDB

**Q21.** A company wants a fully managed relational database that is compatible with MySQL and PostgreSQL and offers higher performance than standard MySQL. Which service should it choose?
A. Amazon DynamoDB
B. Amazon Redshift
C. Amazon Aurora
D. Amazon Neptune

**Q22.** A company has users around the world who download static website content. Which service reduces latency by caching content at edge locations?
A. Amazon ElastiCache
B. Amazon CloudFront
C. AWS Direct Connect
D. Amazon Route 53

**Q23.** A gaming company needs to improve the performance of a non-HTTP TCP/UDP application for global users by using static anycast IP addresses and the AWS global network. Which service should it use?
A. AWS Global Accelerator
B. Amazon CloudFront
C. Amazon Route 53
D. AWS Site-to-Site VPN

**Q24.** A company wants a subnet-level firewall that is stateless and supports both allow and deny rules. What should it use?
A. Security groups
B. AWS WAF
C. AWS Shield
D. Network ACLs

**Q25.** Which statements about security groups are true? (Select TWO)
A. They are stateful
B. They support explicit deny rules
C. They operate at the subnet boundary
D. They support allow rules only
E. Rules are processed in numbered order

**Q26.** Instances in a private subnet need to download software updates from the internet but must not accept inbound connections from the internet. What should the company use?
A. An internet gateway attached directly to the private subnet
B. A public IP on each instance
C. A NAT gateway
D. AWS Direct Connect

**Q27.** A company needs an encrypted connection between its on-premises network and its VPC that can be set up quickly over the public internet. Which option is MOST appropriate?
A. AWS Direct Connect
B. AWS Site-to-Site VPN
C. Amazon CloudFront
D. AWS Snowball Edge

**Q28.** An order event must be delivered to several different systems (email, inventory, billing) at the same time. Which service supports this publish/subscribe fan-out pattern?
A. Amazon SNS
B. Amazon SQS standard queue consumed by one worker
C. Amazon Kinesis Data Firehose only
D. AWS Step Functions only

**Q29.** A company wants to apply operating system patches and run commands across a fleet of EC2 instances and on-premises servers from one place. Which service should it use?
A. AWS CloudFormation
B. AWS Elastic Beanstalk
C. Amazon Inspector
D. AWS Systems Manager

**Q30.** A company wants machine-learning-based recommendations to choose the right EC2 instance size to reduce cost and improve performance. Which service should it use?
A. AWS Pricing Calculator
B. AWS Budgets
C. AWS Compute Optimizer
D. AWS Config

**Q31.** A company wants personalized notifications about AWS service events that may affect its own resources. Which service provides this?
A. AWS Trusted Advisor
B. AWS Health Dashboard
C. Amazon CloudWatch Logs
D. AWS Artifact

**Q32.** An application automatically adds EC2 instances when traffic increases and removes them when traffic drops, so the company pays only for what it needs. Which cloud benefit does this describe?
A. Elasticity
B. Fault tolerance
C. Global reach
D. Data durability

**Q33.** A company moves its on-premises servers to Amazon EC2 without making any changes to the applications. Which migration strategy is this?
A. Refactor
B. Repurchase
C. Retire
D. Rehost

**Q34.** A company needs to transfer data continuously and online from an on-premises NFS file server to Amazon S3 on a schedule. Which service is the BEST fit?
A. AWS Snowball Edge
B. AWS Direct Connect
C. AWS DataSync
D. Amazon Kinesis Data Streams

**Q35.** Which AWS services or features are provided at no additional charge? (Select TWO)
A. AWS Identity and Access Management (IAM)
B. AWS Organizations (consolidated billing)
C. Amazon RDS Multi-AZ deployments
D. AWS Direct Connect port hours
E. NAT gateways

**Q36.** What are benefits of consolidated billing in AWS Organizations? (Select TWO)
A. Automatic encryption of all member account data
B. A single bill for all member accounts
C. Free upgrade to Enterprise Support
D. Combined usage that can qualify for volume pricing discounts
E. Removal of the need for IAM permissions

**Q37.** A company wants to extract printed text, tables, and form fields from scanned documents automatically. Which service should it use?
A. Amazon Rekognition
B. Amazon Textract
C. Amazon Polly
D. Amazon Lex

**Q38.** A company wants to build a generative AI application using foundation models through an API without managing any infrastructure. Which service should it use?
A. Amazon Bedrock
B. Amazon SageMaker AI notebooks on self-managed EC2
C. Amazon Comprehend
D. Amazon Transcribe

**Q39.** Which actions follow IAM best practices for an application running on an EC2 instance that needs to read from Amazon S3? (Select TWO)
A. Attach an IAM role to the EC2 instance
B. Store long-term access keys in the application code
C. Grant only the minimum permissions required (least privilege)
D. Use the root user access keys
E. Share one IAM user across all applications

**Q40.** A company must meet a requirement for dedicated, single-tenant hardware security modules to generate and store its encryption keys. Which service should it use?
A. AWS Key Management Service (AWS KMS) with AWS managed keys
B. AWS Secrets Manager
C. AWS Certificate Manager
D. AWS CloudHSM

### Answers

- **Q1 — C.** RDS managed service එකක් නිසා DB engine සහ OS patching AWS ගේ වගකීම; DB users, security groups, data සහ encryption settings customer ගේ.
- **Q2 — A.** Software vulnerabilities සහ network exposure scan කරන්නේ Inspector; GuardDuty කරන්නේ threat detection.
- **Q3 — D.** S3 වල PII හොයාගන්නේ Macie (machine learning පාවිච්චි කරලා sensitive data discover කරනවා).
- **Q4 — B.** Shield Standard හැම customer කෙනෙක්ටම free සහ automatic; SQL injection block කරන්නේ WAF.
- **Q5 — A.** SQL injection patterns සහ IP ranges block කරන්නේ AWS WAF (CloudFront, ALB, API Gateway එක්ක).
- **Q6 — A, C.** Security groups සහ guest OS patching customer ගේ; physical network, hosts, fiber network AWS ගේ.
- **Q7 — C.** Configuration history සහ compliance rules → AWS Config; CloudTrail කියන්නේ "who made the API call".
- **Q8 — B.** Forecasted spend එකට alert දෙන්නේ AWS Budgets; Cost Explorer කරන්නේ past costs analyze කිරීම.
- **Q9 — A.** වඩාත්ම detailed cost data S3 එකට deliver කරන්නේ Cost and Usage Report (CUR).
- **Q10 — B.** Designated TAM ලැබෙන්නේ Enterprise Support plan එකේ.
- **Q11 — D.** Interrupt වෙන්න පුළුවන් fault-tolerant workloads වලට Spot Instances (90% දක්වා discount) ලාබම.
- **Q12 — C.** Compute Savings Plans EC2, Fargate, Lambda ඔක්කොටම apply වෙනවා; EC2 Instance Savings Plans EC2 විතරයි.
- **Q13 — A.** Per-socket/per-core server-bound licenses වලට Dedicated Hosts (physical server visibility එක්ක).
- **Q14 — A, C.** Region තෝරද්දි latency, compliance/data residency, pricing, service availability බලනවා.
- **Q15 — B.** Region failure එකකට survive වෙන්න multiple Regions (DR); multi-AZ එකෙන් HA විතරයි.
- **Q16 — D.** Re-create කරන්න පුළුවන්, අඩුවෙන් access කරන data → One Zone-IA (millisecond access, Standard-IA වලට වඩා ලාබයි).
- **Q17 — C.** AZs කිහිපයක Linux instances share කරන file system එකක් → EFS; EBS එක single instance එකකට.
- **Q18 — B.** පැය 3ක් run වෙන container job එකට Fargate; Lambda max විනාඩි 15 යි.
- **Q19 — A.** Managed Kubernetes → Amazon EKS; ECS කියන්නේ AWS ගේම container orchestrator එක.
- **Q20 — D.** Single-digit millisecond NoSQL, serverless → DynamoDB.
- **Q21 — C.** MySQL/PostgreSQL compatible, high performance managed relational DB → Aurora.
- **Q22 — B.** Edge locations වල static content cache කරනවා → CloudFront.
- **Q23 — A.** Static anycast IPs සහ TCP/UDP performance → Global Accelerator; CloudFront HTTP content caching සඳහා.
- **Q24 — D.** Subnet-level, stateless, allow සහ deny rules → Network ACLs.
- **Q25 — A, D.** Security groups stateful සහ allow rules විතරයි; NACL තමයි stateless සහ numbered rules.
- **Q26 — C.** Private subnet එකෙන් outbound විතරක් internet යන්න → NAT gateway.
- **Q27 — B.** Internet හරහා ඉක්මනින් encrypted connection එකක් → Site-to-Site VPN; Direct Connect private line එක setup කරන්න කාලය යනවා.
- **Q28 — A.** එකම message එක subscribers ගොඩකට යවන fan-out pattern → SNS.
- **Q29 — D.** Fleet එකට patching සහ commands run කරන්න Systems Manager (on-premises servers වලටත් වැඩ කරනවා).
- **Q30 — C.** ML අනුව right-sizing recommendations දෙන්නේ Compute Optimizer.
- **Q31 — B.** ඔයාගේ resources වලට බලපාන events වල personalized view එක → AWS Health Dashboard.
- **Q32 — A.** Demand එක්ක automatically scale out/in වීම → Elasticity.
- **Q33 — D.** Changes නැතිව servers move කිරීම → Rehost (lift and shift).
- **Q34 — C.** On-prem NFS සිට S3 වලට online, scheduled transfer → DataSync; Snowball offline physical device එකක්.
- **Q35 — A, B.** IAM සහ AWS Organizations (consolidated billing) free; ඒවා පාවිච්චි කරන resources වලට විතරයි ගෙවන්නේ.
- **Q36 — B, D.** Single bill එකයි combined usage නිසා volume discounts ලැබීමයි consolidated billing වල benefits.
- **Q37 — B.** Scanned documents වලින් text, tables, forms extract කරන්නේ Textract; Rekognition images/videos analyze කරනවා.
- **Q38 — A.** Foundation models API එකෙන්, infrastructure නැතිව → Amazon Bedrock.
- **Q39 — A, C.** EC2 එකට IAM role එකක් attach කරලා least privilege දෙන්න; access keys code එකට දාන්න එපා.
- **Q40 — D.** Dedicated single-tenant HSM hardware එකක් ඕන නම් CloudHSM; KMS multi-tenant managed service එකක්.
