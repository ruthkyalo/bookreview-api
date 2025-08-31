from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

# Router automatically generates URLs for CRUD operations
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls
