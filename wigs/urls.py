# wigs/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LoginView  
from .views import WigViewSet, UserDetailsViewSet

router = DefaultRouter()
router.register(r'wigs', WigViewSet, basename='wig')

urlpatterns = [
    # Redirect the root URL to the authentication page
    path('', LoginView.as_view(template_name='registration/login.html'), name='api-homepage'),

    # Include the API URLs under a versioned path
    path('api/v1/', include(router.urls)),
    path('api/v1/user/', UserDetailsViewSet.as_view(), name='user-details'),
]
