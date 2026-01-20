from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# 1. Đăng ký
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerCreationForm # <--- Import form mới

# 1. Đăng ký
def register_view(request):
    if request.method == 'POST':
        # Dùng form mới ở đây
        form = CustomerCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomerCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


# 2. Đăng nhập
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# 3. Đăng xuất
def logout_view(request):
    logout(request)
    return redirect('login')