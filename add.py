import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentdb')

# Define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    id = event['id']
    name = event['name']
    gender = event['gender']
    
    # Write student data to the DynamoDB table and save the response in a variable
    response = table.put_item(
        Item={
            'id': id,
            'name': name,
            'gender': gender
        }
    )
    
    # Return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps('Student data saved successfully!')
    }