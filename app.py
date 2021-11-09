#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from cdk_codepipeline_cicd.cdk_codepipeline_cicd_stack import CdkCodepipelineCicdStack
from cdk_codepipeline_cicd.account import Account

# account = os.getenv('CDK_DEFAULT_ACCOUNT')
# region = 'ap-northeast-1'
account = Account()

app = cdk.App()

CdkCodepipelineCicdStack(
    scope=app,
    construct_id="CdkCodepipelineCicdStack",
    env=cdk.Environment(
        account=account.id,
        region=account.region),
    account=account
)

app.synth()
