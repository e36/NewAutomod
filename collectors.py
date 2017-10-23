import praw

def comment_scraper_entrypoint( queue, resume=None, lastid=None):
    for comment in comment_gen(resume, lastid):
        queue.put(comment)

def comment_gen(resume=None, lastid=None):
    reddit = make_reddit()
    ar = reddit.subreddit("AskReddit")
    if resume and lastid and resume == True:
        for comment in ar.comments(limit=1000):
            yield comment
            if comment.id == lastid:
                break
    for comment in ar.stream.comments():
        yield comment


def submission_scraper_entrypoint( queue, resume=None, lastid=None):
    for submission in submission_gen(resume, lastid):
        queue.put(submission)

def submission_gen( resume=None, lastid=None):
    reddit = make_reddit()
    ar = reddit.subreddit("AskReddit")
    if resume and lastid and resume == True:
        for submission in ar.new(limit=1000):
            yield submission
            if submission.id == lastid:
                break
    for submission in ar.stream.submissions():
        yield submission


#ar = reddit.subreddit("AskReddit")
def make_reddit():
    reddit = praw.Reddit(client_id='***',
                        client_secret='***',
                        password='***',
                        user_agent='The new Automoderator data collection service',
                        username='***')
    return reddit
