import json
from pprint import pprint



with open('info_MP_unified.json') as data_file:

    jdata = json.load(data_file)
while(True):

    search = input('Enter your consituency: ')
    print(next((item for item in jdata if item.get("consituency") or item["constituency"] == search), "Invalid Constituency"))
