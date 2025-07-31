# google-news-rss

This repository contains a simple Python script for querying Google News RSS
feeds to gather recent articles mentioning specific keywords on selected
websites. The script can be used to monitor automotive news across multiple
sources.

## Usage

1. Install the required dependencies:
   ```bash
   pip install requests feedparser
   ```

2. Run the search script:
   ```bash
   python search_websites.py
   ```

The script prints articles from the last seven days for each keyword and
website combination.
