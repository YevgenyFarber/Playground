import requests
import feedparser

# URL of the RSS feed
rss_url = "https://kinozal.tv/rss.xml"  # Replace with the actual RSS feed URL

# Fetch the RSS feed
response = requests.get(rss_url)
content = response.content

# Parse the feed
feed = feedparser.parse(content)

# Iterate through entries and extract information
for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = entry.published
    # Process other fields as needed

    # Do something with the extracted information
    print(f"Title: {title}, Link: {link}, Published: {published}")
