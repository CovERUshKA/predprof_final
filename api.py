from requests import get


def get_api_data():
    head = {
        'X-Auth-Token': 'c2up4twf'
    }
    req = get('https://dt.miet.ru/ppo_it_final', headers=head)

    api_data = []
    messages = req.json().get('message')
    for message in messages:
        api_data.append(message.get('points'))
    
    return api_data
