"""
Author: Jiri Volprecht
"""

import os
import requests
from collections import defaultdict
import re

BASE_URL = "https://slack.com/api"


def get_json_response(url, params=None):
    """
    Helper method to respect DRY
    :param url: url to request
    :param params: if additional query params needed
    :return: response in json
    """
    payload = {'token': os.getenv("SLACK_API_TOKEN")}
    if params:
        payload = {**payload, **params}

    response = requests.get(url, params=payload)
    return response.json()


def find_channel_id(name):
    """
    Find channel id by name
    :param name: channel name
    :return: channel id
    """
    json_res = get_json_response(f"{BASE_URL}/conversations.list")
    if "ok" in json_res and json_res["ok"]:
        for channel in json_res["channels"]:
            if channel["name"] == name:
                return channel["id"]
    return None


def get_conversation_history(channel_id):
    """
    https://slack.com/api/conversations.history?token=YOUR_TOKEN_HERE&channel=CONVERSATION_ID_HERE
    :param channel_id: id of channel to get a history from
    :return: Generator of messages
    """
    json_res = get_json_response(f"{BASE_URL}/conversations.history", {"channel": channel_id})
    if "ok" in json_res and json_res["ok"]:
        for message in json_res["messages"]:
            yield message["text"]


def process_messages():
    """
    Create a stats about usage of emojis
    :return: results in dictionary
    """
    emojis = load_all_emojis()
    res = defaultdict(lambda: 0)
    for msg in get_conversation_history("CL113PJE8"):       # static channel id for testing purposes
        pattern = re.compile(r":(\w+):")
        for match in re.findall(pattern, msg):
            if f":{match}:" in emojis:
                res[match] += 1
    return dict(res)


def load_all_emojis():
    """
    Read emojis.txt list of all emojis
    :return: list of available emojis
    """
    if (os.path.join("slackmoji", "emojis.txt")):
        with open(os.path.join("slackmoji", "emojis.txt"), "r") as file:
            return file.read().splitlines()
    raise Exception("Emojis file is missing. Run scrape_emojis.py script first!")
