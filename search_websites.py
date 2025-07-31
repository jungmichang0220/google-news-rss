import requests
import feedparser
from datetime import datetime, timedelta
from urllib.parse import quote_plus

KEYWORDS = [
    "Fabricante de automóviles nueva planta de producción en México",
    "Wiring Harness",
    "General Motors",
    "General Motors korea",
    "Ford Motor",
    "Stellantis",
    "Tesla",
    "Rivian",
    "Lucid",
    "Volkswagen",
    "scout motors",
    "Toyota",
    "Mercedes-Benz",
    "BMW",
    "Honda",
    "BYD",
    "Sumitomo Electric Industries, Ltd.",
    "Yazaki Corporation",
    "LEAR",
    "KYUNGSHIN CABLE",
    "YURA CORPORATION",
]

WEBSITES = [
    "https://www.autonews.com/",
    "https://www.caranddriver.com/",
    "https://www.motortrend.com/",
    "https://www.roadandtrack.com/",
    "https://jalopnik.com/",
    "https://www.edmunds.com/",
    "https://www.autoblog.com/",
    "https://carbuzz.com/",
    "https://www.motorauthority.com/",
    "https://www.thedrive.com/",
    "https://motorbit.com.mx/",
    "https://www.autocosmos.com.mx/",
    "https://www.elfinanciero.com.mx/autos/",
]

RSS_URL = "https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"


def search_site(keyword, site):
    query = quote_plus(f"{keyword} site:{site}")
    url = RSS_URL.format(query=query)
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    feed = feedparser.parse(response.text)
    return feed.entries


def filter_recent(entries, days=7):
    cutoff = datetime.utcnow() - timedelta(days=days)
    recent = []
    for entry in entries:
        if "published_parsed" in entry:
            published = datetime(*entry.published_parsed[:6])
            if published >= cutoff:
                recent.append({
                    "title": entry.title,
                    "link": entry.link,
                    "published": published.isoformat(),
                })
    return recent


def main():
    for site in WEBSITES:
        domain = site.replace("https://", "").replace("http://", "").strip("/")
        print(f"\nResults for site: {domain}\n" + "-" * 40)
        for keyword in KEYWORDS:
            entries = search_site(keyword, domain)
            recent = filter_recent(entries)
            if recent:
                print(f"\nKeyword: {keyword}")
                for item in recent:
                    print(
                        f"  - {item['published'][:10]} | {item['title']} | {item['link']}"
                    )


if __name__ == "__main__":
    main()
