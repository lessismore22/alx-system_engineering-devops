#!/usr/bin/python3
"""
this module contains the function top_ten
"""

import requests
from sys import argv


def top_ten(subreddit):
    """
    returns the top ten posts for a given subreddit
    """
    url = f"https://www.reddit.com/r/{}/.json?limit=10"
    headers = {"User-Agent': 'Mozilla/5.0"}
    response = requests.get(url, headers=headers, params=params)
    results = response.json()

    try:
        post_data = results.get('data').get('children')

        for i in post_data:
            print(i.get('data').get('title'))
    except Exception:
        print("None")


if __name__ == "__main__":
    top_ten(argv[1])
