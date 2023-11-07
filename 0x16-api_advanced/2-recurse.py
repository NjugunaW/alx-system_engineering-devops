#!/usr/bin/python3
"""A recursive function that queries the Reddit API and returns a list containing the titles.
"""
import requests


def recurse(subreddit, hot_list=[], next="", _count_=0):
    """This function queries and returns a list of titles of all hot posts on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "next": next,
        "_count_": _count_,
        "threshold": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    next = results.get("next")
    _count_ += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if next is not None:
        return recurse(subreddit, hot_list, next, _count_)
    return hot_list
