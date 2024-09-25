"""
Generates performance reports for your stock portfolio.
"""

import csv
from collections import OrderedDict
import argparse
from concurrent.futures import ThreadPoolExecutor
import pathlib
import requests
from . import config

def read_portfolio(input_file):
    """
    Returns data from a CSV file.
    """
    pf_data = []
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pf_data.append(OrderedDict([
                ('symbol', row['symbol']),
                ('units', row['units']),
                ('cost', row['cost'])
            ]))
    return pf_data

def save_portfolio(output_data, output_file):
    """
    Saves data to a CSV file, overwriting any existing content.
    """
    if 'latest_price' in output_data[0]:
        cols = [
            'symbol', 'units', 'cost', 'latest_price',
            'book_value', 'market_value', 'gain_loss', 'change'
        ]
    else:
        cols = ['symbol', 'units', 'cost']

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=cols)
        writer.writeheader()
        writer.writerows(output_data)

def get_args():
    """
    Parse and return command line argument values.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--portfolio_source', required=True)
    parser.add_argument('--report_name', required=True)

    return parser.parse_args()

def call_fh_api(symbol):
    """
    Calls the FinnHub API to return data for the indicated symbol.
    """
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={config.API_KEY}"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        response_data = response.json()

        if all(value in (0, None) for value in response_data.values()):
            print(f"{symbol} is not a valid stock symbol")
            return None

        return response_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None


def get_portfolio_symbols(stocks_list):
    """
    Get a list of symbols owned in the portfolio.
    """

    symbols_owned = []

    for stock in stocks_list:
        symbol = list(stock.values())[0]
        symbols_owned.append(symbol)

    return symbols_owned

def get_market_data(symbols_list):
    """
    Get the latest market data for the given stock symbols using concurrent requests.
    """
    stock_market_data = {}

    with ThreadPoolExecutor() as executor:
        data_results = list(executor.map(call_fh_api, symbols_list))

    for symbol, data in zip(symbols_list, data_results):
        stock_market_data[symbol] = data

    return stock_market_data


def update_portfolio_values(portfolio_data, market_data):
    """
    Updates the portfolio values to now include the current
    market value which will help with our calculations. 
    """

    for stock in portfolio_data:
        symbol = stock['symbol']
        if symbol in market_data:
            stock['current_price'] = market_data[symbol]['c']


def calculate_metrics(portfolio_data):
    """
    Calculates the various metrics of each of the stocks and returns the full report.
    """
    full_portfolio_report = []

    for stock in portfolio_data:
        units = int(stock['units'])
        cost = float(stock['cost'])
        latest_price = float(stock['current_price'])
        book_value = units * cost # The value of the shares at time of purchase
        market_value = units * latest_price # value of the shares based on the latest market value
        gain_loss = market_value - book_value # The dollar amount either gained or lost
        change = (gain_loss / book_value) * 100 # A percentage (decimal) of the gain/loss

        full_portfolio_report.append(OrderedDict([
                ('symbol', stock['symbol']),
                ('units', units),
                ('cost', round(cost, 2)),
                ('latest_price', round(latest_price, 2)),
                ('book_value', round(book_value, 2)),
                ('market_value', round(market_value, 2)),
                ('gain_loss', round(gain_loss, 2)),
                ('change', round(change, 2)),
            ]))

    return full_portfolio_report

def main():
    """
    Brings all of the functions together to make the program function.
    """

    args = get_args()

    portfolio_data = read_portfolio(args.portfolio_source)
    owned_symbols = get_portfolio_symbols(portfolio_data)
    live_market_data = get_market_data(owned_symbols)
    update_portfolio_values(portfolio_data, live_market_data)
    calculated_data = calculate_metrics(portfolio_data)
    save_portfolio(calculated_data, args.report_name)

    report_path = pathlib.Path(args.report_name).resolve()
    print(f"Report created at path: {report_path}")

if __name__ == '__main__':
    main()
