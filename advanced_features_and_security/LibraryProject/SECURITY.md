HTTPS Enforcements:
DEBUG = False  # Turn off debug in production

# Redirect HTTP to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Optional browser security headers
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

Deployment on Windows:
Generating certificate...
$cert = New-SelfSignedCertificate -DnsName "localhost" -CertStoreLocation "Cert:\LocalMachine\My"
Export-Certificate -Cert $cert -FilePath "C:\certs\localhost.cer"
Export-PfxCertificate -Cert $cert -FilePath "C:\certs\localhost.pfx" -Password (ConvertTo-SecureString -String "yourpassword" -Force -AsPlainText)

Serve Django with HTTPS...
pip install django-extensions Werkzeug
python manage.py runserver_plus --cert-file C:\certs\localhost.pem


Testing:
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
