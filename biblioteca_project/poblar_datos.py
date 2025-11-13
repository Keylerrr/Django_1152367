from biblioteca.models import Autor, Libro, Resena

# autores
autor1 = Autor.objects.create(nombre="Gabriel García Márquez", nacionalidad="Colombiana")
autor2 = Autor.objects.create(nombre="William Bruce Cameron", nacionalidad="Estadounidense")
autor3 = Autor.objects.create(nombre="Isabel Allende", nacionalidad="Chilena")

# libros
libro1 = Libro.objects.create(
    titulo="Cien Años de Soledad",
    autor=autor1,
    fecha_publicacion="1967-06-05",
    resumen="Una novela que narra la historia de la familia Buendía a lo largo de siete generaciones en el pueblo ficticio de Macondo."
)
libro2 = Libro.objects.create(
    titulo="El amor en los tiempos del cólera",
    autor=autor1,
    fecha_publicacion="1985-09-05",
    resumen="Una historia de amor que perdura más de medio siglo entre Florentino Ariza y Fermina Daza."
)
libro3 = Libro.objects.create(
    titulo="Crónica de una muerte anunciada",
    autor=autor1,
    fecha_publicacion="1981-03-01",
    resumen="Una narración en torno al asesinato anunciado de Santiago Nasar, donde todos sabían lo que iba a ocurrir."
)

libro4 = Libro.objects.create(
    titulo="A Dog’s Purpose",
    autor=autor2,
    fecha_publicacion="2010-07-06",
    resumen="Un perro reencarna varias veces para encontrar el significado de su vida junto a los humanos que ama."
)
libro5 = Libro.objects.create(
    titulo="A Dog’s Journey",
    autor=autor2,
    fecha_publicacion="2012-05-06",
    resumen="Continuación de A Dog’s Purpose, donde el perro Buddy busca proteger a una niña en crecimiento."
)
libro6 = Libro.objects.create(
    titulo="A Dog’s Way Home",
    autor=autor2,
    fecha_publicacion="2017-12-12",
    resumen="La historia de Bella, una perra que viaja más de 600 kilómetros para volver con su dueño."
)

libro7 = Libro.objects.create(
    titulo="La casa de los espíritus",
    autor=autor3,
    fecha_publicacion="1982-01-01",
    resumen="Una saga familiar chilena que combina política, amor y elementos sobrenaturales en un contexto histórico."
)
libro8 = Libro.objects.create(
    titulo="Paula",
    autor=autor3,
    fecha_publicacion="1994-01-01",
    resumen="Una emotiva carta de una madre a su hija, escrita mientras está en coma, llena de recuerdos y reflexiones."
)
libro9 = Libro.objects.create(
    titulo="Eva Luna",
    autor=autor3,
    fecha_publicacion="1987-01-01",
    resumen="Relato de una mujer con una vida marcada por la pobreza, la imaginación y el poder de las historias."
)

# reseñas
Resena.objects.create(libro=libro1, texto="Una obra maestra del realismo mágico.", calificacion=5)
Resena.objects.create(libro=libro2, texto="Una historia de amor profunda y poética.", calificacion=5)
Resena.objects.create(libro=libro3, texto="Narrativa intensa y atrapante.", calificacion=4)

Resena.objects.create(libro=libro4, texto="Una historia conmovedora sobre la lealtad de los perros.", calificacion=5)
Resena.objects.create(libro=libro5, texto="Hermosa continuación, muy emotiva.", calificacion=4)
Resena.objects.create(libro=libro6, texto="Inspiradora y llena de ternura.", calificacion=5)

Resena.objects.create(libro=libro7, texto="Una obra mágica que mezcla historia y fantasía.", calificacion=5)
Resena.objects.create(libro=libro8, texto="Muy conmovedora y personal, llena de amor y dolor.", calificacion=5)
Resena.objects.create(libro=libro9, texto="Una historia poderosa sobre la vida y la imaginación.", calificacion=4)
