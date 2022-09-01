from dataclasses import dataclass
from email.mime import image
from multiprocessing import context
import os
from django.shortcuts import render,redirect,HttpResponseRedirect
from . models import *
from .forms import SignupForm,BlogForms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 


#signup_form
def sign_up(request):
    if request.method=="POST":
         fm=SignupForm(request.POST)
         if fm.is_valid():

            fm.save()
            messages.success(request,'Account created successfully')
            return redirect('login')
            
    else:
        fm = SignupForm()          
    
    return render(request,"signup.html",{'form':fm})




def login_form(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'login successfully')
                    return redirect('front')
                    
        else:
            fm=AuthenticationForm()
        return render(request,"login.html",{'form':fm})

    else:
        return redirect('front')



def userlogout(request):
    logout(request)
    return HttpResponseRedirect('login')


def front(request):
    if request.user.is_authenticated:
        post=Blog.objects.all()
        return render(request,"front.html",{'post':post})
    else:
        return redirect('login')

def fdepth(request,pk):
    if request.user.is_authenticated:
        post=Blog.objects.get(id=pk)
        return render(request,"dpost.html",{'post':post})
    else:
        return redirect('login')
def contact(request):
    if request.user.is_authenticated:
        return render(request,"contact.html")
    else:
        return redirect('login')


def about(request):
    if request.user.is_authenticated:
        return render(request,"about.html")
    else:
        return redirect('login')

def post(request):
    if request.user.is_authenticated:
        return render(request,"post.html")
    else:
        return redirect('login')

# def blog(request):
    
#     return render(request,'contact.html',{'fm':fm})

def save_blog(request):
    if request.method=="POST":
        newblog=BlogForms(request.POST,request.FILES)
        if newblog.is_valid():
            newblog.save()
            return redirect('front')
    else:
        fm=BlogForms()
        return render(request,'contact.html',{'fm':fm})



# update view for details
def update(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Blog    , id = id)
 
    # pass the object as instance in form
    form = BlogForms(data=(request.POST or None),
    files=(request.FILES or None),
    instance=obj,)


    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("front")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update.html", context)


def destroy(request,id):
    blogdata=Blog.objects.get(id=id)
    blogdata.delete()
    return redirect('front')