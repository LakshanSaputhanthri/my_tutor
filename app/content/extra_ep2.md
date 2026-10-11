# Extra Practice — Episode 2 (40 Questions)

## Questions

**Q1.** A company runs its code on AWS Lambda. Which task remains the customer's responsibility?
A. Writing secure function code and assigning IAM permissions
B. Patching the underlying operating system
C. Maintaining the hypervisor
D. Securing the physical servers

**Q2.** Which of the following is part of "security OF the cloud"?
A. Configuring security groups
B. Encrypting objects in S3
C. Managing IAM user permissions
D. Protecting the AWS Regions, Availability Zones and edge locations

**Q3.** An S3 bucket containing customer data was accidentally made public. Who is responsible for this configuration?
A. AWS
B. The ISP
C. The customer
D. The AWS Marketplace seller

**Q4.** Which tasks are the customer's responsibility for Amazon EC2? (Select TWO)
A. Replacing failed physical hosts
B. Patching the guest operating system
C. Configuring security group rules
D. Maintaining the hypervisor
E. Destroying old storage devices

**Q5.** Which statement about AWS IAM is correct?
A. IAM is a global service and has no additional charge
B. IAM is a Regional service that costs per user
C. IAM can only be used from the AWS CLI
D. IAM is used only for S3

**Q6.** What is the recommended practice for the root user's access keys?
A. Create them and store them in source code
B. Share them with administrators
C. Rotate them weekly
D. Do not create root access keys at all

**Q7.** Which task requires the AWS account root user?
A. Creating an IAM group
B. Launching an EC2 instance
C. Closing the AWS account
D. Attaching a policy to a user

**Q8.** Which statement about IAM groups is true?
A. A group can contain other groups
B. A group can contain only users, not other groups
C. A group can contain only roles
D. A group can be used to log in to AWS

**Q9.** A company wants a partner's AWS account to access its S3 bucket temporarily without creating long-term credentials. What should it use?
A. Create an IAM role that the other account can assume
B. Share an IAM user password
C. Share root access keys
D. Make the bucket public

**Q10.** Which are best practices for protecting the root user? (Select TWO)
A. Enable MFA
B. Use it for daily administrative tasks
C. Create access keys for it
D. Lock away its credentials and use it only for tasks that need it
E. Share the password in a team chat

**Q11.** In what format are IAM policies written?
A. XML
B. CSV
C. JSON
D. YAML only

**Q12.** A company wants to prevent every account in its organization from using a specific AWS Region. Which feature should it use?
A. IAM groups
B. Service Control Policies (SCPs) in AWS Organizations
C. Amazon Cognito
D. AWS Shield

**Q13.** Which AWS Organizations feature combines usage across accounts to receive volume discounts and one bill?
A. Consolidated billing
B. Service Control Policies
C. AWS Artifact
D. AWS Config

**Q14.** Which service sets up a secure multi-account environment automatically using best practices?
A. AWS Trusted Advisor
B. Amazon Macie
C. AWS Shield
D. AWS Control Tower

**Q15.** A company wants employees to sign in to AWS with their existing corporate Active Directory credentials. Which concept does this describe?
A. Encryption at rest
B. Consolidated billing
C. Federation
D. Horizontal scaling

**Q16.** Which service gives workforce users single sign-on access to multiple AWS accounts and applications?
A. AWS Config
B. AWS IAM Identity Center
C. AWS KMS
D. Amazon Inspector

**Q17.** Which services help detect or assess security issues? (Select TWO)
A. Amazon GuardDuty
B. AWS Artifact
C. Amazon Inspector
D. AWS Marketplace
E. AWS Health Dashboard

**Q18.** Which benefit does AWS Shield Advanced provide over Shield Standard?
A. It is free for all customers
B. It scans S3 for PII
C. It rotates database passwords
D. 24/7 access to the Shield Response Team and enhanced DDoS protection

**Q19.** A company wants to block traffic from specific IP addresses at the application layer for its Application Load Balancer. Which service should it use?
A. AWS Shield Standard
B. AWS Config
C. AWS WAF
D. AWS CloudHSM

