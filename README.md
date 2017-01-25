

# Hodor [![PyPI](https://img.shields.io/pypi/v/hodorlive.svg?maxAge=2592000?style=plastic)](https://pypi.python.org/pypi/hodorlive/)

A simple html scraper with xpath or css.

## Install

```pip install hodorlive```

## Usage

### As python package

***WARNING: This package by default doesn't verify ssl connections. Please check the [arguments](#arguments) to enable them.***

#### Sample code
```python
from hodor import Hodor
from dateutil.parser import parse


def date_convert(data):
    return parse(data)

url = 'http://www.nasdaq.com/markets/stocks/symbol-change-history.aspx'

CONFIG = {
    'old_symbol': {
        'css': '#SymbolChangeList_table tr td:nth-child(1)',
        'many': True
    },
    'new_symbol': {
        'css': '#SymbolChangeList_table tr td:nth-child(2)',
        'many': True
    },
    'effective_date': {
        'css': '#SymbolChangeList_table tr td:nth-child(3)',
        'many': True,
        'transform': date_convert
    },
    '_groups': {
        'data': '__all__',
        'ticker_changes': ['old_symbol', 'new_symbol']
    },
    '_paginate_by': {
        'xpath': '//*[@id="two_column_main_content_lb_NextPage"]/@href',
        'many': False
    }
}

h = Hodor(url=url, config=CONFIG, pagination_max_limit=5)

h.data
```
#### Sample output
```python
{'data': [{'effective_date': datetime.datetime(2016, 11, 1, 0, 0),
           'new_symbol': 'ARNC',
           'old_symbol': 'AA'},
          {'effective_date': datetime.datetime(2016, 11, 1, 0, 0),
           'new_symbol': 'ARNC$',
           'old_symbol': 'AA$'},
          {'effective_date': datetime.datetime(2016, 8, 16, 0, 0),
           'new_symbol': 'MALN8',
           'old_symbol': 'AHUSDN2018'},
          {'effective_date': datetime.datetime(2016, 8, 16, 0, 0),
           'new_symbol': 'MALN9',
           'old_symbol': 'AHUSDN2019'},
          {'effective_date': datetime.datetime(2016, 8, 16, 0, 0),
           'new_symbol': 'MALQ6',
           'old_symbol': 'AHUSDQ2016'},
          {'effective_date': datetime.datetime(2016, 8, 16, 0, 0),
           'new_symbol': 'MALQ7',
           'old_symbol': 'AHUSDQ2017'},
          {'effective_date': datetime.datetime(2016, 8, 16, 0, 0),
           'new_symbol': 'MALQ8',
           'old_symbol': 'AHUSDQ2018'}]}
```

#### Arguments

- ```ua``` (User-Agent)
- ```proxies``` (check requesocks)
- ```auth```
- ```crawl_delay``` (crawl delay in seconds across pagination - default: 3 seconds)
- ```pagination_max_limit``` (max number of pages to crawl - default: 100)
- ```ssl_verify``` (default: False)
- ```robots``` (if set respects robots.txt - default: True)
- ```reppy_capacity``` (robots cache LRU capacity - default: 100)
- ```trim_values``` (if set trims output for leading and trailing whitespace - default: True)


#### Config parameters:
- By default any key in the config is a rule to parse.
    - Each rule can be either a ```xpath``` or a ```css```
    - Each rule can extract ```many``` values by default unless explicity set to ```False```
    - Each rule can allow to ```transform``` the result with a function if provided
- Extra parameters include grouping (```_groups```) and pagination (```_paginate_by```) which is also of the rule format.


