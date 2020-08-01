from django.urls import path
from update.api.views import (UpdateModelDetailApiView, UpdateModelListApiView)

urlpatterns = [
    path("", UpdateModelListApiView.as_view()),
    path("<int:id>", UpdateModelDetailApiView.as_view()),

]
