# Amazon-connect-phone-number-blocking-with-dynamodb
This solution allows you to maintain a blocklist of phone numbers in DynamoDB and automatically reject calls from blocked numbers at the Amazon Connect contact flow level. When a call comes in, Lambda checks the caller's number against DynamoDB and determines whether to allow or block the call.
