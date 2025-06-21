import requests
from bs4 import BeautifulSoup
import logging

def scrape_article(url):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        return text
    except Exception as e:
        logging.error(f"Error scraping {url}: {e}")
        return ""

def scrape_multiple(urls):
    articles = []
    for url in urls:
        article = scrape_article(url)
        if article:
            articles.append({'url': url, 'text': article})
    return articles
