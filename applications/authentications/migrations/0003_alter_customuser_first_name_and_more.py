# Generated by Django 5.1.4 on 2024-12-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnLogAuth', '0002_alter_customuser_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]