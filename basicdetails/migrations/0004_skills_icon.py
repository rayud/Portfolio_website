# Generated by Django 4.1.4 on 2023-01-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicdetails', '0003_remove_skills_user_about_skillset'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='icon',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]