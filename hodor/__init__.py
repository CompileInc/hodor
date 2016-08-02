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

    def get_value(self, xpath):
        '''Returns result for a specific xpath'''
        tree = html.fromstring(self.content)
        return tree.xpath(xpath)

    def parse(self):
        '''Parses the content based on the config set and stores in _data'''
        if self.content is None:
            self.fetch()
        if len(self.config) is 0:
            self._data = {'content': self.content}
        else:
            self._data = {}
            for key, xpath in self.config.items():
                self._data[key] = self.get_value(xpath)
        return self._data

    def get(self):
        return self.parse()

    @property
    def data(self):
        if not hasattr(self, '_data'):
            self.parse()
        return self._data
