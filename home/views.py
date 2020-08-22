from django.shortcuts import render, redirect, get_object_or_404
from .models import Rent,Contact,Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


# Create your views here.
def index(request):

    rents = Rent.objects.all()
    return render(request, 'index.html',{'rents': rents})

def about(request):
    return render(request,"about.html")

@login_required(login_url="accounts/login")
def car(request):
    rents = Rent.objects.all()
    return render(request,"car.html",{'rents': rents})

@login_required(login_url="accounts/login")
def profile(request):
        orders = Order.objects.all()
        return render(request,"profile.html",{'orders': orders})

@login_required(login_url="accounts/login")
def cardetail(request,cid):
    rents = Rent.objects.filter(id=cid)
    return render(request,"car-detail.html",{'rents':rents})

@login_required(login_url="accounts/login")
def b_history(request,id=None):
    details = Order.objects.filter(user_id=id)
    return render(request, "booking_history.html", {'details': details})
    

@login_required(login_url="accounts/login")
def book(request):
            return render(request,"book.html")

@login_required(login_url="accounts/login")
def search(request):
    if request.method=='POST':
        srch=request.POST['srh']

        if srch:
            match= Rent.objects.filter(Q(model_name__icontains=srch) |
                                       Q(car_name__icontains=srch))

            if match:
                return render(request,"search.html",{'sr':match})
            else:
                messages.error(request,'No result found')
        else:
            return HttpResponseRedirect('search')
    return render(request, "search.html")

@login_required(login_url="accounts/login")
def orderlist(request):
        orders = Order.objects.all()
        return render(request,"order-list.html",{'orders':orders})
@login_required(login_url="accounts/login")
def adminmsg(request):
        contacts = Contact.objects.all()
        return render(request,"admin-msg.html",{'contacts':contacts})


@login_required(login_url="accounts/login")
def adminuser(request):
    users = User.objects.all()
    return render(request, 'admin_user.html', {'users': users})


@login_required(login_url="accounts/login")
def contact(request):
    if request.method == "POST":
        c_name = request.POST.get('c_name','')
        c_email = request.POST.get('c_email','')
        c_subject = request.POST.get('c_subject','')
        c_message = request.POST.get('c_message','')
        contact = Contact(c_name=c_name,c_email=c_email,c_subject=c_subject,c_message=c_message)
        contact.save()

    return render(request,"contact.html")

@login_required(login_url="accounts/login")
def order(request,cid):

    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        o_amount = request.POST.get('o_amount', '')
        user_id = request.POST.get('user_id', '')
        o_name = request.POST.get('o_name','')
        o_num = request.POST.get('o_num','')
        o_address = request.POST.get('o_address','')
        o_email = request.POST.get('o_email','')
        o_from_date = request.POST.get('o_from_date', '')
        o_to_date = request.POST.get('o_to_date', '')
        order = Order(items_json=items_json,user_id=user_id,o_amount=o_amount,o_name=o_name,o_num=o_num,o_address=o_address,o_email=o_email,o_from_date=o_from_date,o_to_date=o_to_date)
        order.save()
        thank = True
        id = order.id
        e_subject = 'BOOKING CONFIRMED!'
        e_msg = 'Thank you for booking with us! Your booking has been confirmed'
        e_email = settings.EMAIL_HOST_USER
        #e_to_list = [order.o_email, settings.EMAIL_HOST_USER]
        send_mail(
            e_subject,
            e_msg,
            e_email,
            [o_email])
        #send_mail(e_subject,e_msg,e_email,e_to_list,fail_silently=True)
        return render(request, 'order.html', {'thank': thank, 'id': id})
    rents = Rent.objects.filter(id=cid)
    users = User.objects.all()
    return render(request,"order.html",{'rents':rents,'users':users})
