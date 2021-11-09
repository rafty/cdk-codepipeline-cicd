#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
# from cdk_codepipeline_cicd.configurations import Configurations
from cdk_codepipeline_cicd.cdk_codepipeline_cicd_stack import CdkCodepipelineCicdStack


account = os.getenv('CDK_DEFAULT_ACCOUNT')
region = 'ap-northeast-1'

app = cdk.App()
CdkCodepipelineCicdStack(app, "CdkCodepipelineCicdStack",
                         env=cdk.Environment(account=account, region=region))

app.synth()
