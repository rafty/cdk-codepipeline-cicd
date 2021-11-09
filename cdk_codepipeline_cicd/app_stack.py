from aws_cdk import core as cdk
from aws_cdk import aws_lambda


class MyAppStack(cdk.Stack):
    def __init__(self,
                 scope: cdk.Construct,
                 construct_id: str,
                 environment: str,  # Dev/Stg/Prod
                 **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        aws_lambda.Function(
            scope=self,
            id=f'MyLambdaFunction-{environment}',
            function_name=f'MyApp-{environment}',
            description=f'My sample App Function - {environment}',
            code=aws_lambda.Code.asset('src/lambda'),
            handler='new_app.handler',
            runtime=aws_lambda.Runtime.PYTHON_3_8
        )
