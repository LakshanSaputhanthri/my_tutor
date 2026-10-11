# Extra Practice — Episode 5 (40 Questions)

## Questions

**Q1.** Which option lists the three main categories that make up most AWS charges for a typical workload?
A. Compute, storage, and data transfer out
B. Compute, IAM users, and inbound data transfer
C. Storage, support tickets, and Region selection
D. Networking, monitoring, and encryption only

**Q2.** A company uploads 5 TB of data from its office into Amazon S3 over the internet. How is the data transfer into AWS charged?
A. It is charged at the same rate as outbound transfer
B. It is usually free
C. It is charged per Availability Zone
D. It is charged only if the bucket is encrypted

**Q3.** A company replicates data from the us-east-1 Region to the eu-west-1 Region. What is true about the cost?
A. Inter-Region data transfer is charged
B. Inter-Region data transfer is always free
C. Only the receiving Region charges for it
D. It is free if the data is encrypted

**Q4.** Which statement describes the AWS Free Tier "Always Free" offer?
A. It is available only for the first 12 months after sign-up
B. It never expires and applies to certain services, such as a monthly number of AWS Lambda requests
C. It is a short trial that ends after a fixed number of days
D. It gives unlimited usage of every AWS service

**Q5.** Which statements describe the AWS pricing philosophy? (Select TWO)
A. Customers pay for what they use (pay-as-you-go)
B. Customers must sign a 3-year contract before using any service
C. Customers can save money by committing to a usage level
D. Prices per unit always increase as usage grows
E. Customers pay a fixed license fee for each AWS service

**Q6.** As a company's storage usage grows very large, the price per GB for Amazon S3 becomes lower. What is this pricing benefit called?
A. Volume discounts
B. Spot pricing
C. Cost allocation
D. Consolidated alerts

**Q7.** A company wants the maximum discount on a Reserved Instance and is willing to pay the entire amount at the start of the term. Which payment option fits?
A. No Upfront
B. Partial Upfront
C. All Upfront
D. Pay-per-second

**Q8.** A company buys Reserved Instances but may need to change the instance family during the 3-year term. Which type should it choose?
A. Standard Reserved Instances
B. Convertible Reserved Instances
C. Spot Instances
D. Dedicated Hosts

**Q9.** Which statement about Standard Reserved Instances compared with Convertible Reserved Instances is correct?
A. Standard offers a higher discount but less flexibility
B. Standard offers a lower discount but more flexibility
C. Standard has no commitment term
D. Standard can only be used for Lambda functions

**Q10.** A company wants a flexible commitment that automatically applies to EC2 in any Region, any instance family, and also to AWS Fargate and AWS Lambda. Which option fits?
A. EC2 Instance Savings Plans
B. Standard Reserved Instances
C. Compute Savings Plans
D. Spot Instances

**Q11.** What happens to a Spot Instance when AWS needs the capacity back?
A. It is interrupted, with a two-minute warning
B. It is converted to an On-Demand Instance for free
C. It keeps running until the customer stops it
D. It is moved to a Dedicated Host

**Q12.** Which workloads are good candidates for Spot Instances? (Select TWO)
A. A production relational database with strict uptime needs
B. Fault-tolerant big data processing jobs
C. Stateless web workers that can be replaced quickly
D. A single server that holds the only copy of customer data
E. A license server that must never stop

**Q13.** A company needs an EC2 instance on hardware that is not shared with other AWS accounts, but it does not need visibility into physical sockets and cores. Which option is the best fit?
A. Spot Instances
B. Dedicated Instances
C. Savings Plans
D. Standard Reserved Instances

**Q14.** A company wants to reserve EC2 capacity in a specific Availability Zone for a product launch next week, with no 1-year or 3-year commitment. Which option should it use?
A. Standard Reserved Instances
B. Compute Savings Plans
C. Spot Instances
D. On-Demand Capacity Reservations

