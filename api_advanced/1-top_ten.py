#!/usr/bin/python3
'''
Defines function that prints the top ten posts of a subreddit
'''
import requests


def top_ten(subreddit):
    '''Prints the top ten posts of a subreddit'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:api_advanced:v1.0 (by /u/api_advanced)"
    }
    params = {"limit": 10}
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
    except Exception:
        print(None)
        return

    if response.status_code == 301 or response.status_code == 302:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        results = response.json()
    except Exception:
        print(None)
        return

    data = results.get("data", {}).get("children", [])
    if not data:
        print(None)
        return

    for post in data:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
