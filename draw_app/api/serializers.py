from rest_framework import serializers
from .models import Author, Book

class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = ['id', 'name', 'email', 'password', 'added_by', 'created_date']
