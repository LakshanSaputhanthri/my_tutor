# Cheat Sheet — Exam Night

**Exam එකට කලින් රෑ මේ page එක විතරක් කියවන්න.**

## Exam එක

| Item | Detail |
| --- | --- |
| Questions | 65 (scored 50 + unscored 15) |
| Time | 90 minutes (+30 with ESL) |
| Pass | 700 / 1000 |
| Wrong answers | No penalty — හැම එකටම answer කරන්න |
| Fee | USD 100 |
| Valid | 3 years · pass වුණාම ඊළඟ exam එකට 50% discount |

| Domain | Weight |
| --- | --- |
| 1. Cloud Concepts | 24% |
| 2. Security and Compliance | 30% |
| 3. Cloud Technology and Services | 34% |
| 4. Billing, Pricing, and Support | 12% |

## Lists — කටපාඩම්

> **Six advantages:** variable expense · economies of scale · stop guessing capacity · speed and agility · no data centers · go global in minutes
>
> **Well-Architected pillars 6:** Operational Excellence · Security · Reliability · Performance Efficiency · Cost Optimization · Sustainability
>
> **CAF perspectives 6:** Business · People · Governance ("බත් පොල් ගෙඩි") · Platform · Security · Operations ("පාන් සීනි ඔලු")
>
> **7 Rs:** Retire · Retain · Rehost · Relocate · Replatform · Repurchase · Refactor

## Commonly confused services

| Pair | First one when… | Second one when… |
| --- | --- | --- |
| CloudTrail vs CloudWatch | "Who made this API call?" | "CPU is high, send an alarm" |
| CloudTrail vs Config | Record of **actions** | Record of **configuration** + compliance rules |
| Trusted Advisor vs Inspector | Account best-practice checks | Software **vulnerabilities** |
| GuardDuty vs Inspector | **Threats** (CCTV) | **Vulnerabilities** (lock check) |
| GuardDuty vs Macie | Threat detection | **PII** in S3 |
| Shield vs WAF | **DDoS** | SQL injection, XSS |
| KMS vs CloudHSM | Managed keys | Dedicated key hardware |
| Secrets Manager vs Parameter Store | Auto **rotation** | Simple config values |
| Security Group vs NACL | Instance, stateful, allow only | Subnet, stateless, allow + deny |
| EBS vs EFS vs S3 | Disk for one EC2 | Shared Linux files / object storage |
| RDS vs DynamoDB | SQL, joins | NoSQL, huge scale |
| Multi-AZ vs Read Replica | **Availability** (spare tyre) | **Read performance** (more cashiers) |
| Redshift vs Athena | Data warehouse | SQL directly on S3 |
| SQS vs SNS | Queue — pull | Notifications — push |
| CloudFront vs Global Accelerator | Cache content at edge | Faster network path, static IPs, no cache |
| Direct Connect vs VPN | Private line, no internet | Encrypted tunnel over internet |
| CloudFormation vs Elastic Beanstalk | Any infrastructure as code | Just deploy my web app |
| Pricing Calculator vs Cost Explorer | Estimate **before** building | Analyze **past** spend |
| Budgets vs Cost Anomaly Detection | Alert on your limit | ML finds unusual spend |
| Reserved Instances vs Savings Plans | Specific instance commitment | $/hour commitment, more flexible |
| Polly vs Transcribe | Text → speech (parrot) | Speech → text (writer) |
| SageMaker AI vs Bedrock | Build your own ML models | Use ready GenAI foundation models |
| Organizations vs Control Tower | Accounts, SCPs, one bill | Automated secure multi-account setup |
| Artifact vs Audit Manager | AWS's compliance reports | Evidence for **your** audits |
| Cognito vs IAM Identity Center | App users sign-in | Employees, many AWS accounts |
| Snowball vs DataSync | Offline device, huge data | Online transfer |

## Shared Responsibility

| AWS (OF the cloud) | Customer (IN the cloud) |
| --- | --- |
| Data centers, hardware, network | Data, encryption choices |
| Hypervisor | IAM users and permissions |
| RDS / Lambda OS patching | **EC2 OS patching** |
| Hardware disposal | Security groups, NACLs |

## EC2 pricing

| Keyword | Option |
| --- | --- |
| Short-term, unpredictable, can't interrupt | On-Demand |
| Steady, 1 or 3 years | Reserved Instances / Savings Plans |
| Can be interrupted, cheapest | Spot (up to 90%) |
| Server-bound licenses | Dedicated Hosts |
| Capacity in one AZ, no commitment | Capacity Reservations |

## Support plans (2026)

| Plan | Key point |
| --- | --- |
| Basic | Free · docs, re:Post, core Trusted Advisor |
| Business Support+ | Minimum for production · 24/7 · full Trusted Advisor · < 1 hour production down |
| Enterprise Support | Designated TAM · < 15 min critical down |
| Unified Operations | Mission-critical · < 5 min |
