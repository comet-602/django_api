from django.db import models
# Create your models here.
class fooddata(models.Model):
    date = models.TextField()
    name = models.TextField()
    price = models.TextField()
    img_url = models.TextField()
    content = models.TextField()
class Meta:
    db_table = "food_table"
