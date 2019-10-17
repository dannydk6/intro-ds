import requests
import json

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
    if type(resp) is str:
        print(resp)
    elif type(resp) is dict and 'is_correct' in resp:
        is_correct = 'correct' if resp['is_correct'] else 'incorrect'
        print(f'Your answer is {is_correct}')


def submit_four(answer, username, password):
    try:
        parsed = json.dumps([int(x) for x in list(answer.values)])
    except:
        return 'Error parsing. Please make sure you are sending a series of ints.'
    submit_question(qnumber=4,
                    response=parsed,
                    username=username,
                    password=password)
    
def submit_six(answer, username, password):
    try:
        parsed = json.dumps([str(x) for x in list(answer.values)])
    except:
        return 'Error parsing. Please make sure you are sending a series of ints.'
    submit_question(qnumber=6,
                    response=parsed,
                    username=username,
                    password=password)

