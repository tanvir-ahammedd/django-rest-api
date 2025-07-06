from django.urls import path, include
from . views import ProductViewSet, ProductReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ProductReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]