**Q15.** A startup is testing a new application for a few weeks. The workload is unpredictable and cannot be interrupted. Which EC2 pricing option is the best fit?
A. Spot Instances
B. On-Demand Instances
C. 3-year Reserved Instances
D. Dedicated Hosts

**Q16.** A company wants to use its existing per-socket and per-core software licenses on AWS. Which option helps it with this requirement?
A. Spot Instances
B. On-Demand Instances
C. Capacity Reservations
D. Dedicated Hosts

**Q17.** A company runs its database 24/7, handles seasonal spikes, and runs nightly reports. Which combination is the MOST cost-effective?
A. Spot for the database, Reserved for the spikes, On-Demand for reports
B. Reserved for the database, On-Demand with Auto Scaling for spikes, Spot for reports
C. On-Demand for everything
D. Dedicated Hosts for everything

**Q18.** A solutions architect wants to estimate the monthly cost of a planned architecture with EC2, EBS, and S3 before deploying anything. Which tool should be used?
A. AWS Cost Explorer
B. AWS Budgets
C. AWS Pricing Calculator
D. AWS Trusted Advisor

**Q19.** Which tasks can be done with AWS Cost Explorer? (Select TWO)
A. View and analyze past costs and usage
B. Forecast future spending based on historical data
C. Estimate the cost of a new architecture that does not exist yet
D. Block users from launching resources
E. Report on abuse of AWS resources

**Q20.** A finance team wants to be notified by email when actual spending reaches 80% of a monthly limit. Which feature should they configure?
A. AWS Budgets alerts
B. Amazon Inspector findings
C. AWS Artifact reports
D. AWS Config rules

**Q21.** A company wants AWS Budgets to automatically apply restrictive actions, such as attaching a policy, when a budget threshold is exceeded. Which AWS Budgets feature supports this?
A. Budgets actions
B. Cost Explorer forecasts
C. Cost allocation tags
D. Support API

**Q22.** A data analyst wants the most comprehensive, line-item cost and usage data delivered to Amazon S3 so it can be queried with Amazon Athena. Which should be used?
A. AWS Budgets
B. AWS Cost and Usage Report (CUR)
C. AWS Pricing Calculator
D. AWS Health Dashboard

**Q23.** A company wants machine learning to detect unusual spending patterns and send an alert. Which service should it use?
A. AWS Cost Anomaly Detection
B. AWS Pricing Calculator
C. Amazon GuardDuty
D. AWS CloudTrail

**Q24.** A company added a "Project" tag to its EC2 instances but cannot see the tag in billing reports. What must it do?
A. Create a new IAM role for billing
B. Activate the tag as a cost allocation tag in the Billing and Cost Management console
C. Move the instances to another Region
D. Enable AWS Shield Advanced

**Q25.** Which statement about AWS Organizations consolidated billing is correct?
A. It costs extra per linked account
B. It provides one bill for all accounts in the organization at no additional charge
C. It prevents sharing of Reserved Instance discounts
D. It works only for a single AWS account

**Q26.** Which benefits does consolidated billing provide for accounts in an organization? (Select TWO)
A. Combined usage can reach higher volume-discount tiers
B. Reserved Instance and Savings Plans discounts can be shared across accounts
C. All accounts automatically receive Enterprise Support
D. All data is encrypted by default
E. Data transfer between all accounts becomes free

**Q27.** Which AWS Support plan is available to ALL customers at no additional cost?
A. Business Support+
B. Enterprise Support
C. Basic Support
D. Unified Operations

**Q28.** Which resources are included with Basic Support? (Select TWO)
A. AWS re:Post community access and documentation
B. A designated Technical Account Manager
C. Access to the core Trusted Advisor checks and AWS Health
D. 24/7 phone support from cloud support engineers
E. A billing concierge

**Q29.** A company runs production workloads and wants 24/7 access to cloud support engineers and the full set of Trusted Advisor checks at the lowest cost. Which plan should it choose?
A. Basic Support
B. Business Support+
C. Enterprise Support
D. Unified Operations

