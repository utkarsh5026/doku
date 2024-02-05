from django.urls import path
from app.views.images import ImageView
from app.views.search import SearchView
from app.views.volume import VolumeView

urlpatterns = [
    path("images/", ImageView.as_view(), name="images"),
    path("search/", SearchView.as_view(), name="search"),
    path("volumes/", VolumeView.as_view(), name="volumes"),
]
