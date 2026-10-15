from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)

        if self.path == "/good":
            self.send_header(
                "Set-Cookie",
                "session=abc; Path=/; Secure; HttpOnly; SameSite=Strict"
            )
            self.send_header(
                "Set-Cookie",
                "prefs=dark; Path=/; Secure; SameSite=Lax"
            )

        elif self.path == "/weak":
            self.send_header("Set-Cookie", "secure_id=abc; Path=/")
            self.send_header(
                "Set-Cookie",
                "legacy=abc; Path=/; SameSite=None"
            )

        elif self.path == "/expires":
            self.send_header(
                "Set-Cookie",
                "session=abc; Expires=Wed, 21 Oct 2026 07:28:00 GMT; HttpOnly"
            )
            self.send_header(
                "Set-Cookie",
                "prefs=dark; Path=/; SameSite=Lax"
            )

        if self.path == "/policy-good":
            self.send_header(
                "Strict-Transport-Security",
                "max-age=31536000; includeSubDomains; preload"
            )
            self.send_header(
                "Content-Security-Policy",
                "default-src 'self'; script-src 'self'; "
                "object-src 'none'; frame-ancestors 'none'"
            )

        elif self.path == "/policy-weak":
            self.send_header(
                "Strict-Transport-Security",
                "max-age=0"
            )
            self.send_header(
                "Content-Security-Policy",
                "default-src *; script-src 'self' 'unsafe-inline' "
                "'unsafe-eval' *"
            )

        elif self.path == "/policy-invalid":
            self.send_header(
                "Strict-Transport-Security",
                "max-age=invalid"
            )
            self.send_header(
                "Content-Security-Policy",
                "script-src https://example.com"
            )

        self.send_header("Content-Type", "text/plain")
        self.end_headers()

    def log_message(self, format, *args):
        pass

HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
