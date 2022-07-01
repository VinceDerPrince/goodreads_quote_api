from typing import List, Dict
import bs4 as _bs4
import requests as _requests

def _generate_url(page:int) -> str:
    url = f"https://www.goodreads.com/quotes?page={page}"
    return url

def _get_page_url(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def popular_quotes(page: int) -> List[str]:
    url = _generate_url(page)
    page = _get_page_url(url)

    raw_quotes = page.find_all(class_="quote")
    quotes = [quote.text for quote in raw_quotes]
    encode = quotes[1].encode(encoding="UTF-8", errors="ignore").decode()
    clean_text = " ".join([word for word in encode.split()])
    # output = {
    #     "quote": 
    # }
    return clean_text[:-5]

print(popular_quotes(1))
