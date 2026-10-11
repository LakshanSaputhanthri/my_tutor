# Episode 1 — Exam එක + Cloud Concepts (Domain 1, 24%)

**Hosts:** **නදී** (AWS engineer, සරලව කියලා දෙනවා) · **කසුන්** (developer, හැම දේටම තර්ක කරනවා)

**මේ episode එකෙන් ඉගෙන ගන්නේ:**
- Exam එක කොහොමද
- Cloud එකේ වාසි 6
- Well-Architected pillars 6, CAF, 7 Rs

---

## 1. Exam එක — කෙටියෙන්

**කසුන්:** නදී, exam එක අමාරුද?

**නදී:** නෑ. මේක **foundational** exam එකක්. Coding නෑ. Design කරන්න කියන්නේ නෑ. "මේ වැඩේට හරි AWS service එක මොකක්ද?" — ඒක තමයි ගොඩක් questions.

**කසුන්:** Questions කීයද?

**නදී:** **65**යි. **50**ක් විතරයි marks වලට ගණන් වෙන්නේ. ඉතුරු **15** test questions. ඒවා මොනවද කියලා දැනගන්න බෑ.

**කසුන්:** වැරදුණොත් marks කපනවද?

**නදී:** නෑ. ඉතින් **හැම question එකටම answer එකක් දාන්න.** Blank තිබ්බොත් වැරදි විදිහටම ගණන් වෙනවා.

**කසුන්:** "**Nothing ventured, nothing gained**" — guess කරන්න බය වෙන්න එපා!

> **මතක තියාගන්න:**
> - විනාඩි **90** · Questions **65** (scored **50**) · Pass **700/1000** · USD **100** · අවුරුදු **3**ක් valid
> - Domain weights: Cloud Concepts **24%** · Security **30%** · Technology **34%** · Billing **12%**
> - English මව් භාෂාව නෙවෙයි නම් → **ESL +30 minutes** request කරන්න (book කරන්න **කලින්**)
> - Section එකින් section pass වෙන්න ඕන නෑ. **Total** එක 700 වුණාම ඇති.

---

## 2. Cloud කියන්නේ මොකක්ද?

**කසුන්:** Cloud කියන්නේ වෙන කෙනෙක්ගේ computer එකක් විතරයි නේ?

**නදී:** ඔව්, ඒත් වෙනස මෙතන — ඔයා **ඕන වෙලාවට** ගන්නවා, **පාවිච්චි කරන ප්‍රමාණයට** විතරක් ගෙවනවා. ඒකට කියන්නේ **pay-as-you-go**.

**නදී:** කරන්ට් බිල වගේ. Power station එකක් ඔයා හදන්නේ නෑ. Switch එක දාලා, පාවිච්චි කරන units වලට ගෙවනවා.

**කසුන්:** ඒ example එක හොඳයි.

> **මතක තියාගන්න:**
> **Cloud computing = on-demand delivery of IT resources over the internet with pay-as-you-go pricing.**

### Deployment models 3

| Model | සරලව |
| --- | --- |
| **Cloud** | ඔක්කොම AWS එකේ |
| **On-premises** | තමන්ගේම data center එකේ |
| **Hybrid** | දෙකම connect කරලා |

### Service models 3 — Pizza එකෙන්

| Model | Pizza | AWS උදාහරණය |
| --- | --- | --- |
| **IaaS** | කුස්සිය කුලියට. උයන්නේ ඔයා | **EC2** |
| **PaaS** | Base එක ලෑස්තියි. Topping විතරක් ඔයා | **Elastic Beanstalk** |
| **SaaS** | Pizza එක ගෙදරටම | Gmail, Zoom |

---

## 3. Cloud එකේ වාසි 6 — කටපාඩම් කරන්න

**කසුන්:** මම server එකක් ගන්නම්. එක පාරයි ගෙවන්නේ.

**නදී:** Sale කාලෙට traffic 10 ගුණයක් වුණොත්?

**කසුන්:** ලොකු server එකක් ගන්නවා.

