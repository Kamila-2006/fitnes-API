from rest_framework.pagination import PageNumberPagination


class WorkoutPagination(PageNumberPagination):
    page_size = 10