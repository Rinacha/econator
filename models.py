# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'Post'
# The error was: cannot unpack non-iterable NoneType object
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Product(models.Model):
    product_id = models.AutoField()
    product_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.IntegerField(blank=True, null=True)
    form = models.TextField(blank=True, null=True)  # This field type is a guess.
    mate = models.TextField(blank=True, null=True)  # This field type is a guess.
    method = models.TextField(blank=True, null=True)  # This field type is a guess.
    color = models.CharField(blank=True, null=True)
    size_d = models.IntegerField(blank=True, null=True)
    size_w = models.IntegerField(blank=True, null=True)
    url = models.CharField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class ShopPost(models.Model):
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True)
    form = models.TextField()
    mate = models.TextField()
    method = models.TextField()
    color = models.CharField(max_length=100)
    size_d = models.IntegerField(blank=True, null=True)
    size_w = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'shop_post'
