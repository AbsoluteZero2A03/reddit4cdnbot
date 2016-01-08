import os
import requests
import oauth2
import SimpleHTTPServer

def reddit_authorize():
    payload={"grant_type": "password", "username": "4cdnbot", "password": os.environ["REDDIT_PASSWORD"]}
    auth_params=(os.environ["REDDIT_APP_ID"],os.environ["REDDIT_APP_SECRET"])
    res = requests.post("https://www.reddit.com/api/v1/access_token", data=payload, auth=auth_params,headers={"user-agent":"/u/4cdnbot"})
    token = res.json()[u"access_token"]
    return token

def get_modhash(token):
    headers = {"User-Agent": "/u/4cdnbot", "Authorization": "bearer {0}".format(token)}
    auth_params=(os.environ["REDDIT_APP_ID"],os.environ["REDDIT_APP_SECRET"])
    print headers
    res2 = requests.get("https://oauth.reddit.com/api/v1/me.json", headers=headers)
    return res2.json()

def comment(token,thread,image_link):
    headers = {"user-agent": "/u/4cdnbot", "Authorization": "bearer {0}".format(token)}
    modhash = get_modhash(token)
    payload = {
        "api_type": "json",
        "text": "Imgur Mirror: {0}".format(image_link),
        "thing_id": thread,
        "uh" : modhash
    }
    res = requests.post("https://reddit.com/api/comment",data=payload,headers=headers)
    return res.status_code

if __name__ == "__main__":
    r=reddit_authorize()
    print r
    print get_modhash(r)
