import boto3
import json
from datetime import datetime

def create_kinesis_resources():
    kinesis = boto3.client('kinesis')
    
    # Create Kinesis Data Stream
    try:
        response = kinesis.create_stream(
            StreamName='econosense-stream',
            ShardCount=1
        )
        print("Created Kinesis stream: econosense-stream")
    except kinesis.exceptions.ResourceInUseException:
        print("Kinesis stream already exists")
    
    # Create Kinesis Firehose for S3 delivery
    firehose = boto3.client('firehose')
    try:
        response = firehose.create_delivery_stream(
            DeliveryStreamName='econosense-firehose',
            DeliveryStreamType='DirectPut',
            S3DestinationConfiguration={
                'RoleARN': 'arn:aws:iam::YOUR_ACCOUNT_ID:role/firehose-role',
                'BucketARN': 'arn:aws:s3:::econosense-data',
                'Prefix': 'raw-data/',
                'BufferingHints': {
                    'SizeInMBs': 5,
                    'IntervalInSeconds': 300
                },
                'CompressionFormat': 'GZIP'
            }
        )
        print("Created Kinesis Firehose: econosense-firehose")
    except Exception as e:
        print(f"Error creating Firehose: {str(e)}")

def put_record_to_stream(data):
    kinesis = boto3.client('kinesis')
    
    try:
        response = kinesis.put_record(
            StreamName='econosense-stream',
            Data=json.dumps(data),
            PartitionKey=str(datetime.now().timestamp())
        )
        return response
    except Exception as e:
        print(f"Error putting record to stream: {str(e)}")
        return None

if __name__ == "__main__":
    # Create Kinesis resources
    create_kinesis_resources()
    
    # Test putting a record
    test_data = {
        "timestamp": datetime.now().isoformat(),
        "indicator": "GDP",
        "value": 21400.0,
        "source": "test"
    }
    
    response = put_record_to_stream(test_data)
    print(f"Put record response: {response}")