from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)

        if self.path == "/good":
            self.send_header(
                "Strict-Transport-Security",
                "max-age=31536000; includeSubDomains; preload"
            )
            self.send_header(
                "Content-Security-Policy",
                "default-src 'self'; script-src 'self'; "
                "object-src 'none'; frame-ancestors 'none'"
            )

        elif self.path == "/zero":
            self.send_header("Strict-Transport-Security", "max-age=0")
            self.send_header(
                "Content-Security-Policy",
                "default-src 'self'"
            )

        elif self.path == "/invalid":
            self.send_header(
                "Strict-Transport-Security",
                "max-age=invalid"
            )
            self.send_header(
                "Content-Security-Policy",
                "script-src 'self' 'unsafe-inline' *"
            )

        self.send_header("Content-Type", "text/plain")
        self.end_headers()

    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", 8443), Handler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(
    "tests/certs/cert.pem",
    "tests/certs/key.pem"
)
server.socket = context.wrap_socket(server.socket, server_side=True)
server.serve_forever()
