# Extra Practice — Episode 3 (50 Questions)

## Questions

**Q1.** A developer wants to call Amazon S3 and Amazon DynamoDB directly from the code of a Python application. Which AWS access method should the developer use?
A. AWS Management Console
B. AWS CloudFormation
C. AWS SDK
D. AWS Elastic Beanstalk

**Q2.** A system administrator wants to automate daily AWS tasks by running commands from shell scripts. Which tool should the administrator use?
A. AWS CLI
B. AWS Management Console
C. AWS Artifact
D. Amazon Lightsail

**Q3.** A developer wants to upload application code and let AWS automatically handle capacity provisioning, load balancing, and Auto Scaling. Which service meets this requirement?
A. AWS CloudFormation
B. AWS Batch
C. Amazon Lightsail
D. AWS Elastic Beanstalk

**Q4.** Which are benefits of using AWS CloudFormation? (Select TWO)
A. Infrastructure can be created repeatedly and consistently from a template
B. It caches content at edge locations
C. It automatically encrypts all S3 objects
D. Infrastructure definitions can be stored in version control as code
E. It distributes traffic across EC2 instances

**Q5.** What is the minimum number of Availability Zones in an AWS Region (as described in the lesson)?
A. 1
B. 3
C. 6
D. 10

**Q6.** Which are valid reasons for a company to use multiple AWS Regions? (Select TWO)
A. To reduce the number of IAM users
B. To support disaster recovery and business continuity
C. To avoid paying for data transfer
D. To give users around the world lower latency
E. To get unlimited free storage

**Q7.** A company runs a video-rendering application and needs single-digit millisecond latency to end users in a large metropolitan area. Which AWS infrastructure option places compute and storage close to that population center?
A. AWS Outposts
B. Amazon CloudFront
C. AWS Local Zones
D. AWS Direct Connect

**Q8.** A mobile gaming company wants to run application code at the edge of a telecommunications provider's 5G network. Which AWS infrastructure offering should it use?
A. AWS Wavelength
B. AWS Local Zones
C. AWS Outposts
D. Amazon Route 53

**Q9.** Which pair of AWS services uses edge locations to serve users from a nearby location?
A. Amazon EBS and Amazon EFS
B. Amazon RDS and Amazon Aurora
C. AWS Lambda and AWS Fargate
D. Amazon CloudFront and Amazon Route 53

**Q10.** A company runs a web application on Amazon EC2. Which task is the customer's responsibility?
A. Patching the guest operating system
B. Maintaining the physical servers
C. Replacing failed data center hardware
D. Securing the data center buildings

**Q11.** A company runs a large in-memory database that needs a very high amount of RAM. Which EC2 instance family is MOST suitable?
A. Memory optimized (R, X)
B. Compute optimized (C)
C. Storage optimized (I, D)
D. General purpose (T, M)

**Q12.** A company wants to train machine learning models that need GPUs. Which EC2 instance category should it choose?
A. General purpose
B. Memory optimized
C. Accelerated computing
D. Storage optimized

**Q13.** Which statements about EC2 instance families are correct? (Select TWO)
A. Compute optimized instances are designed for CPU-intensive workloads
B. Memory optimized instances are designed for high disk I/O only
C. Accelerated computing instances never use GPUs
D. Memory optimized instances are designed for workloads that process large data sets in memory
E. General purpose instances cannot run web servers

**Q14.** A company needs a load balancer that routes HTTP and HTTPS traffic to different targets based on the URL path. Which load balancer should it use?
A. Network Load Balancer
B. Application Load Balancer
C. Gateway Load Balancer
D. Amazon Route 53

**Q15.** A company needs a load balancer that handles millions of TCP requests per second with very low latency. Which should it use?
A. Application Load Balancer
B. Amazon Route 53
C. Network Load Balancer
D. AWS Auto Scaling plans only

**Q16.** How does EC2 Auto Scaling help reduce costs?
A. It terminates instances that are no longer needed when demand drops
B. It moves data to cheaper S3 storage classes
C. It buys Reserved Instances automatically
D. It encrypts instance volumes

**Q17.** How is AWS Lambda charged?
A. A fixed monthly fee per function
B. Per hour for every provisioned server
C. Per GB of storage used by the code
D. Based on the number of requests and the duration of code execution

**Q18.** A batch job runs continuously for about 2 hours. Which service is MOST suitable, considering the Lambda execution time limit?
A. AWS Lambda
B. Amazon EC2
C. Amazon CloudFront
D. Amazon S3

**Q19.** A company wants to orchestrate Docker containers using an AWS-native service rather than Kubernetes. Which service should it choose?
A. Amazon EKS
B. AWS Lambda
C. Amazon ECS
D. Amazon ECR

