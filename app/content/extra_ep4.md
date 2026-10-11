# Extra Practice — Episode 4 (50 Questions)

## Questions

**Q1.** What is an Amazon VPC?
A. A managed DNS service
B. A content delivery network
C. A logically isolated virtual network that you define in the AWS Cloud
D. A dedicated physical connection to AWS

**Q2.** A company wants its web servers reachable from the internet while its databases are not. How should it design the VPC?
A. Put web servers in a public subnet and databases in a private subnet
B. Put both in a public subnet and rely on IAM
C. Put both in a private subnet with an Internet Gateway attached to the database
D. Put web servers in another Region

**Q3.** Which statement about a subnet is TRUE?
A. A subnet spans multiple Regions
B. A subnet resides within a single Availability Zone
C. A subnet is a physical data center
D. A subnet can only hold databases

**Q4.** Which VPC component acts as the "back door" that lets private-subnet instances start outbound connections but blocks inbound connections from the internet?
A. Internet Gateway
B. Network ACL
C. NAT Gateway
D. Security group

**Q5.** An application in a VPC must access Amazon S3 without sending traffic over the public internet. What should the company create?
A. A Site-to-Site VPN
B. A VPC endpoint
C. An Amazon CloudFront distribution
D. A Route 53 hosted zone

**Q6.** Which statements about security groups are correct? (Select TWO)
A. They operate at the subnet level
B. They support only allow rules
C. They are stateful, so return traffic for an allowed request is automatically allowed
D. They process rules in numbered order and support deny rules
E. They are stateless

**Q7.** What does it mean that a network ACL is "stateless"?
A. Return traffic must be explicitly allowed by rules
B. It cannot be associated with a subnet
C. It only works with IPv6
D. It automatically allows all outbound responses

**Q8.** A company transfers several terabytes of data daily from its data center to AWS and needs consistent network performance. Which service is BEST?
A. AWS Site-to-Site VPN
B. AWS Client VPN
C. Amazon Route 53
D. AWS Direct Connect

**Q9.** A company needs an encrypted connection between its office router and its VPC that can be set up within hours over the internet. Which service?
A. AWS Site-to-Site VPN
B. AWS Direct Connect
C. AWS Transit Gateway
D. VPC peering

**Q10.** Remote employees working from home need to securely connect their individual laptops to resources in a VPC. Which service?
A. AWS Direct Connect
B. VPC peering
C. AWS Client VPN
D. Amazon CloudFront

**Q11.** Which are valid ways to connect an on-premises network to AWS? (Select TWO)
A. AWS Direct Connect
B. Amazon Kinesis
C. AWS Site-to-Site VPN
D. Amazon SES
E. Amazon Lex

**Q12.** A bank uses Direct Connect and wants a low-cost backup connection if the dedicated line fails. What is a common approach?
A. Add a Site-to-Site VPN as backup
B. Add Amazon CloudFront
C. Add AWS Glue
D. Add a NAT Gateway

**Q13.** A company wants to connect exactly two VPCs so resources can communicate privately. Which feature is the simplest fit?
A. AWS Direct Connect
B. VPC peering
C. Amazon API Gateway
D. AWS Client VPN

**Q14.** A company has 50 VPCs and an on-premises network and wants a central hub instead of many peering connections. Which service?
A. AWS Transit Gateway
B. Internet Gateway
C. VPC endpoint
D. Amazon Route 53

**Q15.** Which Route 53 routing capability sends each user to the AWS Region that gives the lowest network delay?
A. Weighted routing
B. Failover routing
C. Latency-based routing
D. Simple routing

**Q16.** Which service lets a company register a domain name and also manage its DNS records?
A. Amazon CloudFront
B. AWS Global Accelerator
C. Amazon API Gateway
D. Amazon Route 53

**Q17.** A company wants to cache static website content at edge locations close to viewers, with an Amazon S3 bucket as the origin. Which service?
A. Amazon CloudFront
B. AWS Direct Connect
C. Amazon EFS
D. AWS Global Accelerator

**Q18.** A gaming company wants static IP addresses as entry points and wants user traffic routed over the AWS global network to the nearest healthy endpoint, without caching content. Which service?
A. Amazon CloudFront
B. AWS Global Accelerator
C. Amazon Route 53 only
D. AWS Direct Connect

