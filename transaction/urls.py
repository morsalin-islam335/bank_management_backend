from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views  import TransactionViewSets

router = DefaultRouter()
router.register("", TransactionViewSets)
urlpatterns = [
    path('', include(router.urls)),    
]
