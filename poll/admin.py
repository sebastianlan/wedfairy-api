from django.contrib import admin
import models


@admin.register(models.Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'message', 'select', 'type', 'deadline', 'created_date', 'changed_date']


@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'pos', 'content']


@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'option', 'user_id', 'avatar', 'name', 'created_date']