**Q20.** Where can a company securely store, manage, and deploy Docker container images?
A. Amazon ECR
B. Amazon EBS
C. AWS Backup
D. Amazon Neptune

**Q21.** A company needs to run hundreds of thousands of batch computing jobs and wants AWS to provision the right amount of compute. Which service should it use?
A. Amazon Lightsail
B. AWS Elastic Beanstalk
C. Amazon Redshift
D. AWS Batch

**Q22.** A company runs a steady-state database server that will be needed for the next 3 years. Which EC2 purchasing option gives a significant discount for this commitment?
A. Spot Instances
B. Reserved Instances
C. On-Demand Instances
D. Dedicated Hosts only

**Q23.** A company must use its existing per-socket server software licenses on AWS and needs visibility of physical sockets and cores. Which EC2 option fits?
A. On-Demand Instances
B. Spot Instances
C. Dedicated Hosts
D. Lambda

**Q24.** Which workloads are suitable for Amazon EC2 Spot Instances? (Select TWO)
A. A critical production database that must never be interrupted
B. Fault-tolerant batch processing jobs
C. A single-instance license server
D. A workload that cannot tolerate any interruption
E. Stateless, flexible data analysis jobs

**Q25.** What is an Amazon Machine Image (AMI)?
A. A tool that monitors CPU usage
B. A network firewall for instances
C. A load balancer for containers
D. A template that contains the operating system and software used to launch EC2 instances

**Q26.** A company needs a petabyte-scale data warehouse to run complex analytic queries on structured data. Which service should it use?
A. Amazon Redshift
B. Amazon DynamoDB
C. Amazon ElastiCache
D. Amazon Neptune

**Q27.** A company wants to protect S3 objects from accidental deletion and overwrites by keeping multiple versions. What should it enable?
A. S3 Transfer Acceleration
B. AWS Shield
C. Amazon Macie
D. S3 Versioning

**Q28.** A company wants to automatically copy S3 objects to a bucket in another Region for disaster recovery. Which S3 feature should it use?
A. S3 Select
B. S3 Cross-Region Replication
C. S3 Object Lock only
D. S3 Glacier Deep Archive

**Q29.** Which statements about Amazon EBS are correct? (Select TWO)
A. EBS volumes persist independently of the life of an EC2 instance
B. EBS is object storage accessed over a URL
C. An EBS volume is created in a specific Availability Zone and attaches to instances in that same AZ
D. EBS volumes can be shared by thousands of Linux instances as a file system
E. EBS data is lost whenever the instance is stopped

**Q30.** A company needs to move the data of an EBS volume to an EC2 instance in a different Availability Zone. What should it do?
A. Create a snapshot and create a new volume from it in the other AZ
B. Attach the volume directly to the instance in the other AZ
C. Convert the volume to S3
D. Enable Multi-AZ on the volume

**Q31.** Which is the BEST use of an EC2 instance store?
A. Long-term archival of financial records
B. Storing a database that must survive instance termination
C. Temporary data such as buffers, caches, and scratch data
D. A shared drive for many instances

**Q32.** A company migrates a Windows-based application that needs a fully managed file share using the SMB protocol and Active Directory integration. Which service should it use?
A. Amazon EFS
B. Amazon FSx for Windows File Server
C. Amazon S3
D. Amazon EBS

**Q33.** A company runs high-performance computing (HPC) and machine learning workloads that need a fast parallel file system. Which service is MOST suitable?
A. Amazon EFS
B. AWS Storage Gateway
C. Amazon S3 Glacier
D. Amazon FSx for Lustre

**Q34.** On-premises applications need to use cloud storage while keeping frequently used data cached locally. Which service provides this hybrid storage?
A. AWS Storage Gateway
B. Amazon EBS
C. AWS Snowball
D. Amazon Redshift

**Q35.** A company wants to centrally manage and automate backups for EC2, EBS, RDS, DynamoDB, and EFS from one place. Which service should it use?
A. AWS CloudTrail
B. AWS Backup
C. AWS Config
D. Amazon Inspector

**Q36.** A company has petabytes of data in its data center and a slow internet connection. It wants to transfer the data to AWS physically. Which service should it use?
A. AWS DataSync
B. Amazon CloudFront
C. AWS Snowball Edge
D. AWS Direct Connect only

**Q37.** A company wants to automate and speed up online transfer of data between an on-premises NFS file server and Amazon S3 or EFS. Which service should it use?
A. AWS DataSync
B. AWS Snowball Edge
C. Amazon Kinesis
D. AWS CloudFormation

