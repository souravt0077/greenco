# Generated by Django 4.2.2 on 2023-07-07 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_order_phone_alter_order_pincode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='fname',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lname',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
