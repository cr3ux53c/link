from django.urls import path

from www.views import *

urlpatterns = [
    path('', Index.as_view()),
]
