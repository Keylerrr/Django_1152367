from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from biblioteca.views import AutorViewSet, LibroViewSet, ResenaViewSet

router = DefaultRouter()
router.register(r'authors', AutorViewSet, basename='author')
router.register(r'books', LibroViewSet, basename='book')
router.register(r'reviews', ResenaViewSet, basename='review')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
