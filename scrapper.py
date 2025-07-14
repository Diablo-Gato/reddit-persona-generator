# scrapper.py

import os
import praw
from typing import Dict, Union
from prawcore.exceptions import NotFound, ResponseException, OAuthException
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_reddit_data(username: str) -> Union[Dict, None]:
    """
    Fetches a Reddit user's posts and comments with metadata for citation.

    Args:
        username (str): The Reddit username to scrape.

    Returns:
        Union[Dict, None]: A dictionary containing the username, a list of post details,
                           and a list of comment details, or None if an error occurs.
    """
    try:
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent="RedditPersonaScript by u/YOUR_USERNAME"
        )

        user = reddit.redditor(username)

        # Force a lookup to validate user
        _ = user.id

        posts = []
        comments = []

        # Fetch latest 50 posts
        for submission in user.submissions.new(limit=50):
            posts.append({
                "id": submission.id,
                "title": submission.title,
                "selftext": submission.selftext or "",
                "url": submission.url,
                "permalink": f"https://www.reddit.com{submission.permalink}"
            })

        # Fetch latest 50 comments
        for comment in user.comments.new(limit=50):
            comments.append({
                "id": comment.id,
                "body": comment.body,
                "permalink": f"https://www.reddit.com{comment.permalink}",
                "submission_id": comment.submission.id,
                "submission_title": comment.submission.title
            })

        return {
            "username": username,
            "posts": posts,
            "comments": comments
        }

    except NotFound:
        print(f"[❌] Error: Reddit user '{username}' not found.")
        return None
    except (ResponseException, OAuthException) as e:
        print(f"[⚠️] Reddit API error: {e}")
        print("Check your credentials (client_id, client_secret) and internet connection.")
        return None
    except Exception as e:
        print(f"[‼️] Unexpected error: {e}")
        return None
