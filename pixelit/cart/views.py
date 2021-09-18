from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User,auth
from  django.contrib import messages
from App1.models import user_profile,contactus,course,lecture
from .models import CART
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

def user_cart(request,slug):
    if request.method == 'POST':
        email=request.POST["email"]
        name=request.POST["name"]
        mycourse = request.POST["course"]
        TransectionID = request.POST["TransectionID"]
        Transection_Number = request.POST["Transection_Number"]

        carts = CART(user=request.user,email=email,name=name, mycourse=mycourse, TransectionID=TransectionID,
                     Transection_Number=Transection_Number)
        carts.save()

        return redirect('phome')
    else:
        mycart = course.objects.get(slug=slug)
        return render(request, "checkout.html", {"mycart": mycart})