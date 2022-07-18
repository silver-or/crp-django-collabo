from django.urls import path, include
from files import views

urlpatterns = [
    path(r'', views.recommend_user_prod)
]
