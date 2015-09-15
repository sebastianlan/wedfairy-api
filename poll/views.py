from rest_framework import viewsets, decorators, throttling, mixins
from rest_framework.response import Response
from poll.models import Poll, Option, Vote
from poll.serializers import PollSerializer, OptionSerializer, VoteSerializer
from poll.permissions import IsAppAuthorized_poll, IsAppAuthorized_vote


class OncePerSecUserThrottle(throttling.UserRateThrottle):
        rate = '1/second'


class TwicePerSecUserThrottle(throttling.UserRateThrottle):
        rate = '2/second'


class PollViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    throttle_classes = [OncePerSecUserThrottle]
    permission_classes = [IsAppAuthorized_poll]

    @decorators.detail_route(methods=['GET'])
    def options(self, request, pk):
        queryset = Poll.objects.get(id=pk).option_set.all()
        serializer = OptionSerializer(queryset, many=True)
        return Response(serializer.data)

    @decorators.detail_route(methods=['GET'], permission_classes=[IsAppAuthorized_vote])
    def votes(self, request, pk):
        queryset = Poll.objects.get(id = pk).vote_set.all()
        serializer = VoteSerializer(queryset, many = True)
        return Response(serializer.data)


class OptionViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    throttle_classes = [TwicePerSecUserThrottle]
    permission_classes = [IsAppAuthorized_poll]

    @decorators.detail_route(methods=['GET'], permission_classes=[IsAppAuthorized_vote])
    def votes(self, request, pk):
        queryset = Option.objects.get(id=pk).vote_set.all()
        serializer = VoteSerializer(queryset, many=True)
        return Response(serializer.data)


class VoteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
