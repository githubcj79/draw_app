from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# User authentication

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"message": "Bienvenido al Sorteo!"}
    return JsonResponse(content)

# User can add a competitor
from .serializers import CompetitorSerializer
from .models import Competitor
import json
from django.core.exceptions import ObjectDoesNotExist

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_competitor(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        competitor = Competitor.objects.create(
            name=payload["name"],
            email=payload["email"],
            password=payload["password"],
            added_by=user
        )
        serializer = CompetitorSerializer(competitor)
        return JsonResponse({'competitors': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Draw

from random import randint
from rest_framework import status

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def do_draw(request):
    user = request.user.id
    competitors = Competitor.objects.filter(added_by=user)
    count = competitors.count()
    winner = competitors[randint(0, count - 1)] #single random object
    serializer = CompetitorSerializer(winner)
    return JsonResponse({'winner': serializer.data}, safe=False, status=status.HTTP_200_OK)
