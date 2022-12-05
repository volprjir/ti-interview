"""
Author: Jiri Volprecht
"""

import requests
from bs4 import BeautifulSoup
import os


def get_all_emojis():
    # TODO: get complete list of emojis
    """
    Scrape webfx web to get a full list of emojis - not really complete list
    :return:
    """
    response = requests.get("https://www.webfx.com/tools/emoji-cheat-sheet/")
    soup = BeautifulSoup(response.text, "html.parser")
    with open("emojis.txt", "w") as file:
        [file.write(f":{item.text}:{os.linesep}") for item in soup.find_all("span", {"class": "name"})]


if __name__ == "__main__":
    get_all_emojis()
