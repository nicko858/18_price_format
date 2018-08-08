# Price Formatter
The program accepts the string like `3245.000000` and formats it in pretty print like `3 245`

# Quickstart

The program is represented by the module ```format_price.py```. Module ```format_price.py``` contains the following functions:

- ```format_price()```
- ```get_args()```

The program uses these libs from Python standart library:

- ```locale```
- ```argparse```

The program is covered by tests with ```unittest```- module. You can check it in module ```tests.py```


# How to Install
Python 3 should be already installed.


# How to run
The program has 2 interfaces: programm and console. To use console -interface, just run the program with price argument:
```bash
python3.5 format_price.py 1234567
```
If everything is fine, you'll see such output:
```text
1 234 567
```

To use programm interface, just import module called ```format_price```:
```python
from format_price import format_price

format_price(4356987)
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
