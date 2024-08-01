from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User 


@receiver(post_save, sender=User)
def create_user_tokens(sender, instance, created, **kwargs):
	if created:
		instance.tokens = 4000
		instance.save()