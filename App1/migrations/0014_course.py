# Generated by Django 3.2.6 on 2021-09-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0013_alter_user_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('discription', models.TextField(max_length=1000000)),
                ('image', models.ImageField(upload_to='course')),
            ],
        ),
    ]
