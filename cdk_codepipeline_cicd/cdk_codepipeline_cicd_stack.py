import os
from aws_cdk import core as cdk
from aws_cdk.pipelines import CodePipeline
from aws_cdk.pipelines import CodePipelineSource
from aws_cdk.pipelines import ShellStep
from aws_cdk.pipelines import ManualApprovalStep
from app_stage import MyAppStage
# from configurations import Configurations

account = os.getenv('CDK_DEFAULT_ACCOUNT')
region = 'ap-northeast-1'


class CdkCodepipelineCicdStack(cdk.Stack):

    def __init__(self,
                 scope: cdk.Construct,
                 construct_id: str,
                 **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        github_source = CodePipelineSource.connection(
            repo_string='rafty/cdk-codepipeline-cicd',
            branch='main',
            connection_arn='hoge'
        )

        my_pipeline = CodePipeline(
            scope=self,
            id='Pipeline',
            pipeline_name='MyPipeline',
            self_mutation=False,
            synth=ShellStep(
                id='Synth',
                input=CodePipelineSource.git_hub(
                    'rafty/cdk-codepipeline-cicd',
                    'master'
                ),
                commands=[
                    'npm install -g aws-cdk',
                    'python -m pip install -r requirements.txt',
                    'cdk synth'
                ])
            # cross_account_keys=True
        )

        dev_stage = my_pipeline.add_stage(
            MyAppStage(self, 'myAppDev',
                       env=cdk.Environment(
                           account=account, region=region))
        )

        dev_stage.add_post(ManualApprovalStep('approval'))

        prod_stage = my_pipeline.add_stage(
            MyAppStage(self, 'myAppProd',
                       env=cdk.Environment(
                           account=account, region=region))
        )

        prod_stage.add_post(ManualApprovalStep('approval'))
