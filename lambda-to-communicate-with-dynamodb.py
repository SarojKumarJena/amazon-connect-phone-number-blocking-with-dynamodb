import json
import boto3
from botocore.exceptions import ClientError
import re

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BlockedPhoneNumbers')

def normalize_phone_number(phone_number):
    """
    Normalize phone number to E.164 format
    """
    # Remove all non-digit characters
    cleaned = re.sub(r'\D', '', phone_number)
    
    # If number starts with 0 (for local numbers) or doesn't have country code
    # Adjust based on your country code
    if cleaned.startswith('0'):
        cleaned = '91' + cleaned[1:]  # Replace with your country code
    elif len(cleaned) == 10:
        cleaned = '91' + cleaned  # Add country code for 10-digit numbers
    
    return '+' + cleaned

def lambda_handler(event, context):
    """
    Check if a phone number is blocked in DynamoDB
    """
    print("Received event: " + json.dumps(event))
    
    try:
        # Extract phone number from Amazon Connect event
        if 'Details' in event and 'ContactData' in event['Details']:
            customer_number = event['Details']['ContactData']['CustomerEndpoint']['Address']
        else:
            customer_number = event.get('phoneNumber', '')
        
        if not customer_number:
            return {
                'statusCode': 400,
                'isBlocked': False,
                'error': 'No phone number provided'
            }
        
        # Normalize phone number
        normalized_number = normalize_phone_number(customer_number)
        print(f"Checking number: {normalized_number}")
        
        # Check DynamoDB for blocked number
        response = table.get_item(
            Key={
                'phoneNumber': normalized_number
            }
        )
        
        # If item exists, number is blocked
        if 'Item' in response:
            blocked_info = response['Item']
            return {
                'statusCode': 200,
                'isBlocked': True,
                'phoneNumber': normalized_number,
                'blockedReason': blocked_info.get('blockedReason', 'Not specified'),
                'blockedDate': blocked_info.get('blockedDate', 'Unknown'),
                'message': f'Number {normalized_number} is blocked'
            }
        else:
            return {
                'statusCode': 200,
                'isBlocked': False,
                'phoneNumber': normalized_number,
                'message': f'Number {normalized_number} is not blocked'
            }
            
    except ClientError as e:
        print(f"DynamoDB error: {str(e)}")
        return {
            'statusCode': 500,
            'isBlocked': False,
            'error': f'DynamoDB error: {str(e)}'
        }
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'isBlocked': False,
            'error': f'Unexpected error: {str(e)}'
        }
