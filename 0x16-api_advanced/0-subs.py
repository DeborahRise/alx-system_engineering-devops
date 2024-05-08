#!/usr/bin/python3
"""
all subscribers of a subreddit
"""

import requests as r


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    }
    response = r.get(url, headers=headers)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
