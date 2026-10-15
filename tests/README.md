# Test Plan

Test the original and enhanced scripts against a controlled local server.

Scenarios:
1. Correctly configured cookie attributes.
2. Missing Secure, HttpOnly, and SameSite attributes.
3. Multiple Set-Cookie headers.
4. HSTS with a positive max-age.
5. HSTS with max-age=0.
6. Missing HSTS on HTTPS.
7. CSP with restrictive directives.
8. CSP with potentially unsafe directives.
9. Missing CSP directives.

Record the actual command, response configuration, and observed output
for every test. Do not treat expected output as observed output.
