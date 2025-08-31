from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book                # Connects this serializer to the Book model
        fields = '__all__'          # Includes ALL fields from the Book model automatically
