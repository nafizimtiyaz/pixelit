# Generated by Django 3.2.6 on 2021-08-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0006_alter_user_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
