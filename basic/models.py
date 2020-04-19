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

