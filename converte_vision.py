"""Etl process based on Image Magic."""
import base64
import json
from googleapiclient import discovery
VISIO_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


def convert_image_to_json(_base64):
    """Call Google Vision Api."""
    # [START authenticate]
    # TODO change to dot file
    server_key = ''
    service = discovery.build('vision', 'v1', developerKey=server_key,
                              discoveryServiceUrl=VISIO_URL)

    service_request = service.images().annotate(body={
        'requests': [{
            'image': {
                'content': _base64
            },
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 1
            }]
        }]
    })

    # [START parse_response]
    response = service_request.execute()

    return response


if __name__ == '__main__':
    with open('resultado.jpg') as t:
        with open('./resultado.json', 'w') as f:
            f.write(json.dumps(convert_image_to_json(base64.b64encode(t.read()))))
