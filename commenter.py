import os
import requests
import oauth2
import SimpleHTTPServer

def reddit_authorize():
    payload={"grant_type": "password", "username": "4cdnbot", "password": os.environ["REDDIT_PASSWORD"]}
    auth_params=(os.environ["REDDIT_APP_ID"],os.environ["REDDIT_APP_SECRET"])

    res = requests.post("https://www.reddit.com/api/v1/access_token", data=payload, auth=auth_params,headers={"user-agent":"/u/4cdnbot"})
    print res.json()
    token = res.json()[u"access_token"]
    return token

def comment(token,thread,image):
    pass


if __name__ == "__main__":
    print reddit_authorize()
