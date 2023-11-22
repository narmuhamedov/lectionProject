from django.urls import path
from . import views

urlpatterns = [
    path('person_list/', views.PersonListView.as_view()),
    path('person_list/<int:id>/', views.PersonDetailView.as_view()),
    path('create_person/', views.PersonCreateView.as_view())
]