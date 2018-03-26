from django.conf.urls import url

from supervisor_neural_network.snippets.simple_network_creator import SimpleNeuralNetworkCreator
from supervisor_neural_network.snippets.simple_neural_network import SimpleNeuralNetwork

urlpatterns = (
    [
        url(r'^simple_neural_network_creator', SimpleNeuralNetworkCreator.as_view(),
            name='simple_neural_network_creator'),

        url(r'^simple_neural_network', SimpleNeuralNetwork.as_view(),
            name='simple_neural_network'),
    ], 'supervisor_neural_network')
