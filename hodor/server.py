import json
import tornado.ioloop
import tornado.web

from hodor import Hodor

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("POST with the {'url':<url>, 'config':<config>}")

    def post(self):
        body = json.loads(self.request.body)
        hodor = Hodor(**body)
        self.write(hodor.data)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
