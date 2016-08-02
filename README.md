# Hodor

A simple html scraper with xpath.

## Usage
```
import hodor
config = {'src':'/html/body/div[1]/nav/div/div[1]/a/img/@src',
'width': '/html/body/div[1]/nav/div/div[1]/a/img/@width'}
hodor.get(url='https://www.compile.com', config=config)
```

```
{'src': ['/img/compile-logo-white.1002b288.svg'], 'width': ['100px']}
```

It also takes arguments:

- ```proxies``` (check requesocks)
- ```auth```


![DO one thing](https://pbs.twimg.com/media/CjSN_N5XIAEmnc0.jpg)
