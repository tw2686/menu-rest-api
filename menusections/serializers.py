from rest_framework import serializers
from .models import MenuSections


class MenuSectionsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format"""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = MenuSections
        fields = ('id', 'name')
