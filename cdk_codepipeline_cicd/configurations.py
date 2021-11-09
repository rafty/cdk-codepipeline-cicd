import os


class Configurations:

    def __init__(self):
        self._account = os.getenv('CDK_DEFAULT_ACCOUNT')
        self._region = 'ap-northeast-1'

    @property
    def account(self):
        return self._account

    @property
    def region(self):
        return self._region
