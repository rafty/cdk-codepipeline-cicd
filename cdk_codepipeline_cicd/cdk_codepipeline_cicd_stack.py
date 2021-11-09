import os
from aws_cdk import core as cdk
from aws_cdk.pipelines import CodePipeline
from aws_cdk.pipelines import CodePipelineSource
from aws_cdk.pipelines import ShellStep
from aws_cdk.pipelines import ManualApprovalStep
from app_stage import MyAppStage
from account import Account


class CdkCodepipelineCicdStack(cdk.Stack):

    def __init__(self,
                 scope: cdk.Construct,
                 construct_id: str,
                 account: Account,
                 **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        # github_source = CodePipelineSource.connection(
        #     repo_string='rafty/cdk-codepipeline-cicd',
        #     branch='main',
        #     connection_arn='hoge'
        # )

        github_connection = CodePipelineSource.connection(
            repo_string='rafty/cdk-codepipeline-cicd',
            branch='master',
            connection_arn=('arn:aws:codestar-connections:ap-northeast-1:338456725408:'
                            'connection/39acd667-020f-4a82-8dcd-f80dc5bcb443')
        )

        my_pipeline = CodePipeline(
            scope=self,
            id='Pipeline',
            pipeline_name='MyPipeline',
            self_mutation=False,
            synth=ShellStep(
                id='Synth',
                input=github_connection,
                commands=[
                    'npm install -g aws-cdk',
                    'python -m pip install -r requirements.txt',
                    # 'pip install -r requirements.txt',
                    'cdk synth'
                ])
            # cross_account_keys=True
        )

        dev_stage = MyAppStage(self, 'Dev',
                               env=cdk.Environment(
                                   account=account.id,
                                   region=account.region)
                               )

        my_pipeline.add_stage(dev_stage)

        prod_stage = MyAppStage(self, 'Prod',
                                env=cdk.Environment(
                                    account=account.id,
                                    region=account.region)
                                )

        prod_stage_deployment = my_pipeline.add_stage(prod_stage)
        prod_stage_deployment.add_pre(
            ManualApprovalStep('approval')
        )
