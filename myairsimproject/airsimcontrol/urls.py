from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/takeoff/', views.takeoff_view, name='takeoff'),
    path('api/land/', views.land_view, name='land'),
    path('api/move/', views.move_view, name='move'),
    path('api/state/', views.state_view, name='state'),
]