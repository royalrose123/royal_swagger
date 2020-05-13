from django.db import models
from django.utils.timezone import now


class Book(models.Model):
    id = models.AutoField(primary_key=True, db_column="book_id")
    name = models.CharField(max_length=100, null=False, blank=False, db_column="name")
    price = models.PositiveIntegerField(null=False, db_column="price")
    rent_price = models.PositiveIntegerField(null=True, db_column="rent_price")
    created_at = models.DateField(default=now, null=False, db_column="created_at")
    updated_at = models.DateField(default=now, null=False, db_column="updated_at")

    objects = models.Manager()

    class Meta:
        db_table = "book"


class User(models.Model):
    id = models.AutoField(primary_key=True, db_column="user_id")
    username = models.CharField(max_length=20, null=False, blank=False, db_column="username", unique=True)
    password = models.CharField(max_length=20, null=False, blank=False, db_column="password")
    email = models.CharField(default="123@gmail.com", max_length=20, null=False, blank=False, db_column="email")
    phone = models.CharField(default="0912345678", max_length=20, null=False, blank=False, db_column="phone")
    created_at = models.DateField(default=now, null=False, db_column="created_at")
    updated_at = models.DateField(default=now, null=False, db_column="updated_at")

    objects = models.Manager()

    class Meta:
        db_table = "user"

