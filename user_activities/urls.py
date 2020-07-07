from django.urls import path

from . import views

urlpatterns = [
    path('activities', views.activities, name='activities'),
    path('activity/<int:user_id>', views.user_activity, name='activity'),
]
