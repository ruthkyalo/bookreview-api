from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    # Serializer converts Review model objects to JSON
    class Meta:
        model = Review
        fields = '__all__'  # include all model fields in the API response
        read_only_fields = ('user',)  # user is set automatically

    def validate_rating(self, value):
        """Ensure rating is between 1 and 5."""
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
