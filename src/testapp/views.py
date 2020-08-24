"""Views for Testapp"""

from django.views import View
from django.http import HttpResponse


class Pong(View):
    """Respond to ping requests"""

    def get(self, request):
        """Handle get request"""
        return HttpResponse("pong")
