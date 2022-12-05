#!/usr/bin/env python3
"""
Author: Jiri Volprecht
"""

import os
from flask import Flask, render_template
from slackmoji.script import process_messages

app = Flask(__name__)


@app.route("/")
def statistic():
    stats = process_messages()
    return render_template('statistics.html', keys=stats.keys(), stats=stats)


if __name__ == "__main__":
    if (os.path.exists(os.path.join('slackmoji', 'emojis.txt'))):
        app.run()
    else:
        print("Emoji list is missing. Please run slackmoji/scrape_emojis.py script first!")
        exit(1)
