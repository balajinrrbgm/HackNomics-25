# EconoSense AI

An AI-powered Economic Policy and Financial Impact Analysis Platform for the HackNomics 2025 Hackathon.

## Project Overview

EconoSense AI is a comprehensive platform that combines fintech innovation with economic data analysis to help policymakers, businesses, and individuals make informed decisions. The platform leverages artificial intelligence to provide real-time economic impact analysis, policy recommendations, and financial inclusion metrics.

### Key Features

- Real-time economic impact analysis using machine learning models
- AI-driven policy recommendation engine powered by SageMaker
- Financial sentiment analysis using AWS Comprehend and custom FinBERT model
- Interactive data visualization with D3.js and Amazon QuickSight
- Real-time data processing with AWS Kinesis and Glue
- Serverless architecture using AWS Lambda and API Gateway

### Problem Statement

In today's rapidly evolving economic landscape, decision-makers face challenges in:
1. Processing vast amounts of economic data in real-time
2. Understanding market sentiment and its impact on economic indicators
3. Making data-driven policy decisions
4. Predicting economic trends and potential risks

EconoSense AI addresses these challenges by providing:
1. Real-time data integration and analysis
2. AI-powered economic forecasting
3. Sentiment analysis of financial news and social media
4. Interactive visualization for better decision-making

## Business Impact

1. **For Policymakers**
   - Real-time economic impact assessment
   - Data-driven policy recommendations
   - Risk analysis and forecasting

2. **For Businesses**
   - Market sentiment analysis
   - Economic trend predictions
   - Investment opportunity identification

3. **For Individuals**
   - Financial literacy tools
   - Economic indicator tracking
   - Investment insights

### AWS Services
- **AI/ML Services**
  - Amazon SageMaker - ML model training and deployment
  - Amazon Comprehend - NLP and sentiment analysis
  - Amazon Forecast - Economic predictions
  - Amazon Personalize - Recommendation engine

- **Backend Services**
  - AWS Lambda - Serverless functions
  - Amazon API Gateway - API management
  - Amazon DynamoDB - NoSQL database
  - Amazon S3 - Data storage
  - AWS Glue - ETL jobs
  - Amazon Kinesis - Real-time data processing

- **Frontend Services**
  - AWS Amplify - Frontend hosting and CI/CD
  - Amazon QuickSight - Embedded analytics
  - Amazon Cognito - Authentication

### Development Stack
- Frontend: Next.js (React) with TypeScript
- Backend: AWS Lambda with Python
- Infrastructure: AWS CDK for IaC
- Data Visualization: Amazon QuickSight, D3.js

## Project Structure

```
econosense-ai/
├── frontend/         # Next.js frontend application with AWS Amplify
├── infrastructure/   # AWS CDK Infrastructure as Code
│   ├── lib/         # Stack definitions
│   └── bin/         # CDK app entry point
├── backend/         # AWS Lambda functions
│   ├── api/        # API Lambda functions
│   ├── ml/         # ML processing functions
│   └── etl/        # Data processing functions
├── ml/             # SageMaker notebooks and model artifacts
└── docs/           # Documentation and architecture diagrams
```

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.9+
- AWS CLI configured
- AWS CDK CLI
- AWS Account with appropriate permissions

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/econosense-ai.git
cd econosense-ai
```

2. Install and configure AWS CDK
```bash
npm install -g aws-cdk
cdk bootstrap
```

3. Deploy AWS Infrastructure
```bash
cd infrastructure
npm install
cdk deploy
```

4. Set up the frontend
```bash
cd frontend
npm install
# Configure Amplify
amplify init
amplify push
npm run dev
```

5. Set up local development environment
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### AWS Configuration

1. Configure AWS credentials
```bash
aws configure
```

2. Required AWS Services Setup:
- Enable Amazon SageMaker
- Configure Amazon Cognito User Pool
- Set up Amazon QuickSight account
- Create necessary IAM roles and policies

## Contributing

This project is part of the HackNomics 2025 Hackathon. Please contact the team for contribution guidelines.

## License

This project is licensed under the MIT License - see the LICENSE file for details.