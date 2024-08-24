from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationForm,CustomUserLoginForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.signals import user_logged_out



@login_required(login_url=reverse_lazy('signin'))
def index(request):
    
    message="Home Page"
    return render(request, 'home.html',{'msg':message})




def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request,"Successfully registered and logged in")
            return redirect('home')
        else:
             # Capture form errors and print them
            errors = form.errors.as_data()
            for field, error_list in errors.items():
                for error in error_list:
                    print(f"Error in {field}: {error}")
            print("Form is invalid")  # Redirect to a success page or the home page
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})



def user_login(request):
    if request.method =='POST':
        form=CustomUserLoginForm(request.POST)
        if form.is_valid():
            
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']

            user=authenticate(request,email=email,password=password)

            if user is not None:
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request,f"Successfully signed in as {user.username}")
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
            
    else:
        form=CustomUserLoginForm()

    return render(request,'signin.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.success(request,"Succesfully logged out")
    return redirect('signin')










