# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import aws_cdk as cdk
import boto3
from cdk.cdk.sagemaker_studio_stack import SagemakerStudioStack

AWS_REGION = boto3.session.Session().region_name

app = cdk.App()

SagemakerStudioStack(app, "SagemakerStudioStack", env={"region": AWS_REGION})

app.synth()
