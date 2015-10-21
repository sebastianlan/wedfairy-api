from rest_framework import serializers
from aidaijia_coupon.models import CouponCandidate, Coupon


class CouponCandidateSerializer(serializers.ModelSerializer):
    url = serializers.CharField(required=False)

    class Meta:
        model = CouponCandidate
        fields = ('id', 'url', 'used')


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('id', 'url', 'created_date')