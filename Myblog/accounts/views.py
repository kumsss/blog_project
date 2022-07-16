from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        user = User.objects.create_user(username = username, password = password1 )
        user.save()
        print ('created user')
        return redirect('/')
        
    else:
        return render (request, 'accounts/register.html')
