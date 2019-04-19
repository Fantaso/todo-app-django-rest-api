from django.urls import include, path

from .routers import todo_api_router

urlpatterns = [
    path('', include(todo_api_router.urls)),
]
