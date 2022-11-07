# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from aws_cdk import aws_sagemaker as sagemaker
from constructs import Construct
from cdk.cdk.helpers import get_sagemaker_image_arn
from typing import List

JUPYTER_SERVER_APP_IMAGE_NAME = "jupyter-server-3"
KERNEL_GATEWAY_APP_IMAGE_NAME = "datascience-2.0"


class SageMakerStudio(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        vpc: ec2.Vpc,
        aws_region: str,
        user_names: List[str] = ["default-user"],
        default_instance_type: str = "ml.t3.medium"
    ):
        super().__init__(scope, id)
        private_subnets = [subnet.subnet_id for subnet in vpc.private_subnets]
        self.sagemaker_studio_execution_role = iam.Role(
            self,
            "SagemakerStudioExecutionRole",
            assumed_by=iam.ServicePrincipal("sagemaker.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    # Warning: might need to scope down AmazonSageMakerFullAccess permissions as required for improved security.
                    "AmazonSageMakerFullAccess"
                )
            ],
        )
        standard_security_group = ec2.SecurityGroup(
            self,
            "StandardTrafficSecurityGroup",
            vpc=vpc,
            description="only outbound traffic is allowed by default",
            allow_all_outbound=True,
        )
        sagemaker_studio_domain = sagemaker.CfnDomain(
            self,
            "SageMakerStudioDomain",
            auth_mode="IAM",
            default_user_settings=sagemaker.CfnDomain.UserSettingsProperty(
                execution_role=self.sagemaker_studio_execution_role.role_arn,
                jupyter_server_app_settings=sagemaker.CfnDomain.JupyterServerAppSettingsProperty(
                    default_resource_spec=sagemaker.CfnDomain.ResourceSpecProperty(
                        instance_type="system",
                        sage_maker_image_arn=get_sagemaker_image_arn(
                            JUPYTER_SERVER_APP_IMAGE_NAME, aws_region
                        ),
                    )
                ),
                kernel_gateway_app_settings=sagemaker.CfnDomain.KernelGatewayAppSettingsProperty(
                    default_resource_spec=sagemaker.CfnDomain.ResourceSpecProperty(
                        instance_type=default_instance_type,
                        sage_maker_image_arn=get_sagemaker_image_arn(
                            KERNEL_GATEWAY_APP_IMAGE_NAME, aws_region
                        ),
                    ),
                ),
                security_groups=[standard_security_group.security_group_id],
                sharing_settings=sagemaker.CfnDomain.SharingSettingsProperty(
                    notebook_output_option="Disabled"
                ),
            ),
            domain_name="SageMakerStudioDomain",
            subnet_ids=private_subnets,
            vpc_id=vpc.vpc_id,
            app_network_access_type="VpcOnly",
        )
        for user_name in user_names:
            sagemaker.CfnUserProfile(
                self,
                "SageMakerStudioUserProfile_" + user_name,
                domain_id=sagemaker_studio_domain.attr_domain_id,
                user_profile_name=user_name,
            )
