from .views import RegisterationViewset
from rest_framework.routers import DefaultRouter

# since we are using viewset instead of view here
router = DefaultRouter()
router.register(r'api/register', RegisterationViewset, basename="register")
urlpatterns = router.urls