**Q19.** A company wants to create, publish, and monitor REST APIs that front its Lambda functions. Which service?
A. AWS Amplify
B. Amazon SQS
C. Amazon API Gateway
D. AWS X-Ray

**Q20.** In Amazon SQS, how do consumers receive messages?
A. SQS pushes messages to all consumers by email
B. SQS pushes messages to mobile devices
C. SQS routes messages by DNS
D. Consumers pull messages from the queue

**Q21.** An order-processing front end sometimes receives bursts of orders that overwhelm the back-end servers. Which service helps smooth the load by buffering orders?
A. Amazon SNS
B. Amazon Route 53
C. Amazon SQS
D. Amazon QuickSight

**Q22.** Which statements about Amazon SNS are correct? (Select TWO)
A. It uses a publish/subscribe model to push messages to subscribers
B. Subscribers must poll SNS to get messages
C. It can deliver messages to email, SMS, and HTTP endpoints
D. It is a data warehouse
E. It translates text between languages

**Q23.** A company wants to automatically invoke a Lambda function whenever an EC2 instance changes state. Which service routes this event?
A. Amazon EventBridge
B. Amazon SES
C. Amazon Kinesis Data Firehose only
D. AWS Direct Connect

**Q24.** A retailer must ingest and analyze clickstream data from its website in real time. Which service?
A. Amazon Redshift
B. Amazon Athena
C. Amazon Kinesis
D. AWS Glue

**Q25.** Which service is a serverless ETL service that discovers, prepares, and moves data between data stores?
A. AWS Glue
B. Amazon Athena
C. Amazon Redshift
D. Amazon EMR

**Q26.** A company needs a petabyte-scale data warehouse for complex analytics on structured data that it loads regularly. Which service?
A. Amazon Athena
B. Amazon Redshift
C. Amazon DynamoDB
D. Amazon ElastiCache

**Q27.** A company wants to run Apache Spark and Hadoop big data jobs without managing the cluster software installation manually. Which service?
A. AWS Glue DataBrew
B. Amazon Kendra
C. Amazon EMR
D. Amazon Lex

**Q28.** A company wants to search application logs and build a search box for its website with a managed service. Which service?
A. Amazon Athena
B. Amazon OpenSearch Service
C. Amazon Rekognition
D. AWS CodeDeploy

**Q29.** Business users need interactive dashboards and charts from data in many sources, using a serverless business intelligence (BI) service. Which service?
A. Amazon Quick Sight
B. Amazon Redshift
C. Amazon EMR
D. Amazon Kinesis

**Q30.** Which statements correctly compare Amazon Athena and Amazon Redshift? (Select TWO)
A. Athena queries data directly in S3 using SQL without loading it
B. Redshift is serverless-only and cannot hold data
C. Redshift is a data warehouse where data is loaded for repeated large-scale analytics
D. Athena requires you to provision a cluster of nodes
E. Athena is used to build chatbots

**Q31.** A data science team needs a fully managed service to build, train, and deploy its own machine learning models. Which service?
A. Amazon Comprehend
B. Amazon Polly
C. Amazon Personalize
D. Amazon SageMaker AI

**Q32.** A company wants to build generative AI applications by choosing from foundation models from multiple providers through one API. Which service?
A. Amazon Bedrock
B. Amazon SageMaker Ground Truth
C. Amazon Textract
D. Amazon Lex

**Q33.** Which service is a generative AI-powered assistant that can answer business questions and help developers write code?
A. Amazon Rekognition
B. Amazon Q
C. Amazon Kendra
D. Amazon Translate

**Q34.** A company builds a voice-and-text conversational interface for ordering food. Which service?
A. Amazon Polly
B. Amazon Transcribe
C. Amazon Lex
D. Amazon Comprehend

**Q35.** A company wants its app to read news articles aloud with lifelike voices. Which service?
A. Amazon Transcribe
B. Amazon Polly
C. Amazon Translate
D. Amazon Lex

**Q36.** A company wants automatic subtitles generated from the audio of recorded webinars. Which service?
A. Amazon Polly
B. Amazon Textract
C. Amazon Transcribe
D. Amazon Rekognition

