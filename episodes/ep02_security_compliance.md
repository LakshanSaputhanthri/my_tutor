# Episode 2 — Security and Compliance (Domain 2, 30%)

**Hosts:** **නදී** (AWS engineer) · **කසුන්** (තර්ක කරන developer)

**මේ episode එකෙන් ඉගෙන ගන්නේ:**
- Shared Responsibility Model — **exam එකේ වැදගත්ම එක**
- IAM සහ root user
- Security services — එක service එකකට එක keyword එක

---

## 1. Shared Responsibility Model

**කසුන්:** මම AWS ට ගෙවනවා. ඉතින් security ඔක්කොම AWS ගේ වැඩේ නේද?

**නදී:** නෑ! Apartment එකක් කුලියට ගත්තා වගේ. Building එක, lift එක, gate එකේ guard — **owner ගේ** වැඩේ. ඔයාගේ කාමරේ දොර lock කරන එක — **ඔයාගේ** වැඩේ.

**කසුන්:** මම දොර ඇරලා ගියොත්?

**නදී:** ඒක owner ගේ වරද නෙවෙයි.

> **මතක තියාගන්න:**
> **AWS = security OF the cloud. Customer = security IN the cloud.**

| AWS කරනවා (OF) | ඔයා කරනවා (IN) |
| --- | --- |
| Data centers, guards, විදුලිය | ඔයාගේ **data** |
| Hardware, network | **IAM** users, permissions |
| Hypervisor | **EC2 OS patching** |
| Regions, AZs | **Security groups** |
| පරණ disks විනාශ කිරීම | **Encryption** on කරනවද නැද්ද කියන එක |

**කසුන්:** RDS database එකේ OS එක patch කරන්නේ කවුද?

**නදී:** **AWS.** RDS **managed** නිසා. ඒත් **EC2** එකේ OS එක patch කරන්නේ **ඔයා**. Exam එකේ ප්‍රියතම trap එක ඒක.

> **Rule:** Service එක **managed** වෙන තරමට ඔයාගේ වැඩ **අඩුයි**.
> **EC2** (ඔයාට වැඩිම) → **RDS** (මැද) → **Lambda, S3, DynamoDB** (ඔයාට අඩුම)
>
> **Shared controls** (දෙගොල්ලම කරනවා): **Patch management · Configuration management · Awareness & training**

---

## 2. IAM — කවුද ඇතුළට එන්නේ?

**නදී:** **IAM = Identity and Access Management.** කවුද එන්නේ, එයාට මොනවද කරන්න පුළුවන් — ඒක IAM. **Global** service එකක්. **Free**.

### Root user

**කසුන්:** මම root user එකෙන්ම ඔක්කොම වැඩ කරනවා. ලේසියි.

**නදී:** ඒක "**වඳුරාට දැලි පිහියක් දුන්නා වගේ**." Root user ට **ඕනම දෙයක්** කරන්න පුළුවන්. Account එකම delete කරන්නත් පුළුවන්.

> **Root user rules:**
> - **MFA** දාන්න
> - දවස් පතා පාවිච්චි කරන්න **එපා**
> - **Access keys** හදන්න **එපා**
>
> **Root user ට විතරක් කරන්න පුළුවන්:** account එක **close** කරන එක · **support plan** එක වෙනස් කරන එක · account settings (email, name) වෙනස් කරන එක

### IAM කොටස් 4

| කොටස | සරලව |
| --- | --- |
| **User** | මිනිහෙක් හෝ app එකක් |
| **Group** | Users ගොඩක් (Group එකක් ඇතුළේ group **බෑ**) |
| **Role** | **තාවකාලික** permissions — EC2, Lambda වගේ services වලට, හෝ වෙන account එකක අයට |
| **Policy** | **JSON** document — Allow / Deny |

**කසුන්:** Role එක ඕන ඇයි? Access key එක code එකේ දැම්මොත් ඉවරයි නේ.

**නදී:** ඒක "**හොරාට යතුර දුන්නා වගේ**." Code එක GitHub එකට ගියොත් key එක ලෝකෙටම පේනවා. ඊට පස්සේ ලොකු bill එකක් — "**ගහෙන් වැටුණු මිනිහාට ගොනා ඇන්නා වගේ.**"

> **Exam:** "EC2 needs to access S3" → **IAM Role** (access keys නෙවෙයි)

### Least privilege

**නදී:** "**වැටත් නියරත් ගොයම කෑවා වගේ**" — ආරක්ෂා කරන්න ඕන කෙනාම හානි කරනවා. ඒක වළක්වන්න **principle of least privilege** — වැඩේට **ඕන අවම** permissions විතරයි.

### Accounts ගොඩක් තියෙනවා නම්

