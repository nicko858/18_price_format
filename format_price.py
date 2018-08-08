import locale
import argparse


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
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    try:
        return locale.format('%d', float(price), grouping=True)
    except (ValueError, TypeError):
        return None


if __name__ == '__main__':
    args = get_args()
    price = args.price
    print(format_price(price))
