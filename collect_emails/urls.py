from django.urls import path
from .views import supporter_form
urlpatterns = [
    path('', supporter_form )
]
