from rest_framework.decorators import api_view
from rest_framework.response import Response

from eventmanager.models import Matches
from .serializers import MatchSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/match/data/slug',
            'method': 'GET',
            'body': None,
            'description': 'Returns match data.',
        },

    ]
    return Response(routes)

@api_view(['GET'])
def getMatchData(request, slug):
    match = Matches.objects.get(slug=slug)
    serializer = MatchSerializer(match, many=False)
    return Response(serializer.data)
