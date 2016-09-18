import requests
import json
import os

base_auth = "https://api.imgur.com/oauth2/authorize?client_id={0}&response_type={1}&state={2}" 

class StreamableUploadFailException(Exception): pass
class ImgurUploadFailException(Exception): pass

def authorize():
    auth=base_auth.format(os.environ["IMGUR_APP_CLIENT_ID"], "pin", "asdf")
    auth_response = requests.get(auth)
    print auth_response.text


def upload(link):

    linkheaders = requests.head(link)
    content_type = linkheaders.headers["content-type"]
    if content_type == "video/webm": 
        streamable_request = requests.get("https://api.streamable.com/import?url={0}".format(link))
        if streamable_request.status_code != 200:
            print streamable_request.status_code
            raise StreamableUploadFailException
        else: 
            streamable_shortcode = streamable_request.json()[u"shortcode"]
            secondary_req = requests.get("https://api.streamable.com/videos/{0}".format(streamable_shortcode))
            #while secondary_req.status_code != 200: 
                #secondary_req = requests.get("https://api.streamable.com/videos/{0}".format(streamable_shortcode))
            print secondary_req.status_code
            return {"type" : "streamable", "url" : "https://"+secondary_req.json()[u"url"]}
    else:
    
        headers = {"Authorization": "Client-ID {0}".format(os.environ["IMGUR_APP_CLIENT_ID"]), "user-agent": "/u/qyfaf"}

        payload = {"type": "url","image":link}

        res = requests.post("https://api.imgur.com/3/image",headers=headers,data=payload)
        if res.status_code == 200:
            return {"type": "imgur", "url": res.json()["data"]["link"]}
        else: 
            print link
            print res.text
            print res.status_code
            raise ImgurUploadFailException

if __name__ == "__main__":
    print upload("http://i.4cdn.org/r/1453129178416.webm")
