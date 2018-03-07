from typing import List

import numpy as np
import pandas as pd
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from core.base_components import BaseSnippet, BaseTag, SimpleLayout
from core.models import RawUserFile
from core.snippets_view.simple_view import LabelView, ScalarView, UploadFile, ButtonView


class SimpleNeuralNetworkCreator(BaseSnippet):

    @property
    def layout(self) -> SimpleLayout:
        return (
            SimpleLayout(view_id='root')
                .add(LabelView(value=_('Enter network shape in next format :: `number neuron on first layer '
                                       'layer;number neuron on second hiden layer;....;number neuron on output '
                                       'layer`')))
                .add(ScalarView(view_id='matrix_shape', value='784;40;10'))
                .add(LabelView(value=_('label column name')))
                .add(ScalarView(view_id='label_column_name', value='label'))
                .add(UploadFile(view_id='train_data'))
                .add(ButtonView(view_id='learn', text=_('Learn!!'), on_submit=self.on_learn))
                .add(LabelView(view_id='learning_accuracy', value=_('accuracy'), visible=False))
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

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_delta(self, z):
        return self.sigmoid(z) * (1 - self.sigmoid(z))

    def transform_results(self, scalar_result):
        shortcut = np.eye(int(self.matrix_shape.value.split(';')[-1]))
        return np.array([shortcut[i] for i in scalar_result])

    def cost(self, input: np.ndarray, theta: List[np.ndarray], espect: np.ndarray, lambda_value=0.01):
        a = input
        m = input.shape[0]
        layer_z = []
        layer_a = []
        for t in theta:
            z = np.insert(a, a.shape[1], 1, axis=1).dot(t)
            layer_z.append(z)
            a = self.sigmoid(z)
            layer_a.append(a)
        layer_z = list(reversed(layer_z))
        cost = (sum(espect[i].dot(np.log(a[i].transpose())) + (1 - espect[i]).dot(np.log(1 - a[i].transpose()))
                    for i in range(a.shape[0])) / (-m) +
                sum(np.sum(t ** 2) for t in theta) * lambda_value / (2 * m))
        delta = [(a-espect)]
        for i in reversed(range(1,len(theta))):
            delta.append(np.delete(theta[i],-1,axis=0).transpose().dot(delta[-1].transpose())*self.sigmoid_delta(layer_z[i]))
        return a

    def on_learn(self):
        if not self.train_data.value:
            # show some error message
            pass
        filepath = RawUserFile.objects.get(id=int(self.train_data.value)).filename
        data = pd.read_csv(filepath, delimiter=',')
        results = data['label'].values
        y = self.transform_results(results)
        data = data.loc[:, data.columns != self.label_column_name.value].values

        given_layer_shape = list(map(lambda x: int(x), self.matrix_shape.value.split(';')))
        theta = []
        for i in range(1, len(given_layer_shape)):
            theta.append(np.random.rand(given_layer_shape[i - 1] + 1, given_layer_shape[i]))
        coust = self.cost(data, theta, y)
        a = 0
