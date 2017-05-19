
#  This is an api Wrapper for HackerRank api

import requests


APP_ACCESS_TOKEN = "hackerrank|1477209-1439|5df27efb8aaee3f89aaa2cfd77a809f0c9fd941b"

BASE_URL = "http://api.hackerrank.com/checker/"


def get_language_code(language_opted):
    url = BASE_URL + 'languages.json/' + '?format=json'
    data = requests.get(url).json()
    return data['languages']['codes'][language_opted]


def check_code(language_opted, source_code, test_cases):
    language_opted_code = get_language_code(language_opted)
    url = BASE_URL + "submission.json"
    requests_data = {'api_key': APP_ACCESS_TOKEN, 'source': source_code, 'lang': language_opted_code,
                     'testcases': test_cases, 'wait': True, 'format': 'json'
                     }
    data = requests.post(url, requests_data).json()
    return data['result']['stdout']

source_code = "print 3"
test_cases = '["1 2 3","5 4 6"]'

print check_code('python', source_code, test_cases)
