from typing import List

from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from core.base_components import BaseSnippet, BaseTag, SimpleLayout
from core.snippets_view.simple_view import LabelView, ScalarView, UploadFile


class SimpleNeuralNetworkCreator(BaseSnippet):

    @property
    def layout(self) -> SimpleLayout:
        return (
            SimpleLayout(view_id='root')
                .add(LabelView(value=_(
                    'Enter network shape in next format :: `number neuron on input layer;number neuron on first '
                    'layer;....;number neuron on output layer`'))
                )
                .add(ScalarView(view_id='matrix_shape'))
                .add(UploadFile(view_id='train_data'))
        )

    @property
    def content_url(self) -> str:
        return reverse('supervisor_neural_network:simple_neural_network_creator')

    @property
    def tags(self) -> List[BaseTag]:
        return []

    @property
    def display_name(self) -> str:
        return _(u'Simple Neural Network Creator')

    @property
    def description(self) -> str:
        return _(u'Simple Neural Network Creator')
