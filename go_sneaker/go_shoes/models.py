from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.
class GO_Shoes(models.Model):
    shoesID = models.AutoField(primary_key=True)
    shoes_image_path = models.TextField()
    shoes_name = models.TextField()
    shoes_description = models.TextField()
    shoes_price = models.DecimalField(max_digits=16, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    shoes_color = models.CharField(max_length=10)
    shoes_quantity = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        managed = False
        db_table = 'go_shoes'