**Q37.** A website must show product descriptions in Spanish, French, and Japanese from English text. Which service?
A. Amazon Translate
B. Amazon Polly
C. Amazon Comprehend
D. Amazon Kendra

**Q38.** A social media company wants to automatically detect inappropriate content in uploaded photos and videos. Which service?
A. Amazon Comprehend
B. Amazon Textract
C. Amazon Personalize
D. Amazon Rekognition

**Q39.** A company wants to extract printed text, forms, and tables from scanned invoices. Which service?
A. Amazon Textract
B. Amazon Rekognition
C. Amazon Transcribe
D. Amazon Polly

**Q40.** An online store wants to show "customers who bought this also bought" suggestions using the same technology as Amazon.com. Which service?
A. Amazon Kendra
B. Amazon Lex
C. Amazon Personalize
D. Amazon Comprehend

**Q41.** Employees want to ask natural-language questions and get answers from documents across internal repositories such as SharePoint and S3. Which service?
A. Amazon OpenSearch Service
B. Amazon Kendra
C. Amazon Athena
D. Amazon Textract

**Q42.** Which AI/ML services analyze or generate text and language? (Select TWO)
A. Amazon Comprehend
B. Amazon Translate
C. AWS Direct Connect
D. Amazon EBS
E. AWS Transit Gateway

**Q43.** Which service compiles source code, runs tests, and produces deployable software packages without managing build servers?
A. AWS CodeDeploy
B. AWS CodePipeline
C. AWS X-Ray
D. AWS CodeBuild

**Q44.** Which service automates deploying application updates to EC2 instances, Lambda functions, or on-premises servers?
A. AWS CodeDeploy
B. AWS CodeBuild
C. AWS Config
D. AWS CloudTrail

**Q45.** A team wants a release workflow that automatically moves code through source, build, test, and deploy stages. Which service orchestrates this?
A. AWS X-Ray
B. AWS CodeDeploy
C. AWS CodePipeline
D. AWS Systems Manager

**Q46.** Which service gives users a managed cloud desktop, while which other service streams a single desktop application to a web browser? (Choose the correct pair)
A. AppStream 2.0 for desktops; WorkSpaces for streaming apps
B. WorkSpaces for desktops; Amazon Connect for streaming apps
C. WorkSpaces for desktops; AppStream 2.0 for streaming apps
D. Lightsail for desktops; Amplify for streaming apps

**Q47.** A company wants employees to browse internal websites securely from a managed browser without installing software or exposing corporate data to local devices. Which service?
A. AWS Client VPN
B. Amazon WorkSpaces Secure Browser
C. Amazon CloudFront
D. AWS Shield

**Q48.** Which service lets a company send bulk marketing and transactional emails at scale?
A. Amazon SES
B. Amazon SQS
C. Amazon Connect
D. Amazon Lex

**Q49.** Which AWS service helps frontend web and mobile developers build, host, and deploy full-stack applications quickly?
A. AWS CodeCommit
B. Amazon Lightsail
C. AWS Amplify
D. AWS Elastic Beanstalk

**Q50.** Which services are used for IoT and for fleet operations such as patching and managing EC2 and on-premises servers? (Select TWO)
A. AWS IoT Core
B. AWS Systems Manager
C. Amazon Polly
D. Amazon Athena
E. Amazon Connect

### Answers

