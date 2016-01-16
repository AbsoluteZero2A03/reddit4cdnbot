import os
import requests

def reddit_authorize():
    payload={"grant_type": "password", "username": "4cdnbot", "password": os.environ["REDDIT_PASSWORD"]}
    auth_params=(os.environ["REDDIT_APP_ID"],os.environ["REDDIT_APP_SECRET"])
    res = requests.post("https://www.reddit.com/api/v1/access_token", data=payload, auth=auth_params,headers={"user-agent":"/u/4cdnbot"})
    token = res.json()[u"access_token"]
    return token

def get_modhash(token):
    headers = {"User-Agent": "/u/4cdnbot", "Authorization": "bearer {0}".format(token)}
    auth_params=(os.environ["REDDIT_APP_ID"],os.environ["REDDIT_APP_SECRET"])
    #print headers
    res2 = requests.get("https://oauth.reddit.com/api/v1/me.json", headers=headers)
    return res2.json()

def comment(token,thread,image_link):
    headers = {"user-agent": "/u/4cdnbot", "Authorization": "bearer {0}".format(token)}
    payload = {
        "api_type": "json",
        "text": "[imgur mirror]({0})\n\nDon't directly link to 4chan!".format(image_link),
        "thing_id": thread,
    }
    res = requests.post("https://oauth.reddit.com/api/comment",data=payload,headers=headers)

    if len(res.json()[u"json"][u"errors"]) == 0:
        return True
    else:
        print res.text
        return False

if __name__ == "__main__":
    print comment(reddit_authorize(),"t3_416cxm", "http://www.google.com")
