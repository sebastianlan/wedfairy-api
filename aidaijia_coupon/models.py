from django.db import models


class CouponCandidate(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    used = models.IntegerField()


class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)

