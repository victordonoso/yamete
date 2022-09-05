from django.urls import path
from . import views

urlpatterns = [
    path('match/overlay/<slug:slug>', views.match_overlay), # GET /api/match/overlay/slug
]