**Q30.** Which support plan offers the fastest response time, under 5 minutes, for critical incidents on mission-critical workloads?
A. Business Support+
B. Enterprise Support
C. Unified Operations
D. Basic Support

**Q31.** A company running business-critical workloads wants proactive guidance from a designated Technical Account Manager (TAM) and a 15-minute response for critical issues. Which plan should it choose?
A. Basic Support
B. Business Support+
C. Enterprise Support
D. AWS re:Post

**Q32.** A developer searches for answers to common AWS questions that are frequently asked by customers, written as articles by AWS support. Where should the developer look?
A. AWS Knowledge Center
B. AWS Marketplace
C. AWS Artifact
D. AWS Organizations

**Q33.** Which resources help a company plan a migration to AWS? (Select TWO)
A. AWS Prescriptive Guidance
B. AWS Professional Services
C. AWS Trust & Safety
D. AWS Cost and Usage Report
E. AWS Budgets

**Q34.** A company needs a third-party firewall appliance and wants it to be billed on its regular AWS invoice. Where should it find and purchase it?
A. AWS Marketplace
B. AWS Artifact
C. AWS re:Post
D. AWS Support Center

**Q35.** A company wants to find a consulting partner or an independent software vendor that has experience with AWS. What should it use?
A. AWS Trusted Advisor
B. AWS Partner Network (APN)
C. AWS Health Dashboard
D. AWS Budgets

**Q36.** A company wants to know when AWS service events, such as a Regional outage or scheduled maintenance, affect its resources. Which service shows personalized information about AWS service events that impact the company's account?
A. AWS Cost Explorer
B. AWS Artifact
C. Amazon Macie
D. AWS Health Dashboard

**Q37.** Which Trusted Advisor category checks for idle or underutilized resources to help reduce spending?
A. Fault tolerance
B. Cost optimization
C. Performance
D. Operational excellence only

**Q38.** Which are Trusted Advisor check categories? (Select TWO)
A. Security
B. Service limits
C. Machine learning accuracy
D. Software licensing
E. Network latency billing

**Q39.** An employee needs to open a technical support case with AWS for an impaired production service. Where is the case created?
A. AWS Marketplace
B. AWS Artifact
C. AWS Support Center
D. AWS Prescriptive Guidance

**Q40.** A team forgot to stop a large GPU instance and was surprised by the bill. Which combination would have best helped detect this early?
A. Buy a 3-year Reserved Instance and enable AWS Shield
B. Move to Dedicated Hosts and enable Amazon Inspector
C. Enable AWS Artifact and use Amazon Macie
D. Create an AWS Budgets alert and enable Cost Anomaly Detection

### Answers

