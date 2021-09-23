from django.urls import path
from . import views


app_name = 'authi'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path("password_reset", views.password_reset_request, name="password_reset")
     
]
