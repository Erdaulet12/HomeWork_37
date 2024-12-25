from django.http import HttpResponseForbidden

ALLOWED_ADMIN_IPS = ['123.456.789.000']


class AdminIPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/secure-admin/') and request.META['REMOTE_ADDR'] not in ALLOWED_ADMIN_IPS:
            return HttpResponseForbidden("Access denied.")
        return self.get_response(request)
