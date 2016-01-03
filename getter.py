import requests
import json
import sys

def get_reddit_data():
    res = requests.get("https://www.reddit.com/domain/i.4cdn.org/new/.json", headers = { "User-Agent" : "/u/qyfaf" })
    if res.status_code == 429:
        print "too many requests" 
        return 
    st = json.loads(res.text)
    objs = st["data"]["children"]
    links = map(lambda j: j["data"]["url"], objs)

    return links
    
def get_4chan_images(links):
    print len(links)
    items = []
    for i in range(len(links)):
        f=requests.get(links[i])
        if f.status_code == 404:
            continue
        print f.headers["content-type"]
        items.append(f)
    return items


if __name__ == "__main__":
    get_4chan_images(get_reddit_data())
