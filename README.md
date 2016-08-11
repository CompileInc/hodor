# Hodor

A simple html scraper with xpath.

## Usage

### As python package
```
from hodor import Hodor
config = {'src': {'xpath': '/html/body/div[1]/nav/div/div[1]/a/img/@src', 'many':False},
          'width': {'xpath': '/html/body/div[1]/nav/div/div[1]/a/img/@width', 'many':True},
          'heading': {'css': '.container.homepage-hero h1 strong', 'many': False}
         }
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
docker-compose up
```

### Client
```
curl -X POST -F "url=https://www.compile.com/" -F "config={\"src\": {\"css\": \"strong\", \"many\":false}, \"width\": {\"xpath\": \"/html/body/div[1]/nav/div/div[1]/a/img/@width\", \"many\":false}}" "http://localhost:8888"
```


## Result
```
{'src': '/img/compile-logo-white.1002b288.svg', 'width': ['100px']}
```

![DO one thing](https://pbs.twimg.com/media/CjSN_N5XIAEmnc0.jpg)
