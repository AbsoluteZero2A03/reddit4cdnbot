import getter
import uploader
import time

def iterate():
    links = getter.get_reddit_data()
    imgur_images = []
    for link in links:
        try:
            imgur_images.append(uploader.upload(link))
            print imgur_images[-1]
        except:
            pass
if __name__ == "__main__":
    #while True:
    #    iterate()
        #time.sleep(30)
    #pass
    iterate()
