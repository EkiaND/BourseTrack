# import sys
# import os
# import pytest

# # Ajouter le dossier `src/` au chemin d'importation
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# from gestionnaire_api import GestionnaireAPI

# #@pytest.fixture
# def api():
#     return GestionnaireAPI()

# def test_collecter_donnees_entreprises(api, mocker):
#     mock_response = {
#         "Time Series (Daily)": {
#             "2024-11-26": {
#                 "1. open": "1000.0",
#                 "2. high": "1050.0",
#                 "3. low": "950.0",
#                 "4. close": "1005.0",
#                 "5. volume": "5000000",
#             }
#         }
#     }
#     mocker.patch("gestionnaire_api.GestionnaireAPI.get_stock_data", return_value=mock_response)
#     entreprises = {"TSLA": {"nom": "Tesla, Inc.", "secteur": "Automobile"}}
#     result_financieres, _ = api.collecter_donnees_entreprises(entreprises)
#     assert "TSLA" in result_financieres
#     assert result_financieres["TSLA"][0]["Open"] == 1000.0

# def test_rate_limit_handling(api, mocker):
#     """
#     Teste la gestion du dépassement de quota pour `get_stock_data`.
#     """
#     # Mock de requests.get pour simuler un dépassement de quota
#     mock_response = mocker.Mock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = {"Note": "Rate limit exceeded"}
#     mocker.patch("requests.get", return_value=mock_response)

#     with pytest.raises(Exception, match="Rate limit atteint"):
#         api.get_stock_data("TSLA", max_retries=3)

# def test_get_news_invalid_query(api, mocker):
#     mocker.patch("requests.get", return_value=mocker.Mock(status_code=200, json=lambda: {"articles": []}))
#     news = api.get_news("InvalidQuery")
#     assert len(news) == 0

# def test_get_news_rate_limit(api, mocker):
#     """
#     Teste la gestion du dépassement de quota pour `get_news`.
#     """
#     mock_response = mocker.Mock()
#     mock_response.status_code = 429  # Simuler une erreur HTTP 429
#     mocker.patch("requests.get", return_value=mock_response)

#     with pytest.raises(Exception, match="Rate limit HTTP 429"):
#         api.get_news("Tesla", max_retries=3)
