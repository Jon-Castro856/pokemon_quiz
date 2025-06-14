import requests
from io import BytesIO

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

def image_request(url=None): #call the pokemon API to request an image
    if not url:
        raise Exception("no url passed.")
    
    response = requests.get(url)

    response.raise_for_status() #check if request was succesful
    return BytesIO(response.content)
    

