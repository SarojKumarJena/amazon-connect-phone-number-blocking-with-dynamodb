# Amazon-connect-phone-number-blocking-with-dynamodb
This solution allows you to maintain a blocklist of phone numbers in DynamoDB and automatically reject calls from blocked numbers at the Amazon Connect contact flow level. When a call comes in, Lambda checks the caller's number against DynamoDB and determines whether to allow or block the call.

<br/>

**Architecture**

  ✅ **Amazon Connect**: Handles incoming calls and contact flows
  
  ✅ **AWS Lambda**: Python function to check if number is blocked
  
  ✅ **DynamoDB**: Stores blocked phone numbers with metadata
  
  ✅ **CloudWatch**: Logging and monitoring
  
<br/>

**Features**

  ✅ Real-time phone number blocking
  
  ✅ E.164 phone number normalization
  
  ✅ Simple admin functions to add/remove numbers
  
  ✅ Scalable serverless architecture
  
  ✅ Easy integration with existing contact flows
  
  ✅ Comprehensive error handling
  
<br/>

**Quick Start**

✅ **Create DynamoDB Table** - Store blocked numbers

✅ **Deploy Lambda Function** - Check number against blocklist

✅ **Configure Amazon Connect** - Integrate with contact flow

✅ **Manage Blocklist** - Add/remove numbers as needed

<br/>

**Use Cases**

✅ Block spam callers

✅ Prevent harassment calls

✅ Restrict calls from specific regions

✅ Temporary number blocking

✅ Compliance and regulatory requirements

<br/>

**Technologies**

✅ AWS Lambda (Python 3.9+)

✅ Amazon DynamoDB

✅ Amazon Connect

✅ AWS IAM

✅ Amazon CloudWatch

<br/>

📄 **License**

MIT License - feel free to use this solution in your projects!

<br/>

🚀 **Implementation Steps**

**Prerequisites**

➡️ AWS Account with appropriate permissions

➡️ Amazon Connect instance setup

➡️ Basic knowledge of AWS services

<br/>

**Step 1: Create DynamoDB Table**

Create a DynamoDB table named **BlockedPhoneNumbers** with:

  ✔️ **Partition Key**: ***phoneNumber*** (String)

  ✔️ **Capacity Mode**: On-demand/Provisioned

<br/>

✔️ **Required IAM Permissions**: (Your account should have below permissions to create/update/delete the DynamoDB Table)

    { 
        "dynamodb:GetItem",
        "dynamodb:PutItem", 
        "dynamodb:DeleteItem",
        "dynamodb:DescribeTable"
    }

<br/>

**Step 2: Deploy Lambda Function**

Create Lambda Function:

✔️ Runtime: Python 3.9 or later

✔️ Execution role with DynamoDB and CloudWatch permissions

✔️ Use the provided Lambda code from <a href="https://github.com/SarojKumarJena/amazon-connect-phone-number-blocking-with-dynamodb/blob/main/lambda-to-communicate-with-dynamodb.py"> here </a>











