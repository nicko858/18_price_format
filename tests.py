import unittest
import locale
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_return_str(self):
        price = format_price(4356987)
        self.assertIsInstance(price, str)

    def test_return_none_if_letters(self):
        price = format_price('hahaha')
        self.assertIsNone(price)

    def test_return_none_if_none(self):
        price = format_price(None)
        self.assertIsNone(price)

    def test_return_price_in_locale_format(self):
        test_price = 4356987
        price = format_price(test_price)
        locale_price = locale.format('%d', test_price, grouping=True)
        self.assertIn(price, locale_price)


if __name__ == '__main__':
    unittest.main()