**Q38.** A company archives data it accesses once or twice a year. Retrieval can take minutes to hours, and the company wants low cost. Which S3 storage class fits?
A. S3 Standard
B. S3 Glacier Flexible Retrieval
C. S3 Intelligent-Tiering
D. S3 One Zone-IA

**Q39.** A company stores data that is accessed infrequently but must be available quickly when needed, and it requires data to be stored across multiple Availability Zones. Which S3 storage class fits?
A. S3 Glacier Deep Archive
B. S3 One Zone-IA
C. S3 Glacier Flexible Retrieval
D. S3 Standard-IA

**Q40.** Which database engines are supported by Amazon RDS? (Select TWO)
A. Microsoft SQL Server
B. MongoDB
C. Oracle
D. Apache Cassandra
E. Amazon Neptune

**Q41.** Reporting queries are slowing down a production Amazon RDS database. The company wants to offload the read traffic. What should it use?
A. RDS Multi-AZ standby
B. AWS Backup
C. RDS Read Replicas
D. Amazon S3

**Q42.** Which is a feature of Amazon Aurora?
A. It supports only Oracle
B. It is a NoSQL database
C. It can only run on-premises
D. It is MySQL and PostgreSQL compatible and offers higher performance than standard engines

**Q43.** A company needs a database to store highly connected data, such as relationships in a social network or fraud detection. Which service is BEST?
A. Amazon Neptune
B. Amazon RDS
C. Amazon Redshift
D. Amazon Timestream

**Q44.** A company already uses DynamoDB and needs a fully managed in-memory cache that gives microsecond response times for reads. Which should it use?
A. Amazon RDS Read Replicas
B. DynamoDB Accelerator (DAX)
C. Amazon Redshift
D. AWS DMS

**Q45.** A web application repeatedly runs the same expensive database queries, and the company wants to reduce database load by caching results in memory. Which service should it use?
A. AWS Backup
B. Amazon Neptune
C. Amazon ElastiCache
D. AWS SCT

**Q46.** A company collects billions of IoT sensor readings and needs a purpose-built database for time-series data. Which service should it use?
A. Amazon DocumentDB
B. Amazon RDS
C. Amazon Keyspaces
D. Amazon Timestream

**Q47.** A company runs Apache Cassandra workloads and wants a serverless, managed, Cassandra-compatible database. Which service should it use?
A. Amazon Keyspaces
B. Amazon DocumentDB
C. Amazon Neptune
D. Amazon Redshift

**Q48.** A company has a MongoDB application and wants a managed database that is compatible with MongoDB. Which service should it use?
A. Amazon Keyspaces
B. Amazon DocumentDB
C. Amazon DynamoDB
D. Amazon ElastiCache

**Q49.** Which are reasons to choose Amazon RDS instead of installing a database on Amazon EC2? (Select TWO)
A. The company needs full control of the underlying operating system
B. The company wants AWS to handle patching and automated backups
C. The company wants to install custom OS-level agents
D. The company wants to reduce operational overhead and get easy Multi-AZ failover
E. The company wants to manage the database hardware itself

**Q50.** A company is moving an on-premises Oracle database to Amazon Aurora PostgreSQL. Which services does it need? (Select TWO)
A. AWS SCT, to convert the schema to the new engine
B. Amazon CloudFront, to cache the database
C. AWS DMS, to migrate the data with minimal downtime
D. AWS Shield, to protect the database
E. Amazon Macie, to convert the schema

### Answers

