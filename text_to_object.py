import requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'f580f520daf249a3983aba208997fbfb',
}

test = 'Greg, find me my wallet';

params ={
    # Query parameter
    'q': test,
    # Optional request parameters, set to default values
    'timezoneOffset': '0',
    'verbose': 'false',
    'spellCheck': 'false',
    'staging': 'false',
}

try:
    r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/6f6cc16c-c8dd-4ff4-a009-982bba115530',headers=headers, params=params)
    print(r.json())
    anal = r.json()
    finding = 'find' == anal['topScoringIntent']['intent']
    obj = anal['entities'][0]['entity']
    print(finding)
    print(obj)

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