**Q20.** Which service lets an organization manage AWS WAF rules centrally across many accounts?
A. Amazon Detective
B. AWS Firewall Manager
C. AWS Artifact
D. Amazon Cognito

**Q21.** Which data sources does Amazon GuardDuty analyze to find threats?
A. CloudTrail events, VPC Flow Logs and DNS logs
B. Only S3 object contents
C. Only billing reports
D. Only IAM passwords

**Q22.** A security team wants to discover known software vulnerabilities such as CVEs on EC2 instances automatically. Which service?
A. Amazon GuardDuty
B. AWS WAF
C. AWS Artifact
D. Amazon Inspector

**Q23.** Which service uses machine learning to discover and protect sensitive data such as credit card numbers in S3?
A. AWS Shield
B. AWS KMS
C. Amazon Macie
D. AWS Config

**Q24.** Which service gives a single view of security alerts and compliance status from multiple AWS security services?
A. AWS Health Dashboard
B. AWS Security Hub
C. AWS Marketplace
D. AWS Artifact

**Q25.** After GuardDuty raises a finding, which service helps investigate the root cause by analyzing related activity?
A. Amazon Detective
B. AWS Shield
C. Amazon Cognito
D. AWS Secrets Manager

**Q26.** Which services help encrypt data at rest? (Select TWO)
A. AWS KMS
B. AWS CloudHSM
C. AWS Health Dashboard
D. Amazon Route 53
E. AWS Trusted Advisor

**Q27.** A company has a compliance need for single-tenant, dedicated hardware security modules to store its encryption keys. Which service?
A. AWS KMS
B. AWS Secrets Manager
C. AWS CloudHSM
D. AWS WAF

**Q28.** Which service provisions and renews SSL/TLS certificates for use with Elastic Load Balancing and CloudFront?
A. AWS Secrets Manager
B. AWS Certificate Manager (ACM)
C. AWS Config
D. Amazon Macie

**Q29.** An application stores API keys and needs them rotated automatically without code changes. Which service?
A. AWS Secrets Manager
B. AWS CloudTrail
C. Amazon Detective
D. AWS Artifact

**Q30.** A mobile app needs sign-up and sign-in for millions of end users, including social identity providers. Which service?
A. AWS IAM Identity Center
B. AWS Organizations
C. AWS Control Tower
D. Amazon Cognito

**Q31.** Which technology protects data while it moves between a user's browser and an AWS-hosted website?
A. EBS snapshots
B. Security Hub
C. TLS/SSL (HTTPS)
D. AWS Artifact

**Q32.** A security auditor needs to find out which user terminated an EC2 instance last week. Where should they look?
A. Amazon CloudWatch alarms
B. AWS CloudTrail event history
C. AWS Trusted Advisor
D. AWS Health Dashboard

**Q33.** Which Amazon CloudWatch capabilities help operate workloads? (Select TWO)
A. Collecting metrics and logs
B. Creating alarms on metrics
C. Downloading AWS compliance reports
D. Recording who called each API
E. Tracking resource configuration history

**Q34.** A company wants to evaluate resource configurations against rules and see the configuration history of a security group. Which service?
A. Amazon Cognito
B. AWS Shield
C. Amazon Inspector
D. AWS Config

**Q35.** An auditor asks for the AWS ISO 27001 certificate and SOC reports. Where can the customer get them on demand?
A. AWS Audit Manager
B. AWS Security Hub
C. AWS Artifact
D. AWS CloudTrail

**Q36.** Which service helps a company continuously collect evidence to simplify audits of its own AWS usage?
A. AWS Artifact
B. AWS Audit Manager
C. Amazon Detective
D. AWS Trusted Advisor

**Q37.** Which tool inspects an AWS account and recommends improvements in cost optimization, performance, security, fault tolerance and service limits?
A. AWS Trusted Advisor
B. AWS Config
C. Amazon GuardDuty
D. AWS Shield

**Q38.** Where can a customer see a personalized view of AWS service events that may affect its own resources?
A. AWS Artifact
B. AWS Marketplace
C. IAM credential report
D. AWS Health Dashboard

