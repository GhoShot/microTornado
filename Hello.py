# coding: utf-8

from tornado.web import Application
#運行管理
from tornado.ioloop import IOLoop
#資源處理類
from tornado.web import RequestHandler

#創建請求處理類
class IndexHandler(RequestHandler):
    def get(self):
        #Response to client
        self.write('<h1>Hello Tornado</h1>')

if __name__ == '__main__':
    app = Application(handlers= [
        ('/',IndexHandler)
    ])

    #bind port
    port  = 7000
    app.listen(port)

    #start wen server
    print('starting http://localhost:%s' % port)
    IOLoop.current().start()