# Episode 5 — Billing, Pricing, and Support (Domain 4, 12%)

**Hosts:** **නදී** (AWS engineer) · **කසුන්** (තර්ක කරන developer)

**මේ episode එකෙන් ඉගෙන ගන්නේ:**
- AWS වලට ගෙවන ක්‍රම — EC2 options 7
- Cost tools — Pricing Calculator, Cost Explorer, Budgets
- **අලුත්** Support plans (2026)
- Help ගන්න තැන්

---

## Opening

**කසුන්:** මගේ යාළුවෙක් GPU server එකක් on කරලා අමතක වුණා. Bill එක dollars 3000යි!

**නදී:** "**Learn from others' mistakes.**" අද episode එකෙන් පස්සේ ඔයාට එහෙම වෙන්නේ නෑ.

---

## 1. මූලික pricing

**නදී:** ගෙවන්න වෙන ප්‍රධාන දේවල් **3**:
1. **Compute** (servers run වෙන කාලය)
2. **Storage** (GB ගණන)
3. **Data transfer OUT** (AWS එකෙන් **එළියට** යන data)

| Data transfer | ගෙවන්න ඕනද? |
| --- | --- |
| Internet එකෙන් AWS **ඇතුළට** (inbound) | **Free** |
| AWS එකෙන් internet එකට (outbound) | **ගෙවන්න ඕන** |
| එක **Region** එකකින් තව Region එකකට | **ගෙවන්න ඕන** |
| එකම Region එකේ **AZs අතර** | **ගෙවන්න ඕන** (පොඩි ගණනක්) |

**කසුන්:** ඇතුළට එන්න නිදහස්, එළියට යන්න ගෙවන්න. Hotel එකක් වගේ!

> **Pricing philosophy:** Pay-as-you-go · **Commit** කළොත් save · **වැඩිපුර** පාවිච්චි කළොත් unit එකක මිල අඩුයි (volume discounts)
>
> **Free Tier:** **Always free** (Lambda requests වගේ) · **12 months free** (පරණ accounts) · **Trials** — AWS 2025 දී අලුත් accounts වලට credit-based free plan එකක් ගෙනාවා. Exam එකට concept එක දැනගත්තම ඇති.

---

## 2. EC2 ගෙවන ක්‍රම 7 — ලොකු තර්කය

**කසුන්:** On-Demand තමයි හොඳම. Commitment නෑ!

**නදී:** Flexibility එකට ඔයා **වැඩිම මිල** ගෙවනවා. Hotel එකක් හිතන්න:

| Option | Hotel උදාහරණය | Discount | කවදද? |
| --- | --- | --- | --- |
| **On-Demand** | එක රැයකට කාමරයක් | නෑ | කෙටි කාලීන, **unpredictable** |
| **Reserved Instances** | අවුරුදු 1/3 lease | **72%** දක්වා | **Steady** 24/7 workloads |
| **Savings Plans** | මාසෙට **$/hour** package එකක් | **72%** දක්වා | Steady, ඒත් **flexible** (Lambda, Fargate ත්) |
| **Spot Instances** | හිස් කාමර — ඕන වුණාම ඉවත් කරනවා | **90%** දක්වා | **Interrupt** වුණාට කමක් නැති වැඩ |
| **Dedicated Hosts** | **මුළු ගෙදරම** ඔයාට | — | **Server-bound licenses** (BYOL), compliance |
| **Dedicated Instances** | ඔයාට විතරක් **කාමරයක්** | — | Hardware share නොකර |
| **Capacity Reservations** | කාමරය **reserve** කරලා තියනවා | නෑ | Specific AZ එකක capacity **guarantee** |

**කසුන්:** 90% discount! මම database එක Spot එකේ දානවා.

**නදී:** *(හිනාවෙලා)* Spot එක AWS ට ඕන වුණාම **විනාඩි 2ක warning** එකකින් ආපහු ගන්නවා. Database එක එකපාරටම නැති වුණොත් shop එකම නවතිනවා. **Database එකට Spot කවදාවත් එපා.**

