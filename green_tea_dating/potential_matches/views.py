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
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        for instance in request.data['potential_matches']:
            serializer = PotentialMatchesSerializer(data={'potential_matcher':instance['potential_matched'], 'potential_matched': instance['potential_matcher']})
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()

            serializer = PotentialMatchesSerializer(data=instance)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        username = request.user
        potentialMatchedUsers = PotentialMatches.objects.filter(Q(potential_matcher=username))
        serializer = PotentialMatchesSerializer(potentialMatchedUsers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete_potential_match(self, request, *args, **kwargs):
        potential_match = get_object_or_404(PotentialMatches, Q(potential_matcher=request.data['matcher'], potential_matched=request.data['matched']))
        self.perform_destroy(potential_match)
        return Response(status=status.HTTP_204_NO_CONTENT)
