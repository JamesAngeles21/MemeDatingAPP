import praw
import requests
import hashlib



reddit = praw.Reddit(client_id="C0gnqnonnbFUiw",
                     client_secret="5jeS-QgvyPnl98uovHkWHIfgwlM",
                     user_agent="my user agent")

pngTag = ".png"
jpgTag = ".jpg"
gifTag = ".gif"
subbreddits = ["gifs", "memes"]

pngCollector = []
jpgCollector = []
gifCollector = []

for sub in subbreddits:
    for submission in reddit.subreddit(sub).top("week", limit=100):
        if pngTag in submission.url:
            pngCollector += [submission.url]
        elif jpgTag in submission.url:
            jpgCollector += [submission.url]
        elif gifTag in submission.url:
            gifCollector += [submission.url]

for image in pngCollector:
    url = image
    m = hashlib.sha256()
    m.update(url.encode('utf-8'))

    with open('./images/'+m.hexdigest()+".png",'wb') as f:
        f.write(requests.get(url).content)

for image in jpgCollector:
    url = image
    m = hashlib.sha256()
    m.update(url.encode('utf-8'))

    with open('./images/'+m.hexdigest()+".jpg",'wb') as f:
        f.write(requests.get(url).content)

for image in gifCollector:
    url = image
    m = hashlib.sha256()
    m.update(url.encode('utf-8'))

    with open('./images/'+m.hexdigest()+".gif",'wb') as f:
        f.write(requests.get(url).content)