> **Exam keywords:**
> - "**can be interrupted**", "**flexible start/end time**", batch jobs → **Spot**
> - "**steady**", "**1 or 3 years**", "**24/7**" → **Reserved / Savings Plans**
> - "**short-term**", "**unpredictable**", "**cannot be interrupted**" → **On-Demand**
> - "**existing server-bound licenses**", "**sockets/cores**" → **Dedicated Hosts**

**Reserved Instances ගැන තව:**
- **Standard RI** — වැඩිම discount, instance type එක වෙනස් කරන්න බෑ
- **Convertible RI** — අඩු discount, instance family එක **වෙනස් කරන්න පුළුවන්**
- **All Upfront** ගෙව්වොත් වැඩිම discount
- **AWS Organizations** එකේ RI discount එක accounts අතර **share** වෙනවා

**කසුන්:** මගේ shop එකට එහෙනම්?

**නදී:** Mix එකක්! Database — **Reserved**. Sale කාලේ spike — **On-Demand + Auto Scaling**. රෑට reports — **Spot**.

**කසුන්:** "**එක ගලෙන් කුරුල්ලෝ දෙන්නා**" නෙවෙයි — ගල් තුනෙන් කුරුල්ලෝ තුන්දෙනා!

---

## 3. Cost Tools

**නදී:** "**ඇඳේ දිගට කකුල් දිගහරින්න.**" Budget එක ඇතුළේ ඉන්න මේ tools:

| Tool | කාලය | සරල උදාහරණය |
| --- | --- | --- |
| **Pricing Calculator** | **අනාගතය** — build කරන්න **කලින්** estimate | ගෙදර හදන්න කලින් **quotation** එක |
| **Cost Explorer** | **අතීතය** — වියදම් graphs, forecast | බැංකු **statement** එක |
| **Budgets** | **Limit** එක — පනිනකොට **alert** | Credit card **limit SMS** එක |
| **Cost and Usage Report (CUR)** | **ඉතාම විස්තර** data | Receipt එකේ හැම line එකක්ම |
| **Cost Anomaly Detection** | **අමුතු** වියදම් ML වලින් | "සාමාන්‍ය නැති වියදමක්!" |
| **Cost allocation tags** | Cost **බෙදන්න** (project, department) | ගෙදර බිල් කාමර අනුව බෙදනවා |

**කසුන්:** මගේ යාළුවා Budgets alert එකක් හදලා තිබ්බා නම් $3000 ඉතුරු.

### AWS Organizations — Consolidated Billing

- Accounts ගොඩකට **එක bill** එකක්
- Usage **එකතු** වෙලා → **volume discounts**
- RI / Savings Plans discounts accounts අතර **share**
- **Free**

---

## 4. Support Plans — 2026 අලුත් plans

**නදී:** වැදගත්! AWS support plans **වෙනස් කළා**. AWS exam guide එකේ දැන් තියෙන්නේ මේවා:

| Plan | කාටද? | Critical system down | ප්‍රධාන දේවල් |
| --- | --- | --- | --- |
| **Basic** | හැමෝටම, **free** | — (technical cases නෑ) | Customer service, docs, **re:Post**, **core** Trusted Advisor checks, AWS Health |
| **Business Support+** | **Production** workloads (අවම recommended plan එක) | **< 30 min** (production down < 1 hour) | **24/7** phone/chat/email, **full** Trusted Advisor, AI recommendations |
| **Enterprise Support** | **Business-critical** workloads | **< 15 min** | **Designated TAM** (Technical Account Manager), Well-Architected reviews, billing concierge |
| **Unified Operations** | **Mission-critical** workloads | **< 5 min** (Incident Management Engineer) | Designated domain specialist engineers, 24/7 workload monitoring |

