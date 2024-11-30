from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
       class Meta:
        model = Book
        fields = ('id', 'title', 'publication_year','author')
        
        # custom validation added to ensure that the publication_year is not in the future.     
        def validate(self, data):
            if data['publication_year'] > datetime.now().year:
                raise serializers.ValidationError("Publication year cannot be in the future")
            return data
    
class AuthorSerializer(serializers.ModelSerializer):
     # A nested BookSerializer to serialize the related books dynamically.
    author = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ('id', 'name')