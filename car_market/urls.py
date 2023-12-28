from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('', views.CarListView.as_view(), name='car_list'),
    path('car_list/<int:id>/', views.CarDetailView.as_view(), name='car_detail'),
    path('create_car/', views.CarCreateView.as_view(), name='create_car'),
    path('car_list_delete/', views.car_list_delete_view, name='car_list_delete'),
    path('car_drop/<int:id>/delete/', views.CarDropView.as_view(), name='car_drop'),
    path('car_list_update/', views.car_list_edit_view, name='car_list_update'),
    path('car_update/<int:id>/update/', views.CarUpdateView.as_view(), name='car_update'),
    path('search/', views.SearchView.as_view(), name='search')
]
