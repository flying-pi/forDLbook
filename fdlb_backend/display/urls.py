from django.conf.urls import url

from display.snippets.PCA_snippet import PCA_DisplaySnippet
from supervisor_neural_network.snippets.simple_network_creator import SimpleNeuralNetworkCreator
from supervisor_neural_network.snippets.simple_neural_network import SimpleNeuralNetwork

urlpatterns = (
    [
        url(r'^pca_display', PCA_DisplaySnippet.as_view(),
            name='pca_display'),
    ], 'display')
