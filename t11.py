from wsgiref.simple_server import  make_server
def app(environ,start_response):
    from io import StringIO
    stdout = StringIO()
    print('Hello world!',file=stdout)
    print(file=stdout)
    h = sorted(environ.items())
    for k,v in h:
        if k.startswith('HTTP_'):
            print(k,'=',repr(v),file=stdout)
    start_response("200 ok", [('Content-Type','text/plain; charset=utf-8')]) # app 1 start_response
    return [stdout.getvalue().encode("utf-8"), b'abc~~~~~']     # 可迭代对象 内部是内容 最后拼接

return_res = b'abcd~~~~~~~~~~'
def app(environ,start_response): # 1 function
    start_response("200 ok", [('Content-Type','text/plain; charset=utf-8')])
    return [return_res]

class App:
    def __init__(self,environ,start_response):
        self.e=environ
        self.sr=start_response
    pass
    def __iter__(self):
        self.sr('200 ok', [('Content-Type','text/plain; charset=utf-8')])
        yield from [b'mn~~~~~~~',b'opq']

class Application:  # instance
    def __call__(self, environ,start_response):
        start_response("200 ok", [('Content-Type', 'text/plain; charset=utf-8'),
                                  ('X-server','MyApplication')])
        ret = []
        for k,v in environ.items():
            if k.startswith('HTTP') or k.startswith('REQUEST') or k in ('REQUEST_STRING','PATH_INFO'):
                ret.append("{} = {}\n".format(k,v).encode())

        return ret
        pass
ws = make_server('127.0.0.1',9999,Application())
ws.serve_forever()