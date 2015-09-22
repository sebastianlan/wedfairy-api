from django.contrib import admin


from django.contrib import admin
import models


@admin.register(models.Rsvp)
class RsvpAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'deadline', 'created_date', 'changed_date']


@admin.register(models.Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'rsvp', 'avatar', 'name', 'people', 'mobile', 'created_date']

