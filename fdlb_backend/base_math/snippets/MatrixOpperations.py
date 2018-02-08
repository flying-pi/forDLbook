from typing import List

from django.http import JsonResponse
from django.views import View

from core.BaseComponents import BaseSnippet, BaseTag


class MatrixScalarMull(BaseSnippet, View):
    @property
    def content_url(self) -> str:
        return 'example.com'

    @property
    def tags(self) -> List[BaseTag]:
        return []

    @property
    def display_name(self) -> str:
        return u'Множення матриць на скаляр'

    @property
    def description(self) -> str:
        return u'Множення матриць на скаляр'

    def get(self, request):
        return JsonResponse(data={'info': 'ok'})


class MatrixByMatrixMull(BaseSnippet):
    @property
    def content_url(self) -> str:
        return 'example.com'

    @property
    def tags(self) -> List[BaseTag]:
        return []

    @property
    def display_name(self) -> str:
        return u'Множення матриць на матрицю'

    @property
    def description(self) -> str:
        return u'Множення матриць на матрицю'
