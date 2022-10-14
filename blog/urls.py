from django.urls import path, include
from .views import BlogListView, BlogDetailView


urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
]