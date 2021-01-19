from django.urls import path
from portfolioApp.views import indexView

urlpatterns = [
    path('', indexView, name='index')
]
