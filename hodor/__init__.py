from lxml import html
from lxml.cssselect import CSSSelector
import requesocks

DEFAULT_HODOR_UA = 'Hodor 1.0'
DEFAULT_HODO_MAX_PAGES = 100

class Hodor(object):
    def __init__(self, url, config={}, proxies={}, auth=None, ua=DEFAULT_HODOR_UA, trim_values=True):
        self.content = None
        self.url = url
        self.proxies = proxies
        self.auth = auth
        self.ua = ua
        self.trim_values = trim_values
        self.config = {}
        self.extra_config = {}

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
            r = session.get(url, headers=headers, auth=self.auth, verify=False)
        else:
            r = session.get(url, headers=headers, verify=False)
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

    @classmethod
    def parse(cls, content, config={}, extra_config={}, trim_values=True):
        '''Parses the content based on the config set'''
        if len(config) is 0:
            _data = {'content': content}
        else:
            _data = {}
            for key, rule in config.items():
                value = cls.get_value(content, rule)
                if trim_values and value:
                    if rule['many']:
                        value = [v.strip() if isinstance(v, basestring) else v for v in value]
                    else:
                        value = value.strip() if isinstance(value, basestring) else value
                _data[key] = value

        next = extra_config.get('next', None)
        if next:
            next = self.get_value(content, next)

        groups = extra_config.get('groups', {})
        if groups:
            cls._group_data(_data, groups)
        return _data, next

    def _get(self, url):
        self.fetch(url)
        return self.parse(self.content, self.config, self.extra_config, self.trim_values)

    def get(self):
        self._data, next = self._get(self.url)
        return self._data

    @property
    def data(self):
        if not hasattr(self, '_data'):
            self.get()
        return self._data
