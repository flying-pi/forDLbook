from django.conf.urls import url

from base_math.snippets.MatrixOpperations import MatrixScalarMull

urlpatterns = (
    url(r'^matrix_scalar_mull', MatrixScalarMull.as_view(), name='create_user'),
)
