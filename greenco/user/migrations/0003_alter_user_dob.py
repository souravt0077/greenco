# Generated by Django 4.2.2 on 2023-06-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.IntegerField(null=True),
        ),
    ]
