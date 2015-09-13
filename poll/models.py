from django.db import models

class Poll(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(blank = True, max_length = 255)
    message = models.TextField(blank = True)
    select = models.IntegerField()
    type = models.IntegerField(blank = True)
    deadline = models.DateField(blank = True)
    created_date = models.DateField()
    changed_date = models.DateField(blank = True)
    class Meta:
        db_table = 'poll'

class Option(models.Model):
    id = models.AutoField(primary_key = True)
    poll = models.ForeignKey(Poll)
    pos = models.IntegerField()
    content = models.CharField(blank = True, max_length = 255)
    class Meta:
        db_table = 'option'

class Vote(models.Model):
    id = models.AutoField(primary_key = True)
    poll = models.ForeignKey(Poll)
    option = models.ForeignKey(Option)
    avatar = models.CharField(max_length = 255)
    name = models.CharField(max_length = 50)
    created_date = models.DateField()
    class Meta:
        db_table = 'vote'

