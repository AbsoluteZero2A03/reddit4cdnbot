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
    links = map(lambda j: { "url": j["data"]["url"], "id": j["kind"]+"_"+j["data"]["id"]}, objs)
    return links
    
def get_4chan_images(links):
    print links
    items = []
    for i in range(len(links)):
        f=requests.get(links[i]["url"])
        if f.status_code != 200:
            continue
        items.append(f)
    return items


if __name__ == "__main__":
    print get_reddit_data()
