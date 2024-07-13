from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

global user1


@login_required(login_url='log_in')
def main(request):
    if request.method == 'POST':

        name = request.POST['vender']
        item = request.POST['item']
        qty = request.POST['qty']   
        ref = request.POST['ref']

        vender = Vendor.objects.get(id=name)
        
        v = Purchase.objects.create(vendor=vender,item=item,quantity=qty,ref=ref)
        v.save()
        
    return render(request,'test.html',{'venders': Vendor.objects.all()})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #user.objects.filter(username=username)
        user1 = user.objects.create(username=username,password=password)
        alert = True
        user1.save()
        return render(request,'login.html',{'alert':alert})
    return render(request,'signup.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = authenticate(username=username,password=password)
        if user1 is not None:
                login(request, user1)
                
                return redirect('main')
        else:
               return redirect('log_in')

    return render(request,'login.html')

@login_required(login_url='log_in')
def log_out(request):
    logout(request)
    return redirect('/')

@login_required(login_url='log_in')
def logs(request):
    result = Purchase.objects.all()
    if request.GET.get('search'):
         result = Purchase.objects.filter(item__icontains = request.GET.get('search'))
         
    return render(request,'log.html',{'hem':result })

@login_required(login_url='log_in')
def vender(request):
    if request.method == 'POST':
        name = request.POST['name']
        com = request.POST['company']
        cont=request.POST['contact']
        add=request.POST['add']

        v = Vendor.objects.create(company_name=com,vendor_name=name,contact_number=cont,address=add)
        v.save()
    ds = Vendor.objects.all()

    if request.GET.get('search'):
         ds = Vendor.objects.filter(company_name__icontains = request.GET.get('search'))
         

    
 #ven = Vendor.objects.all()
    return render(request,'vender_detail.html',{'ven':ds})
