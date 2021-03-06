from typing import List

from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from core.base_components import BaseSnippet, BaseTag, SimpleLayout
from core.snippets_view.simple_view import MatrixView, ScalarView, LabelView, ButtonView


class MatrixScalarMull(BaseSnippet):

    @property
    def layout(self) -> SimpleLayout:
        return (
            SimpleLayout(view_id='root')
                .add(LabelView(value=_('Matrix mull by scalar')))
                .add(MatrixView(view_id='matrix'))
                .add(LabelView(value=_('mull by:')))
                .add(ScalarView(view_id='scalar'))
                .add(ButtonView(view_id='calculate', text=_('Calculate!!'), on_submit=self.on_submit))
                .add(LabelView(view_id='result_label', value=_('Result'), visible=False))
                .add(MatrixView(view_id='result_matrix', visible=False, editable=False))
        )

    @property
    def content_url(self) -> str:
        return reverse('base_math:matrix_scalar_mull')

    @property
    def tags(self) -> List[BaseTag]:
        return []

    @property
    def display_name(self) -> str:
        return _(u'Множення матриць на скаляр')

    @property
    def description(self) -> str:
        return _(u'Множення матриць на скаляр')

    def on_submit(self):
        scalar = self.scalar.value
        self.result_matrix.value = [[c * scalar for c in r] for r in self.matrix.value]
        self.result_matrix.visible = True
        self.result_label.visible = True


class MatrixByMatrixMull(BaseSnippet):

    @property
    def layout(self) -> SimpleLayout:
        return (
            SimpleLayout(view_id='root')
                .add(LabelView(value=_('Matrix mull by matrix')))
                .add(MatrixView(view_id='matrix_a'))
                .add(LabelView(value=_('mull by:')))
                .add(MatrixView(view_id='matrix_b'))
                .add(ButtonView(view_id='calculate', text=_('Calculate!!'), on_submit=self.on_submit))
                .add(LabelView(view_id='result_label', value=_('Result'), visible=False))
                .add(MatrixView(view_id='result_matrix', visible=False, editable=False))
        )

    @property
    def content_url(self) -> str:
        return reverse('base_math:matrix_matrix_mull')

    @property
    def tags(self) -> List[BaseTag]:
        return []

    @property
    def display_name(self) -> str:
        return _(u'Множення матриць на матрицю')

    @property
    def description(self) -> str:
        return _(u'Множення матриць на матрицю')

    def on_submit(self):
        a = self.matrix_a.value
        b = self.matrix_b.value

        error_message = None
        if len(a) == 0 or len(a[0]) == 0 or len(b) == 0 or len(b[0]) == 0:
            error_message = _("Can not mull zero matrix")
        elif len(a[0]) != len(b):
            error_message = _("Count of the column first matrix must be equal to count of the rows second matrix")

        if error_message is not None:
            self.result_label.visible = True
            self.result_label.value = error_message
            return

        result = [[sum([a[i][r]*b[r][j] for r in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]
        self.result_matrix.value = result
        self.result_matrix.visible = True
        self.result_label.visible = True