**කසුන්:** Developer plan, Enterprise On-Ramp කියලා plans ගැන practice tests වල තියෙනවා නේ?

**නදී:** ඒවා **පරණ** plan names. පරණ practice tests වල තාමත් එනවා. Exam එකේ ආවොත් මේ විදිහට හිතන්න: **plan එක ලොකු වෙන තරමට response time එක අඩුයි**, **TAM** ඉහළ plans වල විතරයි.

> **Exam keywords:**
> - **Free**, documentation, re:Post → **Basic**
> - **Production** workload, **cheapest** with 24/7 + **full Trusted Advisor** → **Business Support+**
> - **Designated TAM**, **15 minutes** → **Enterprise Support**
> - **Mission-critical**, **5 minutes** → **Unified Operations**

### Help ගන්න තැන්

| Keyword | කොහෙද? |
| --- | --- |
| Community **Q&A** | **AWS re:Post** |
| නිතර අහන ප්‍රශ්න | **AWS Knowledge Center** |
| Migration strategies, patterns | **AWS Prescriptive Guidance** |
| AWS experts ලා hire කරන්න | **AWS Professional Services** / **Solutions Architects** |
| Consulting / software **partners** | **AWS Partner Network** (ISVs, system integrators) |
| Third-party software (AWS bill එකෙන්) | **AWS Marketplace** |
| AWS resources වලින් **abuse** (spam, phishing) | **AWS Trust & Safety team** |
| Best-practice checks (cost, security, limits) | **Trusted Advisor** |
| AWS service events, ඔයාට බලපාන issues | **AWS Health Dashboard / Health API** |
| Support case එකක් open කරන්න | **AWS Support Center** |

**Partner වෙන එකේ වාසි:** training & certification · partner events · **volume discounts**

---

## Practice Questions (20)

**Q1.** Which pricing model is BEST for a workload that runs 24/7 for the next 3 years?
A. On-Demand Instances
B. Spot Instances
C. Reserved Instances
D. Dedicated Hosts

**Q2.** A company runs batch jobs that can be stopped and restarted at any time. Which is MOST cost-effective?
A. On-Demand Instances
B. Spot Instances
C. Reserved Instances
D. Dedicated Instances

**Q3.** A company has a short-term workload that cannot be interrupted, and usage is unpredictable. Which option?
A. Spot Instances
B. Reserved Instances
C. On-Demand Instances
D. Savings Plans (3-year)

**Q4.** A company wants to use its existing server-bound software licenses on AWS. Which option?
A. Dedicated Hosts
B. Spot Instances
C. On-Demand Instances
D. Reserved Instances

**Q5.** Which pricing model gives a discount for committing to a dollar-per-hour amount and also covers AWS Lambda and AWS Fargate?
A. Standard Reserved Instances
B. Compute Savings Plans
C. Spot Instances
D. Dedicated Hosts

**Q6.** Which data transfer is usually free?
A. Data transfer out to the internet
B. Data transfer between Regions
C. Data transfer into AWS from the internet
D. Data transfer between Availability Zones

**Q7.** Which tool estimates the cost of an architecture BEFORE it is built?
A. AWS Cost Explorer
B. AWS Pricing Calculator
C. AWS Budgets
D. AWS Cost and Usage Report

**Q8.** Which tool shows graphs of past AWS spending and forecasts future costs?
A. AWS Cost Explorer
B. AWS Pricing Calculator
C. AWS Artifact
D. AWS Trusted Advisor

**Q9.** A company wants an alert when its monthly AWS costs are forecast to go above $1,000. Which tool?
A. AWS Cost Explorer
B. AWS Budgets
C. AWS Pricing Calculator
D. Amazon CloudWatch Logs

**Q10.** Which provides the MOST detailed AWS billing data?
A. AWS Budgets
B. AWS Cost and Usage Report
C. AWS Pricing Calculator
D. AWS Health Dashboard

**Q11.** A company wants to see costs for each project and department. What should it use?
A. Cost allocation tags
B. Security groups
C. IAM roles
D. Availability Zones

