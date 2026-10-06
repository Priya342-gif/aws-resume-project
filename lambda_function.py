import json
import boto3

table = boto3.resource('dynamodb').Table('visitor-counter')

def lambda_handler(event, context):
    response = table.update_item(
        Key={'id': 'visits'},
        UpdateExpression='ADD #c :inc',
        ExpressionAttributeNames={'#c': 'count'},
        ExpressionAttributeValues={':inc': 1},
        ReturnValues='UPDATED_NEW'
    )

    count = int(response['Attributes']['count'])

    return {
        'statusCode': 200,
        'body': json.dumps({'count': count})
    }