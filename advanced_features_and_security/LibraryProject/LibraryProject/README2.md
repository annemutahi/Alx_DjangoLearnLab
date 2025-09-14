# Security Configuration Notes

This Django application implements multiple layers of security:

1. **Django Settings**
   - DEBUG = False → Prevents sensitive debug info exposure.
   - SECURE_CONTENT_TYPE_NOSNIFF, SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS → Browser-side protections against XSS/clickjacking.
   - CSRF_COOKIE_SECURE, SESSION_COOKIE_SECURE → Enforce HTTPS-only cookies.

2. **Permissions & Groups**
   - Custom model permissions (can_create, can_edit, can_delete).
   - Views are protected using @permission_required decorators.

3. **Content Security Policy (CSP)**
   - Limits sources for JS, CSS, fonts, and images.
   - Reduces XSS attack surface.

4. **Safe Input Handling**
   - All user input handled via Django ORM and Forms to prevent SQL injection and unsafe queries.

---

# Testing Security

## Manual Tests
- **XSS Test**: Enter `<script>alert(1)</script>` in input fields. Expected: script should not execute; CSP blocks inline JS.
- **CSRF Test**: Try submitting a form without a valid CSRF token. Expected: Request should be rejected with 403.
- **Permissions Test**: Log in with different user roles (e.g., no `can_edit` permission) and attempt restricted actions. Expected: Access denied.
- **HTTPS Cookie Test**: Inspect cookies in browser dev tools → verify `Secure` flag is set.

## Next Steps
- Run automated security scans with `bandit` (Python) or OWASP ZAP.
- Continuously review whitelisted CSP domains to avoid overexposure.
