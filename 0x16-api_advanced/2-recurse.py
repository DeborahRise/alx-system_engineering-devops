#!/usr/bin/python3
""" a recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit.
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    Hint: The Reddit API uses pagination for separating
    pages of responses.
    """
    global after
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    params = {'after': after}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    resp = requests.get(url, params=params, headers=headers,
                        allow_redirects=False)
    if resp.status_code == 200:
        after_data = resp.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = resp.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
