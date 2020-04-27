# from tornado import ioloop,web
import json

import tornado.web
import tornado.ioloop
import tornado.options
from tornado.httputil import HTTPServerRequest


class IndexHandler(tornado.web.RequestHandler):
    # 不需要調用request方法，在繼承的RequestHandler里有包含的attr對象
    # 使用 get_argument類內置方法獲取
    # 函數名需要顯式地代表受到的請求方法method
    def get(self):
        # 讀取多個參數名相同的參數,返回list['haha', 'xixi']
        wd = self.get_arguments('wd')

        # 從查詢參數中讀取url路徑參數,針對get請求
        wd2 = self.get_query_argument('wd')
        print(wd2)
        wd3 = self.get_query_arguments('title')
        print(wd3)

        # 從請求對象self.request中讀取參數,但所有數據都是字典，所有數據都是字節碼:[b'haha', b'xixi']
        # wd3事前聲明類型
        # 不建議使用這種方法
        # 但在充分了解的情況下使用非常方便
        req: HTTPServerRequest = self.request
        wd3 = req.arguments.get('wd')
        wd3 = req.query_arguments.get('wd')

        print(wd3)

    def post(self):
        data = self.get_argument('data')
        print(data)
        self.write('<h1>I am post method</h1>')

    def put(self):
        # get_body_argument直接獲取表單參數/form一類的
        name = self.get_body_argument('form1')
        print(name)
        self.write('<h1>I am put method</h1>')

    def delete(self):
        self.write('<h1>I am delete</h1>')

class SearchHandler(tornado.web.RequestHandler):
    mapper = {
        1:'group 1 goods',
        2:'group 2 goods',
        3:'Python is the most popular programming language',
        4:"oldest fashion",
        5:'most use html language'
    }

    def get(self,word, wd):
        html = '''
            <h3>搜索%s結果</h3>
            <p>
                group:%s<br>
                result:%s<br>
            </p>
        '''
        result = self.mapper.get(int(wd))

        # self.write(html %(wd,result))
        # tornado jsonify
        # resp_data = {
        #     'title':wd, debugger (bu
        #     'data':result
        # }
        self.write(html % (wd,word,result))
        # self.write(json.dumps(resp_data))
        self.set_header('Content-type','text/html;charset=utf-8')
        self.set_status(200)
        self.set_cookie('keyword',wd)

class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        handler_ = self.get_query_argument('name')
        # 從請求部獲取Cookie
        value = self.get_cookie(handler_)

        if value:
            print(type(value))
            self.write(value)
        else:
            all_cookies = self.request.cookies
            res = dict()
            for key in all_cookies:
                res[key]=self.get_cookie(key)
            print(res)
            self.write(res)

    def delete(self):
        handler = self.request.cookies


def make_app():
    # create and return an app
    return tornado.web.Application([
        ('/', IndexHandler),
        (r'/search/(?P<word>\w+)/(?P<wd>\w+)', SearchHandler),
        ('/cookie', CookieHandler)
    ], default_host=tornado.options.options.host)


if __name__ == '__main__':
    # define command option
    tornado.options.define('port',default=7000,
                           type=int,
                           help='bind socket port')
    tornado.options.define('host',
                           default='localhost',
                           type=str,
                           help='sets hostname')
    # capable
    tornado.options.parse_command_line()


    app = make_app()
    app.listen(tornado.options.options.port)

    print("start http://localhost:7000")
    #start server
    tornado.ioloop.IOLoop.current().start()