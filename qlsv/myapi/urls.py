from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('rest/', views.StudentListView.as_view(), name='view'),
    path('rest/<int:pk>/', views.StudentDetailView.as_view(), name='view'),
    path('create', views.Create.as_view(), name='create'),
    path('update/<str:pk>/', views.Update.as_view(), name='update'),
    path('delete/<str:pk>/', views.Delete.as_view(), name='delete'),
    path('', views.Main.as_view(), name='view'),
    path('search', views.Search.as_view(), name='search'),
    path('rest/login', views.TokenLogin.as_view(), name='login'),
    path('rest/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]

