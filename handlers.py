def comment_handler(q):
    while True:
        comment = q.get()
        print("Got comment, processing it")
        print(comment)
        print("")

def submission_handler(q):
    while True:
        submission = q.get()
        print("Got submission, processing it")
        print(submission)
        print("")
