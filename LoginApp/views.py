from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import CustomUserForm,EditUserProfileForm

from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('/LoggedInPage')

    else:
        if request.method == 'POST':
            uname = request.POST.get('email')
            passw = request.POST.get('pswd')
            usr = authenticate(request, username=CustomUser.objects.get(email=uname), password=passw)
            if usr is not None:
                request.session.set_expiry(300)
                login(request,usr)
                return redirect('/LoggedInPage')
            else:
                return render(request, 'login.html')

        else:
            return render(request, 'login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('/LoggedInPage')

    else:
        if request.method == 'POST':
            form = CustomUserForm(request.POST)
            form.save()
            return redirect("/")
        else:
            form = CustomUserForm
            context = {'registerForm': form}
            return render(request, 'SignUpForm.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

    
import datetime

@login_required(login_url='/')
def afterlogin_view(request):
        id = request.user.id
        userlist = CustomUser.objects.filter(id=id)
        
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST,instance=request.user)
            fm.save()
            return redirect('/LoggedInPage')
        else:
            fm = EditUserProfileForm(instance=request.user)
            context = {'editform':fm , 'ul' : userlist}
            return render(request, 'home.html',context)

    

# @login_required(login_url='/')
# def profile_view(request):
#     if request.session <= 10 :
#         if request.method == 'POST':
#             fm = EditUserProfileForm(request.POST,instance=request.user)
#             fm.save()
#             return redirect('/LoggedInPage')
#         else:
#             fm = EditUserProfileForm(instance=request.user)
#             context = {'editform':fm}
#             return render(request,'home.html',context)

#     else:
#         logout(request)
#         return redirect('/')

@login_required(login_url='/')
def delete_details(request):
    id = request.GET.get('id')
    list = CustomUser.objects.get(id=id)
    list.delete()
    return redirect('/LoggedInPage')
    
