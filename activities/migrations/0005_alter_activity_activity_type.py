# Generated by Django 5.1.2 on 2024-10-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_alter_activity_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(max_length=100),
        ),
    ]
