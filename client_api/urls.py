
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('episodes/<int:id>', views.episodes, name='episodes'),
    path('characters/<int:id>', views.characters, name='characters'),
    path('locations/<int:id>', views.locations, name='locations')
]
