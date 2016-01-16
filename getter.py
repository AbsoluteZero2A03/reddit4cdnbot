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

if __name__ == "__main__":
    print get_reddit_data()
