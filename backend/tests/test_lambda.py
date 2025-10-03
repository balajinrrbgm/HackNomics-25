import unittest
import json
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lambda.get_economic_data import lambda_handler as economic_handler
from lambda.analyze_sentiment import lambda_handler as sentiment_handler
from lambda.get_quicksight_embed import lambda_handler as quicksight_handler

class TestLambdaFunctions(unittest.TestCase):
    @patch('boto3.resource')
    def test_economic_data_handler(self, mock_resource):
        # Mock DynamoDB response
        mock_table = MagicMock()
        mock_table.query.return_value = {
            'Items': [
                {
                    'timestamp': '2025-10-01',
                    'indicator': 'GDP',
                    'value': 21400.0
                }
            ]
        }
        mock_resource.return_value.Table.return_value = mock_table
        
        # Test event
        event = {
            'queryStringParameters': {
                'indicator': 'GDP',
                'startDate': '2025-01-01',
                'endDate': '2025-12-31'
            }
        }
        
        response = economic_handler(event, None)
        self.assertEqual(response['statusCode'], 200)
        
        body = json.loads(response['body'])
        self.assertEqual(len(body), 1)
        self.assertEqual(body[0]['indicator'], 'GDP')

    @patch('boto3.client')
    def test_sentiment_handler(self, mock_client):
        # Mock Comprehend response
        mock_comprehend = MagicMock()
        mock_comprehend.detect_sentiment.return_value = {
            'Sentiment': 'POSITIVE',
            'SentimentScore': {
                'POSITIVE': 0.8,
                'NEGATIVE': 0.1,
                'NEUTRAL': 0.1
            }
        }
        mock_client.return_value = mock_comprehend
        
        # Test event
        event = {
            'queryStringParameters': {
                'text': 'The economy is showing strong growth.'
            }
        }
        
        response = sentiment_handler(event, None)
        self.assertEqual(response['statusCode'], 200)

    @patch('boto3.client')
    def test_quicksight_handler(self, mock_client):
        # Mock QuickSight response
        mock_quicksight = MagicMock()
        mock_quicksight.get_dashboard_embed_url.return_value = {
            'EmbedUrl': 'https://quicksight.aws.com/embed/12345'
        }
        mock_client.return_value = mock_quicksight
        
        response = quicksight_handler({}, None)
        self.assertEqual(response['statusCode'], 200)
        
        body = json.loads(response['body'])
        self.assertIn('embedUrl', body)

if __name__ == '__main__':
    unittest.main()