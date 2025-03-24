from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'workouts', views.WorkoutViewSet, basename='workouts')

urlpatterns = [
    path('', include(router.urls)),
]