
#Download from Instagram
from itertools import islice
from math import ceil
from instaloader import Instaloader, Profile
#Desktop notifications
from win10toast import ToastNotifier as notify
#File management
import os
#Post to instagram
from instabot import Bot

root = ''
PROFILE = ['','']

def makeNotification(body):
    toaster = notify()
    toaster.show_toast('AutoInsta', body, threaded=True, icon_path=None, duration=5)

def downloadPost(PROFILE):
    #Set percentage of files to download from specified profile
    per = 10
    l = Instaloader()
    profile = Profile.from_username(l.context, PROFILE)
    posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda p: p.likes + p.comments, reverse=True)
    for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * per / 100)):
        l.download_post(post,PROFILE)
        #Remove break statement below to download more than one post
        break

def removeUnwanted():
    fileArray = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            fileArray.append(os.path.join(path, name))
    for i in fileArray:
        if ("comments") in i:
            os.remove(i)
            makeNotification("File removed: {}".format(i))
        if ("json") in i:
            os.remove(i)
            makeNotification("File removed: {}".format(i))


def postImage():
    fileArray = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            fileArray.append(os.path.join(path,name))
    for i in fileArray:
        if ".txt" in i:
            cap = i
            break
    for i in fileArray:
        if ".jpg" or ".png" in i:
            img = i
            break
    bot = Bot()
    bot.login(username = "", password = "")
    bot.upload_photo(img, caption = cap)
    makeNotification("Image posted: {}".format(i))
    os.remove(cap)
    os.remove(img)
    
                             
for i in PROFILE:
    downloadPost(i)
    
removeUnwanted()
postImage()
