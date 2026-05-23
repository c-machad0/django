from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarListView.as_view(), name='cars_list'),
    path('new_car/', views.CarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/edit/', views.CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),
]