from typing import List

from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from core.base_components import BaseSnippet, BaseTag, SimpleLayout
from core.snippets_view.simple_view import MatrixView, ScalarView, LabelView, ButtonView


class MatrixScalarMull(BaseSnippet):

    @property
    def layout(self) -> SimpleLayout:
        return SimpleLayout().add(
            LabelView(value=_('Matrix mull by scalar'))
        ).add(
            MatrixView(view_id='matrix')
        ).add(
            LabelView(value=_('mull by:'))
        ).add(
            ScalarView(view_id='scalar')
        ).add(
            ButtonView(view_id='calculate', value=_('Calculate!!'), on_submit=self.on_submit)
        )

    @property
    def content_url(self) -> str:
        return reverse('base_math:create_user')

    @property
    def tags(self) -> List[BaseTag]:
        return []

    @property
    def display_name(self) -> str:
        return u'Множення матриць на скаляр'

    @property
    def description(self) -> str:
        return u'Множення матриць на скаляр'

    def on_submit(self):
        print("submited")

    def process_request(self, data) -> SimpleLayout:
        scalar = float(data['scalar'])
        return SimpleLayout().add(MatrixView(
            label=_('Matrix: '),
            view_id='matrix',
            value=[[float(cell) * scalar for cell in row] for row in data['matrix']],
            editable=False,
        ))


class MatrixByMatrixMull(BaseSnippet):
    @property
    def layout(self) -> SimpleLayout:
        return SimpleLayout()

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
