#!/usr/bin/python3

# import requests
import requests
import sys


def number_of_subscribers(subreddit):
    """
    main function for the subcriber count
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Testapi/1.0 by Danjor667'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search")
        sys.exit()
    subreddit_name = sys.argv[1]
    subscribers = number_of_subscribers(subreddit_name)
    print("{:d}".format(subscribers))
