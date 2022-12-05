This tools is getting all messages from public Slack channels and show analysis of all used emojis.

## Usage

Firstly you need to scrape all emojis used in your slack by running `python3 slackmoji/scrape_emojis.py` This will generate `emojis.txt` file with all emojis used in your slack.

Then you can run `python3 app.py` to get simple analysis of all emojis used in your slack.
