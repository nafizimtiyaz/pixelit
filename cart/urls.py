from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib import admin
from django.urls import path
from cart import views
from django.conf.urls.static import static
urlpatterns = [
    path('cart/<str:slug>',views.user_cart,name="carts"),
]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)