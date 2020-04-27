#Tornado 微服務搭建
#1、搭建：tornado的請求與相應
###1.1請求的參數如何獲取
來源：
1 RequestHandler對象中提供的方法
2 RequestHandler對象的request對象(HTTPServerRequest類的對象)的字典獲取

self.get_argument()/self.get_arguments() 可以獲取人一請求方式的請求參數
self.get_query_argument()/s 可以get請求的查詢參數

Tornado中設定的獲取參數沒有獲取時返回400
Flask不會報錯，參數會返回None

###1.2請求對象中包含那些信息
###1.3Cookie和Header如何設置
