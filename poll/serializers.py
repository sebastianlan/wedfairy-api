from rest_framework import serializers
from poll.models import Poll, Option, Vote


class PollSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.vote_set.count()

    class Meta:
        model = Poll
        fields = ('id', 'title', 'message', 'select', 'type', 'deadline', 'created_date', 'changed_date', 'count')


class OptionSerializer(serializers.ModelSerializer):
    # pos = serializers.IntegerField(required=True)
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.vote_set.count()

    class Meta:
        model = Option
        fields = ('id', 'poll', 'pos', 'content', 'count')


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'poll', 'option', 'user_id', 'avatar', 'name', 'created_date')
