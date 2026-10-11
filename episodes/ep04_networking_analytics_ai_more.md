# Episode 4 — Networking, Messaging, Analytics, AI/ML, Other Services (Domain 3, 34% — Part 2)

**Hosts:** **නදී** (AWS engineer) · **කසුන්** (තර්ක කරන developer)

**මේ episode එකෙන් ඉගෙන ගන්නේ:**
- VPC — "වත්ත" උදාහරණයෙන්
- Office එක AWS එකට connect කරන ක්‍රම
- SQS, SNS, EventBridge
- Analytics සහ AI services — keyword එකෙන්
- Developer, end-user, IoT services

---

## 1. VPC — ඔයාගේ වත්ත

**නදී:** **Amazon VPC** = AWS එක ඇතුළේ ඔයාගේම **private network** එක. වත්තක් හිතන්න.

| කොටස | වත්තේ | සරලව |
| --- | --- | --- |
| **VPC** | මුළු වත්තම | ඔයාගේ network එක |
| **Public subnet** | පාරට මුහුණලා ඉස්සරහ කොටස | Internet එකට විවෘතයි (web servers) |
| **Private subnet** | ගෙයි ඇතුළත කාමරය | Internet එකෙන් එන්න බෑ (databases) |
| **Internet Gateway** | ප්‍රධාන **gate** එක | VPC ↔ Internet |
| **NAT Gateway** | **පිටිපස්සේ දොර** | Private subnet එකෙන් **එළියට** යන්න විතරයි |

### Firewalls දෙක

| | **Security Group** | **Network ACL** |
| --- | --- | --- |
| කොහෙද? | **Instance** එකේ (දොරේ guard) | **Subnet** එකේ (gate එකේ guard) |
| Rules | **Allow** විතරයි | **Allow + Deny** |
| මතකය | **Stateful** — ආපු කෙනාට යන්න ඉබේම පුළුවන් | **Stateless** — යනකොටත් එනකොටත් check |

**කසුන්:** "Block one IP address" කිව්වොත්?

**නදී:** **Network ACL** — Security Group එකට **deny** කරන්න බෑ.

---

## 2. Office එක AWS එකට connect කරන්නේ කොහොමද?

**කසුන්:** Internet එක තියෙනවා නේ. VPN එකක් ඇති. ලාභයි!

**නදී:** "**Buy cheap, buy twice.**" ඕන දේ අනුවයි.

| Service | සරලව | කවදද? |
| --- | --- | --- |
| **Site-to-Site VPN** | **Internet** හරහා **encrypted** tunnel එකක් | ඉක්මනින්, ලාභෙට |
| **Direct Connect** | **Private dedicated** line එකක් — internet එක **නෙවෙයි** | **Consistent** speed, data ගොඩක් |
| **Client VPN** | එක **laptop** එකක් VPC එකට | Work from home |

**කසුන්:** ඉතින් bank එකකට Direct Connect, පොඩි office එකකට VPN.

**නදී:** හරියටම. ගොඩක් අය Direct Connect එකට **backup** විදිහට VPN එකකුත් තියාගන්නවා.

**අනෙක්:**
- **VPC Peering** — VPCs **දෙකක්** connect
- **Transit Gateway** — VPCs **ගොඩක්** + on-prem → **central hub**

### DNS සහ Content Delivery

| Keyword | Service |
| --- | --- |
| **DNS**, domain names, routing, health checks | **Route 53** |
| **CDN**, content **cache** at edge | **CloudFront** |
| Static IPs, AWS network එකෙන් **වේගවත්** (cache නෑ) | **Global Accelerator** |
| **APIs** හදන්න | **API Gateway** |

---

## 3. Messaging — "Decouple"

**කසුන්:** "Decouple" කියන වචනය හැම තැනම.

**නදී:** Restaurant එකක්. Waiter order එක cook ට කෙලින්ම කියනවා. Cook busy නම් waiter ට බලාගෙන ඉන්න වෙනවා. ඒත් **order slips දාන rail** එකක් තිබ්බොත් — waiter දාලා යනවා, cook ඉඩ ලැබුණම ගන්නවා. ඒක තමයි **queue** එක. කොටස් දෙක එකිනෙකා නිසා හිරවෙන්නේ නෑ.

| Service | සරලව |
| --- | --- |
| **Amazon SQS** | **Queue** — තැපැල් පෙට්ටිය. Messages **pull** කරනවා. **Decouple** |
| **Amazon SNS** | **Notifications** — loudspeaker. හැමෝටම **push** (email, SMS) |
| **Amazon EventBridge** | **Events** අනුව services trigger කරනවා, schedules |

> **Exam:** "**send alerts / notifications** (email, SMS)" → **SNS**. "**decouple** / **queue**" → **SQS**.

---

## 4. Analytics — keyword එකෙන්

