from django.urls import path
from . import views

urlpatterns = [
    path('routes/', views.getRoutes),
    path('match/data/<slug:slug>', views.getMatchData), # GET /api/match/data/slug
]