from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserModel(AbstractUser):
    '''A customer user model for users.

    Args:
        models (Model): A model class from django.db.models
    '''
    pass