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

✔️ **Add a Phone number to Test**: Add a phone number in the table **phoneNumber** section.

<br/>

**Step 2: Deploy Lambda Function**

Create Lambda Function:

✔️ Runtime: Python 3.9 or later

✔️ Use the provided Lambda code from <a href="https://github.com/SarojKumarJena/amazon-connect-phone-number-blocking-with-dynamodb/blob/main/lambda-to-communicate-with-dynamodb.py"> lambda-to-communicate-with-dynamodb.py </a>

✔️ Deploy the Lambda

✔️ Go to **Configuration** tab in lambda, select **Permission** and select the lambda role.

✔️ Under the **Permission Policy** , Select **Add permissions** and add the **AmazonDynamoDBReadOnlyAccess** policy.

✔️ Test the lambda function with this event:

    {
      "phoneNumber": "+1234567890"
    }

<br/>

**Step 3: Configure Amazon Connect**

**In your AWS Console, Go for your Amazon Connect instance:**

✔️ Navigate to your instance → Flows

✔️ Add Your Lambda Function

<br/>

You can direct download the <a href="https://github.com/SarojKumarJena/amazon-connect-phone-number-blocking-with-dynamodb/blob/main/contact-flow-with-reporting-attributes.json">contact-flow-with-reporting-attributes.json</a> and import it inside your contact flow or can follow the basic steps to configure your contact flow.

<br/>

**In your Amazon Connect instance:**

✔️ Navigate to Routing → Contact flows

✔️ Create or edit a contact flow

<br/>

**Add Lambda Invocation:**

✔️ Use the "Invoke AWS Lambda Function" block

✔️ Select your Lambda function

✔️ Set timeout to 8 seconds

<br/>

**Configure call handling:**

✔️ Check if External.isBlocked equals true

    For blocked calls: Play message and disconnect

    For allowed calls: Continue normal flow

<br/>

**Testing**

➡️ Add a test number to DynamoDB

➡️ Call your Amazon Connect number from the test number

➡️ Verify the call is blocked with your configured message

➡️ Check CloudWatch logs for debugging information

<br/>

**Monitoring**

➡️ **CloudWatch Logs**: Lambda execution logs

➡️ **DynamoDB Metrics**: Table read/write capacity

➡️ **Connect Metrics**: Call volume and block statistics

<br/>

**Troubleshooting**

Lambda timeout	➡️ Increase timeout to 8+ seconds

DynamoDB errors	➡️ Verify table exists and IAM permissions

Number not blocked	➡️ Check phone number normalization

Connect integration error	➡️ Verify Lambda ARN and region


<br/>

🤝 **Contributing**

Contributions welcome! Please feel free to submit issues and enhancement requests.

<br/>

📄 **License**

MIT License - feel free to use this solution in your projects!


