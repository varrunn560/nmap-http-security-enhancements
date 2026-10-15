# Test Results

## Environment
- Nmap: 7.94SVN
- Python: 3.12.3
- Target: Local HTTP test server on 127.0.0.1:8000
- Test type: Controlled local testing

## Enhancement 1: Cookie Security Attribute Audit

| Test | Expected result | Observed result |
|---|---|---|
| /good | Detect Secure, HttpOnly and SameSite attributes independently | Passed |
| /weak | Do not mistake `secure_id` for the Secure attribute | Passed |
| /weak | Flag SameSite=None without Secure | Passed |
| /expires | Preserve cookie parsing when Expires contains a comma | Passed |

## Notes
The test server was accessed locally. These tests validate the listed
cases only; they do not establish coverage of every possible HTTP response
or cookie-header representation.

## Enhancement 2: HSTS and CSP Policy Audit

### Environment
- Nmap: 7.94SVN
- HTTPS test server: Python 3.12.3
- Target: 127.0.0.1:8443
- TLS: Local self-signed certificate

### Results

| Test | Expected result | Observed result |
|---|---|---|
| /good | Recognize valid HSTS and selected CSP directives | Passed |
| /zero | Detect HSTS max-age=0 | Passed |
| /invalid | Detect invalid HSTS max-age | Passed |
| /invalid | Flag unsafe-inline and wildcard CSP source | Passed |
| /zero and /invalid | Identify absent selected CSP directives | Passed |

### Limitations
Tests used controlled local HTTP and HTTPS responses. Results validate
the listed cases only. They do not establish exhaustive HTTP header
parsing, browser behavior, or exploitability of reported policy findings.
The local TLS certificate was self-signed.
