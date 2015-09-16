from rest_framework import serializers
from poll.models import Poll, Option, Vote


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'title', 'message', 'select', 'type', 'deadline', 'created_date', 'changed_date')


class OptionSerializer(serializers.ModelSerializer):
    # pos = serializers.IntegerField(required=True)
    class Meta:
        model = Option
        fields = ('id', 'poll', 'pos', 'content')


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'poll', 'option', 'avatar', 'name', 'created_date')