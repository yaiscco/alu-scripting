#!/usr/bin/python3
'''
Defines function that prints the top ten posts of a subreddit
'''
import requests


def top_ten(subreddit):
    '''Prints the top ten posts of a subreddit'''
    if not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "linux:api_advanced.project:v1.0 (by /u/shobi_ola)"
    }

    params = {"limit": 10}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {}).get("children", [])

    if not data:
        print(None)
        return

    for post in data:
        print(post.get("data").get("title"))
