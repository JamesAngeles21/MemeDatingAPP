from django.shortcuts import render, get_object_or_404, get_list_or_404
from matches.models import Matches
from matches.serializers import MatchesSerializer
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q

# Create your views here.
class MatchesViewSet(viewsets.ModelViewSet):
	queryset = Matches.objects.all()
	serializer_class = MatchesSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def create(self, request, *args, **kwargs):
		serializer= MatchesSerializer(data={'matcher': request.data['matched'], 'matched': request.data['matcher']})
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		serializer.save()

		serializer= MatchesSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		serializer.save()

		return Response(serializer.data, status=status.HTTP_200_OK)

	@action(methods=['post'], detail=False)
	def delete_match(self, request, *args, **kwargs):
		match = get_list_or_404(Matches, Q(matcher=request.data['matcher'], matched=request.data['matched']) | Q(matcher=request.data['matched'], matched=request.data['matcher']))
		for instance in match:
			self.perform_destroy(instance)
		return Response(status=status.HTTP_204_NO_CONTENT)