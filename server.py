import json
import tornado.httpserver
import tornado.ioloop
import tornado.web

from hodor import Hodor

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("server/index.html")

    def post(self):
        body = json.loads(self.request.body)
        hodor = Hodor(**body)
        self.write(hodor.data)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def main():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
