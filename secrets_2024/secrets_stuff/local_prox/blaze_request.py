import requests

from secrets_stuff.utils import load_credentials
# from ..utils import load_credentials

proxy = {
    "http": "http://localhost:4444",  # Change the address if necessary
    "https": "http://localhost:4444"  # Same proxy for HTTPS requests
}

json_data = {
    'id': 14524348,
    'isNewTest': True,
    'name': 'gondalak',
    'userId': 1862206,
    'creatorClientId': 'gui',
    'overrideExecutions': [
        {
            'concurrency': 20,
            'executor': '',
            'holdFor': '19m',
            'locations': {
                'us-east4-a': 20,
            },
            'locationsPercents': {
                'us-east4-a': 100,
            },
            'rampUp': '1m',
            'steps': 0,
        },
    ],
    'executions': [
        {
            'concurrency': 20,
            'usersNotConfigured': False,
            'holdFor': '19m',
            'durationIsNotConfigured': False,
            'iterationAndDurationDisabled': False,
            'rampUp': '1m',
            'steps': 0,
            'locations': {
                'us-east4-a': 20,
            },
            'locationsPercents': {
                'us-east4-a': 100,
            },
            'scenario': 'default-scenario-14524348',
        },
    ],
    'hasThreadGroupsToOverride': False,
    'hasNonRegularThreadGroup': False,
    'hasMultipleThreadGroups': False,
    'shouldSendReportEmail': True,
    'dependencies': {},
    'shouldRemoveJmeter': True,
    'created': 1733763063,
    'updated': 1733763067,
    'projectId': 1679992,
    'lastUpdatedById': 1862206,
    'configuration': {
        'type': 'taurus',
        'dedicatedIpsEnabled': False,
        'canControlRampup': False,
        'targetThreads': 500,
        'executionType': 'taurusCloud',
        'enableLoadConfiguration': True,
        'threads': 500,
        'testMode': '',
        'extraSlots': 0,
        'plugins': {
            'jmeter': {
                'version': 'stable',
                'consoleArgs': '',
                'enginesArgs': '',
                'versionInfo': [
                    {
                        'key': 'stable',
                        'text': 'Stable',
                        'number': '5.5',
                        'enabled': True,
                    },
                    {
                        'key': 'latest',
                        'text': 'Latest',
                        'number': '5.6.3',
                        'enabled': True,
                    },
                    {
                        'key': 'auto',
                        'text': 'Auto Detect',
                        'number': '',
                        'enabled': False,
                    },
                ],
            },
            'thresholds': {
                'thresholds': [],
                'fromTaurus': False,
            },
        },
    },
    'subscribers': [
        1862206,
    ],
    'revisionTimestamp': 1733763084386,
}

key, secret = load_credentials()
auth = (key, secret)


session = requests.Session()
# session.verify = '/Users/shayaajzner/.mitmproxy/mitmproxy-ca-cert.cer'
# session.verify = '/shared/.mitmproxy/mitmproxy-ca-cert.cer'
session.verify = '/Users/yajzner/.mitmproxy/mitmproxy-ca-cert.cer'


# Make the GET request through the proxy
response = session.put('https://a.blazemeter.com/api/v4/tests/14524348', proxies=proxy, auth=auth, json=json_data)



# response = requests.put('https://a.blazemeter.com/api/v4/tests/14524348', auth=auth,  json=json_data)
print(response.json())