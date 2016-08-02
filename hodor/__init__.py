from lxml import html
import requesocks

class Hodor(object):
    def __init__(self, url, config={}, proxies={}, auth=None):
        self.content = None
        self.url = url
        self.config = config
        self.proxies = proxies
        self.auth = auth

    def fetch(self):
        '''Does the requests fetching and stores result in self.content'''
        session = requesocks.session()
        if len(self.proxies) > 0:
            session.proxies = proxies
        if self.auth:
            r = session.get(self.url, auth=self.auth)
        else:
            r = session.get(self.url)
        self.content = r.content
        return self.content

    @staticmethod
    def get_value(content, rule):
        '''Returns result for a specific xpath'''
        tree = html.fromstring(content)
        data = tree.xpath(rule['xpath'])

        many = rule.get('many', True)
        if not many:
            if len(data) == 0:
                data = None
            else:
                data = data[0]

        return data

    @classmethod
    def parse(cls, content, config={}):
        '''Parses the content based on the config set'''
        if len(config) is 0:
            _data = {'content': content}
        else:
            _data = {}
            for key, rule in config.items():
                _data[key] = cls.get_value(content, rule)
        return _data

    def get(self):
        self.fetch()
        self._data = self.parse(self.content, self.config)
        return self._data

    @property
    def data(self):
        if not hasattr(self, '_data'):
            self.get()
        return self._data
