import unittest
from unittest.mock import MagicMock, patch
import urllib.request
import json


API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год
    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


class TestYearNow(unittest.TestCase):
    def get_mock_temporaty(self, resp):
        mock_tmp = MagicMock()
        mock_tmp.read.return_value = resp
        mock_tmp.__enter__.return_value = mock_tmp
        return mock_tmp

    @patch('urllib.request.urlopen')
    def test_first_format(self, mock_urlopen):
        resp = '{"currentDateTime": "2022-12-08T21:12Z", "utcOffset": "00:00:00"}'
        mock_urlopen.return_value = self.get_mock_temporaty(resp)
        self.assertEqual(what_is_year_now(), 2022)

    @patch('urllib.request.urlopen')
    def test_second_format(self, mock_urlopen):
        resp = '{"currentDateTime": "01.03.2022", "utcOffset": "00:00:00"}'
        mock_urlopen.return_value = self.get_mock_temporaty(resp)
        self.assertEqual(what_is_year_now(), 2022)

    @patch('urllib.request.urlopen')
    def test_wrong_data_format(self, mock_urlopen):
        resp = '{"currentDateTime": "01_03_2022"}'
        mock_urlopen.return_value = self.get_mock_temporaty(resp)
        with self.assertRaises(ValueError):
            what_is_year_now()

    @patch('urllib.request.urlopen')
    def test_wrong_json(self, mock_urlopen):
        resp = '{"CURRDateTime": "01.03.2022"}'
        mock_urlopen.return_value = self.get_mock_temporaty(resp)
        with self.assertRaises(KeyError):
            what_is_year_now()
