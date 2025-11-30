import feedparser

url = "http://feeds.bbci.co.uk/news/world/rss.xml"

feed = feedparser.parse(url)

print("RSS Feed Title:", feed.feed.title)
print("\nLatest News:\n")

for entry in feed.entries[:5]:
    print("Title:", entry.title)
    print("Link:", entry.link)
    print("-" * 40)
