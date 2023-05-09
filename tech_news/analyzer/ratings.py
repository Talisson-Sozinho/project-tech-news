from tech_news.database import get_collection


def top_5_categories():
    categories_db_population = (
        get_collection()
        .find({}, {"_id": False, "category": True})
        .sort("category", 1)
    )

    category_summary_quantity = {}

    for news in categories_db_population:
        if news["category"] in category_summary_quantity:
            category_summary_quantity[news["category"]] += 1
        else:
            category_summary_quantity[news["category"]] = 1

    category_quantity_list_sorted = sorted(
        category_summary_quantity.items(), key=lambda x: x[1], reverse=True
    )

    return [category for category, _ in category_quantity_list_sorted[:5]]
