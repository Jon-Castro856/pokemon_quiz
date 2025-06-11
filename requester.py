import requests
import pprint as pp
import json


def request_call():

    url = 'https://pokeapi.co/api/v2/pokemon/?limit=1025'
    response = requests.get(url)

    if response.status_code == 200:
        print("api request successful")
        data = response.json()
        dex = data['results']
        with open('data.json', 'w') as file:
            print("dumping data into file")
            json.dump(dex, file, indent= 4)

    else:
        print(f"failed to retreive data: {response.status_code}")

