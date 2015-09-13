from django.db import models

class Rsvp(models.Model):
    id = models.AutoField(primary_key = True)
    message = models.TextField(blank = True)
    deadline = models.DateField(blank = True)
    created_date = models.DateField()
    changed_date = models.DateField(blank = True)
    class Meta:
        db_table = 'rsvp'

class Guest(models.Model):
    id = models.AutoField(primary_key = True)
    rsvp = models.ForeignKey(Rsvp)
    avatar = models.CharField(max_length = 255)
    name = models.CharField(max_length = 50)
    people = models.IntegerField()
    created_date = models.DateField()
    class Meta:
        db_table = 'guest'

