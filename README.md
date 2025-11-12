# Amazon-connect-phone-number-blocking-with-dynamodb
This solution allows you to maintain a blocklist of phone numbers in DynamoDB and automatically reject calls from blocked numbers at the Amazon Connect contact flow level. When a call comes in, Lambda checks the caller's number against DynamoDB and determines whether to allow or block the call.

**Architecture**

  ✅ **Amazon Connect**: Handles incoming calls and contact flows
  
  ✅ **AWS Lambda**: Python function to check if number is blocked
  
  ✅ **DynamoDB**: Stores blocked phone numbers with metadata
  
  ✅ **CloudWatch**: Logging and monitoring
  


**Features**

  ✅ Real-time phone number blocking
  
  ✅ E.164 phone number normalization
  
  ✅ Simple admin functions to add/remove numbers
  
  ✅ Scalable serverless architecture
  
  ✅ Easy integration with existing contact flows
  
  ✅ Comprehensive error handling
  

**Quick Start**

✅ **Create DynamoDB Table** - Store blocked numbers

✅ **Deploy Lambda Function** - Check number against blocklist

✅ **Configure Amazon Connect** - Integrate with contact flow

✅ **Manage Blocklist** - Add/remove numbers as needed


**Use Cases**

✅ Block spam callers

✅ Prevent harassment calls

✅ Restrict calls from specific regions

✅ Temporary number blocking

✅ Compliance and regulatory requirements

**Technologies**

✅ AWS Lambda (Python 3.9+)

✅ Amazon DynamoDB

✅ Amazon Connect

✅ AWS IAM

✅ Amazon CloudWatch

📄 **License**

MIT License - feel free to use this solution in your projects!
