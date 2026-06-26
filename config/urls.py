from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import HttpResponse

urlpatterns = [
    path("", lambda _request: HttpResponse("SoftDesk API is running")),
    path("admin/", admin.site.urls),
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("api/", include("users.urls")),
    path("api/", include("projects.urls")),
]
