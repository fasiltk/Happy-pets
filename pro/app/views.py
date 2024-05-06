# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Users,Pets,Buy,Confirm,ChatUser,ChatManager
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username'] = username
        request.session['password'] = password

        customer_Users = Users.objects.filter(username=username, password=password, role="customer").exists()
        manager_Users = Users.objects.filter(username=username, password=password, role="manager").exists()
        request.session['customer_Users']=customer_Users
        request.session['manager_Users']=manager_Users

        if customer_Users:
            return redirect('customer')
        elif manager_Users:
            return redirect('manager')
        else:
            # Handle case where user doesn't match any role
            messages.error(request, "Invalid username or password")    
    return render(request, "user_login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')
        role = request.POST.get('role')
        fm = Users(username=username, password=password, name=name, phonenumber=phonenumber, role=role)
        fm.save()
        return redirect(user_login)
    return render(request, "register.html")
def customer(request):
    customer_Users=request.session.get('customer_Users')
    if customer_Users:
        a=Pets.objects.all()
        return render(request, "customer.html",{'a':a})
    else:
        return redirect('index')
def manager(request):
    manager_Users=request.session.get('manager_Users') #using session and if username can't navigate / first request.session.flush
    if manager_Users:
        a=Pets.objects.all()
        return render(request,"manager.html",{'a':a})
    return redirect(index)
def cart(request,id):
    username=request.session.get('username')
    d=Pets.objects.get(id=id)
    pet_name=d.pet_name
    description=d.description
    image=d.image
    fm=Buy(pet_name=pet_name,description=description,image=image,username=username)
    fm.save()
    subject = 'Replay mail'
    message = f'Thanks for contacting us, {username} for more details contact us'
    send_mail(subject,message, settings.EMAIL_HOST_USER, [username],fail_silently=False)
    return redirect('customer')
def cart_view(request):
    a=Buy.objects.all()
    return render(request, "cart.html",{'a':a})
from django.core.files.storage import FileSystemStorage

def upload(request):
    if request.method == 'POST':
        pet_name = request.POST.get('pet_name')
        description = request.POST.get('description')
        age=request.POST.get('age')
        food=request.POST.get('food')
        medical=request.POST.get('medical')
        price=request.POST.get('price')
        image = request.FILES['image']  # Access the uploaded file using request.FILES
        # Save the uploaded image
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_image_url = fs.url(filename)
        # Now, save the data to the Pets model
        fm = Pets(pet_name=pet_name, description=description, image=uploaded_image_url,age=age,food=food,medical=medical,price=price)
        fm.save()
    return render(request, "upload.html")

def aprove(request,id):
    d=Buy.objects.get(id=id)
    pet_name=d.pet_name
    description=d.description
    image=d.image
    username=d.username
    fm=Confirm(pet_name=pet_name,description=description,image=image,username=username)
    fm.save()
    d.delete()
    return redirect('cart_view')
def delete(request,id):
    d=Pets.objects.get(id=id)
    d.delete()
    return redirect('manager')
def customer_cart(request,id):
    username=request.session.get('username')
    a=Confirm.objects.filter(username=username)
    return render(request,"customer_cart.html",{'a':a})
def done(request,id):
    d=Confirm.objects.get(id=id)
    d.delete()
    return redirect('confirm_view')
def confirm_view(request):
    username=request.session.get('username')
    a=Confirm.objects.filter(username=username)
    return render(request,"customer_cart.html",{'a':a})
def index(request):
    return render(request,"index.html")
def logout_view(request):
   request.session.flush()
   return redirect('index')
def details(request):
    return render(request,"details.html")
def detail(request, id):
    pet = get_object_or_404(Pets, id=id)
    return render(request, "details.html", {'a': [pet]})
def chat(request):
    a = ChatUser.objects.all()
    username = request.session.get('username')
    b = ChatManager.objects.all()
    n = Users.objects.filter(username=username).first()  # Corrected line
    name = n.name
    if request.method == 'POST':
        message = request.POST.get('message')
        fm = ChatUser(usr=username, message=message)
        fm.save()
        return redirect('chat')
    
    return render(request, "chat.html", {'a': a, 'b': b, 'username': username,'name':name})
def chatmanager(request):
    a=ChatUser.objects.all()
    if request.method == 'POST':
        message = request.POST.get('message')
        usruser=request.POST.get('email')
        fm=ChatManager(message=message,usruser=usruser)
        fm.save()
        return redirect('chatmanager')
    return render(request,"chatmanager.html",{'a':a})
