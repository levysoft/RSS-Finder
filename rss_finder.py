import urllib.parse
import html5lib
import feedparser
import requests

def find_feed(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = response.text
        tree = html5lib.parse(html, namespaceHTMLElements=False)

        # base for relative URLs
        base = tree.findall('.//base')
        base_url = base[0].attrib['href'] if base and 'href' in base[0].attrib else url

        # prioritize Atom over RSS
        links = tree.findall("""head/link[@rel='alternate'][@type='application/atom+xml']""") + tree.findall("""head/link[@rel='alternate'][@type='application/rss+xml']""")
        for link in links:
            href = link.attrib.get('href', '').strip()
            if href:
                return urllib.parse.urljoin(base_url, href)

        # heuristic search for common feed paths
        for suffix in [
            'feed', 'feed/', 'rss', 'atom', 'feed.xml',
            '/feed', '/feed/', '/rss', '/atom', '/feed.xml',
            'index.atom', 'index.rss', 'index.xml', 'atom.xml', 'rss.xml',
            '/index.atom', '/index.rss', '/index.xml', '/atom.xml', '/rss.xml',
            '.rss', '/.rss', '?rss=1', '?feed=rss2',
        ]:
            try:
                potential_feed = urllib.parse.urljoin(base_url, suffix)
                response = requests.get(potential_feed)
                if response.status_code == 200:
                    return potential_feed
            except Exception:
                continue

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python rss_finder.py [URL]")
        sys.exit(1)

    url = sys.argv[1]
    feed_url = find_feed(url)
    if feed_url:
        print(f"Feed URL found: {feed_url}")
    else:
        print("No feed URL found.")