**නදී:** අවුරුද්දේ ඉතුරු දවස් ටිකේ ඒක හිස්ව තියෙනවා. අපේ අය කියනවා "**ඇඳේ දිගට කකුල් දිගහරින්න**" කියලා. ඒත් server එක ගන්නකොට ඔයාට ඇඳ තෝරගන්න වෙන්නේ ලොකුම කකුල් දිගට. Cloud එකේ ඇඳ කකුල අනුව ලොකු-පොඩි වෙනවා.

**කසුන්:** *(හිනාවෙලා)* හරි, මම පරාදයි.

> **මතක තියාගන්න — Six advantages:**
> 1. **Trade fixed expense for variable expense** — CapEx → OpEx
> 2. **Benefit from massive economies of scale** — AWS ලොකු නිසා මිල අඩුයි
> 3. **Stop guessing capacity**
> 4. **Increase speed and agility**
> 5. **Stop spending money running and maintaining data centers**
> 6. **Go global in minutes**

**නදී:** **CapEx** = මුලින්ම ලොකු මුදලක් (server එක ගන්නවා). **OpEx** = පාවිච්චියට ගෙවනවා (කුලියට වගේ).

---

## 4. Cloud Economics — සල්ලි ගැන

**කසුන්:** On-premises වල වියදම් මොනවද?

**නදී:** Server එකේ මිල විතරක් නෙවෙයි. ගොඩනැගිල්ල, විදුලිය, AC, security, IT staff, hardware replace කිරීම. මේ හැංගිලා තියෙන වියදම් ගොඩයි.

**නදී:** තව වචන කිහිපයක්:

- **Rightsizing** — වැඩේට **හරියන size** එක තෝරන එක. ලොකු instance එකක් 5% CPU එකකින් run වෙනවා නම්, පොඩි එකකට මාරු කරන්න.
- **Automation** — අතින් කරන වැඩ code එකකින්. වේගයි, වැරදි අඩුයි.
- **Licensing:**
  - **License included** — AWS එකෙන්ම license එක එක්ක ගන්නවා. (Windows එක්ක EC2)
  - **BYOL — Bring Your Own License** — ඔයා ළඟ තියෙන license එක ගෙනත් පාවිච්චි කරනවා.

---

## 5. වැදගත් වචන — මිනිස්සු පටලවන තැන

**කසුන්:** Scalability, elasticity — දෙකම එකයි නේද?

**නදී:** "**Same same, but different!**"

| වචනය | සරල තේරුම |
| --- | --- |
| **Scalability** | Load වැඩි වුණාම **ලොකු වෙන්න පුළුවන්** |
| **Elasticity** | Demand අනුව **ඉබේම** ලොකු වෙලා, ආයෙ **පොඩිත් වෙනවා** (Auto Scaling) |
| **High availability** | කොටසක් fail වුණත් system එක **දිගටම** වැඩ (Multi-AZ) |
| **Fault tolerance** | Fail වුණත් **zero downtime** |
| **Agility** | ඉක්මනින්, ලාභෙට අලුත් දේවල් try කරන්න පුළුවන් |

**නදී:** Scaling වර්ග දෙක:
- **Vertical (scale up)** — instance එක **ලොකු** කරනවා
- **Horizontal (scale out)** — instances **ගණන** වැඩි කරනවා

> **Exam trick:** "**automatically**" + "**demand**" + "**ආයෙ අඩු වෙනවා**" → **Elasticity**

### Disaster Recovery — 4 ක්‍රම

ලාභම/හෙමින්ම → ගණන්ම/වේගවත්ම:

1. **Backup & Restore** — backup විතරයි
2. **Pilot Light** — database එක විතරක් හැමවෙලේම on
3. **Warm Standby** — පොඩි copy එකක් හැමවෙලේම on
4. **Multi-site** — සම්පූර්ණ copy දෙකක්

**කසුන්:** හැමෝම Multi-site කරන්නේ නැත්තේ ඇයි?

**නදී:** "**Don't use a sledgehammer to crack a nut.**" පොඩි blog එකකට ඒක ඕනවට වඩා ගණන්.

---

## 6. Well-Architected Framework — Pillars 6

**නදී:** AWS කියනවා හොඳ system එකකට කුළුණු 6ක් ඕන කියලා.

