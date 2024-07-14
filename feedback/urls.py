from django.urls import path
from . import views

urlpatterns = [
    path('feedback_form/', views.feedback_view, name='feedback'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
    path('testimonials/', views.testimonials_view, name='testimonials'),
]