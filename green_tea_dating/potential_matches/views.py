from potential_matches.models import PotentialMatches
from potential_matches.serializers import PotentialMatchesSerializer
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q

# Create your views here.
class PotentialMatchesViewSet(viewsets.ModelViewSet):
    queryset = PotentialMatches.objects.all()
    serializer_class = PotentialMatchesSerializer
    permissions_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = PotentialMatchesSerializer(data={'potential_matcher':request.data['potential_matched'], 'potential_matched': request.data['potential_matcher']})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        serializer = PotentialMatchesSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        if (request.data['potential_matcher'] != request.user.username):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        potential_match = get_object_or_404(PotentialMatches, Q(id=request.data["id"]))
        serializer = PotentialMatchesSerializer(potential_match, data={'swipedOn': True, 'liked': request.data['liked']}, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        #create a match instance into matches table
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        username = request.user
        potentialMatchedUsers = PotentialMatches.objects.filter(Q(matcher=username1))
        serializer = PotentialMatchesSerializer(potentialMatchedUsers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_not_swiped_matched(self, request, *args, **kwargs):
        username = request.user.username
        potentialMatchedUsers = PotentialMatches.objects.filter(Q(matcher=username1, swipedOn=False))
        serializer = PotentialMatchesSerializer(potentialMatchedUsers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def get_swiped_and_liked_matched(self, request, *args, **kwargs):
        username = request.user.username
        potentialMatchedUsers = PotentialMatches.objects.filter(Q(matcher=username1, swipedOn=True, liked=True))
        serializer = PotentialMatchesSerializer(potentialMatchedUsers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)