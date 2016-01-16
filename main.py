import getter
import commenter 
import checker
import uploader
import time

def iterate():
    links = getter.get_reddit_data()
    token = reddit_authorize()
    for link in links:
        try:
            url, tid = link["url"], link["id"]
            image = uploader.upload(url)
            commenter.comment(token,tid,image)
            
        except:
            pass
if __name__ == "__main__":
    iterate()
