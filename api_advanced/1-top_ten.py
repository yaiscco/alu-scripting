#!/usr/bin/python3
'''
Defines function that prints the top ten posts of a subreddit
'''
import requests


def top_ten(subreddit):
    '''Prints the top ten posts of a subreddit'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "MyRedditBot/1.0 by api_advanced"
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
        print(post.get("data", {}).get("title"))
