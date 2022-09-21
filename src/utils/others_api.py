import requests
import json

class ExternalJoke():
    @classmethod
    def Chuck(self):
        url = 'https://api.chucknorris.io/jokes/random'
        data =  requests.get(url)
        if data.status_code == 200:
            data = data.json()
            return {
                        'origin':url,
                        'joke':data['value']
                        }

    @classmethod
    def Dad(self):
        url = 'https://icanhazdadjoke.com/'
        headers = {"Accept": "application/json"}
        data =  requests.get(url, headers=headers)
        if data.status_code == 200:
            data = data.json()
            return {
                        'origin':url,
                        'joke':data['joke']
                        }
