import argparse
from decimal import Decimal
from decimal import InvalidOperation
from decimal import ROUND_05UP


def get_args():
    script_usage = "python format_price.py <price>"
    parser = argparse.ArgumentParser(
        description="How to run format_price.py:",
        usage=script_usage
    )
    parser.add_argument(
        "price",
        type=str,
        help="Specify the price"
    )
    args = parser.parse_args()
    return args


def format_price(price):
    try:
        if float.is_integer(float(price)):
            return "{:,}".format(
                Decimal(str(price)).normalize()).replace(",", " ")
        else:
            return "{:,}".format(
                Decimal(str(price)).quantize(
                    Decimal("1.00"), ROUND_05UP)
            ).replace(",", " ")
    except (ValueError, TypeError, InvalidOperation):
        return None


if __name__ == "__main__":
    args = get_args()
    price = args.price
    print(format_price(price))
