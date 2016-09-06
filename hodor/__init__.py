from lxml import html
from lxml.cssselect import CSSSelector
import requesocks
import time

DEFAULT_HODOR_UA = 'Hodor 1.0'
DEFAULT_HODOR_MAX_PAGES = 100
DEFAULT_CRAWL_DELAY = 3
EMPTY_VALUES = (None, '', [], (), {})

class Hodor(object):
    def __init__(self, url, config={}, proxies={},
                 auth=None, ua=DEFAULT_HODOR_UA,
                 pagination_max_limit=DEFAULT_HODOR_MAX_PAGES,
                 crawl_delay=DEFAULT_CRAWL_DELAY,
                 ssl_verify=False,
                 trim_values=True):
        self.content = None
        self.url = url
        self.proxies = proxies
        self.auth = auth
        self.ua = ua
        self.trim_values = trim_values
        self.config = {}
        self.extra_config = {}

        self._pages = []
        self._page_count = 0
        self._pagination_max_limit = pagination_max_limit
        self._default_crawl_delay = crawl_delay

        for k, v in config.items():
            if k.startswith("_"):
                self.extra_config[k.lstrip("_")] = v
            else:
                self.config[k] = v

    def fetch(self, url):
        '''Does the requests fetching and stores result in self.content'''
        session = requesocks.session()
        headers = {'User-Agent': self.ua}
        if len(self.proxies) > 0:
            session.proxies = self.proxies
        if self.auth:
            r = session.get(url, headers=headers, auth=self.auth, verify=self.ssl_verify)
        else:
            r = session.get(url, headers=headers, verify=self.ssl_verify)
        self.content = r.content
        return self.content

    @staticmethod
    def get_value(content, rule):
        '''Returns result for a specific xpath'''
        tree = html.fromstring(content)
        data = ""

        if 'xpath' in rule:
            data = tree.xpath(rule['xpath'])
        elif 'css' in rule:
            data = [node.text_content() for node in tree.cssselect(rule['css'])]

        many = rule.get('many', True)
        if not many:
            if len(data) == 0:
                data = None
            else:
                data = data[0]

        return data

    @staticmethod
    def _group_data(data, groups):
        for dest, group_fields in groups.items():
            gdata = []
            for field in group_fields:
                gdata.append(data[field])
            data[dest] = []
            for gd in zip(*gdata):
                d = {}
                for i, field in enumerate(group_fields):
                    d[field] = gd[i]
                data[dest].append(d)
        group_fields = [field for field_set in groups.values() for field in field_set]
        for field in group_fields:
            del data[field]

    def package_pages(self):
        #TODO: Context aware packaging has to go here.
        if len(self._pages) == 1:
            self._data = self._pages[0]
        else:
            self._data = self._pages
        return self._data

    @classmethod
    def parse(cls, content, config={}, extra_config={}, trim_values=True):
        '''Parses the content based on the config set'''
        if len(config) is 0:
            _data = {'content': content}
        else:
            _data = {}
            for key, rule in config.items():
                value = cls.get_value(content, rule)
                if trim_values not in EMPTY_VALUES and value not in EMPTY_VALUES:
                    if 'many' in rule and rule['many']:
                        value = [v.strip() if isinstance(v, basestring) else v for v in value]
                    else:
                        value = value.strip() if isinstance(value, basestring) else value
                _data[key] = value

        paginate_by = extra_config.get('paginate_by')
        if paginate_by:
            paginate_by = cls.get_value(content, paginate_by)

        groups = extra_config.get('groups', {})
        if groups:
            cls._group_data(_data, groups)
        return _data, paginate_by

    def _get(self, url):
        self.fetch(url)
        return self.parse(self.content, self.config, self.extra_config, self.trim_values)

    def get(self, url=None):
        url = url if url else self.url
        self._data, paginate_by = self._get(url)

        self._pages.append(self._data)
        self._page_count += 1

        if paginate_by and self._page_count < self._pagination_max_limit:
            time.sleep(self._default_crawl_delay)
            self.get(paginate_by)

        self.package_pages()
        return self._data

    @property
    def data(self):
        if not hasattr(self, '_data'):
            self.get()
        return self._data
