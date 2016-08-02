# Hodor

A simple html scraper with xpath.

## Usage
```
from hodor import Hodor
config = {'src': '/html/body/div[1]/nav/div/div[1]/a/img/@src',
          'width': '/html/body/div[1]/nav/div/div[1]/a/img/@width'}
h = Hodor(url='https://www.compile.com', config=config)
h.data
```

It also takes arguments:

- ```proxies``` (check requesocks)
- ```auth```

## Result
```
{'src': ['/img/compile-logo-white.1002b288.svg'], 'width': ['100px']}
```

![DO one thing](https://pbs.twimg.com/media/CjSN_N5XIAEmnc0.jpg)
