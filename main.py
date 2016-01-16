import getter
import commenter 
import checker
import uploader
import time
import sys


def iterate():
    checker.setup()
    links = getter.get_reddit_data()
    token = commenter.reddit_authorize()
    print links
    for link in links:
        try:
            url, tid = link["url"], link["id"]
            image = uploader.upload(url)
            commenter.comment(token,tid,image)
            checker.add(tid)
            checker.commit()
            break
        except Exception as e:
            print sys.exc_info()
if __name__ == "__main__":
    iterate()

