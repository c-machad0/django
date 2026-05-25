from django.urls import path
from cars.views import CarListView, CarCreateView, CarDetailView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('', CarListView.as_view(), name='list'),
    path('new/', CarCreateView.as_view(), name='create'),
    path('<int:pk>/', CarDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', CarUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='delete'),
]