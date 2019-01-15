from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('matches/', views.MatchList.as_view()),
    path('matches/<int:pk>/', views.MatchDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