- **Q1 — C.** **VPC** = AWS ඇතුළේ ඔයාගේම logically isolated private network එක (වත්ත).
- **Q2 — A.** Web servers **public subnet**, databases **private subnet** — සාමාන්‍ය design එක.
- **Q3 — B.** **Subnet** එකක් තනි **Availability Zone** එකකට සීමා වෙනවා.
- **Q4 — C.** **NAT Gateway** = පිටිපස්සේ දොර — එළියට යන්න විතරයි, ඇතුළට එන්න බෑ.
- **Q5 — B.** **VPC endpoint** (gateway endpoint for S3) → internet නැතුව private access.
- **Q6 — B, C.** **Security group** = allow rules විතරයි සහ **stateful** (subnet level එක NACL).
- **Q7 — A.** **Stateless** = ආපසු එන traffic එකත් rules වලින් **explicitly allow** කරන්න ඕන.
- **Q8 — D.** Data ගොඩක් + **consistent** performance → **Direct Connect**.
- **Q9 — A.** ඉක්මනින් internet හරහා encrypted tunnel → **Site-to-Site VPN**.
- **Q10 — C.** තනි laptop එකක් VPC එකට → **Client VPN**.
- **Q11 — A, C.** On-premises ↔ AWS = **Direct Connect** සහ **Site-to-Site VPN**.
- **Q12 — A.** Direct Connect එකට ලාභ **backup** එකක් විදිහට **Site-to-Site VPN**.
- **Q13 — B.** VPCs **දෙකක්** → **VPC peering**.
- **Q14 — A.** VPCs ගොඩක් + on-prem → **Transit Gateway** (central hub).
- **Q15 — C.** අඩුම delay එකට → **Latency-based routing** (Route 53).
- **Q16 — D.** Domain register කිරීම සහ DNS → **Route 53**.
- **Q17 — A.** Edge locations වල **cache** කරන CDN → **CloudFront** (origin = S3).
- **Q18 — B.** Static IPs + AWS network එකෙන් වේගවත් + cache නෑ → **Global Accelerator**.
- **Q19 — C.** APIs හදන්න/publish කරන්න → **API Gateway**.
- **Q20 — D.** **SQS** එකේ consumers messages **pull** කරනවා (SNS තමයි push).
- **Q21 — C.** Burst load **buffer** කරන **queue** → **SQS** (decouple).
- **Q22 — A, C.** **SNS** = pub/sub, subscribers ට **push**; email, SMS, HTTP වලට යනවා.
- **Q23 — A.** Events අනුව services trigger කරන්නේ **EventBridge**.
- **Q24 — C.** Real-time streaming data → **Kinesis**.
- **Q25 — A.** **ETL** (data clean කරලා move) → **Glue**.
- **Q26 — B.** **Data warehouse**, data load කරලා ලොකු analytics → **Redshift**.
- **Q27 — C.** Hadoop / Spark **big data** → **EMR**.
- **Q28 — B.** **Search** සහ log analytics → **OpenSearch Service**.
- **Q29 — A.** **Dashboards**, BI, charts → **Quick Sight**.
- **Q30 — A, C.** **Athena** = S3 එකට කෙලින්ම SQL; **Redshift** = data load කරන warehouse.
- **Q31 — D.** ඔයාගේම ML models build, train, deploy → **SageMaker AI**.
- **Q32 — A.** **Foundation models** API එකකින් → **Bedrock** (generative AI).
- **Q33 — B.** GenAI **assistant** (business questions, code) → **Amazon Q**.
- **Q34 — C.** Voice/text **chatbot** → **Lex**.
- **Q35 — B.** Text → speech → **Polly** (ගිරවා කතා කරනවා).
- **Q36 — C.** Speech → text (subtitles) → **Transcribe** (ලියන කෙනා).
- **Q37 — A.** භාෂා **translate** කිරීම → **Translate**.
- **Q38 — D.** Images / video වල objects, faces, unsafe content → **Rekognition**.
- **Q39 — A.** Scanned documents, forms, tables → text → **Textract**.
- **Q40 — C.** **Recommendations** → **Personalize**.
- **Q41 — B.** **Enterprise search** (natural language, internal documents) → **Kendra**.
- **Q42 — A, B.** Text/language services → **Comprehend** (sentiment) සහ **Translate**.
- **Q43 — D.** Code **build** සහ test, packages → **CodeBuild**.
- **Q44 — A.** Deploy කරන්න (EC2, Lambda, on-prem) → **CodeDeploy**.
- **Q45 — C.** **CI/CD pipeline** orchestrate කරන conveyor belt එක → **CodePipeline**.
- **Q46 — C.** **WorkSpaces** = virtual desktop; **AppStream 2.0** = app එකක් browser එකට stream.
- **Q47 — B.** Secure web browsing → **WorkSpaces Secure Browser**.
- **Q48 — A.** Bulk / marketing **emails** → **SES**.
- **Q49 — C.** Web සහ mobile apps ඉක්මනින් → **Amplify**.
- **Q50 — A, B.** IoT devices → **IoT Core**; EC2 patching / fleet manage → **Systems Manager**.
