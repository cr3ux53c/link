from django.urls import path
from www.views import *

urlpatterns = [
    # path('', Welcome.as_view()),
    path('', LinkListView.as_view(), name='welcome'),
    path('<str:path>/', Redirect.as_view(), name='redirect')
]
