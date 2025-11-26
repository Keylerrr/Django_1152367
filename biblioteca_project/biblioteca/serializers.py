from rest_framework import serializers
from .models import Autor, Libro, Resena

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = ['id', 'libro', 'texto', 'calificacion', 'fecha']

class LibroSerializer(serializers.ModelSerializer):
    nombre_autor = serializers.ReadOnlyField(source='autor.nombre')
    resenas_recientes = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'nombre_autor', 'resumen', 'fecha_publicacion', 'resenas_recientes']

    def get_resenas_recientes(self, obj):
        resenas = obj.resenas.order_by('-fecha')[:5]
        return ResenaSerializer(resenas, many=True).data

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad']
