#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    returns the number of total subscribers for a given subreddit.
    """

    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    if not subreddit:
        return 0
    url = 'https://www.reddit.com/r/{subreddit}'

    resp = requests.get(url, headers=headers)
    subs = resp.json()['subcribers']

    return subs
