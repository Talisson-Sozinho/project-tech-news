from parsel import Selector
import requests
import time


def fetch(url: str) -> str | None:
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )

        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    return response.text


def scrape_updates(html_content: str) -> list[str]:
    selector = Selector(html_content)
    return selector.css('article header h2 a::attr(href)').getall()


def scrape_next_page_link(html_content: str) -> str | None:
    selector = Selector(html_content)
    return selector.css('.nav-links a.next::attr(href)').get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
