from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.StudentListView.as_view(), name='view'),
    path('hello/<str:pk>/', views.StudentDetailView.as_view(), name='view'),
    path('create', views.Create.as_view(), name='create'),
    path('update/<str:pk>/', views.Update.as_view(), name='update'),
    path('delete/<str:pk>/', views.Delete.as_view(), name='delete'),
    path('', views.Main.as_view(), name='view'),
    path('search', views.Search.as_view(), name='search')
]

