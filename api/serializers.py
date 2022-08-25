from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer): # Serializer for Note model
    class Meta:
        model = Note # Model to serialize
        fields = '__all__' # Fields to serialize
"""         read_only_fields = ('created', 'updated') # Fields marked as read-only
        extra_kwargs = {
            'body': {'required': True}, # Required field
        } """