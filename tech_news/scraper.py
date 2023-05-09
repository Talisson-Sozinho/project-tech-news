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
    return selector.css("article header h2 a::attr(href)").getall()


def scrape_next_page_link(html_content: str) -> str | None:
    selector = Selector(html_content)
    return selector.css(".nav-links a.next::attr(href)").get()


def scrape_news(html_content):
    selector = Selector(html_content)

    news_details = {
        "url": selector.css(".pk-share-buttons-items a::attr(href)")
        .get()
        .split("=")[1],
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".meta-author .author a::text").get(),
        "reading_time": int(
            selector.css(".meta-reading-time::text").get().split()[0]
        ),
        "summary": "".join(
            selector.css(
                "div.entry-content > p:first-of-type *::text"
            ).getall()
        ).strip(),
        "category": selector.css(".meta-category span.label::text").get(),
    }

    return news_details


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
