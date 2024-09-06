


from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),  # Ensure this matches your view
    path("detail/<int:news_id>/", views.detail_news, name="detail_news"),
]


