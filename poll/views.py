from rest_framework import viewsets, decorators, throttling
from rest_framework.response import Response
from poll.models import Poll, Option, Vote
from poll.serializers import PollSerializer, OptionSerializer, VoteSerializer

class OncePerSecUserThrottle(throttling.UserRateThrottle):
        rate = '1/second'

class TwicePerSecUserThrottle(throttling.UserRateThrottle):
        rate = '2/second'

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    throttle_class = OncePerSecUserThrottle

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    throttle_class = TwicePerSecUserThrottle

    @decorators.detail_route(methods=['get'])
    def bypoll(self, request, pk):
        queryset = Poll.objects.get(id = pk).option_set.all()
        serializer = OptionSerializer(queryset, many = True)
        return Response(serializer.data)


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    @decorators.detail_route(methods=['get'])
    def bypoll(self, request, pk):
        queryset = Poll.objects.get(id = pk).vote_set.all()
        serializer = VoteSerializer(queryset, many = True)
        return Response(serializer.data)

    @decorators.detail_route(methods=['get'])
    def byoption(self, request, pk):
        queryset = Option.objects.get(id = pk).vote_set.all()
        serializer = VoteSerializer(queryset, many = True)
        return Response(serializer.data)