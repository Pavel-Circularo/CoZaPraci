# Generated by Django 4.0.2 on 2022-05-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0003_alter_job_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]