import datetime
import unittest
from unittest.mock import patch
from stock_api.stock_apis import get_prices


class TestGetPricesFunction(unittest.TestCase):
    @patch("requests.get")
    def test_get_prices_success(self, mock_requests_get):
        mock_response = {
            "chart": {
                "result": [
                    {
                        "timestamp": [1633406400, 1633084800],
                        "indicators": {
                            "quote": [
                                {
                                    "high": [150.0, 155.0],
                                    "low": [140.0, 145.0],
                                    "close": [145.0, 150.0],
                                    "open": [140.0, 145.0],
                                }
                            ]
                        },
                    }
                ]
            }
        }
        mock_requests_get.return_value.status_code = 200

        mock_requests_get.return_value.json.return_value = mock_response

        result = get_prices(symbol="AAPL", intv="1wk", rng="1d", ohlc="high")

        expected_result = [
            [datetime.datetime.fromtimestamp(1633406400).ctime(), 150.0],
            [datetime.datetime.fromtimestamp(1633084800).ctime(), 155.0],
        ]
        self.assertEqual(result, expected_result)

    @patch("requests.get")
    def test_get_prices_error(self, mock_requests_get):
        mock_requests_get.return_value.status_code = 404
        result = get_prices(symbol="AAPL", intv="1wk", rng="1d", ohlc="high")
        expected_result = KeyError("Something went wrong")
        self.assertEqual(str(result), str(expected_result))


if __name__ == "__main__":
    unittest.main()
