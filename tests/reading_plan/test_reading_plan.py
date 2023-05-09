from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch

mock = [
    {
        "url": "https://blog.betrybe.com/tecnologia/armazenamento-em-nuvem/",
        "title": "Armazenamento em nuvem: o que é e quais os 7 melhores?",
        "timestamp": "20/04/2023",
        "writer": "Cairo Noleto",
        "reading_time": 12,
        "summary": "Em algum momento você já se perguntou se ",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/componentizacao-tudo-so",
        "title": "Componentização: o que é, por que usar e exemplo na prática",
        "timestamp": "17/04/2023",
        "writer": "Cairo Noleto",
        "reading_time": 10,
        "summary": "Se você é uma pessoa programadora, ",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/10-navegadores-leves/",
        "title": "10 navegadores leves, rápidos e seguros para PC fraco!",
        "timestamp": "13/04/2023",
        "writer": "Cairo Noleto",
        "reading_time": 9,
        "summary": "Dá pra se imaginar sem internet?",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/cabos-de-rede/",
        "title": "Cabos de rede: o que são, quais os tipos e como crimpar?",
        "timestamp": "10/04/2023",
        "writer": "Dayane Arena dos Santos",
        "reading_time": 9,
        "summary": "Os cabos de rede são itens extremamente necessários ",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/desenvolvimento-web/estruturas-de",
        "title": "Estruturas de repetição: quais as 4 principais e quando",
        "timestamp": "05/04/2023",
        "writer": "Vinicius Martins",
        "reading_time": 5,
        "summary": "As estruturas de repetição estão muito presentes na vida",
        "category": "Desenvolvimento Web",
    },
]


def test_reading_plan_group_news():
    value_error_text = "Valor 'available_time' deve ser maior que zero"
    with pytest.raises(ValueError, match=value_error_text):
        ReadingPlanService.group_news_for_available_time(-19)

    with patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy"
    ) as mock_reading_plan_service:

        mock_reading_plan_service.return_value = mock

        response = ReadingPlanService.group_news_for_available_time(9)

        assert len(response["readable"]) == 3
        assert len(response["unreadable"]) == 2

        list_unfilled_time = [
            readable["unfilled_time"] for readable in response["readable"]
        ]
        assert list_unfilled_time == [0, 0, 4]
