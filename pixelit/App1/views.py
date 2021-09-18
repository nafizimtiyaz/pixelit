from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User,auth
from  django.contrib import messages
from .form import ProfileUpdate
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .models import user_profile,contactus,course,lecture
from .token import account_activation_token



def home(request):
    if request.session.has_key('is_logged'):
        return redirect('profile')


    return render(request, 'index.html')

@login_required()
def student_profile(request):
    if request.session.has_key('is_logged'):
        return render(request, "profile.html")

@login_required()
def phome(request):
    if request.session.has_key('is_logged'):
        return render(request,"phome.html")

def registration(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if (password == password2):


            if User.objects.filter(username=username).exists():
                messages.info(request, "Email Is used")
                return render(request, 'SignUp.html')


            else:
                user = User.objects.create_user(username=username, password=password2, first_name=f_name,last_name=l_name)


                current_site = get_current_site(request)
                user.is_active = False
                user.save()

                email_subject = 'Active Your Account'
                message = render_to_string('Activation.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': user.id,
                    'token': account_activation_token.make_token(user)
                })

                from_email = settings.DEFAULT_FROM_EMAIL
                to_list = [user.username]
                send_mail(email_subject, message, from_email, to_list, fail_silently=True)

                messages.info(request, 'Account successfully created')
                return HttpResponse(
                    "<h1>Thank You For Registration;We send a Confirmation mail to you Mail Please Cnfirm MAil</h1>")
                #return render(request, "Login.html")

        else:
            messages.info(request, 'password not match')
            return render(request, 'SignUp.html')

    else:
        return render(request, 'SignUp.html')

def activate(request, uid, token):
    try:
         user=get_object_or_404(User, pk=uid)
    except:
        return HttpResponse('<h1>User Not found</h1>')
    if user is not None and account_activation_token.check_token(user, token):
         user.is_active= True
         user.save()
         return HttpResponse('<h1>Active, Now You Can <a href="http://127.0.0.1:8000/student/signup">Login</a></h1>')
    else:
        return HttpResponse('<h1>Invalid User Registration</h1>')


def singup(request):
    if request.session.has_key('is_logged'):
        return redirect('profile')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['is_logged'] = 1
            return redirect('home')
        else:
            messages.info(request, "Email or Password does not matched")
            return render(request, "Login.html")
    else:
        return render(request, "Login.html")

@login_required()
def logout(request):
    auth.logout(request)
    return redirect('signup')

@login_required()
def changePass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect("changePass")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form})
@login_required()
def profile(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        url = fs.url(filename)
        education = request.POST['education']
        location = request.POST['location']
        bio = request.POST['bio']
        image = url


        u_update = user_profile(user=request.user ,education=education, location=location, bio=bio, image=image)

        u_update.save()

        return render(request, "phome.html")

    else:
        return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        feedback = contactus(name=name,email=email,subject=subject,message=message)
        feedback.save()
        return redirect('/')

    else:
        return render(request,"contact.html")

def all_courses(request):
    allcourse=course.objects.all()
    return render(request,'allcourses.html',{"allcourse":allcourse})

def single(request,slug):
    obj = course.objects.get(slug=slug)
    courses = lecture.objects.filter(course_id=obj)
    return render(request, "course-details.html", {'obj': obj,"courses":courses})


def compiler(request):
    return render(request,"compiler.html")