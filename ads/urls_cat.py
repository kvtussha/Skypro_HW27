from django.urls import path

from ads import views

urlpatterns = [
    path('', views.CategoryView.as_view(), name="category_list"),
    path('<int:pk>/', views.CategoryDetailView.as_view(), name="category"),
    path('data/', views.CategoryDataView.as_view(), name="category_data")
]
