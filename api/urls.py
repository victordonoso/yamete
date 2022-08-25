from django.urls import path
from . import views

urlpatterns = [
    path('routes/', views.getRoutes),
    path('notes/', views.getNotes), # GET /api/notes/
    path('notes/create/', views.createNote), # POST /api/notes/create/
    path('notes/<str:pk>/update/', views.updateNote), # PUT /api/notes/id/update/
    path('notes/<str:pk>/delete/', views.deleteNote), # DELETE /api/notes/id/delete/
    path('notes/<str:pk>/', views.getNote), # GET /api/notes/id
    

]
