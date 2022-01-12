from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField
from django.contrib.auth.models import User

FOUNDATION = 0
NG_ORGANIZATION = 1
LOCAL_COLLECTION = 2
INSTITUTION_TYPES = (
    (FOUNDATION, 'Fundacja'),
    (NG_ORGANIZATION, 'Organizacja pozarządowa'),
    (LOCAL_COLLECTION, 'Zbiórka lokalna')
)


class Category(models.Model):
    name = models.CharField(max_length=128)


class Institution(models.Model):
    name = CharField(max_length=128)
    description = models.TextField()
    type = models.IntegerField(choices=INSTITUTION_TYPES, default=FOUNDATION)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    address = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.PROTECT)

