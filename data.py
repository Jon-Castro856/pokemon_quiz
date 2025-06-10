import requests
import pprint


def request_call():

    url = 'https://pokeapi.co/api/v2/pokemon/1'
    response = requests.get(url)

    if response.status_code == 200:
        pprint.pprint(data)
    else:
        print(f"failed to retreive data: {response.status_code}")

