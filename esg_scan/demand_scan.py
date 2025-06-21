import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

ESG_KEYWORDS = [
    'sustainability', 'carbon neutral', 'net zero', 'renewable', 'diversity', 'inclusion',
    'governance', 'decarbonization', 'climate risk', 'csr', 'social responsibility',
    'emissions', 'green energy', 'circular economy'
]

def extract_articles(urls):
    articles = []
    for url in urls:
        try:
            resp = requests.get(url, timeout=10)
            soup = BeautifulSoup(resp.text, 'html.parser')
            paragraphs = soup.find_all('p')
            text = ' '.join([p.get_text() for p in paragraphs])
            articles.append({'url': url, 'text': text})
        except Exception as e:
            print(f"Failed to process {url}: {e}")
    return articles

def scan_for_esg_signals(articles, keywords=ESG_KEYWORDS):
    signals = []
    for article in articles:
        found = []
        for kw in keywords:
            if re.search(rf'\b{re.escape(kw)}\b', article['text'], re.IGNORECASE):
                found.append(kw)
        if found:
            signals.append({
                'url': article['url'],
                'signals': found,
                'summary': article['text'][:300]
            })
    return pd.DataFrame(signals)

# Example usage
if __name__ == "__main__":
    example_urls = [
        "https://www.reuters.com/business/sustainable-business/",
        "https://www.esgtoday.com/category/environment/"
    ]
    articles = extract_articles(example_urls)
    esg_signals_df = scan_for_esg_signals(articles)
    print(esg_signals_df)
