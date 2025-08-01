from django.db import models

# Create your models here.
class Vacant(models.Model):
    house_title = models.CharField(max_length=200)
    rent_fee = models.CharField( max_length = 100 , default = "Amount paid for the rent" )
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.house_title