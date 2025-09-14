class ContentSecurityPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self' cdn.jsdelivr.net; "
            "style-src 'self' fonts.googleapis.com; "
            "font-src 'self' fonts.gstatic.com; "
            "img-src 'self' data: cdn.example.com"
        )
        return response