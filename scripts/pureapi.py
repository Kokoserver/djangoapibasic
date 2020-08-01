import json
import requests

BASE_URL = "http://127.0.0.1:8000"
endpoint = "/api/details/"



def get_list():
    url = BASE_URL+endpoint
    req=  requests.get(url)
    result = req.json()
    result = [content["id"] for content in result] 
    print(req.status_code)
    return result

def get_detail(id):
    url = BASE_URL + endpoint+str(id)
    data = requests.get(url)
    return data.json()

def postData():
    url = BASE_URL+endpoint
    new_data = {
        "user":1,
        # "content":"another content testing"
    } 
    req = requests.post(url, data=new_data)
    print(req.status_code)
    if req.status_code == requests.codes.ok:
        print(req.json())
        print(req.headers)
        return req.json()
    return req.text
    
  
def update(id):
    url = BASE_URL + endpoint+str(id)
    # data = json.dumps({"content":"yeah is working"})
    data = {"content":"yeah now"}
    req = requests.put(url, data)
    return req.text
        
# print(postData())

print(update(1))