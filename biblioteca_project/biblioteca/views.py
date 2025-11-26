from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Autor, Libro, Resena
from .serializers import AutorSerializer, LibroSerializer, ResenaSerializer
from .pagination import LibroPagination

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['nacionalidad', 'nombre']
    search_fields = ['nombre']
    ordering_fields = ['nombre']

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    pagination_class = LibroPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['autor', 'fecha_publicacion']
    search_fields = ['titulo', 'autor__nombre']
    ordering_fields = ['fecha_publicacion', 'titulo']

    def get_queryset(self):
        qs = super().get_queryset()
        year = self.request.query_params.get('year')
        if year:
            qs = qs.filter(fecha_publicacion__year=year)
        return qs

    @action(detail=True, methods=['get'])
    def average_rating(self, request, pk=None):
        libro = self.get_object()
        promedio = libro.resenas.aggregate(average=Avg('calificacion'))['average']
        return Response({'libro_id': libro.id, 'calificacion_promedio': promedio})


class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['libro', 'calificacion']
    search_fields = ['texto']
    ordering_fields = ['fecha', 'calificacion']

    def perform_create(self, serializer):
        serializer.save()
