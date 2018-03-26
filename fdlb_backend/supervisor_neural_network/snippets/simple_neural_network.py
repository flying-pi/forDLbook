from typing import List

from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from base_math.snippets.matrix_operations import MatrixByMatrixMull
from core.base_components import BaseSnippet, BaseTag, SimpleLayout
from core.snippets_view.simple_view import LabelView, SelectView, ButtonView
from supervisor_neural_network.snippets.simple_network_creator import SimpleNeuralNetworkCreator


class SimpleNeuralNetwork(BaseSnippet):

    @property
    def layout(self) -> SimpleLayout:
        return (
            SimpleLayout(view_id='root')
                .add(LabelView(value=_('Stub')))
                .add(SelectView(
                    view_id='network_select',
                    options=['a', 'b'],
                    placeholder=_('Select one of the network')
                ))
                .add(ButtonView(
                    text=_('Add network'),
                    redirect_to=SimpleNeuralNetworkCreator().content_url,
                ))
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
