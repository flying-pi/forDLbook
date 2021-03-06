from typing import List

import numpy as np
import pandas as pd
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from sklearn.neural_network import MLPClassifier

from core.base_components import BaseSnippet, BaseTag, SimpleLayout
from core.models import RawUserFile
from core.snippets_view.simple_view import LabelView, ScalarView, UploadFile, ButtonView, SelectView
from supervisor_neural_network.models import WeightModel
import pickle


class SimpleNeuralNetworkCreator(BaseSnippet):

    @property
    def layout(self) -> SimpleLayout:
        return (
            SimpleLayout(view_id='root')
                .add(LabelView(value=_('NN Name')))
                .add(ScalarView(view_id='nn_name', value='NN'))
                .add(LabelView(value=_('Enter network shape in next format :: `number neuron on first layer '
                                       'layer;number neuron on second hiden layer;....;number neuron on output '
                                       'layer`')))
                .add(ScalarView(view_id='matrix_shape', value='784;40;40;40;40;10'))
                .add(LabelView(value=_('label column name')))
                .add(ScalarView(view_id='label_column_name', value='label'))
                .add(UploadFile(view_id='train_data'))
                .add(SelectView(view_id='learn_type',
                                selected=1,
                                options=['custom', 'scikit-learn'],
                                placeholder=_('Select type of the learning')
                                ))
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

    def train(
            self,
            input: np.ndarray,
            espect: np.ndarray,
            theta: List[np.ndarray],
            lambda_value=0.1,
            learning_rate=0.2
    ):
        a = input
        m = input.shape[0]
        layer_z = [a]
        layer_a = []
        for t in theta:
            a = np.insert(a, a.shape[1], 1, axis=1)
            layer_a.append(a)
            z = a.dot(t.T)
            layer_z.append(z)
            a = self.sigmoid(z)
        cost = (sum((np.log(a[i].transpose()).dot(espect[i])) + (np.log(1 - a[i].transpose()).dot((1 - espect[i])))
                    for i in range(a.shape[1])) / (-m) +
                sum(np.sum(t ** 2) for t in theta) * lambda_value / (2 * m))
        delta = [(a - espect)]
        for i in reversed(range(1, len(theta))):
            layer_z[i] = np.insert(layer_z[i], layer_z[i].shape[1], 1, axis=1)
            d = (delta[0].dot(theta[i]))
            d = d * self.sigmoid_delta(layer_z[i])
            d = d[:, 1:]
            delta.insert(0, d)
        for i in range(len(theta)):
            d = delta[i]
            grad = d.T.dot(layer_a[i]) / m
            grad[:, 1:] = grad[:, 1:] + (1 * lambda_value / m * (theta[i][:, 1:]))
            theta[i] = theta[i] - (grad * learning_rate)
        # https://github.com/nex3z/machine-learning-exercise/blob/master/coursera-machine-learning-python/ex4/nn_cost_function.py
        return cost

    def estimate(self, input, espect, theta):
        a = input
        for t in theta:
            a = np.insert(a, a.shape[1], 1, axis=1)
            z = a.dot(t.T)
            a = self.sigmoid(z)
        result = (a.argmax(axis=1) == espect.argmax(axis=1)).sum() / espect.shape[0]
        return result

    def read_data(self, file_id: str, group_shape=None,is_vectorize_output = True):
        if group_shape is None:
            group_shape = [0.8, 0.1, 0.1]

        for i in range(1, len(group_shape)):
            group_shape[i] += group_shape[i - 1]

        filepath = RawUserFile.objects.get(id=int(file_id)).filename
        data = pd.read_csv(filepath, delimiter=',')
        data_len = len(data)

        result = []
        for group in np.split(data, [int(i * data_len) for i in group_shape]):
            if group.shape[0] == 0:
                continue
            output = group['label'].values
            if is_vectorize_output:
                output = self.transform_results(output)
            input = group.loc[:, group.columns != self.label_column_name.value].values
            input = input / 255.0 * 2.0 - 1.0
            result.append({'input': input, 'output': output})
        return result

    def get_shape(self) -> np.ndarray:
        return np.array(list(map(lambda x: int(x), self.matrix_shape.value.split(';'))))

    def init_theta(self, shape: np.ndarray):
        return np.array([np.random.rand(shape[i], shape[i - 1] + 1) * 2 - 1 for i in range(1, len(shape))])

    def get_model_name(self):
        original_name = self.nn_name.value
        name = original_name
        i = 1
        while WeightModel.objects.filter(name=name).exists():
            name = original_name + str(i)
            i += 1
        return name

    def custom_learn_process(self):
        if not self.train_data.value:
            # show some error message
            pass
        # data = self.read_data(self.train_data.value, group_shape=[0.8, 0.01, 0.2])
        data = self.read_data(self.train_data.value)
        shape = self.get_shape()
        theta = self.init_theta(shape)
        train = data[0]
        test = data[2]
        estimation = 0

        rate_value = 0.001
        lambda_value = 0.0001
        for i in range(10000):
            self.train(train['input'], train['output'], theta, lambda_value=lambda_value, learning_rate=rate_value)
            if i % 5 == 0:
                estimation = self.estimate(test['input'], test['output'], theta)
                print("estimation: %s", estimation)



        serialized_shape = shape.tobytes()
        serialized_theta = theta.tobytes()

        WeightModel.objects.create(
            name=self.model_name,
            classificator_provider='custom',
            shape=serialized_shape,
            body=serialized_theta,
            accuracy=estimation,
            learn_rate=rate_value,
            lambda_value=lambda_value,
        ).save()
        return estimation

    def scikit_learn(self):
        data = self.read_data(self.train_data.value,is_vectorize_output = False)
        shape = self.get_shape()[1:-1]
        lambda_value = 0.01
        learning_rate = 0.03
        clf = MLPClassifier(
            hidden_layer_sizes=tuple(shape),
            activation='logistic',
            solver='adam',
            alpha=lambda_value,
            learning_rate_init=learning_rate,
            learning_rate='adaptive',
            shuffle=True,
            verbose=True,
            max_iter = 500,
        )
        clf.fit(data[0]['input'],data[0]['output'])
        score =  clf.score(data[1]['input'],data[1]['output'])
        print("finish learning .... score :: %s",score)

        WeightModel.objects.create(
            name=self.model_name,
            classificator_provider='sklearn',
            shape= shape.tobytes(),
            body=pickle.dumps(clf),
            accuracy=score,
            learn_rate=learning_rate,
            lambda_value=lambda_value,
        ).save()
        print("boo")

    def on_learn(self):
        print('on learn button press')
        self.model_name = self.get_model_name()
        learn_type = self.learn_type.selected()
        accuracy  = 0
        if learn_type == 'custom':
            accuracy = self.custom_learn_process()
        else:
            accuracy = self.scikit_learn()

        self.nn_name.value = self.get_model_name()
        self.learning_accuracy.value = str(accuracy)