| Keyword | Service |
| --- | --- |
| **SQL** queries **directly on S3** | **Athena** |
| **Real-time streaming** data | **Kinesis** |
| **ETL** (data clean කරලා move) | **Glue** |
| **Dashboards**, BI, charts | **Quick Sight** (QuickSight) |
| **Data warehouse** | **Redshift** |
| **Big data** (Hadoop, Spark) | **EMR** |
| **Search**, log analytics | **OpenSearch Service** |

**කසුන්:** Athena සහ Redshift?

**නදී:** **Athena** — S3 file එකට **කෙලින්ම** ප්‍රශ්නයක්. Load කරන්න ඕන නෑ. **Redshift** — data **load** කරලා හැමදාම ලොකු analytics.

---

## 5. AI / Machine Learning

**කසුන්:** AI නිසා අපේ jobs නැති වෙයිද?

**නදී:** *(හිනාවෙලා)* AI එක්ක වැඩ කරන්න දන්න කෙනා, නොදන්න කෙනාගේ job එක ගනී. ඉතින් ඉගෙන ගමු!

| Keyword | Service |
| --- | --- |
| **Build, train, deploy** ඔයාගේම ML models | **SageMaker AI** |
| **Generative AI**, foundation models | **Bedrock** |
| GenAI **assistant** (code, business questions) | **Amazon Q** |
| **Chatbot** (voice / text) | **Lex** |
| **Text → Speech** | **Polly** |
| **Speech → Text** | **Transcribe** |
| **Translate** languages | **Translate** |
| **Images / video** — faces, objects | **Rekognition** |
| Text **sentiment**, meaning | **Comprehend** |
| Scanned **documents** → text | **Textract** |
| **Recommendations** | **Personalize** |
| **Enterprise search** | **Kendra** |

**කසුන්:** Polly සහ Transcribe ආයෙත් පටලැවෙනවා.

**නදී:** **Polly** = **ගිරවා** — **කතා කරනවා** (text → speech). **Transcribe** = **ලියන කෙනා** — **ලියනවා** (speech → text).

---

## 6. අනෙක් Services — කෙටියෙන්

| Category | Keyword | Service |
| --- | --- | --- |
| Developer | Code **build** සහ test | **CodeBuild** |
| Developer | **CI/CD pipeline** | **CodePipeline** |
| Developer | Deploy කරන්න | **CodeDeploy** |
| Developer | **Trace / debug** distributed apps | **X-Ray** |
| End-user | Cloud **virtual desktop** | **WorkSpaces** |
| End-user | Apps **stream** කරන්න browser එකට | **AppStream 2.0** |
| End-user | Secure web browsing | **WorkSpaces Secure Browser** |
| Business | **Call center** / contact center | **Amazon Connect** |
| Business | **Emails** යවන්න (marketing, bulk) | **Amazon SES** |
| Frontend | **Web & mobile apps** ඉක්මනින් | **Amplify** |
| IoT | **IoT devices** connect / manage | **IoT Core** |
| Management | EC2 **patching**, fleet manage | **Systems Manager** |

**කසුන්:** CodePipeline කියන්නේ factory එකක conveyor belt එක වගේ — build, test, deploy.

**නදී:** නියම උදාහරණය!

---

## Practice Questions (20)

**Q1.** Which VPC component allows resources in a public subnet to reach the internet?
A. NAT Gateway
B. Internet Gateway
C. Security group
D. VPC endpoint

**Q2.** Instances in a private subnet need to download software updates but must not accept inbound connections from the internet. What should be used?
A. Internet Gateway
B. NAT Gateway
C. AWS Direct Connect
D. Amazon Route 53

**Q3.** Which is a stateful firewall at the instance level?
A. Network ACL
B. Security group
C. AWS WAF
D. AWS Shield

**Q4.** A company wants to block traffic from one specific IP address to a subnet. What should it use?
A. Security group
B. Network ACL
C. IAM policy
D. Amazon Inspector

**Q5.** Which service gives a dedicated private network connection from on-premises to AWS that does not use the public internet?
A. AWS Site-to-Site VPN
B. AWS Direct Connect
C. Amazon CloudFront
D. AWS Client VPN

**Q6.** A company needs a quick, low-cost, encrypted connection from its office to AWS over the internet. Which service?
A. AWS Direct Connect
B. AWS Site-to-Site VPN
C. AWS Transit Gateway
D. Amazon Route 53

**Q7.** Which service is a DNS service?
A. Amazon CloudFront
B. Amazon Route 53
C. Amazon VPC
D. AWS Global Accelerator

**Q8.** Which service delivers website images and videos to users with low latency using edge locations?
A. Amazon CloudFront
B. Amazon S3 Glacier
C. AWS Direct Connect
D. Amazon EFS

**Q9.** A company wants to decouple two parts of an application with a message queue. Which service?
A. Amazon SNS
B. Amazon SQS
C. Amazon SES
D. Amazon Connect

