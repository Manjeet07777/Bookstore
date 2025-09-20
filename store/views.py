from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Book,Order
from .forms import RegistrationForm,OrderForm
def index(request):
    # query=request.Get.get('q')
    books=Book.objects.all()
    # if query:
    #     books=books.filter(title_icontains=query)

    return render(request,'store/index.html',{'books':books})

def register_view(request):
    if request.method==('POST'):
        form=RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegistrationForm()

    return render(request,'store/register.html',{'form':form})

def login_view(request):
    if request.method==('POST'):
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user:
            login(request,user)
            return redirect('index')
    return render(request,'store/login.html')

def logout_view(request):
    logout(request)

    return redirect('login')

@login_required

def Place_order(request):
    if request.method==('POST'):
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            order.save()

            return redirect('orders')
    else:
        form=OrderForm()
    return render(request,'store/place_order.html',{'form':form})

@login_required

def order_list(request):
    orders=Order.objects.filter(user=request.user)

    return render (request, 'store/orders.html',{'orders':orders})
        