from rest_framework.routers import DefaultRouter

from breadEngine.api.viewsets import PostViewSet, UserViewSet, CurrentUserViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')
router.register('me', CurrentUserViewSet, basename='me')

urlpatterns = router.urls
