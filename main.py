from window import Window
import json
from requester import request_call

'''

'''
def main():
     # fill the dex with all 1025 pokemon
    data = request_call(url='https://pokeapi.co/api/v2/pokemon/?limit=1025')
    dex_data = data['results']

    for pokemon in range(0, len(dex_data)):
        link = dex_data[pokemon]['url']
        print(f"sending data request for {dex_data[pokemon]}")
        new_data = request_call(link)
        dex_data[pokemon]['content'] = new_data

    with open('data.json', 'w') as file:
        print("dumping data into file")
        json.dump(dex_data, file, indent= 4)

main()