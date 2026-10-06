data = {
    'Records': [{
            'messageId': 'd5f6aa4e-e95a-45ca-a7c8-c486e9339fb3',
            'receiptHandle': 'AQEBwQdfPpTWSu9tsDM7iwhqUxXkJh3XsXN7qtPf0v0PUpl6b30zxwSPQI2kQtYdDDtm4LF3gfb39wdu8zaoNFoAlDAac4XisOKces75rsRPv6YmwebAgvNrcZIhHB7fKB0t4aG/xkF60J0fyuEAb1MHhnSsHQk8xCC4l9l3R3IkRUM2jxJrHFetvVoFjhNRMVvSOPGiiH3Xy59c0ISC3vc3wYd5V8OKo5Wq9uFA5RBj+XAEmLqr3AEaY+qgoyXSgKUad/1ITJNtadLud/tnzcgWa/hFkAz1wNd9fU+sBn0D2G26MB262RW6+nff+BoS/yOA7nPiMni8SUhdqQoRnVyWgO3WaPySIRb3islWn8mLdb8BBohmlSSEL6N/MK5U1085NHManmt2/+SYTNuADDkPvQ==',
            'body': '{\n"Name":"Srinivasa Sameer"\n}',
            'attributes': {
                'ApproximateReceiveCount': '1',
                'SentTimestamp': '1775142100811',
                'SenderId': '218852528943',
                'ApproximateFirstReceiveTimestamp': '1775142100817'
            },
            'messageAttributes': {},
            'md5OfBody': '1fb07d6bfc691dec750c4fb6247229b1',
            'eventSource': 'aws:sqs',
            'eventSourceARN': 'arn:aws:sqs:eu-north-1:218852528943:DemoQueue',
            'awsRegion': 'eu-north-1'
        }
    ]
}

import json

result = json.loads(data['Records'][0]['body'])
print(type(result))
print(result['Name'])