| Pillar | එක වචනයෙන් |
| --- | --- |
| **Operational Excellence** | Run, monitor, **automate** (CloudFormation) |
| **Security** | **Protect** — least privilege, encryption |
| **Reliability** | **Recover** — වැටුණොත් නැගිටින්න |
| **Performance Efficiency** | **Right resource** — හරි වැඩේට හරි tool එක |
| **Cost Optimization** | **No waste** — ඕන නැති දේට ගෙවන්න එපා |
| **Sustainability** | **Environment** — පරිසරයට හානිය අඩු කරන්න |

**කසුන්:** Reliability සහ Performance පටලැවෙනවා.

**නදී:** Reliability — "**වැටුණොත් නැගිටිනවද?**" Performance — "**හරි සපත්තුව දාගෙන දුවනවද?**"

**නදී:** Review එකක් කරන්න → **AWS Well-Architected Tool**.

> **Design principles:** Design for failure · **Decouple** (SQS) · Automate · Use managed services · Think parallel

---

## 7. Cloud Adoption Framework (CAF)

**කසුන්:** CAF මොකටද?

**නදී:** Company එකක් cloud එකට යනකොට technology විතරක් නෙවෙයි — **මිනිස්සු** සහ **process** ත් වෙනස් වෙන්න ඕන. CAF ඒකට guide එකක්.

> **Perspectives 6:**
> - Business පැත්ත: **Business · People · Governance** → "**බත් පොල් ගෙඩි**" (B-P-G)
> - Technical පැත්ත: **Platform · Security · Operations** → "**පාන් සීනි ඔලු**" (P-S-O)
>
> **CAF benefits 4:** reduced **business risk** · improved **ESG** performance · increased **revenue** · increased **operational efficiency**

**නදී:** Keywords:
- **training, staff, culture** → **People**
- **risk, portfolio** → **Governance**
- **monitoring, incidents** → **Operations**

---

## 8. Migration — 7 Rs

**කසුන්:** අපේ පරණ systems ඔක්කොම අලුතෙන් ලියමු!

**නදී:** "**හෙමින් සීරුවේ ගියොත් හිමාලයටත් යන්න පුළුවන්.**" එක පාරට ඔක්කොම rewrite කරන එක වැඩිම effort. පියවරෙන් පියවර යමු.

| R | සරලව |
| --- | --- |
| **Retire** | Off කරනවා |
| **Retain** | දැනට තියාගන්නවා |
| **Rehost** | **Lift and shift** — වෙනසක් නැතුව EC2 එකට |
| **Relocate** | VMware → VMware Cloud on AWS |
| **Replatform** | **Lift, tinker and shift** — පොඩි වෙනසක් (DB → RDS) |
| **Repurchase** | **Drop and shop** — SaaS එකකට |
| **Refactor** | Cloud-native විදිහට අලුතෙන් ලියනවා (වැඩිම effort) |

**Migration tools:**
- **Snow Family (Snowball Edge)** — data **ගොඩක්**, internet **හෙමින්** → device එකක් courier කරනවා
- **AWS DMS** — database migrate කරන්න (DB එක වැඩ කරද්දිම)
- **AWS SCT** — DB engine එක **වෙනස්** කරනවා නම් (Oracle → Aurora)
- **Application Migration Service (MGN)** — servers lift-and-shift
- **DataSync** — network එකෙන් data copy

---

## Practice Questions (15)

උත්තර බලන්න කලින් ඔයාම try කරන්න. උත්තර පහළින්.

**Q1.** A company wants to stop buying hardware based on guesses about future traffic. Which benefit of AWS does this describe?
A. Go global in minutes
B. Stop guessing capacity
C. Economies of scale
D. Increase speed and agility

**Q2.** Which describes moving from large upfront payments to paying only for what you use?
A. Trade fixed expense for variable expense
B. Stop spending money on data centers
C. High availability
D. Rightsizing

**Q3.** An application automatically adds servers during busy hours and removes them at night. Which concept is this?
A. Fault tolerance
B. High availability
C. Elasticity
D. Agility

**Q4.** AWS can offer lower prices because millions of customers share its infrastructure. Which benefit is this?
A. Economies of scale
B. Elasticity
C. Agility
D. Pay-as-you-go

