import requests

API_URL = 'http://ds-leaderboards.com:5000'
#API_URL = 'http://localhost:5000'


def signup(username=None,
           password=None):
    body = {'username': username,
            'password': password}
    r = requests.post(f'{API_URL}/api/register', json=body)
    resp = r.json()
    print(resp)


def submit_question(
                    qnumber,
                    response,
                    username=None,
                    password=None
                    ):
    body = {'username': username,
            'password': password,
            'qnumber': qnumber,
            'response': response}
    r = requests.post(f'{API_URL}/api/question_attempt', json=body)
    resp = r.json()
    print(resp)
