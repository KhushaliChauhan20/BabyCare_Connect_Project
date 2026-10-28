from urllib import request

from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone
from .models import *

# Create your views here.

def index(request):
    if 'login'or'pro_login' in request.session:
        service_data=service.objects.all()
        return render(request,'index.html',{'loggin':True,'service_data':service_data})
    else:
        return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def services(request):
    service_data=service.objects.all()
    return render(request,'service.html',{'service_data':service_data})

def events(request):
    return render(request,'event.html')

def blog(request):
    return render(request,'blog.html')

def team(request,id):
    team=service_provider.objects.filter(service=id)
    return render(request,'team.html',{'team':team})

def all_team_member(request):
    all_member=service_provider.objects.all()
    return render(request,'team.html',{'team':all_member})

def testimonials(request):
    return render(request,'testimonial.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    if request.method=='POST':
        obj=parent()
        obj.name=request.POST['name']
        obj.email=request.POST['email'] 
        obj.password=request.POST['pass']
        obj.par_mobile=request.POST['mobile']
        obj.address=request.POST['address']
        obj.no_child=request.POST['children']
        obj.child_age=request.POST['child_age']
        already_reg=parent.objects.filter(email=obj.email)
        if already_reg:
            return render(request,'registration.html', {'registered': 'Email already registered'})
        obj.save()
        return redirect('/login', {'saved': 'Registration successful'})
        
    else:
        return render(request,'registration.html')
    
def login(request):
    if request.method=="POST":
        try:
            register=parent.objects.get(email=request.POST['email'])
            if register.password==request.POST['pass']:
                request.session['login']=register.email
                return redirect('/',{'login':'login successful'})
            else:
                return render(request,'login.html',{'error':'Invalid password'})
        except:
            return render(request,'login.html',{'error':'Invalid email'})
    else:
        return render(request,'login.html')

def logout(request):
    if 'login' in request.session:
        del request.session['login']

    if 'pro_login' in request.session:
        del request.session['pro_login']

    return redirect('index')

def service_provider_reg(request):
    services = service.objects.all()
    if request.method == 'POST':
        obj = service_provider()
        obj.name = request.POST['name']
        obj.pro_email = request.POST['email']
        obj.pro_password = request.POST['pass']
        obj.pro_address = request.POST['address']
        obj.experience = request.POST['experience']
        obj.age = request.POST['age']
        obj.pro_price=request.POST['price']

        service_id = request.POST.get('service')
        obj.service = service.objects.get(id=service_id)

        already_reg = service_provider.objects.filter(pro_email=obj.pro_email)

        if 'photo' in request.FILES:
            obj.photo = request.FILES['photo']

        if already_reg:
            return render(request, 'service_provider_reg.html', {
                'registered': 'Email already registered',
                'services': services
            })
        else:
            obj.save()
            return redirect('service_prov_log')

    return render(request, 'service_provider_reg.html', {
        'services': services
    })  

def service_prov_log(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')

        try:
            user = service_provider.objects.get(pro_email=email)

            if user.pro_password == password:
                request.session['pro_login'] = user.pro_email
                return redirect('/')
            else:
                return render(request, 'service_pro_log.html', {
                    'error': 'Invalid password'
                })

        except service_provider.DoesNotExist:
            return render(request, 'service_pro_log.html', {
                'error': 'Invalid email'
            })

    return render(request, 'service_pro_log.html')

def book_pro(request,id):
     if 'login' in request.session:
        data=parent.objects.get(email=request.session['login'])
        provider = service_provider.objects.get(id=id)
        if request.method=="POST":
            obj=book()
            obj.parent=data
            obj.book_email=request.POST['email']
            obj.service_provider=provider
            obj.book_price=provider.pro_price
            obj.book_mobile=request.POST['number']
            obj.book_address=request.POST['address']
            obj.book_state=request.POST['state']
            obj.book_city=request.POST['city']
            obj.book_pincode=request.POST['pincode']
            obj.datetime = timezone.now()
            obj.save()
            messages.success(request, "Booking successful")
            return redirect('index')
        else:
            return render(request,'book.html',{'login':data, 'provider':provider})
     else:
         return redirect('login')
     
def your_bookings(request):
    if 'login' in request.session:
        parent_data = parent.objects.get(email=request.session['login'])
        bookings = book.objects.filter(parent=parent_data)
        return render(request, 'booking.html', {'bookings': bookings})
    else:
        return redirect('login')    
def cancel_booking(request,id):
    if 'login' in request.session:
        booking=book.objects.filter(id=id)
        booking.delete()
        messages.success(request, "Booking cancelled successfully")
        return redirect('your_bookings')
    elif 'pro_login' in request.session:
        booking=book.objects.filter(id=id)
        booking.transactions='False'
        booking.save()
        messages.success(request, "Booking cancelled successfully")
        return redirect('bookings_request')
    else:
        messages.error(request, "Not able to delete to cancel a booking")
        return redirect('your bookings')

def bookings_request(request):
    if 'pro_login' in request.session:
        provider_data = service_provider.objects.get(pro_email=request.session['pro_login'])
        bookings = book.objects.filter(service_provider=provider_data)
        return render(request, 'pro_book.html', {'bookings': bookings})
    else:
        return redirect('service_prov_log')

def accept_booking(request,id):
    if 'pro_login' in request.session:
        booking=book.objects.get(id=id)
        booking.transaction='True'
        booking.save()
        messages.success(request, "Booking accepted successfully")
        return redirect('bookings_request')
    else:
        messages.error(request, "Not able to accept the booking")
        return redirect('bookings_request')
