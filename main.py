from http.server import HTTPServer,BaseHTTPRequestHandler
import sqlite3
q = sqlite3.connect("Main.db")
cur = q.cursor()

class serv(BaseHTTPRequestHandler):
    def do_GET(self):
        a = (self.requestline[5:-9])
        if(len(a)>10):
            s = a[11:].split("&")
            a = ()
            for i in s:
                _,b = i.split('=')
                a+=(b,)
            cur.execute(f"insert into reg values(?,?,?,?,?);",a)
            q.commit()
            self.send_response(100)
            self.send_header("Content-type", "text/html")
            self.wfile.write(open('eye.html', 'r+b').read())

        else:
            self.send_response(100)
            self.send_header("Content-type","text/html")
            self.wfile.write(open(a,'r+b').read())



server = HTTPServer(('127.0.0.1',80),serv)
server.serve_forever()
server.server_close()