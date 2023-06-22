from django.contrib import admin
from django.urls import path, include

from ads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.status_view, name="status view"),
    path('cat/', include('ads.urls_cat'), name="categories"),
    path('ad/', include('ads.urls_ads'), name="ads")
]
