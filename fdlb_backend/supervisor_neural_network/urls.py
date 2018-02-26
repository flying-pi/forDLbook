from django.conf.urls import url

from base_math.snippets.matrix_operations import MatrixByMatrixMull
from supervisor_neural_network.snippets.matrix_operations import SimpleNeuralNetwork

urlpatterns = (
    [
        url(r'^simple_neural_network', SimpleNeuralNetwork.as_view(), name='simple_neural_network'),
    ], 'supervisor_neural_network')
