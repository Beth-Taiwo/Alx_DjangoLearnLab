from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Author: {self.name}"
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"
    
    def __repr__(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"