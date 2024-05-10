#!/usr/bin/python3
"""
 a function that queries the Reddit API and prints the titles of
 the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    If not a valid subreddit, print None.
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    params = {'limit': 10}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    resp = requests.get(url, headers=headers, params=params)

    if resp.json() == 200:
        try:
            for post in resp.json()['data']['children']:
                print(post['data']['title'])

        except Exception:
            print(None)
