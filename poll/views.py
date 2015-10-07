from rest_framework import viewsets, decorators, throttling, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from poll.models import Poll, Option, Vote
from poll.serializers import PollSerializer, OptionSerializer, VoteSerializer
from poll.permissions import IsAppAuthorized_poll, IsAppAuthorized_poll_vote, IsAppAuthorized_option_vote


class OncePerSecUserThrottle(throttling.UserRateThrottle):
        rate = '1/second'


class HundredPerMinUserThrottle(throttling.UserRateThrottle):
        rate = '100/minute'


class PollViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    # throttle_classes = [OncePerSecUserThrottle]
    permission_classes = [IsAppAuthorized_poll]

    @decorators.detail_route(methods=['GET'])
    def poll_options(self, request, pk):
        queryset = Poll.objects.get(id=pk).option_set.all()
        serializer = OptionSerializer(queryset, many=True)
        return Response(serializer.data)

    @decorators.detail_route(methods=['GET'], permission_classes=[IsAppAuthorized_poll_vote])
    def votes(self, request, pk):
        queryset = Poll.objects.get(id=pk).vote_set.all()
        serializer = VoteSerializer(queryset, many=True)
        return Response(serializer.data)


class OptionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # throttle_classes = [HundredPerMinUserThrottle]
    permission_classes = [IsAppAuthorized_poll]

    @decorators.detail_route(methods=['GET'], permission_classes=[IsAppAuthorized_option_vote])
    def votes(self, request, pk):
        queryset = Option.objects.get(id=pk).vote_set.all()
        serializer = VoteSerializer(queryset, many=True)
        return Response(serializer.data)


class VoteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


@api_view(['GET'])
def poll_voted(request, poll, user):
    queryset = Vote.objects.filter(poll=poll,user_id=user)
    serializer = VoteSerializer(queryset, many=True)
    return Response(serializer.data)