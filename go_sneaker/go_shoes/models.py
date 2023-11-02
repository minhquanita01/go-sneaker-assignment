<<<<<<< HEAD
from django.db import models

# Create your models here.
class GO_Shoes(models.Model):
    shoesID = models.AutoField(primary_key=True)
    shoes_image_path = models.TextField()
    shoes_name = models.TextField()
    shoes_description = models.TextField()
    shoes_price = models.FloatField()
    shoes_color = models.CharField(max_length=10)
    shoes_quantity = models.IntegerField()

    class Meta:
        managed = False
=======
from django.db import models

# Create your models here.
class GO_Shoes(models.Model):
    shoesID = models.AutoField(primary_key=True)
    shoes_image_path = models.TextField()
    shoes_name = models.TextField()
    shoes_description = models.TextField()
    shoes_price = models.FloatField()
    shoes_color = models.CharField(max_length=10)
    shoes_quantity = models.IntegerField()

    class Meta:
        managed = False
>>>>>>> 0d41086a3a90370f94e40901e573e9ddf10d20c3
        db_table = 'go_shoes'