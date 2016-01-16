import requests
import json
import os

base_auth = "https://api.imgur.com/oauth2/authorize?client_id={0}&response_type={1}&state={2}" 


def authorize():
    auth=base_auth.format(os.environ["IMGUR_APP_CLIENT_ID"], "pin", "asdf")
    auth_response = requests.get(auth)
    print auth_response.text

    #payload = 
    #token = requests.post("https://api.imgur.com/oauth2/token", data = payload) 
    #return token
    

def upload(link):
    headers = {"Authorization": "Client-ID {0}".format(os.environ["IMGUR_APP_CLIENT_ID"]), "user-agent": "/u/qyfaf"}

    payload = {"type": "url","image":link}

    res = requests.post("https://api.imgur.com/3/image",headers=headers,data=payload)
    if res.status_code == 200:
        return res.json()["data"]["link"]
    else:
        print link
        print res.text
        print res.status_code
        raise Exception

if __name__ == "__main__":
    print upload("https://s3.amazonaws.com/prod-heroku/external_greenhouse_job_boards/logos/000/001/201/original/q-icon-black-lg.png?1429101672")
