from django.urls import path
from . import views

urlpatterns = [
    path('<int:salon_id>/', views.salon_details, name='salon_page'),
]
  