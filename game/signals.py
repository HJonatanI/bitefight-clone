from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Battle, Character

@receiver(post_delete, sender=Character)
def eliminar_batallas_sin_participantes(sender, instance, **kwargs):
	# Busca batallas sin atacante ni defensor
	batallas_sin_participantes = Battle.objects.filter(atacante=None, defensor=None)
	# Elimina esas batallas
	batallas_sin_participantes.delete()
