from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):#this serializer takes into account all fields of the Book model.
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):#custom validation to ensure the publication year is not in the future.
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future. Current year is {current_year}.".format(current_year=current_year))

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)#this is a nested serializer to include related books.

    class Meta:
        model = Author
        fields = ['name', 'books']