# Generated by Django 4.2.2 on 2023-07-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_remove_profile_email_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for Shipping', 'Out for Shipping'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Pending', max_length=150),
        ),
    ]
