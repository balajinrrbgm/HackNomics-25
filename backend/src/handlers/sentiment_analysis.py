import json
import boto3
import os
from datetime import datetime

comprehend = boto3.client('comprehend')
sagemaker_runtime = boto3.client('sagemaker-runtime')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['SENTIMENT_DATA_TABLE'])

def analyze_text(text):
    # Use AWS Comprehend for sentiment analysis
    try:
        response = comprehend.detect_sentiment(
            Text=text,
            LanguageCode='en'
        )
        
        return {
            'sentiment': response['Sentiment'].lower(),
            'score': response['SentimentScore'][response['Sentiment']]
        }
    except Exception as e:
        print(f"Error in Comprehend analysis: {str(e)}")
        return None

def custom_model_analysis(text):
    # Use our custom FinBERT model endpoint
    try:
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName=os.environ['FINBERT_ENDPOINT'],
            ContentType='application/json',
            Body=json.dumps({'text': text})
        )
        
        result = json.loads(response['Body'].read().decode())
        return result
    except Exception as e:
        print(f"Error in custom model analysis: {str(e)}")
        return None

def lambda_handler(event, context):
    try:
        # Get query parameters
        query_params = event.get('queryStringParameters', {}) or {}
        text = query_params.get('text')
        source = query_params.get('source', 'api')
        
        if text:
            # Perform both analyses
            comprehend_result = analyze_text(text)
            custom_result = custom_model_analysis(text)
            
            # Combine results
            result = {
                'timestamp': datetime.now().isoformat(),
                'text': text,
                'source': source,
                'comprehend_analysis': comprehend_result,
                'custom_analysis': custom_result
            }
            
            # Store results in DynamoDB
            table.put_item(Item=result)
            
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': True
                },
                'body': json.dumps(result)
            }
        else:
            # Retrieve recent sentiment analysis results
            response = table.query(
                IndexName='timestamp-index',
                Limit=10,
                ScanIndexForward=False
            )
            
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': True
                },
                'body': json.dumps(response['Items'])
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