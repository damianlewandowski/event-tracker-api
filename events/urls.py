from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from rest_framework_simplejwt import views as jwt_views

from . import views

router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
