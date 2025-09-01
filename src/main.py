from rss_fetcher import fetch_rss_feeds
from summarizer import summarize_text
from bs4 import BeautifulSoup

# Define the RSS feeds to process
RSS_FEEDS = [
    'https://research.google/blog/rss/',
    'http://feeds.feedburner.com/TechCrunch/',
    'https://openai.com/blog/rss.xml'
]

# Limit the number of articles to summarize per feed
MAX_ARTICLES_PER_FEED = 2

def get_article_text(entry):
    """
    Extracts the text content from a feed entry.
    It prefers the 'content' field but falls back to 'summary'.
    It also cleans up HTML tags.
    """
    if hasattr(entry, 'content'):
        content = entry.content[0].value
    elif hasattr(entry, 'summary'):
        content = entry.summary
    else:
        return ""

    # Clean up HTML tags using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text()

def main():
    """
    Main function to fetch, summarize, and print articles.
    """
    print("--- RSS Summarizer ---")

    all_entries = fetch_rss_feeds(RSS_FEEDS)

    if not all_entries:
        print("No articles found. Exiting.")
        return

    # To avoid summarizing too many articles, let's limit it.
    # We will group entries by feed and take the top N from each.
    # A simpler approach for now is to just take the first few from the combined list.

    articles_to_summarize = all_entries[:MAX_ARTICLES_PER_FEED * len(RSS_FEEDS)]

    print(f"\nFound {len(all_entries)} total articles. Summarizing the first {len(articles_to_summarize)}...\n")

    for entry in articles_to_summarize:
        print(f"--- Article ---")
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")

        article_text = get_article_text(entry)

        if not article_text:
            print("Could not find content for this article.")
            continue

        print("\nSummarizing...")
        summary = summarize_text(article_text)

        print("\nSummary:")
        print(summary)
        print("-" * 20)

if __name__ == "__main__":
    main()
