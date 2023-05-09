import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


def option_resolve(option):
    if option == 0:
        quantity = input("Digite quantas notícias serão buscadas:")
        return get_tech_news(quantity)

    elif option == 1:
        title = input("Digite o título:")
        return search_by_title(title)

    elif option == 2:
        date = input("Digite a data no formato aaaa-mm-dd:")
        return search_by_date(date)

    elif option == 3:
        category = input("Digite a categoria:")
        return search_by_category(category)

    else:
        return top_5_categories()


def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair.\n"
    )

    if option not in ["0", "1", "2", "3", "4", "5"]:
        print("Opção inválida", file=sys.stderr)
        return

    if int(option) == 5:
        print("Encerrando script")
        return

    print(option_resolve(int(option)))