**Q10.** Which service sends email and SMS notifications to many subscribers at once?
A. Amazon SQS
B. Amazon SNS
C. AWS Step Functions
D. Amazon Kinesis

**Q11.** Which service runs SQL queries directly on data in Amazon S3 without loading it?
A. Amazon Redshift
B. Amazon Athena
C. Amazon RDS
D. AWS Glue

**Q12.** Which service collects and processes real-time streaming data, like website clicks?
A. Amazon Kinesis
B. Amazon Athena
C. Amazon Quick Sight
D. AWS Glue

**Q13.** Which service creates business intelligence dashboards?
A. Amazon Quick Sight
B. Amazon EMR
C. AWS Glue
D. Amazon Kinesis

**Q14.** Which service helps data scientists build, train, and deploy machine learning models?
A. Amazon SageMaker AI
B. Amazon Polly
C. Amazon Lex
D. Amazon Rekognition

**Q15.** A company wants to add a chatbot to its website. Which service?
A. Amazon Lex
B. Amazon Polly
C. Amazon Textract
D. Amazon Translate

**Q16.** Which service converts customer call recordings into text?
A. Amazon Polly
B. Amazon Transcribe
C. Amazon Comprehend
D. Amazon Lex

**Q17.** Which service identifies objects and faces in images?
A. Amazon Rekognition
B. Amazon Comprehend
C. Amazon Kendra
D. Amazon Personalize

**Q18.** Which service provides virtual desktops for employees?
A. Amazon WorkSpaces
B. Amazon Connect
C. AWS Amplify
D. Amazon Lightsail

**Q19.** Which service creates a cloud-based contact center?
A. Amazon SES
B. Amazon Connect
C. Amazon SNS
D. Amazon Lex

**Q20.** Which service helps developers trace requests and find performance problems in distributed applications?
A. AWS X-Ray
B. AWS CodeBuild
C. AWS CloudTrail
D. AWS Config

### Extra (5)

**Q21.** Build GenAI apps with foundation models through an API? → A. SageMaker AI B. Bedrock C. Comprehend D. Kendra
**Q22.** Extract text and tables from scanned forms? → A. Textract B. Transcribe C. Translate D. Polly
**Q23.** Connect and manage millions of IoT devices? → A. IoT Core B. Amplify C. SNS D. Kinesis
**Q24.** Build and host a mobile/web frontend quickly? → A. AWS Amplify B. AppStream 2.0 C. CodeDeploy D. Lightsail
**Q25.** Automate build, test, and deploy as a CI/CD pipeline? → A. CodePipeline B. X-Ray C. CloudFormation D. Systems Manager

### Answers

- **Q1 — B.** ප්‍රධාන gate එක → **Internet Gateway**.
- **Q2 — B.** එළියට විතරයි → **NAT Gateway** (පිටිපස්සේ දොර).
- **Q3 — B.** Instance + stateful → **Security group**.
- **Q4 — B.** Deny / block IP → **Network ACL**.
- **Q5 — B.** Private, no internet → **Direct Connect**.
- **Q6 — B.** ඉක්මන්, ලාභ, internet → **Site-to-Site VPN**.
- **Q7 — B.** DNS → **Route 53**.
- **Q8 — A.** CDN → **CloudFront**.
- **Q9 — B.** Queue → **SQS**.
- **Q10 — B.** Notifications → **SNS**.
- **Q11 — B.** SQL on S3 → **Athena**.
- **Q12 — A.** Real-time streaming → **Kinesis**.
- **Q13 — A.** Dashboards → **Quick Sight**.
- **Q14 — A.** Build/train ML → **SageMaker AI**.
- **Q15 — A.** Chatbot → **Lex**.
- **Q16 — B.** Speech → text → **Transcribe** (ලියන කෙනා).
- **Q17 — A.** Images → **Rekognition**.
- **Q18 — A.** Virtual desktops → **WorkSpaces**.
- **Q19 — B.** Contact center → **Connect**.
- **Q20 — A.** Trace → **X-Ray**. (CloudTrail = who did what)
- **Q21 — B** Bedrock · **Q22 — A** Textract · **Q23 — A** IoT Core · **Q24 — A** Amplify · **Q25 — A** CodePipeline

---

## Closing

**කසුන්:** Services ගොඩක් ආවා, ඒත් keyword tables නිසා ලේසියි.

**නදී:** ඒක තමයි රහස. **Homework:** Console එකේ **default VPC** එක open කරලා subnets, route tables, Internet Gateway බලන්න. **Amazon Polly** එකේ ඔයාගේ නම type කරලා කියවන්න දෙන්න.

**කසුන්:** ඊළඟට — **Billing and Support**. සල්ලි!

**නදී:** ආයෙත් හමුවෙමු!
