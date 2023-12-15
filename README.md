# EasyStocksData

A python module that gives stock price data and stock symbols.

pypi project : https://pypi.org/project/easystockdata/

## Installation

Install `easystocksdata` using `pip`:

```{.sourceCode .bash}
$ pip install easystockdata
```

## Description of functions

### get_prices :

- Input:

  `symbol` : Symbol of stock (string)

  `intv` : Interval of time (string, optional, default=1d)

  `rng` : Range of time (string, optional, default=1wk)

  `intv` and `rng` both takes values from `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`, `1h`, `1d`, `5d`, `1wk`, `1mo` and `3mo`.

  `ohlc` : Specify High, Low, Open and Close prices (string, optional, default='high')

  `stock_exc` : specify stock exchange to get data from (string, optional, default='nse')

- Output:
  list: A list of lists containing the timestamp and corresponding price for each data point.

### get_nse_symbols :

- Input: None

- Output: A list of dictionaries containing the stock names and symbols of nse.

### get_nasdaq_symbols :

- Input: None

- Output: A list of dictionaries containing the stock names and symbols of nasdaq.

### find_nse_stock :

- Input:

  `search_term` : search term to search for stock symbol in nse (string)

- Output: A list of dictionaries containing the stock names and symbols of nse.

### find_nasdaq_stock :

- Input:

  `search_term` : search term to search for stock symbol in nse (string)

- Output: A list of dictionaries containing the stock names and symbols of nasdaq.