- **AWS Organizations** — accounts ගොඩක් එක තැනකින්. **SCPs (Service Control Policies)** වලින් සීමා දානවා. **Consolidated billing**.
- **IAM Identity Center** — accounts ගොඩකට **එක login** (single sign-on).
- **AWS Control Tower** — secure multi-account setup එක ඉබේම හදනවා.
- **Federation** — company එකේ තියෙන login එකෙන්ම (Active Directory) AWS එකට.

---

## 3. Security Services — එකකට එක keyword

**කසුන්:** Services ගොඩයි. මට ඔක්කොම මතක තියාගන්න බෑ.

**නදී:** එකකට **එක keyword** එක විතරක් මතක තියාගන්න.

| Keyword | Service |
| --- | --- |
| **DDoS** | **AWS Shield** (Standard = free, Advanced = paid + 24/7 team) |
| **SQL injection, XSS, block IP** | **AWS WAF** |
| WAF rules accounts ගොඩකට | **AWS Firewall Manager** |
| **Threats** (අමුතු activity) | **Amazon GuardDuty** |
| **Vulnerabilities** (software දුර්වලතා) | **Amazon Inspector** |
| **PII / sensitive data in S3** | **Amazon Macie** |
| Findings ඔක්කොම **එක තැනක** | **AWS Security Hub** |
| Issue එකේ **root cause** | **Amazon Detective** |
| **Encryption keys** | **AWS KMS** |
| **Dedicated** key hardware | **AWS CloudHSM** |
| **SSL/TLS certificates** | **AWS Certificate Manager (ACM)** |
| Passwords **auto-rotate** | **AWS Secrets Manager** |
| App users **sign-in** | **Amazon Cognito** |
| Third-party security tools | **AWS Marketplace** |

**කසුන්:** GuardDuty සහ Inspector පටලැවෙනවා.

**නදී:** **GuardDuty = CCTV camera** — හොරු ආවද බලනවා (**threats**). **Inspector = lock check කරන කෙනා** — දොර කැඩිලද බලනවා (**vulnerabilities**).

**කසුන්:** Shield සහ WAF?

**නදී:** **Shield** — සෙනඟ ගොඩක් එකපාර දොරට කඩාගෙන එනවා (**DDoS**). **WAF** — එක හොරෙක් බොරු key එකකින් දොර අරින්න හදනවා (**SQL injection**).

### Encryption

- **At rest** — disk එකේ තියෙනකොට (KMS, S3, EBS encryption)
- **In transit** — network එකේ යනකොට (**TLS/SSL**, HTTPS)

---

## 4. Monitoring සහ Auditing — ලොකුම trap එක

**නදී:** මේ **තුන** exam එකේ නිතරම එකට එනවා.

| Service | සරලව | උදාහරණ question |
| --- | --- | --- |
| **CloudTrail** | **Visitor's book** — **කවුද, මොනවද, කවදද** (API calls) | "Who deleted the EC2 instance?" |
| **CloudWatch** | **Heart monitor** — metrics, logs, **alarms** | "Alert when CPU > 80%" |
| **AWS Config** | **Photo album** — resource **settings** එදා කොහොමද තිබුණේ | "Are all S3 buckets encrypted?" |

**කසුන්:** "Who" දැක්කොත් CloudTrail. "Alarm" දැක්කොත් CloudWatch. "Configuration" / "compliance rules" දැක්කොත් Config.

**නදී:** නියමයි!

### Compliance සහ help

| Keyword | Service |
| --- | --- |
| AWS ගේ **compliance reports** download (SOC, PCI, ISO) | **AWS Artifact** |
| **ඔයාගේ** audit එකට evidence එකතු කරන්න | **AWS Audit Manager** |
| Best-practice checks (cost, security, limits) | **AWS Trusted Advisor** |
| AWS services down ද? | **AWS Health Dashboard** |
| Security tips කියවන්න | **AWS Security Center, Security Blog, Knowledge Center** |

**කසුන්:** AWS PCI certified නම්, මගේ app එකත් PCI ද?

**නදී:** නෑ. "**A good kitchen doesn't make you a good cook.**" AWS infrastructure compliant. ඔයාගේ app එක compliant කරන්න ඕන ඔයා. Compliance needs **රට** අනුව සහ **industry** එක අනුව වෙනස් වෙනවා.

---

## Practice Questions (20)

**Q1.** Under the shared responsibility model, which is the customer's responsibility?
A. Physical security of data centers
B. Patching the guest operating system on Amazon EC2
C. Maintaining the hypervisor
D. Replacing failed hard drives

**Q2.** Which is AWS's responsibility when using Amazon RDS?
A. Creating database users
B. Patching the database engine
C. Encrypting data the customer chooses to store
D. Configuring security group rules

**Q3.** Which are shared controls between AWS and the customer? (Select TWO)
A. Patch management
B. Physical access control
C. Configuration management
D. Data center cooling
E. Hardware disposal

**Q4.** What is the BEST way to protect the AWS account root user?
A. Share the password with the admin team
B. Enable MFA and avoid using it for daily tasks
C. Create access keys for the root user
D. Delete the root user

