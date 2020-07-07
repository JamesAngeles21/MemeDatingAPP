import praw

reddit = praw.Reddit(client_id="C0gnqnonnbFUiw",
                     client_secret="5jeS-QgvyPnl98uovHkWHIfgwlM",
                     user_agent="my user agent")

imageTag = [".png", ".jpg"]
gifTag = [".gif"]
subbreddits = ["xqcow"]

imageCollector = []
gifCollector = []

for sub in subbreddits:
    for submission in reddit.subreddit(sub).top("week", limit=100):
        imageSubmission = any(string in submission.url for string in imageTag)
        if imageSubmission:
            imageCollector += [submission.url]
        gifSubmission = any(string in submission.url for string in gifTag)
        if gifSubmission:
            gifCollector += [submission.url]

print(imageCollector)
print(gifCollector)