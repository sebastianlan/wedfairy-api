from django.contrib import admin
import models


@admin.register(models.Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'address', 'message', 'map_lng', 'map_lat', 'created_date', 'changed_date']

