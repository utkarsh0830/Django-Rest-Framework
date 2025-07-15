from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('items',views.ItemViewSets)
router.register('orders',views.OrderViewSets)

urlpatterns = [
#    path('items/',views.ItemView),
#    path('items/<int:pk>',views.ItemDetailView),
    path('', include(router.urls))
]