# Generated by Django 2.1.5 on 2020-12-03 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrative',
            name='Contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Contact',
            field=models.IntegerField(null=True),
        ),
    ]
