from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from App1 import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('home',views.phome,name="phome"),
    path('student/registration',views.registration,name="regi"),
    path('student/signup',views.singup,name="signup"),
    path('student/logout', views.logout, name="out"),
    path('account/email/change/password',views.changePass,name="changePass"),
    path('user/profile',views.student_profile,name="profile"),
    path('compiler',views.compiler,name="compiler"),
    path('activate/<uid>/<token>/', views.activate, name="activate"),
    path('profile/update',views.profile,name="m_profile"),
    path('contact-us',views.contact,name="contact"),
    path('course',views.all_courses,name="allcourse"),
    path('course/<str:slug>',views.single,name="single"),
    path('all/',include("cart.urls")),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)