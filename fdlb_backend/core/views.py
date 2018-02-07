from urllib.request import Request

from django.http import JsonResponse
from django.views import View

from core.snippet_utils import get_installed_snippets, snippets_list_serialization


class RootView(View):

    def get(self, request: Request) -> JsonResponse:
        snippets = snippets_list_serialization(get_installed_snippets())
        return JsonResponse(data={'snippets': snippets})
