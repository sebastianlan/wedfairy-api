from django.contrib import admin
import models


@admin.register(models.CouponCandidate)
class CouponCandidateAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'used']


@admin.register(models.Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'created_date']