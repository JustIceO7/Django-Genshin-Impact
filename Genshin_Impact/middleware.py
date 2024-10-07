class DisableStaticCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Add Cache-Control header to static files served by Django's static view
        if request.path.startswith('/static/'):
            response['Cache-Control'] = 'max-age=0'

        return response

class SessionCookieMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "theme_mode" not in request.session:
            request.session["theme_mode"] = "dark" 

        response = self.get_response(request)
        return response
