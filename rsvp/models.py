from django.db import models


class Rsvp(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    changed_date = models.DateField(auto_now=True)


class Guest(models.Model):
    id = models.AutoField(primary_key=True)
    rsvp = models.ForeignKey(Rsvp)
    avatar = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    people = models.IntegerField()
    mobile = models.CharField(max_length=20)
    created_date = models.DateField(auto_now_add=True)

