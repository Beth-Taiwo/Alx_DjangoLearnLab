from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"
    def __repr__(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"
    

class CustomUser(AbstractUser):
   date_of_birth = models.DateTimeField()
   profile_photo = models.ImageField()
    
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, date_of_birth, profile_photo, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password must be provided")
        
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            **extra_fields)
        
    def create_superuser(self, email, password, date_of_birth, profile = None):
        user = self.create_user(email, password, date_of_birth, profile)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user