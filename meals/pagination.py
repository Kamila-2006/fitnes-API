from rest_framework.pagination import PageNumberPagination


class MealPagination(PageNumberPagination):
    page_size = 10