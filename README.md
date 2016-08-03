# Hodor

A simple html scraper with xpath.

## Usage

### As python package
```
from hodor import Hodor
config = {'src': {'xpath': '/html/body/div[1]/nav/div/div[1]/a/img/@src', 'many':False},
          'width': {'xpath': '/html/body/div[1]/nav/div/div[1]/a/img/@width', 'many':True}]
h = Hodor(url='https://www.compile.com', config=config)
h.data
```

It also takes arguments:

- ```ua``` (User-Agent)
- ```proxies``` (check requesocks)
- ```auth```

### As tornado service

#### Server
```
python server.py
```

### Client
```
curl -X POST -H "Content-Type: application/json" -d '{"url":"https://compile.com", "config":{"src": {"xpath": "/html/body/div[1]/nav/div/div[1]/a/img/@src"}, "width": {"xpath": "/html/body/div[1]/nav/div/div[1]/a/img/@width"}}}' "http://localhost:8888/"
```


## Result
```
{'src': '/img/compile-logo-white.1002b288.svg', 'width': ['100px']}
```

![DO one thing](https://pbs.twimg.com/media/CjSN_N5XIAEmnc0.jpg)