- **Q1 — A.** Compute, storage, සහ data transfer OUT තමයි ප්‍රධාන charges තුන.
- **Q2 — B.** Internet එකෙන් AWS ඇතුළට එන data (inbound) සාමාන්‍යයෙන් **free**.
- **Q3 — A.** Region දෙකක් අතර data transfer එකට ගෙවන්න වෙනවා.
- **Q4 — B.** **Always Free** offers කවදාවත් expire වෙන්නේ නෑ (උදා: Lambda requests).
- **Q5 — A, C.** Pay-as-you-go සහ commit කළොත් save කරන්න පුළුවන් — මේවා AWS pricing philosophy එක.
- **Q6 — A.** වැඩිපුර පාවිච්චි කළාම unit මිල අඩු වෙන එක **volume discounts**.
- **Q7 — C.** **All Upfront** ගෙව්වොත් Reserved Instance එකේ වැඩිම discount එක ලැබෙනවා.
- **Q8 — B.** Instance family වෙනස් කරන්න පුළුවන් **Convertible RI** වලින්.
- **Q9 — A.** **Standard RI** වලට වැඩි discount එකක් ඒත් flexibility අඩුයි.
- **Q10 — C.** Region/family/OS ඕනම එකකට සහ Fargate, Lambda වලටත් → **Compute Savings Plans**.
- **Q11 — A.** Spot instance එක AWS ට capacity ඕන වුණාම **විනාඩි 2ක warning** එකකින් interrupt කරනවා.
- **Q12 — B, C.** Fault-tolerant, stateless, replace කරන්න පුළුවන් workloads **Spot** වලට හොඳයි.
- **Q13 — B.** Hardware share නොකර ඒත් socket/core visibility ඕන නැත්නම් **Dedicated Instances**.
- **Q14 — D.** Specific AZ එකේ capacity, long-term commitment නැතුව → **On-Demand Capacity Reservations**.
- **Q15 — B.** Short-term, unpredictable, interrupt කරන්න බෑ → **On-Demand**.
- **Q16 — D.** Per-socket/per-core licenses (BYOL) → **Dedicated Hosts**.
- **Q17 — B.** Database → Reserved, spikes → On-Demand + Auto Scaling, reports → Spot කියන mix එක හොඳම.
- **Q18 — C.** Build කරන්න **කලින්** estimate කරන්නේ **Pricing Calculator** එකෙන්.
- **Q19 — A, B.** **Cost Explorer** එකෙන් අතීත වියදම් බලලා future forecast කරන්න පුළුවන්.
- **Q20 — A.** Spending threshold (80%) එකක alert → **AWS Budgets**.
- **Q21 — A.** Threshold පැනපු ගමන් automatic actions apply කරන්නේ **Budgets actions** වලින්.
- **Q22 — B.** Line-item විස්තරාත්මක data S3 එකට → **Cost and Usage Report (CUR)**.
- **Q23 — A.** ML වලින් අමුතු වියදම් හොයන්නේ **Cost Anomaly Detection**.
- **Q24 — B.** Tag එක billing reports වල පේන්න **cost allocation tag** එකක් විදිහට activate කරන්න ඕන.
- **Q25 — B.** Consolidated billing එකෙන් එක bill එකක් ලැබෙනවා, **අමතර ගාස්තුවක් නෑ**.
- **Q26 — A, B.** Usage එකතු වෙලා volume discounts, RI/Savings Plans discounts accounts අතර share වෙනවා.
- **Q27 — C.** **Basic Support** හැමෝටම free.
- **Q28 — A, C.** Basic එකේ re:Post, documentation, core Trusted Advisor checks සහ AWS Health තියෙනවා.
- **Q29 — B.** Production + 24/7 + full Trusted Advisor අඩුම මිලට → **Business Support+**.
- **Q30 — C.** විනාඩි 5ට අඩු response (mission-critical) → **Unified Operations**.
- **Q31 — C.** Designated **TAM** සහ විනාඩි 15 response → **Enterprise Support**.
- **Q32 — A.** නිතර අහන ප්‍රශ්න වල articles → **AWS Knowledge Center**.
- **Q33 — A, B.** Migration patterns/strategies සඳහා **Prescriptive Guidance** සහ **Professional Services**.
- **Q34 — A.** Third-party software AWS bill එකෙන් ගෙවන්න → **AWS Marketplace**.
- **Q35 — B.** Consulting / ISV partners හොයන්න → **AWS Partner Network**.
- **Q36 — D.** ඔයාගේ account එකට බලපාන service events → **AWS Health Dashboard**.
- **Q37 — B.** Idle/underutilized resources check කරන්නේ **Cost optimization** category එකෙන්.
- **Q38 — A, B.** Trusted Advisor categories වල **Security** සහ **Service limits** ඇතුළත්.
- **Q39 — C.** Support case open කරන්නේ **AWS Support Center** එකෙන්.
- **Q40 — D.** **Budgets alert** + **Cost Anomaly Detection** දෙකෙන් unexpected cost එක ඉක්මනින් අල්ලගන්න පුළුවන්.
