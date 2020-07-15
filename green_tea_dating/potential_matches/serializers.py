from rest_framework import serializers
from potential_matches.models import PotentialMatches


class PotentialMatchesSerializer(serializers.ModelSerializer):

	class Meta:
		model = PotentialMatches
		fields = ('id', 'potential_matcher', 'potential_matched', 'swipedOn')

	def create(self, validated_data):
		potential_match = PotentialMatches.objects.create(**validated_data)
		potential_match.save()
		return potential_match