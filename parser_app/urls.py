from django.urls import path
from . import views

urlpatterns = [
    path("film_list/", views.ParserFilmView.as_view(), name="film_list"),
    path("parser_film/", views.ParserFormView.as_view(), name="start_parsing"),
]