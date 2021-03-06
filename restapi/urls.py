"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from update.views import (update_model_detail_view, 
                          UpdateDetailView, 
                          UpdateDetailView2, 
                          SerializeView,
                          SerializeListView
                          )

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("api/basic", update_model_detail_view),
    # path("api/cbv1", UpdateDetailView.as_view()),
    # path("api/cbv2", UpdateDetailView2.as_view()),
    # path("api/detail", SerializeView.as_view()),
    # path("api/list", SerializeListView.as_view())
    path('api/details/', include('update.api.urls'))
]

