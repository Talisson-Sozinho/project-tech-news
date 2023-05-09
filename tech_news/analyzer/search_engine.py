from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    db_response_list = search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    return [tuple([news["title"], news["url"]]) for news in db_response_list]


def search_by_date(date):
    try:
        f_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    db_response_list = search_news({"timestamp": f_date})

    return [tuple([news["title"], news["url"]]) for news in db_response_list]


def search_by_category(category):
    db_response_list = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    return [tuple([news["title"], news["url"]]) for news in db_response_list]
