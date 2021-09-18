from django.contrib import admin
from .models import user_profile,contactus,course,lecture

admin.site.register(user_profile)
admin.site.register(contactus)
admin.site.register(course)
admin.site.register(lecture)
