from rest_framework.serializers import ModelSerializer
from eventmanager.models import Matches

class MatchSerializer(ModelSerializer): # Serializer for Note model
    class Meta:
        model = Matches # Model to serialize
        fields = '__all__' # Fields to serialize
        read_only_fields = ('parent_event', 'slug') # Fields marked as read-only