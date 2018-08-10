import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_price_is_int(self):
        price = format_price(4356987)
        self.assertEqual(price, "4 356 987")

    def test_price_is_letters(self):
        price = format_price("hahaha")
        self.assertIsNone(price)

    def test_price_is_none(self):
        price = format_price(None)
        self.assertIsNone(price)

    def test_price_is_float(self):
        price = format_price(4356987.65700)
        self.assertEqual(price, "4 356 987.66")

    def test_price_is_tupple(self):
        price = format_price((1, 2, 3, 4, 5, 6))
        self.assertIsNone(price)

    def test_price_is_list(self):
        price = format_price([1, 2, 3, 4, 5, 6])
        self.assertIsNone(price)

    def test_price_is_dict(self):
        price = format_price({})
        self.assertIsNone(price)

    def test_price_is_bool(self):
        price = format_price(False)
        self.assertIsNone(price)


if __name__ == "__main__":
    unittest.main()
