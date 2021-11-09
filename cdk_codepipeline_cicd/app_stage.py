from aws_cdk import core as cdk
from app_stack import MyAppStack


class MyAppStage(cdk.Stage):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        app_stack = MyAppStack(self, 'MyAppStackForStage')
