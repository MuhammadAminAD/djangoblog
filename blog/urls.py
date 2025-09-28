from django.urls import path

from blog.views import BlogListView, BlogDeleteView, BlogCreateView, BlogUpdateView, BlogDetailView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_item"),
    path("post/create/", BlogCreateView.as_view(), name="create_item"),
    path("post/update/<int:pk>/", BlogUpdateView.as_view(), name="edit_item"),
    path("post/delete/<int:pk>/", BlogDeleteView.as_view(), name="delete_item")
]
