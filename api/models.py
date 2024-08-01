import uuid
from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    tokens = models.IntegerField(default=4000)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
 
    objects = UserManager()

    def __str__(self):
        return self.username


class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Chat by {self.user.username} at {self.timestamp}'



