from http.server import BaseHTTPRequestHandler, HTTPServer


class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        print(self.requestline)


def main():
    port = 443
    adress = ('krabchuk.me', port)
    server = HTTPServer(adress, EchoHandler)
    server.serve_forever()

main()
