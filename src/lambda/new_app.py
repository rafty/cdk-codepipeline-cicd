import json


def handler(event, contexts):
    print('event: {}'.format(json.dumps(event)))
    print('new action!!')

    return {}
