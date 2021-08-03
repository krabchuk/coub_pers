from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl


class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        print(self.requestline)


def main():
    port = 443
    adress = ('localhost', port)
    server = HTTPServer(adress, EchoHandler)
    server.socket = ssl.wrap_socket(server.socket, certfile='../certs/server.pem', server_side=True)
    server.serve_forever()

main()
