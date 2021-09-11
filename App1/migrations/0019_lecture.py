# Generated by Django 3.2.6 on 2021-09-08 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0018_alter_course_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecno', models.CharField(max_length=20000)),
                ('title', models.TextField(max_length=20000)),
                ('ldis', models.TextField(max_length=200000)),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App1.course')),
            ],
        ),
    ]
