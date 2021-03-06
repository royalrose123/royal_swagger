# Generated by Django 3.0.5 on 2020-04-19 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(db_column='book_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('price', models.PositiveIntegerField(db_column='price', max_length=100000)),
                ('rent_price', models.PositiveIntegerField(db_column='rent_price', max_length=1000, null=True)),
                ('created_at', models.DateField(db_column='created_at', default=django.utils.timezone.now)),
                ('updated_at', models.DateField(db_column='updated_at', default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
