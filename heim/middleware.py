# heim/middleware.py
from django.utils.deprecation import MiddlewareMixin
from .models import PageVisit

class PageVisitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        url = request.path
        ip_address = request.META.get('REMOTE_ADDR')
        visit, created = PageVisit.objects.get_or_create(url=url)
        visit.add_ip_address(ip_address)

