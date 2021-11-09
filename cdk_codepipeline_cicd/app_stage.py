from aws_cdk import core as cdk
from app_stack import MyAppStack


class MyAppStage(cdk.Stage):

    def __init__(self,
                 scope: cdk.Construct,
                 construct_id: str,  # Dev/Stage/Prod
                 # environment: str,  # Dev/Stg/Prod
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        print(f'------------------MyAppStage construct_id={construct_id}')

        app_stack = MyAppStack(self, 'MyAppStackForStage', construct_id)
