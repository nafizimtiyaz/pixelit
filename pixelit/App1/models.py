from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from App1.slug_url import unique_slug_generator


class user_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    education = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    bio = models.TextField(max_length=1000)
    image = models.URLField()

    def __str__(self):
        return f'{self.user}'


class contactus(models.Model):
    name=models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    subject= models.CharField(max_length=100)
    message= models.TextField(max_length=10000)

    def __str__(self):
        return f'Name:{self.name} | Email: {self.email}'

class course(models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    price=models.CharField(max_length=100, null=True)
    unit=models.CharField(max_length=2000, null=True)
    discription = models.TextField(max_length=1000000)
    image = models.ImageField(upload_to="course")

    def __str__(self):
        return f'{self.title}'

@receiver(pre_save, sender=course)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

class lecture(models.Model):
    course= models.ForeignKey(course,on_delete=models.CASCADE)
    lecno=models.CharField(max_length=20000,null=False)
    title=models.TextField(max_length=20000)
    ldis=models.TextField(max_length=20000)
    def __str__(self):
        return f'Course:{self.course} | Lecture NO.: {self.lecno}'