# Generated by Django 4.0.2 on 2022-04-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0002_job_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='income',
            field=models.CharField(max_length=150),
        ),
    ]
