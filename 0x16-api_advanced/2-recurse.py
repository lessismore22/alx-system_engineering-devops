#!/usr/bin/python3
"""
recursive function that queries the Reddit API
and returns a list containing the titles of all hot
articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests


def recurse(subreddit, hot_list: list = [], count=0, after""):
    """ returns the title of the hot posts of teh subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
            "User-Agent": "0x16-api_advanced:project:\
                    v1.0.0 (by /u/lessismore22)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
