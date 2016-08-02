from lxml import html
import requesocks

def get_value(xpath, content):
    tree = html.fromstring(content)
    return tree.xpath(xpath)

def get(url, config={}, proxies={}, auth=None):
    session = requesocks.session()
    if len(proxies) > 0:
        session.proxies = proxies
    if auth:
        r = session.get(url, auth=auth)
    else:
        r = session.get(url)
    content = r.content
    if len(config) is 0:
        data = {'content': content}
    else:
        data = {}
        for key, xpath in config.items():
            data[key] = get_value(xpath, content)
    return data
