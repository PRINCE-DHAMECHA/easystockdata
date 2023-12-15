"""
datetime module for date handling
json module for JSON file handling
requests module for HTTP requests
"""
import datetime
import requests
from .indian import nse_symbols
from .usa import nasdaq_symbols


BASEURL = "https://query1.finance.yahoo.com/v8/finance/chart/"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


def get_prices(symbol, intv="1d", rng="1wk", ohlc="high", stock_exc="nse"):
    """
    Retrieves historical prices for a given symbol from an YahooFinanceAPI.

    Parameters:
        symbol (str): The symbol of the stock for which to retrieve prices.
        intv (str, optional): The interval at which to fetch prices.
        Possible values: "1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h",
        "1d", "5d", "1wk", "1mo", "3mo".
        Defaults to "1wk".
        rng (str, optional): The range of prices to fetch.
        Possible values: "1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h",
        "1d", "5d", "1wk", "1mo", "3mo".
        Defaults to "1d".
        ohlc (str, optional): The type of price data to
        fetch (open, high, low, close).
        Defaults to "high".
        stock_exchange (str, optional): The stock exchange to fetch data from.
        Defaults to "nse".

    Returns:
        list: A list of lists containing the timestamp
        and corresponding price for each data point.
    """

    if intv not in [
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "60m",
        "90m",
        "1h",
        "1d",
        "5d",
        "1wk",
        "1mo",
        "3mo",
    ]:
        raise KeyError("Enter valid interval value")

    if rng not in [
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "60m",
        "90m",
        "1h",
        "1d",
        "5d",
        "1wk",
        "1mo",
        "3mo",
    ]:
        raise KeyError("Enter valid range value")

    if stock_exc == "nse":
        symbol += ".ns"

    url = BASEURL + symbol + "?&interval=" + intv + "&range=" + rng
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        return KeyError("Something went wrong")

    response_json = response.json()
    result = response_json["chart"]["result"][0]

    timestamps = result["timestamp"]
    timestamps = [
        datetime.datetime.fromtimestamp(ts).strftime("%c") for ts in timestamps
    ]

    prices = []

    quote = result["indicators"]["quote"][0]
    if ohlc == "high":
        prices = quote["high"]
    elif ohlc == "low":
        prices = quote["low"]
    elif ohlc == "close":
        prices = quote["close"]
    elif ohlc == "open":
        prices = quote["open"]
    else:
        raise KeyError("Enter valid OHLC value")

    response = []

    for i, price in enumerate(prices):
        response.append([timestamps[i], price])
    return response


def get_nse_symbols() -> list[dict]:
    """
    Get the NSE symbols.

    :return: A list of dictionaries containing
    the stock names and symbols of nse.
    """
    return nse_symbols


def find_nse_stock(search_term) -> list[dict]:
    """
    Search for a given stock symbol in the NSE stock database
    and return a list of matching stock information.

    Parameters:
        search_term (str): The term to search for in the stock names.

    Returns:
        list: A list of dictionaries containing
        the stock name and symbol for the matching stocks.
    """
    response = []
    for _, value in enumerate(nse_symbols):
        if search_term.lower() in value["name"].lower():
            response.append(value)
    return response


def get_nasdaq_symbols() -> list:
    """
    Get the Nasdaq symbols.

    :return: A list of dictionaries containing
    the stock names and symbols of nasdaq.
    """
    return nasdaq_symbols


def find_nasdaq_stock(search_term) -> list:
    """
    Search for a given stock symbol in the Nasdaq stock database
    and return a list of matching stock information.

    Parameters:
        search_term (str): The term to search for in the stock names.

    Returns:
        list: A list of dictionaries containing
        the stock name and symbol for the matching stocks.
    """
    response = []
    for _, value in enumerate(nasdaq_symbols):
        if search_term.lower() in value["name"].lower():
            response.append(value)
    return response
