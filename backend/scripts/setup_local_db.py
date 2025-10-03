import boto3
import json

def create_tables():
    # Create DynamoDB client
    dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    
    # Create Economic Data table
    dynamodb.create_table(
        TableName='econosense-local-economic-data',
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'},
            {'AttributeName': 'timestamp', 'AttributeType': 'S'},
            {'AttributeName': 'indicator', 'AttributeType': 'S'}
        ],
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'},
            {'AttributeName': 'timestamp', 'KeyType': 'RANGE'}
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'indicator-timestamp-index',
                'KeySchema': [
                    {'AttributeName': 'indicator', 'KeyType': 'HASH'},
                    {'AttributeName': 'timestamp', 'KeyType': 'RANGE'}
                ],
                'Projection': {'ProjectionType': 'ALL'}
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )
    
    # Create Sentiment Data table
    dynamodb.create_table(
        TableName='econosense-local-sentiment-data',
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'},
            {'AttributeName': 'timestamp', 'AttributeType': 'S'}
        ],
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'},
            {'AttributeName': 'timestamp', 'KeyType': 'RANGE'}
        ],
        BillingMode='PAY_PER_REQUEST'
    )
    
    print("Tables created successfully!")

def insert_sample_data():
    dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    
    # Insert sample economic data
    economic_table = dynamodb.Table('econosense-local-economic-data')
    economic_data = [
        {
            'id': '1',
            'timestamp': '2025-10-01',
            'indicator': 'GDP',
            'value': 21.5
        },
        {
            'id': '2',
            'timestamp': '2025-10-02',
            'indicator': 'Inflation',
            'value': 2.1
        }
    ]
    
    for item in economic_data:
        economic_table.put_item(Item=item)
    
    # Insert sample sentiment data
    sentiment_table = dynamodb.Table('econosense-local-sentiment-data')
    sentiment_data = [
        {
            'id': '1',
            'timestamp': '2025-10-01',
            'text': 'The economy is showing strong growth signals',
            'source': 'news',
            'sentiment': 'positive',
            'score': 0.95
        }
    ]
    
    for item in sentiment_data:
        sentiment_table.put_item(Item=item)
    
    print("Sample data inserted successfully!")

if __name__ == '__main__':
    try:
        create_tables()
        insert_sample_data()
    except Exception as e:
        print(f"Error: {str(e)}")