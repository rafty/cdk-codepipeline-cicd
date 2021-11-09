from aws_cdk import core as cdk
from aws_cdk import aws_lambda


class MyAppStack(cdk.Stack):
    def __init__(self,
                 scope: cdk.Construct,
                 construct_id: str,
                 **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        aws_lambda.Function(
            scope=self,
            id='MyLambdaFunction',
            function_name='MyApp',
            description='My sample App Function',
            code=aws_lambda.Code.asset('src/lambda'),
            handler='new_app.handler',
            runtime=aws_lambda.Runtime.PYTHON_3_8
        )
