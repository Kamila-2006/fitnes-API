from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'healthmetrics', views.HealthMetrikViewSet, basename='health-metrics')

urlpatterns = [
    path('', include(router.urls)),
]