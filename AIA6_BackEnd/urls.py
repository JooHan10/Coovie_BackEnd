from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("", include("movies.urls")),
    path("reviews/", include("reviews.urls")),
]
