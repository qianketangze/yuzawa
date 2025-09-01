import feedparser
import ssl

def fetch_rss_feeds(urls):
    """
    Fetches and parses RSS feeds from a list of URLs.

    Args:
        urls: A list of RSS feed URLs.

    Returns:
        A list of feed entries.
    """
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    all_entries = []
    for url in urls:
        print(f"Fetching feed from: {url}")
        try:
            feed = feedparser.parse(url)
            if feed.bozo:
                print(f"Error parsing feed from {url}: {feed.bozo_exception}")
                continue
            all_entries.extend(feed.entries)
        except Exception as e:
            print(f"Could not fetch or parse feed from {url}: {e}")

    return all_entries
