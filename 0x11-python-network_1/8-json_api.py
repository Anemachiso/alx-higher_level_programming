#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to a URL
Uses the letter as a parameter
"""
import requests
from sys import argv


def json_api():
        try:
            q = argv[1]
        except:
            q = ''
        url = 'http://0.0.0.0:5000/search_user'
        payload = {'q': q}
        r = requests.post(url, payload)
        try:
            seart = r.json()
            if len(seart) == 0:
                print('No result')
            else:
                json_id = seart.get('id')
                json_name = seart.get('name')
                print('[{}] {}'.format(json_id, json_name))
        except:
            print('Not a valid JSON')


if __name__ == '__main__':
    json_api()
