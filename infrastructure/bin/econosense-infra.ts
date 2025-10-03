#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { EconoSenseInfraStack } from '../lib/econosense-infra-stack';

const app = new cdk.App();

new EconoSenseInfraStack(app, 'EconoSenseInfraStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION || 'us-east-1'
  },
  description: 'EconoSense AI Infrastructure Stack'
});