**Q5.** Which task can ONLY the root user perform?
A. Launch an EC2 instance
B. Create an IAM user
C. Change the AWS Support plan
D. Create an S3 bucket

**Q6.** An application on Amazon EC2 needs to read files from Amazon S3. What is the MOST secure way to give access?
A. Store access keys in the code
B. Use the root user credentials
C. Attach an IAM role to the EC2 instance
D. Make the S3 bucket public

**Q7.** Granting users only the permissions they need to do their job is called:
A. Defense in depth
B. Principle of least privilege
C. Shared responsibility
D. Elasticity

**Q8.** Which service records API calls to show who made a change in an AWS account?
A. Amazon CloudWatch
B. AWS CloudTrail
C. AWS Config
D. Amazon Inspector

**Q9.** Which service can send an alarm when EC2 CPU usage is above 80%?
A. AWS CloudTrail
B. Amazon CloudWatch
C. AWS Artifact
D. Amazon Macie

**Q10.** A company wants to check continuously that all EBS volumes are encrypted. Which service?
A. AWS Config
B. AWS Shield
C. Amazon Cognito
D. AWS Artifact

**Q11.** Where can a customer download AWS SOC and PCI compliance reports?
A. AWS Trusted Advisor
B. AWS Artifact
C. AWS Security Hub
D. Amazon Inspector

**Q12.** Which service protects against DDoS attacks?
A. AWS Shield
B. Amazon Macie
C. AWS KMS
D. Amazon Cognito

**Q13.** Which service blocks SQL injection and cross-site scripting attacks?
A. AWS Shield Standard
B. AWS WAF
C. Amazon GuardDuty
D. AWS Config

**Q14.** Which service uses machine learning to detect malicious activity in CloudTrail logs and VPC Flow Logs?
A. Amazon Inspector
B. Amazon GuardDuty
C. Amazon Macie
D. AWS Audit Manager

**Q15.** Which service scans EC2 instances and container images for software vulnerabilities?
A. Amazon Inspector
B. AWS Shield
C. AWS WAF
D. Amazon Detective

**Q16.** Which service finds personally identifiable information (PII) stored in Amazon S3?
A. Amazon GuardDuty
B. Amazon Macie
C. AWS Secrets Manager
D. AWS CloudHSM

**Q17.** Which service automatically rotates database passwords?
A. AWS KMS
B. AWS Secrets Manager
C. AWS Certificate Manager
D. IAM Access Analyzer

**Q18.** Which service creates and manages encryption keys?
A. AWS KMS
B. Amazon Cognito
C. AWS WAF
D. AWS Artifact

**Q19.** Which service lets users log in once to access many AWS accounts?
A. Amazon Cognito
B. AWS IAM Identity Center
C. AWS Shield
D. AWS Config

**Q20.** Where can a company buy third-party security software that runs on AWS?
A. AWS Artifact
B. AWS Marketplace
C. AWS Trusted Advisor
D. AWS Professional Services

### Answers

- **Q1 — B.** EC2 OS patch = **customer**.
- **Q2 — B.** RDS managed → DB engine patch = **AWS**. DB users, security groups = customer.
- **Q3 — A, C.** Shared: **patch** + **configuration** management (+ training).
- **Q4 — B.** MFA + daily වැඩට පාවිච්චි නොකිරීම.
- **Q5 — C.** Support plan වෙනස් කිරීම = root only.
- **Q6 — C.** Service එකකට → **IAM role**.
- **Q7 — B.** Least privilege.
- **Q8 — B.** "Who" → **CloudTrail**.
- **Q9 — B.** Alarm → **CloudWatch**.
- **Q10 — A.** Settings check කරනවා → **Config**.
- **Q11 — B.** Compliance reports → **Artifact**.
- **Q12 — A.** DDoS → **Shield**.
- **Q13 — B.** SQL injection → **WAF**.
- **Q14 — B.** Threats → **GuardDuty** (CCTV).
- **Q15 — A.** Vulnerabilities → **Inspector**.
- **Q16 — B.** PII in S3 → **Macie**.
- **Q17 — B.** Rotate → **Secrets Manager**.
- **Q18 — A.** Keys → **KMS**.
- **Q19 — B.** Accounts ගොඩකට එක login → **IAM Identity Center**. (Cognito = app users ට)
- **Q20 — B.** Third-party software → **Marketplace**.

---

## Closing

**කසුන්:** දැන් තේරෙනවා — AWS ගෙදර හදලා දෙනවා. දොර lock කරන එක මගේ වැඩේ.

**නදී:** නියම summary එක! **Homework:** IAM group එකක් හදලා, user කෙනෙක් දාලා, **ReadOnlyAccess** policy එක දෙන්න. Console එකේ **Artifact** සහ **Trusted Advisor** open කරලා බලන්න.

**කසුන්:** ඊළඟට — Compute, Storage, Databases.

**නදී:** ආයෙත් හමුවෙමු!
