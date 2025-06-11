import requests
import pprint as pp
import json


def request_call(url=None): #call the pokemon API and request the data from the url provided
    if not url:
        raise Exception("No URL passed.")
    
    response = requests.get(url)

    if response.status_code == 200: #check if request was succesful
        print("api request successful")
        data = response.json()

        return data

    else:
        print(f"failed to retreive data: {response.status_code}")

