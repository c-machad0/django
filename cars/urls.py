from django.urls import path
from cars.views import CarListView, CarCreateView, CarDetailView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('', CarListView.as_view(), name='car-list'),
    path('novo/', CarCreateView.as_view(), name='car-create'),
    path('<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('<int:pk>/edit/', CarUpdateView.as_view(), name='car-update'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
]