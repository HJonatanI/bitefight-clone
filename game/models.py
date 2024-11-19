from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
	# Se pueden agregar más atributos aquí según lo que se necesite para el juego
	pass

class Character(models.Model):
	usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE, related_name='character')
	nombre = models.CharField(max_length=50)
	salud = models.IntegerField(default=100)
	fuerza = models.IntegerField(default=10)
	defensa = models.IntegerField(default=5)
	nivel = models.IntegerField(default=1)
	experiencia = models.IntegerField(default=0)
	oro = models.IntegerField(default=100)

	def __str__(self):
		return f'{self.nombre} (Nivel {self.nivel})'

class Item(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()
	tipo = models.CharField(max_length=50)  # Ejemplo: "arma", "armadura"
	bono_fuerza = models.IntegerField(default=0)
	bono_defensa = models.IntegerField(default=0)
	precio = models.IntegerField(default=50)

	def __str__(self):
		return self.nombre

class Inventario(models.Model):
	personaje = models.ForeignKey('Character', on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.cantidad}x {self.item.nombre} para {self.personaje.nombre}"

class Battle(models.Model):
	atacante = models.ForeignKey('Character', related_name="batallas_atacante", null=True, blank=True, on_delete=models.SET_NULL)
	defensor = models.ForeignKey('Character', related_name="batallas_defensor", null=True, blank=True, on_delete=models.SET_NULL)
	ganador = models.ForeignKey('Character', related_name="batallas_ganador", null=True, blank=True, on_delete=models.SET_NULL)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.atacante} vs {self.defensor} - Ganador: {self.ganador if self.ganador else 'Empate'}'

