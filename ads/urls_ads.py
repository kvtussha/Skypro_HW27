from django.urls import path

from ads import views

urlpatterns = [
    path('', views.AdsView.as_view(), name="ads_list"),
    path('<int:pk>/', views.AdsDetailView.as_view(), name="ads"),
    path('data/', views.AdsDataView.as_view(), name="ads_data")
]
