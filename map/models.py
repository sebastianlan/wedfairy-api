from django.db import models

class Map(models.Model):
    id = models.AutoField(primary_key = True)
    location = models.CharField(blank = True, max_length = 255)
    address = models.CharField(blank = True, max_length = 255)
    message = models.TextField(blank = True)
    map_lng = models.DecimalField(blank = True, max_digits = 10, decimal_places = 6)
    map_lat = models.DecimalField(blank = True, max_digits = 10, decimal_places = 6)
    created_date =  models.DateField()
    changed_date =  models.DateField(blank = True)
    class Meta:
        db_table = 'map'
