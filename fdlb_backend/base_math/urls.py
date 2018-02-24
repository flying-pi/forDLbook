from django.conf.urls import url

from base_math.snippets.matrix_operations import MatrixScalarMull, MatrixByMatrixMull

urlpatterns = (
    [
        url(r'^matrix_scalar_mull', MatrixScalarMull.as_view(), name='matrix_scalar_mull'),
        url(r'^matrix_matrix_mull', MatrixByMatrixMull.as_view(), name='matrix_matrix_mull')
    ], 'base_math')
