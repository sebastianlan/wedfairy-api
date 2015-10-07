from django.db import models


class Poll(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, null=True, max_length=255)
    message = models.TextField(blank=True, null=True)
    select = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    changed_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'poll'


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    poll = models.ForeignKey(Poll)
    pos = models.IntegerField()
    content = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        db_table = 'option'


class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    poll = models.ForeignKey(Poll)
    option = models.ForeignKey(Option)
    user_id = models.IntegerField()
    avatar = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'vote'

