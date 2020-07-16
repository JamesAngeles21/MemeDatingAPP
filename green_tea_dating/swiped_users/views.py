from django.shortcuts import render, get_object_or_404, get_list_or_404
from swiped_users.models import SwipedUsers
from potential_matches.models import PotentialMatches
from potential_matches.views import PotentialMatchesViewSet
from matches.views import MatchesViewSet
from swiped_users.serializers import SwipedUsersSerializer
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q

# Create your views here.
class SwipedUsersViewSet(viewsets.ModelViewSet):
    queryset = SwipedUsers.objects.all()
    serializer_class = SwipedUsersSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = SwipedUsersSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        potential_match = get_object_or_404(PotentialMatches, Q(potential_matcher=request.data['swiper'], potential_matched=request.data['swiped']))
        PotentialMatchesViewSet.perform_destroy(self, instance = potential_match)

        otherSwipe = SwipedUsers.objects.filter(Q(swiper=request.data['swiped'], swiped=request.data['swiper']))
        if len(otherSwipe) == 0:
            return Response(serializer.data, status=status.HTTP_200_OK)

        if otherSwipe[0].liked == request.data['liked'] == True:
            self.delete_swipes(request)
            return MatchesViewSet.create_from_swipe(self, request={'matcher': request.data['swiper'], 'matched': request.data['swiped']})
        else:
            return self.delete_swipes(request)


        #delete from potentital table
        #stay
        #delete from this table
        #delete and move to matches table


    def delete_swipes(self, request, *args, **kwargs):
        swiped = get_object_or_404(SwipedUsers, Q(swiper=request.data['swiped'], swiped=request.data['swiper']))
        self.perform_destroy(swiped)

        swiped = get_object_or_404(SwipedUsers, Q(swiper=request.data['swiper'], swiped=request.data['swiped']))
        self.perform_destroy(swiped)
        return Response(status=status.HTTP_204_NO_CONTENT)

