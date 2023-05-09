import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


def option_resolve(option):
    options = {
        '0': lambda: get_tech_news(
            input("Digite quantas notícias serão buscadas:")
        ),
        '1': lambda: search_by_title(input("Digite o título:")),
        '2': lambda: search_by_date(
            input("Digite a data no formato aaaa-mm-dd:")
        ),
        '3': lambda: search_by_category(input("Digite a categoria:")),
        '4': lambda: top_5_categories(),
        '5': lambda: "Encerrando script"
    }
    return options[option]()


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

    print(option_resolve(option))
