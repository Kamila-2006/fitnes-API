from rest_framework.pagination import PageNumberPagination


class HealthMetrikPagination(PageNumberPagination):
    page_size = 10