**Q39.** Which statements about compliance on AWS are true? (Select TWO)
A. AWS compliance certifications automatically make every customer application compliant
B. Customers remain responsible for making their own workloads compliant
C. Compliance requirements vary by country and industry
D. AWS handles all compliance for customer data
E. Compliance is irrelevant to the shared responsibility model

**Q40.** Where can a customer find guidance and best practices on AWS security, such as security bulletins and blogs?
A. AWS Cost Explorer
B. AWS Security Center, Security Blog and Knowledge Center
C. Amazon Route 53
D. AWS Snow Family

### Answers

- **Q1 — A.** Lambda managed නිසා OS AWS ගේ; **code** සහ **IAM permissions** customer ගේ.
- **Q2 — D.** Regions, AZs, edge locations = **security OF the cloud** (AWS).
- **Q3 — C.** S3 bucket **configuration** = customer, security IN the cloud.
- **Q4 — B, C.** Guest **OS patching** සහ **security groups** = customer; hardware, hypervisor = AWS.
- **Q5 — A.** IAM = **global** service, **free**.
- **Q6 — D.** Root user ට **access keys** හදන්න එපා.
- **Q7 — C.** Account එක **close** කිරීම = root user only.
- **Q8 — B.** Group එකක් ඇතුළේ group **බෑ**, users විතරයි.
- **Q9 — A.** වෙන account එකකට තාවකාලික access → **IAM role** (assume role).
- **Q10 — A, D.** **MFA** දාලා root එක දවස් පතා පාවිච්චි නොකරන්න.
- **Q11 — C.** IAM **policy** = **JSON** document.
- **Q12 — B.** Organization එකම සීමා කරන්න → **SCPs**.
- **Q13 — A.** **Consolidated billing** → එක bill එක + volume discounts.
- **Q14 — D.** Secure multi-account setup → **Control Tower**.
- **Q15 — C.** Corporate login එකෙන්ම AWS එකට → **Federation**.
- **Q16 — B.** Accounts ගොඩකට **single sign-on** → **IAM Identity Center**.
- **Q17 — A, C.** **GuardDuty** (threats) සහ **Inspector** (vulnerabilities) detect කරනවා.
- **Q18 — D.** **Shield Advanced** = paid + 24/7 **Shield Response Team**; Standard = free.
- **Q19 — C.** IP block, application layer → **AWS WAF**.
- **Q20 — B.** WAF rules accounts ගොඩකට → **Firewall Manager**.
- **Q21 — A.** GuardDuty = **CloudTrail**, **VPC Flow Logs**, **DNS logs** analyze කරනවා.
- **Q22 — D.** Software vulnerabilities (CVE) → **Inspector**.
- **Q23 — C.** Sensitive data / PII in S3 → **Macie**.
- **Q24 — B.** Findings ඔක්කොම එක තැනක → **Security Hub**.
- **Q25 — A.** Root cause investigate → **Detective**.
- **Q26 — A, B.** Encryption keys → **KMS** සහ **CloudHSM**.
- **Q27 — C.** Dedicated, single-tenant HSM → **CloudHSM**.
- **Q28 — B.** SSL/TLS certificates → **ACM**.
- **Q29 — A.** Secrets **auto-rotate** → **Secrets Manager**.
- **Q30 — D.** App users ගේ sign-up/sign-in → **Cognito**.
- **Q31 — C.** **In transit** encryption → **TLS/SSL** (HTTPS).
- **Q32 — B.** "Who" terminated → **CloudTrail** (API calls).
- **Q33 — A, B.** **CloudWatch** = metrics, logs, **alarms**.
- **Q34 — D.** Configuration history + compliance rules → **AWS Config**.
- **Q35 — C.** AWS ගේ compliance reports download → **Artifact**.
- **Q36 — B.** **ඔයාගේ** audit evidence එකතු කරන්න → **Audit Manager**.
- **Q37 — A.** Best-practice checks → **Trusted Advisor**.
- **Q38 — D.** ඔයාගේ resources වලට බලපාන events → **Health Dashboard**.
- **Q39 — B, C.** AWS certified වුණාට app එක customer ම compliant කරන්න ඕන; needs රට/industry අනුව වෙනස්.
- **Q40 — B.** Security tips → **Security Center, Security Blog, Knowledge Center**.
