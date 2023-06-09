from django.urls import path
from movies import views

urlpatterns = [
    path('main/', views.MovieListView.as_view(), name='main'),
    path('movie/', views.MovieListPaginatedView.as_view(), name='movie_paginated'),
    path('recommendation/<int:movie_id>/', views.MovieDetailView.as_view(), name='recommendation'),
    path('save/', views.SaveMoviesView.as_view(), name='csv_save'),
    path('recommendation/', views.SimilarMoviesView.as_view(), name='movie_recommendation'),
]