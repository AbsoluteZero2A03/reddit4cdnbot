import getter
import commenter 
import requests
import checker
import uploader
import time
import sys


def iterate():
    checker.setup()
    links = getter.get_reddit_data()
    token = commenter.reddit_authorize()
    for link in links:
        try:
            url, tid = link["url"], link["id"]
            print url, tid
            fourchan_res = requests.head(url)        
            if fourchan_res.status_code != 200:
                continue
            if checker.check(tid):
                continue
            image = uploader.upload(url)
            result = False
            while not result:
                result = commenter.comment(token,tid,image)
                if result:
                    checker.add(tid)
                    checker.commit()
        except Exception as e:
            print sys.exc_info()

if __name__ == "__main__":
    while True:
        iterate()
