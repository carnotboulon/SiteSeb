import tornado.ioloop
import tornado.web
import tornado.template as tem

class MainHandler(tornado.web.RequestHandler):
    def get(self):     
        loader = tem.Loader("/home/pi/Github/SiteSeb/web")
        self.write(loader.load("index.html").generate(data=""))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/(favicon.ico)', tornado.web.StaticFileHandler, {"path": ""}),
        (r'/(.*)', tornado.web.StaticFileHandler, {"path": "web/"}),
        ],
        debug=True                           
    )
if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
