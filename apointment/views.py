from django.http import  JsonResponse
from django.shortcuts import redirect, render
from shop.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
 
def order_page(request):
  if request.user.is_authenticated:
    order=Cart.objects.filter(user=request.user)
    return render(request,"shop/appointmentorder.html",{"order":order})
  else:
    return redirect("/")
 
def remove_order(request,cid):
  orderitem=order.objects.get(id=cid)
  order.delete()
  return redirect("/order")
 
 
def add_to_appointment(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      docter_qty=data['docter_qty']
      docter_id=data['drid']
      #print(request.user.id)
      docter_status=docter.objects.get(id=docter_id)
      if docter_status:
        if order.objects.filter(user=request.user.id,product_id=docter_id):
          return JsonResponse({'status':'appointment Already in  order'}, status=200)
        else:
          if docter_status.quantity>=docter_qty:
            order.objects.create(user=request.user,docter_id=docter_id,product_qty=docter_qty)
            return JsonResponse({'status':'Product Added to Appointment'}, status=200)
          else:
            return JsonResponse({'status':'Docter Not Available'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add to Appointment'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
 
def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")
 
 
def login_page(request):
  if request.user.is_authenticated:
    return redirect("/")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        messages.success(request,"Logged in Successfully")
        return redirect("/")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("/login")
    return render(request,"template/login.html")
 
def register(request):
  form=CustomUserForm()
  if request.method=='POST':
    form=CustomUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"Registration Success You can Login Now..!")
      return redirect('/login')
  return render(request,"template/register.html",{'form':form})
 
 
def drcollections(request):
  catagory=Catagory.objects.filter(status=0)
  return render(request,"template/drcollections.html",{"catagory":catagory})
 
def drcollectionsview(request,name):
  if(Catagory.objects.filter(name=name,status=0)):
      docter=docter.objects.filter(category__name=name)
      return render(request,"template/docterlist.html",{"docter":docter,"category_name":name})
  else:
    messages.warning(request,"No Such Catagory Found")
    return redirect('drcollections')
 
 
def docter_details(request,cname,dname):
    if(drCatagory.objects.filter(name=cname,status=0)):
      if(docter.objects.filter(name=dname,status=0)):
        docter=docter.objects.filter(name=dname,status=0).first()
        return render(request,"apointment/template/drdetail.html",{"docter":docter})
      else:
        messages.error(request,"No Such docter Found")
        return redirect('drcollections')
    else:
      messages.error(request,"No Such Docter Catagory Found")
      return redirect('drcollections')