# 🚀 AWS Serverless Resume Website

A serverless resume website built using AWS services. The website displays my resume and includes a dynamic visitor counter powered by AWS Lambda, API Gateway, and DynamoDB.

## 🌐 Project Overview

This project demonstrates how to build a simple serverless resume website using AWS cloud services.

The frontend is built using HTML, CSS and JavaScript, while the visitor counter is implemented using AWS Lambda, API Gateway and DynamoDB.

## 🏗️ Architecture

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Amazon S3     │
                    │  Resume Website │
                    └────────┬────────┘
                             │
                       GET /visits
                             │
                             ▼
                    ┌─────────────────┐
                    │  API Gateway    │
                    │   HTTP API      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  AWS Lambda     │
                    │ Visitor Counter │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   DynamoDB      │
                    │ visitor-counter │
                    └─────────────────┘

☁️ AWS Services Used
- Amazon S3 – Stores the resume website files
- Amazon API Gateway – Provides the visitor counter API
- AWS Lambda – Processes visitor counter requests
- Amazon DynamoDB – Stores the visitor count
- AWS IAM – Provides secure permissions to Lambda
- Amazon CloudFront – Planned for CDN and HTTPS deployment
CloudFront creation was pending AWS account verification during development.

⚙️ Features
- Responsive personal resume website
- Serverless visitor counter
- Dynamic visitor count
- API-based backend
- DynamoDB-based persistent counter
- AWS Lambda backend
- IAM least-privilege permissions
- No traditional server required
- Cloud-based serverless architecture
🔄 Visitor Counter Workflow
1. User opens the resume website.
2. JavaScript sends a GET /visits request to API Gateway.
3. API Gateway invokes the Lambda function.
4. Lambda updates the visitor count in DynamoDB.
5. DynamoDB returns the updated count.
6. Lambda sends the count back through API Gateway.
7. JavaScript displays the visitor count on the website.
🔐 IAM Security
The Lambda function uses a least-privilege IAM policy.
The Lambda function is given permission to update only the required DynamoDB table.
Permission used:
dynamodb:UpdateItem

Resource:
visitor-counter

🧪 Testing
The project was tested at multiple levels:
Lambda Testing
The Lambda function was tested using the AWS Lambda Test feature and successfully updated the visitor count.
API Testing
The API Gateway endpoint was tested using the browser and returned the visitor count successfully.
Website Testing
The website was tested locally using VS Code Live Server.
The visitor counter successfully displayed the value returned by the AWS backend.
📁 Project Structure
aws-resume-project/
│
├── index.html
├── lambda_function.py
├── README.md
│
└── screenshots/
    ├── s3-bucket.png
    ├── dynamodb-table.png
    ├── lambda-function.png
    ├── api-gateway.png
    ├── website.png
    └── visitor-counter.png

💻 Technologies Used
Frontend
- HTML
- CSS
- JavaScript
Backend
- Python
- AWS Lambda
- Amazon API Gateway
Database
- Amazon DynamoDB
Cloud & Security
- Amazon S3
- AWS IAM
- Amazon CloudFront
Development Tools
- VS Code
- Git
- GitHub
📸 Screenshots
Amazon S3
<img width="572" height="410" alt="image" src="https://github.com/user-attachments/assets/5bbaeb47-336b-4ebb-8663-970afe3e82ba" />

 
DynamoDB
<img width="750" height="675" alt="image" src="https://github.com/user-attachments/assets/786b89dc-7c70-4d0c-8c09-4d122901ed28" />

 
AWS Lambda
<img width="737" height="706" alt="image" src="https://github.com/user-attachments/assets/1d9effc3-e1e8-45f4-832c-63ba8835f902" />

 
API Gateway
<img width="478" height="382" alt="image" src="https://github.com/user-attachments/assets/ce01422e-ad5c-490b-9d01-335976617735" />

 
Resume Website
<img width="1535" height="783" alt="image" src="https://github.com/user-attachments/assets/e9478d9c-8d1c-4518-a21f-04dcf426cd2c" />

<img width="1535" height="813" alt="image" src="https://github.com/user-attachments/assets/038f2519-c0cd-4a47-954b-3ce643680074" />

<img width="1526" height="762" alt="image" src="https://github.com/user-attachments/assets/7a35ef6d-66ba-4e2f-acb2-1af494f360ea" />

<img width="1507" height="713" alt="image" src="https://github.com/user-attachments/assets/5f0945a5-02ec-4ca4-9e6b-54a10a2f757d" />




 
Visitor Counter

<img width="1507" height="713" alt="image" src="https://github.com/user-attachments/assets/aa381094-eebe-442c-9d68-37d129756fe9" />


<img width="697" height="182" alt="image" src="https://github.com/user-attachments/assets/608faca7-60e3-4e4a-8ef7-0cdd83a62e5e" />



 
🎥 Project Demo
A short demonstration video showing the working serverless resume website can be added here.
Demo Video: Add YouTube/Google Drive link here
🚀 Deployment Steps
1. Create S3 Bucket
Create an S3 bucket and upload the index.html file.
2. Create DynamoDB Table
Create a DynamoDB table named:
visitor-counter

Partition key:
id

Create the visitor counter item:
id     = visits
count  = 0

3. Create Lambda Function
Create a Python Lambda function named:
visitor-counter-function

The Lambda function updates the visitor count in DynamoDB.
4. Configure IAM
Attach the required DynamoDB permission to the Lambda execution role.
5. Create API Gateway
Create an HTTP API with:
GET /visits

Connect the route to the Lambda function.
6. Connect Frontend
The website uses JavaScript to call the API Gateway endpoint and display the visitor count.
📊 Result
The final project provides a serverless resume website with a working dynamic visitor counter.
Website
   ↓
API Gateway
   ↓
Lambda
   ↓
DynamoDB
   ↓
Updated Visitor Count
   ↓
Website

🔒 Security & Cost Considerations
- S3 bucket access was kept private.
- IAM permissions were kept limited to the required DynamoDB operation.
- AWS WAF was not enabled to avoid unnecessary charges.
- Auto Scaling was not enabled for DynamoDB.
- Additional paid services were avoided where possible.
- AWS resources can be deleted after project demonstration to avoid ongoing charges.
AWS pricing and free-tier eligibility may vary. The project was designed to minimize unnecessary AWS usage.

👩‍💻 Author
Priya Chauhan
B.Tech CSE (AI & ML)
KIET Group of Institutions
GitHub: https://github.com/Priya342-gif
⭐ Project Highlights
- Built a serverless cloud application using AWS
- Implemented a dynamic visitor counter
- Used Lambda for serverless backend processing
- Used DynamoDB for persistent data storage
- Used API Gateway for API integration
- Applied IAM least-privilege security
- Managed project source code using Git and GitHub
