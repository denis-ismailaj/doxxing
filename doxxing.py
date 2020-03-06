import praw

r = praw.Reddit(client_id='WXDf0BVWjjbpAA', client_secret="j-CoxH3M6zCj2AfF8QTQQQ7YqGI", password='password', username='username', user_agent='myuseragent accessAPI:v0.0.1')

srname = 'AskReddit'
sr = r.subreddit(srname)

i = 0

for post in sr.comments(limit=10000):
    author = post.author
    print(i, end="\r")
    i += 1
    if author:
        link = author.link_karma
        commk = author.comment_karma
        cake = author.created_utc
        if(link > 7000 and commk > 1000 and link < 10000 and commk < 3000): # Customizable filters
            print(author)
            print("\a")
print(i)
