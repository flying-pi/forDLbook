"""fdlb_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

import base_math.urls as base_math_urls
from core.views import RootView
import display.urls as display
import supervisor_neural_network.urls as supervisor_neural_network
from core.views import RootView, FileView, ImageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RootView.as_view()),
    path('files/', FileView.as_view()),
    path('imagae/<str:image_name>', ImageView.as_view(),name='image'),
]

urlpatterns += (
    url(r'^snippets/base_math/', include(base_math_urls.urlpatterns)),
    url(r'^snippets/supervisor_neural_network/', include(supervisor_neural_network.urlpatterns)),
    url(r'^snippets/display/', include(display.urlpatterns)),
)
