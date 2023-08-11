from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("", include("wall_download.urls")),
    path("admin/", admin.site.urls),
]
