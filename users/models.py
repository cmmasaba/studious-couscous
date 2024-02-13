from django.db import models

# Create your models here.

class CustomUserModel(models.Model):
    '''A customer user model for users.

    Args:
        models (Model): A model class from django.db.models
    '''
    user_code = models.UUIDField(primary_key=True, editable=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)