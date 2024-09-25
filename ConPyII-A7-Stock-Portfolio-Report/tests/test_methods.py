"""
Tests the operational functions of the main script.
"""
from collections import OrderedDict

import requests
from portfolio import portfolio_report
from portfolio import config

def test_api_call_success(requests_mock):
    """
    Tests the FinnHub API call for a succesfull call.
    """
    config.API_KEY = 'fake_key'

    symbol = 'AAPL'
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=fake_key"

    test_response = {
        'c': 420.4,
        'd': 1.93,
        'dp': 0.4612,
        'h': 420.6,
        'l': 416.47,
        'o': 419.07,
        'pc': 418.47,
        't': 1724093221
    }

    requests_mock.get(url, json=test_response)

    response = portfolio_report.call_fh_api(symbol)

    assert isinstance(response, dict)

    expected_dict_keys = ['c', 'd', 'dp', 'h', 'l', 'o', 'pc', 't']
    for key in expected_dict_keys:
        assert key in response
        assert isinstance(response[key], (float, int))

    assert requests_mock.called
    assert requests_mock.request_history[0].url == url

def test_api_call_fail(requests_mock):
    """
    Tests the FinnHub API call function to return the proper response on a fail. 
    """
    config.API_KEY = 'fake_key'

    symbol = 'AAPL'
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=fake_key"

    requests_mock.get(url, exc=requests.exceptions.ConnectionError)

    response = portfolio_report.call_fh_api(symbol)

    assert response is None

def test_api_call_invalid_symbol(requests_mock):
    """
    Tests the FinnHub API call function to return the proper response given an invalid symbol.
    """
    config.API_KEY = 'fake_key'

    symbol = 'INVALID_SYMBOL'
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=fake_key"

    test_response = {
        'c': 0,
        'd': None,
        'dp': None,
        'h': 0,
        'l': 0,
        'o': 0,
        'pc': 0,
        't': 0
    }

    requests_mock.get(url, json=test_response)

    response = portfolio_report.call_fh_api(symbol)

    assert response is None

def test_portfolio_get_symbols():
    """
    Tests the portfolio_get_symbols function returns the expected list of symbols.
    """
    stocks_list = portfolio_report.read_portfolio('portfolio.csv')

    expected_symbols = ['AAPL', 'AMZN']

    symbols_owned = portfolio_report.get_portfolio_symbols(stocks_list)

    assert symbols_owned == expected_symbols
    assert isinstance(symbols_owned, list)

def test_get_market_data(requests_mock):
    """
    Tests the get_marker_data function returns the expected result 
    and correctly formatted market data.
    """
    config.API_KEY = 'fake_key'

    symbols_list = ['AMZN', 'AAPL']

    amzn_url = "https://finnhub.io/api/v1/quote?symbol=AMZN&token=fake_key"
    aapl_url = "https://finnhub.io/api/v1/quote?symbol=AAPL&token=fake_key"

    test_aapl_response = {
        'c': 420.4,
        'd': 1.93,
        'dp': 0.4612,
        'h': 420.6,
        'l': 416.47,
        'o': 419.07,
        'pc': 418.47,
        't': 1724093221
    }

    test_amzn_response = {
        'c': 420.4,
        'd': 1.93,
        'dp': 0.4612,
        'h': 420.6,
        'l': 416.47,
        'o': 419.07,
        'pc': 418.47,
        't': 1724093221
    }

    requests_mock.get(amzn_url, json=test_amzn_response)
    requests_mock.get(aapl_url, json=test_aapl_response)

    response = portfolio_report.get_market_data(symbols_list)

    expected_output = {
        'AMZN': test_amzn_response,
        'AAPL': test_aapl_response
    }

    assert isinstance(response, dict)
    assert response == expected_output

    assert requests_mock.called
    assert requests_mock.request_history[0].url == amzn_url
    assert requests_mock.request_history[1].url == aapl_url

def test_update_portfolio_values():
    """
    Tests the update_portfolio_values function correctly updates 
    the portfolio with the live market price.
    """
    test_portfolio_data = [
        OrderedDict({'symbol': 'AAPL', 'units': '100', 'cost': '154.23'}),
        OrderedDict({'symbol': 'AMZN', 'units': '600', 'cost': '1223.43'})
    ]

    test_market_data = {
        'AAPL': {
            'c': 225.89, 'd': -0.16, 'dp': -0.0708, 'h': 225.97,
            'l': 223.04, 'o': 225.695, 'pc': 226.05, 't': 1724097600
        },
        'AMZN': {
            'c': 178.22, 'd': 1.16, 'dp': 0.6551, 'h': 178.3,
            'l': 176.16, 'o': 177.64, 'pc': 177.06, 't': 1724097601
        }
    }

    portfolio_report.update_portfolio_values(test_portfolio_data, test_market_data)

    expected_output = [
        OrderedDict({'symbol': 'AAPL', 'units': '100', 'cost': '154.23', 'current_price': 225.89}),
        OrderedDict({'symbol': 'AMZN', 'units': '600', 'cost': '1223.43', 'current_price': 178.22})
    ]

    assert test_portfolio_data == expected_output

def test_calculate_metrics():
    """
    Tests the calculate_metrics function properly returns 
    the expected calculated results of the portfolio.
    """

    test_portfolio_data = [
        OrderedDict({'symbol': 'AAPL', 'units': '100', 'cost': '154.23', 'current_price': 225.89}),
        OrderedDict({'symbol': 'AMZN', 'units': '600', 'cost': '1223.43', 'current_price': 178.22})
    ]

    expected_output = [
        OrderedDict({
            'symbol': 'AAPL',
            'units': 100,
            'cost': 154.23,
            'latest_price': 225.89,
            'book_value': 15423.00,
            'market_value': 22589.00,
            'gain_loss': 7166.00,
            'change': 46.46
        }),
        OrderedDict({
            'symbol': 'AMZN',
            'units': 600,
            'cost': 1223.43,
            'latest_price': 178.22,
            'book_value': 734058.00,
            'market_value': 106932.00,
            'gain_loss': -627126.00,
            'change': -85.43
        })
    ]

    calculated_report = portfolio_report.calculate_metrics(test_portfolio_data)

    assert calculated_report == expected_output
