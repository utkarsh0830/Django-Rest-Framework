from django.urls import path
from . import views



urlpatterns = [
    path('items/',views.ItemView.as_view()),
    path('items/<int:pk>',views.ItemDetailView.as_view())
]