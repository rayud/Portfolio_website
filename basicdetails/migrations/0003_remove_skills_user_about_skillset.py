# Generated by Django 4.1.4 on 2023-01-12 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicdetails', '0002_experience_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='user',
        ),
        migrations.AddField(
            model_name='about',
            name='skillset',
            field=models.ManyToManyField(to='basicdetails.skills'),
        ),
    ]