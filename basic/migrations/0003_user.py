# Generated by Django 3.0.5 on 2020-05-11 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20200419_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='user_id', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='username', max_length=20)),
                ('password', models.CharField(db_column='password', max_length=20)),
                ('created_at', models.DateField(db_column='created_at', default=django.utils.timezone.now)),
                ('updated_at', models.DateField(db_column='updated_at', default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