**Q5.** Which Well-Architected pillar focuses on recovering quickly from failures?
A. Performance Efficiency
B. Operational Excellence
C. Reliability
D. Security

**Q6.** Which Well-Architected pillar focuses on reducing the environmental impact of workloads?
A. Cost Optimization
B. Sustainability
C. Reliability
D. Operational Excellence

**Q7.** Which AWS CAF perspective focuses on staff training and organizational culture?
A. Governance
B. Platform
C. People
D. Operations

**Q8.** A company moves an application to Amazon EC2 without making any changes. Which migration strategy is this?
A. Refactor
B. Replatform
C. Repurchase
D. Rehost

**Q9.** A company moves its self-managed database to Amazon RDS with small changes. Which migration strategy is this?
A. Rehost
B. Replatform
C. Retain
D. Retire

**Q10.** A company needs to move 500 TB of data to AWS, but its internet connection is slow. Which service is BEST?
A. AWS DataSync
B. AWS Snowball Edge
C. AWS Direct Connect
D. Amazon S3 Transfer Acceleration

**Q11.** Which deployment model connects on-premises infrastructure with AWS?
A. Public cloud
B. Hybrid
C. Private cloud
D. Multi-cloud

**Q12.** A company uses an EC2 instance that runs at only 5% CPU. What should it do to save cost?
A. Buy a Dedicated Host
B. Rightsize to a smaller instance
C. Add more instances
D. Move to another Region

**Q13.** Which AWS service is an example of Platform as a Service (PaaS)?
A. Amazon EC2
B. AWS Elastic Beanstalk
C. Amazon VPC
D. Amazon EBS

**Q14.** Which are benefits of the AWS Cloud Adoption Framework? (Select TWO)
A. Reduced business risk
B. Free EC2 instances
C. Increased revenue
D. No need for security
E. Automatic code writing

**Q15.** Which disaster recovery strategy has the LOWEST cost but the SLOWEST recovery?
A. Multi-site
B. Warm standby
C. Pilot light
D. Backup and restore

### Answers

- **Q1 — B.** "Guess කරලා buy කරන්නේ නෑ" → **Stop guessing capacity**.
- **Q2 — A.** Upfront (fixed) → use-based (variable).
- **Q3 — C.** ඉබේම වැඩි වෙලා **ආයෙ අඩු වෙනවා** → Elasticity.
- **Q4 — A.** Customers ගොඩක් නිසා මිල අඩුයි → Economies of scale.
- **Q5 — C.** Recover → **Reliability**.
- **Q6 — B.** Environment → **Sustainability**.
- **Q7 — C.** Training, culture → **People**.
- **Q8 — D.** වෙනසක් නැතුව → **Rehost** (lift and shift).
- **Q9 — B.** පොඩි වෙනසක් → **Replatform** (lift, tinker and shift).
- **Q10 — B.** Data ගොඩක් + internet slow → **Snowball Edge**.
- **Q11 — B.** On-prem + cloud → **Hybrid**.
- **Q12 — B.** ඕනවට වඩා ලොකුයි → **Rightsize**.
- **Q13 — B.** Code එක විතරයි දෙන්නේ → **Elastic Beanstalk** (PaaS). EC2 = IaaS.
- **Q14 — A, C.** CAF benefits: business risk අඩු වෙනවා, revenue වැඩි වෙනවා.
- **Q15 — D.** Backup & Restore = ලාභම, හෙමින්ම.

---

## Closing

**කසුන්:** මම තාමත් කියනවා cloud කියන්නේ වෙන කෙනෙක්ගේ computer එකක් කියලා. ඒත් දැන් තේරෙනවා — ඒ කෙනා ළඟ ලෝකයේ හොඳම data centers තියෙනවා.

**නදී:** *(හිනාවෙලා)* **Homework:** Free Tier account එකක් හදන්න → root user ට **MFA** දාන්න → **AWS Budgets** එකෙන් $5 alert එකක් හදන්න.

**කසුන්:** ඊළඟට — **Security**. Exam එකේ 30%!

**නදී:** ආයෙත් හමුවෙමු!
