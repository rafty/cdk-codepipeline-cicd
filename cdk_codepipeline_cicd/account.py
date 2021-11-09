import os


class Account:

    def __init__(self):
        self._id = os.getenv('CDK_DEFAULT_ACCOUNT')
        self._region = 'ap-northeast-1'

    @property
    def id(self) -> str:
        return self._id

    @property
    def region(self) -> str:
        return self._region
