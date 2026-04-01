#!/usr/bin/python3
"""
Defines function that prints the top ten posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """Prints the top ten posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:api_advanced:v1.0.0 (by /u/yourusername)"
    }
    params = {"limit": 10}
    
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        
        # Check for redirects (invalid subreddit)
        if response.status_code in [301, 302, 404]:
            print(None)
            return
            
        # Check for successful response
        if response.status_code != 200:
            print(None)
            return
            
        # Parse JSON
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        # If no posts found, invalid subreddit
        if not posts:
            print(None)
            return
            
        # Print titles of top 10 posts
        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
                
    except Exception:
        print(None)
