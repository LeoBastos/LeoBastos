from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='listings'),
    path('<int:listing_id>', views.List, name='listing'),
    path('search', views.Search, name='search'),
  
]
