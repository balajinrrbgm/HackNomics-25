import json
import boto3
import os
from datetime import datetime

quicksight = boto3.client('quicksight')

def lambda_handler(event, context):
    try:
        # Get dashboard ID from environment variable
        dashboard_id = os.environ['QUICKSIGHT_DASHBOARD_ID']
        aws_account_id = os.environ['AWS_ACCOUNT_ID']
        
        # Get QuickSight embed URL
        response = quicksight.get_dashboard_embed_url(
            AwsAccountId=aws_account_id,
            DashboardId=dashboard_id,
            IdentityType='IAM',
            SessionLifetimeInMinutes=600,
            UndoRedoDisabled=False
        )
        
        embed_url = response['EmbedUrl']
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({
                'embedUrl': embed_url
            })
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