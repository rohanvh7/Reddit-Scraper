from praw.models import MoreComments

import praw


def access_token():
    reddit = praw.Reddit(
    client_id="Fh96ELNF9Kf8q25IF6_Arg",
    client_secret="ZPbZXHajAeoLy5UsiD2MUOOtMQqu7g",
    password="xkh*6acyY7th@kg@Kdjy",
    user_agent="testscript by u/Curious-Cricket-4109",
    username="Curious-Cricket-4109",)
    url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
    submission = reddit.submission(url=url)
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        print(top_level_comment.body)

if __name__ == "__main__":
    access_token()

