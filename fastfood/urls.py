from django.urls import path
from .views import (
    FoodListView,
    FoodCreateView,
    FoodUpdateView,
    FoodDeleteView,
    FoodDetailView,
    Register,
    Login,
    Logout,
)

urlpatterns = [
    path("", FoodListView.as_view(), name="home"),
    path("food/<int:pk>/delete/", FoodDeleteView.as_view(), name="food_delete"),
    path("food/<int:pk>/edit/", FoodUpdateView.as_view(), name="food_edit"),
    path("food/create", FoodCreateView.as_view(), name="food_create"),
    path("food/detail/<int:pk>/", FoodDetailView.as_view(), name="food_detail"),
    path("register/", Register.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]
