# Nmap HTTP Security Header Enhancements

A cybersecurity academic project extending the official Nmap
`http-security-headers.nse` script with two independent enhancements.

## Reference Script

The original script is maintained by the Nmap project:

https://github.com/nmap/nmap/blob/master/scripts/http-security-headers.nse

## Enhancement 1: Cookie Security Attribute Audit

Analyse individual Set-Cookie headers for:
- Secure
- HttpOnly
- SameSite

Report missing attributes and configuration concerns per cookie.

## Enhancement 2: HSTS and CSP Policy Analysis

Analyse selected HSTS parameters and CSP directives to identify
potentially weak or missing security configurations.

## Repository Structure

- `scripts/`: Original reference and enhanced NSE scripts.
- `tests/`: Test setup and test cases.
- `docs/`: Test results and observations.

## Testing

Testing will be performed against a controlled local HTTP server.
Results will be documented after the scripts are implemented and run.

## Disclaimer

For educational use and authorised testing only.
