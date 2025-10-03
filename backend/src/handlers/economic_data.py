import json
import boto3
import os
from datetime import datetime, timedelta

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['ECONOMIC_DATA_TABLE'])

def lambda_handler(event, context):
    try:
        # Get query parameters
        query_params = event.get('queryStringParameters', {}) or {}
        indicator = query_params.get('indicator')
        start_date = query_params.get('startDate')
        end_date = query_params.get('endDate')
        
        # Build query parameters
        query_params = {
            'IndexName': 'indicator-timestamp-index',
        }
        
        if indicator:
            query_params['KeyConditionExpression'] = 'indicator = :indicator'
            query_params['ExpressionAttributeValues'] = {':indicator': indicator}
            
            if start_date and end_date:
                query_params['KeyConditionExpression'] += ' AND timestamp BETWEEN :start AND :end'
                query_params['ExpressionAttributeValues'].update({
                    ':start': start_date,
                    ':end': end_date
                })
        
        # Query DynamoDB
        response = table.query(**query_params)
        items = response['Items']
        
        # Process and format the data
        formatted_data = [{
            'date': item['timestamp'],
            'indicator': item['indicator'],
            'value': item['value']
        } for item in items]
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps(formatted_data)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({
                'error': str(e)
            })
        }