- **Q1 — C.** Code එකෙන් AWS call කරන්න → **SDK** (Python, Java...).
- **Q2 — A.** Command line / scripts → **AWS CLI**.
- **Q3 — D.** Code දුන්නම servers, load balancer, scaling AWS බලාගන්නවා → **Elastic Beanstalk**.
- **Q4 — A, D.** CloudFormation = **Infrastructure as Code**, template එකෙන් repeatable + version control කරන්න පුළුවන්.
- **Q5 — B.** Region එකක අවම **AZ 3**ක් තියෙනවා.
- **Q6 — B, D.** Multiple Regions → **Disaster recovery** සහ ලෝකය පුරා users ට **low latency**.
- **Q7 — C.** ලොකු නගරයකට ළඟින් ඉතා low latency → **Local Zones**.
- **Q8 — A.** 5G network ඇතුළේ → **Wavelength**.
- **Q9 — D.** **CloudFront** සහ **Route 53** කියන්නේ **Edge locations** පාවිච්චි කරන services.
- **Q10 — A.** EC2 = **IaaS**, guest **OS patching** customer ගේ වැඩක්; hardware AWS ගේ.
- **Q11 — A.** In-memory database / RAM වැඩිපුර → **Memory optimized** (**R**AM).
- **Q12 — C.** ML + GPU → **Accelerated computing** (P, G).
- **Q13 — A, D.** Compute optimized = **CPU**, Memory optimized = **RAM** (large in-memory data sets).
- **Q14 — B.** HTTP/HTTPS, URL path routing (layer 7) → **ALB**.
- **Q15 — C.** TCP/UDP, ඉතා වේගවත් (layer 4) → **NLB**.
- **Q16 — A.** Demand අඩු වුණාම අනවශ්‍ය instances **terminate** කරලා cost අඩු කරනවා (**Elasticity**).
- **Q17 — D.** Lambda = **requests ගණන + run වුණ කාලය** අනුව ගෙවනවා.
- **Q18 — B.** Lambda limit **15 minutes**, ඒ නිසා පැය 2ක job එකට **EC2** (හෝ Fargate).
- **Q19 — C.** AWS ගේම container orchestration → **ECS** (Kubernetes → EKS).
- **Q20 — A.** Container **images** store කරන්නේ **ECR** එකේ.
- **Q21 — D.** Batch jobs ගොඩක් → **AWS Batch**.
- **Q22 — B.** අවුරුදු 1-3 steady usage commit කළොත් **Reserved Instances** වලින් ලොකු discount.
- **Q23 — C.** Per-socket/core license + physical server visibility → **Dedicated Hosts**.
- **Q24 — B, E.** **Spot** = interrupt වෙන්න පුළුවන්, ඒ නිසා fault-tolerant / flexible batch jobs වලට හොඳයි.
- **Q25 — D.** **AMI** = OS + software අඩංගු template එකක්, EC2 launch කරන්න.
- **Q26 — A.** Data warehouse + complex analytics → **Redshift**.
- **Q27 — D.** වැරදීමෙන් delete/overwrite වලින් බේරෙන්න → **S3 Versioning**.
- **Q28 — B.** වෙන Region එකකට objects copy කරන්න → **Cross-Region Replication**.
- **Q29 — A, C.** **EBS** instance එකෙන් වෙනම persist වෙනවා, volume එක **එකම AZ** එකකට සීමිතයි (EBS = **block**, file share එකක් නෙවෙයි; stop කළාට data නැති වෙන්නේ නෑ).
- **Q30 — A.** EBS **එකම AZ** එකකට සීමිතයි, ඒ නිසා **snapshot** → අලුත් volume.
- **Q31 — C.** **Instance store** = temporary; buffers, caches, scratch data වලට.
- **Q32 — B.** Windows file server, **SMB** + AD → **FSx for Windows File Server**.
- **Q33 — D.** HPC / ML parallel file system → **FSx for Lustre**.
- **Q34 — A.** On-prem + cloud storage + local cache → **Storage Gateway**.
- **Q35 — B.** Services ගොඩකට **central** backup → **AWS Backup**.
- **Q36 — C.** Petabytes + offline physical transfer → **Snowball Edge** (Snow Family).
- **Q37 — A.** Online data transfer automate කරන්න → **DataSync**.
- **Q38 — B.** Archive, **minutes-hours** retrieval → **Glacier Flexible Retrieval**.
- **Q39 — D.** කලාතුරකින් ඒත් ඉක්මනින් ඕන, multi-AZ → **Standard-IA** (One Zone-IA නම් එක AZ එකයි).
- **Q40 — A, C.** RDS engines: MySQL, PostgreSQL, MariaDB, **Oracle**, **SQL Server** (MongoDB/Cassandra නෑ).
- **Q41 — C.** Read performance වැඩි කරන්න → **Read Replicas** (Multi-AZ = availability).
- **Q42 — D.** **Aurora** = AWS ගේ MySQL/PostgreSQL compatible, වේගවත් relational DB.
- **Q43 — A.** Highly connected data, social networks → **Neptune** (graph).
- **Q44 — B.** DynamoDB සඳහා in-memory cache (microseconds) → **DAX**.
- **Q45 — C.** DB queries cache කරන්න, in-memory (Redis/Memcached) → **ElastiCache**.
- **Q46 — D.** IoT time-series data → **Timestream**.
- **Q47 — A.** Cassandra compatible → **Keyspaces**.
- **Q48 — B.** MongoDB compatible → **DocumentDB**.
- **Q49 — B, D.** **RDS** = patching, backups, failover AWS බලාගන්නවා (**reduce operational overhead**); OS full control ඕන නම් EC2.
- **Q50 — A, C.** Engine වෙනස් නිසා **SCT** schema convert කරනවා, **DMS** data migrate කරනවා.