**Q12.** Which are benefits of consolidated billing in AWS Organizations? (Select TWO)
A. One bill for multiple accounts
B. Free EC2 instances
C. Combined usage for volume discounts
D. Automatic encryption of data
E. Free Enterprise Support

**Q13.** Which support plan is free for all AWS customers?
A. Basic
B. Business Support+
C. Enterprise Support
D. Unified Operations

**Q14.** Which support plan includes a designated Technical Account Manager (TAM)?
A. Basic
B. Business Support+
C. Enterprise Support
D. AWS re:Post

**Q15.** Which is AWS's minimum recommended support plan for production workloads?
A. Basic
B. Business Support+
C. Enterprise Support
D. Unified Operations

**Q16.** Where can users ask questions and get answers from the AWS community?
A. AWS re:Post
B. AWS Artifact
C. AWS Marketplace
D. AWS Organizations

**Q17.** Who should a customer contact to report that AWS resources are being used for spam or phishing?
A. AWS Professional Services
B. AWS Trust & Safety team
C. AWS Marketplace
D. AWS Partner Network

**Q18.** A company wants to hire AWS experts to help with a large migration project. What should it use?
A. AWS Professional Services
B. AWS re:Post
C. AWS Trusted Advisor
D. AWS Basic Support

**Q19.** Which service gives recommendations to reduce costs, improve security, and check service limits?
A. AWS Trusted Advisor
B. Amazon Inspector
C. AWS CloudTrail
D. AWS Budgets

**Q20.** Which option guarantees EC2 capacity in a specific Availability Zone without a long-term commitment?
A. Spot Instances
B. On-Demand Capacity Reservations
C. Savings Plans
D. Dedicated Hosts

### Answers

- **Q1 — C.** 24/7 + අවුරුදු 3 → **Reserved**. (Savings Plans ත් හරි — options වල නැත්නම්)
- **Q2 — B.** Interrupt වුණාට කමක් නෑ → **Spot**.
- **Q3 — C.** Short-term + interrupt කරන්න බෑ → **On-Demand**.
- **Q4 — A.** Server-bound licenses → **Dedicated Hosts**.
- **Q5 — B.** $/hour + Lambda/Fargate → **Compute Savings Plans**.
- **Q6 — C.** Inbound → **free**.
- **Q7 — B.** Build කරන්න කලින් → **Pricing Calculator** (quotation).
- **Q8 — A.** අතීතය + forecast → **Cost Explorer** (statement).
- **Q9 — B.** Alert → **Budgets** (limit SMS).
- **Q10 — B.** Most detailed → **CUR**.
- **Q11 — A.** Project අනුව → **Cost allocation tags**.
- **Q12 — A, C.** එක bill + volume discounts.
- **Q13 — A.** Free → **Basic**.
- **Q14 — C.** Designated TAM → **Enterprise Support**.
- **Q15 — B.** Production අවම → **Business Support+**.
- **Q16 — A.** Community Q&A → **re:Post**.
- **Q17 — B.** Abuse → **Trust & Safety**.
- **Q18 — A.** AWS experts → **Professional Services**.
- **Q19 — A.** Cost + security + limits → **Trusted Advisor**.
- **Q20 — B.** Capacity guarantee, no commitment → **Capacity Reservations**.

---

## Closing

**කසුන්:** Cloud ලාභයි — **ඒත්** ඔයා බලාගෙන ඉන්නවා නම් විතරයි.

**නදී:** ඒක තමයි cost optimization. **Homework:** **Budgets** alert එකක් හදන්න. **Pricing Calculator** එකේ t3.micro + 20 GB EBS + 50 GB S3 estimate එකක් හදන්න. **Cost Explorer** open කරලා බලන්න.

**කසුන්:** ඊළඟට — අන්තිම episode එක. Mock exam එක!

**නදී:** ආයෙත් හමුවෙමු!
