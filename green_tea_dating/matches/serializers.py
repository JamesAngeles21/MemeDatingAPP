from rest_framework import serializers
from matches.models import Matches

class MatchesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Matches
		fields = ('id', 'matcher', 'matched')

	def create(self, validated_data):
		match = Matches.objects.create(**validated_data)
		match.save()
		return match
