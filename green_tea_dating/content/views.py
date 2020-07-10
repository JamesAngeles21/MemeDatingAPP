from django.shortcuts import render, get_object_or_404
from content.models import Content
from content.serializers import ContentSerializer
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response 
from rest_framework.decorators import action

# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
	queryset = Content.objects.all()
	serializer_class = ContentSerializer
	permission_classes = (permissions.AllowAny,)

	@action(methods=['post'], detail=False)
	def batch_create(self, request, *args, **kwargs):
		content_urls = request.data['urls']
		serialized_content = []

		for url in content_urls:
			serializer = ContentSerializer(data={'path': url})
			if not serializer.is_valid():
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			serialized_content.append(serializer)

		serialized_content = [serializer.save() for serializer in serialized_content]
		return Response(status=status.HTTP_201_CREATED)

	def create(self, request, *args, **kwargs):
		serializer = ContentSerializer(data=request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	@action(methods=['post'], detail=False)
	def delete(self, request, *args, **kwargs):
		content = get_object_or_404(Content, path=request.data['path'])
		self.perform_destroy(content)
		return Response(status=status.HTTP_204_NO_CONTENT)

	@action(methods=['post'], detail=False)
	def batch_delete(self, request, *args, **kwargs):
		content_urls = request.data['urls']
		contents = [get_object_or_404(Content, path=url) for url in content_urls]

		for content in contents:
			self.perform_destroy(content)

		return Response(status=status.HTTP_204_NO_CONTENT)

