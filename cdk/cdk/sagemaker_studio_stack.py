# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from aws_cdk import aws_ec2 as ec2
from aws_cdk import Stack
from constructs import Construct
from .sagemaker_studio_construct import SageMakerStudio


class SagemakerStudioStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpc = ec2.Vpc(self, "SageMakerStudioVpc")
        SageMakerStudio(self, "SageMakerStudio", vpc=vpc, aws_region=self.region)
