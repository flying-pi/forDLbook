from typing import List

from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from core.base_components import BaseSnippet, BaseTag, SimpleLayout
from core.snippets_view.simple_view import LabelView


class SimpleNeuralNetwork(BaseSnippet):

    @property
    def layout(self) -> SimpleLayout:
        return (
            SimpleLayout(view_id='root')
                .add(LabelView(value=_('Stub')))
        )

    @property
    def content_url(self) -> str:
        return reverse('supervisor_neural_network:simple_neural_network')

    @property
    def tags(self) -> List[BaseTag]:
        return []

    @property
    def display_name(self) -> str:
        return _(u'Simple Neural Network')

    @property
    def description(self) -> str:
        return _(u'Simple Neural Network')
