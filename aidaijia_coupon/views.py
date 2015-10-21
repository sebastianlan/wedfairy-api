from rest_framework.decorators import api_view
from rest_framework.response import Response
from aidaijia_coupon.models import CouponCandidate, Coupon
from aidaijia_coupon.serializers import CouponCandidateSerializer, CouponSerializer


@api_view(['POST'])
def create_coupon(request):
    queryset = CouponCandidate.objects.filter(used=0)
    serializer = CouponCandidateSerializer(queryset, many=True)
    coupon_candidate_id = serializer.data[0].get("id")
    coupon_candidate_url = serializer.data[0].get("url")

    data = {"used": 1}
    queryset = CouponCandidate.objects.get(id=coupon_candidate_id)
    serializer = CouponCandidateSerializer(queryset, data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=400)

    data = {"url": coupon_candidate_url}
    serializer = CouponSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def retrieve_coupon(request,pk):
    queryset = Coupon.objects.get(id=pk)
    serializer = CouponSerializer(queryset)
    return Response(serializer.data)