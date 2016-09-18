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
    for link in links:
        try:
            url, tid = link["url"], link["id"]
            image = uploader.upload(url)
            if not checker.check(tid):
                result = False
                while not result:
                    print url, tid
                    result = commenter.comment(token,tid,image)
                    if result:
                        checker.add(tid)
                        checker.commit()
        except Exception as e:
            print sys.exc_info()
if __name__ == "__main__":
    iterate()

