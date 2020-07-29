import requests

BASE_URL = "http://127.0.0.1:8000"
endpoint = "/api/update/"



def get_list():
    url = BASE_URL+endpoint
    data = [content for content in requests.get(url)] 
    return data

def get_detail(id):
    url = BASE_URL + endpoint+str(id)
    data = requests.get(url)
    return data.json()
 
print(get_detail(2))