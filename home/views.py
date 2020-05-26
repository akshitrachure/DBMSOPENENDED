from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
#from django.contrib.auth import login, logout, authenticate
from home.models import passenger,bookings,trainDetails,payment_details
import requests,random,time,datetime

def home(request):
    return render(request,'first.html')


def login(request):
    if request.method=='POST':
        request.session['username'] = request.POST.get('name')
        request.session['password'] = request.POST.get('pass')
        uname = request.session['username']
        user1=None
        try:
            user1 =passenger.objects.get(username=request.session['username'],password=request.session['password'])
        except:
            user1=None        
        if user1 :
            return redirect('/link')                   
        else:
            messages.error(request,"Invalid Login Details given")
            return render(request,'login.html')
    else:
        return render(request,'login.html',{})

def link(request):
    return render(request,'link.html')


def signup(request):
    if request.method=='POST':
        request.session['name']=request.POST.get('name')
        request.session['username'] = request.POST.get('uname')
        request.session['email'] = request.POST.get('email')
        request.session['passw'] = request.POST.get('pass')
        request.session['phone'] = request.POST.get('phn')
        uname=request.session['username']
        check = None
        try:
            check = passenger.objects.get(username=request.session['username'])
            check1 = passenger.objects.get(email=request.session['email'])
            check2 = passenger.objects.get(username=request.session['username'],email=request.session['email'])
        except:
            check = None
            check1 = None
            check2 = None
        if check2:
            messages.error(request,'Username and email both already exists')
            return HttpResponseRedirect("/signup")
        if check1:
            messages.error(request,'Email already exists')
            return HttpResponseRedirect("/signup")
        if check:
            messages.error(request,'Username already exists')
            return HttpResponseRedirect("/signup")
        else:
            k = False
            user = passenger.objects.create(name=request.session['name'],username=request.session['username'],email=request.session['email'],phone=request.session['phone'],password=request.session['passw'])
            user.save()
            messages.success(request,'Your are registered successfully!!')
           # return redirect('/home/login1/You have successfully signed up')
            return redirect('/login')
    else:
        return render(request,'signup.html',{'msg':''})


def booking(request):
    if request.method=='POST':
        request.session['logname']=request.POST.get('loginname')
        request.session['train_no']=request.POST.get('trainno')
        request.session['train_name']=request.POST.get('trainname')
        request.session['jdate']=request.POST.get('journeyDate')
        request.session['froms']=request.POST.get('from')
        request.session['to']=request.POST.get('to')
        request.session['mobile']=request.POST.get('mobile')
        request.session['name']=request.POST.get('name')
        request.session['nation'] =request.POST.get('nationality')
        request.session['gender']=request.POST.get('gender')
        request.session['age']=request.POST.get('age')
        request.session['berth']=request.POST.get('cob')
        #a=booking.objects.all()        
        log=bookings.objects.create(train_name=request.session['train_name'],journey_date=request.session['jdate'],From=request.session['froms'],to=request.session['to'],phone=request.session['mobile'],name=request.session['name'],nationality=request.session['nation'],gender=request.session['gender'],age=request.session['age'],choice_of_berth=request.session['berth'],train_no_id=request.session['train_no'],username_id=request.session['logname'])
        log.save()
        return redirect('/payment')
    else:
        return render(request,'booking.html')


def payment(request):
    if request.method == "POST" :          
        #global uname,amount_to_be_paid
        request.session['uname']=request.session['username']
        request.session['nameoncard'] = request.POST.get('nameoncard')
        request.session['cardnumber'] = request.POST.get('cardnumber')
        request.session['expirymonth'] = request.POST.get('expirymonth')
        request.session['expiryyear'] = request.POST.get('expiryyear')
        request.session['cvv'] = request.POST.get('cvv')
        date=str(datetime.datetime.now())
        k = date.split(' ')
        p = str(k[0])
        p=p.split('-')
        if (request.session['expiryyear'] == p[0] and request.session['expirymonth'] > p[1]) or (request.session['expiryyear'] > p[0]) :
            log = payment_details.objects.create(username=request.session['uname'],card_no=request.session['cardnumber'],name_of_card_holder= request.session['nameoncard'],expiry_month=request.session['expirymonth'],expiry_year=request.session['expiryyear'],cvv=request.session['cvv'])
            log.save()
            return redirect('/otp')
        else:
            messages.error(request,"Your card is expired")
            return HttpResponseRedirect('/payment')
    else:
        users1 = None
        try:
            users1 = payment_details.objects.filter(username= request.session['uname'])
        except:
            users1 = None
        if users1:
            value1=int(users1[0].card_no)
            value2=str(users1[0].name_of_card_holder)
            return render(request,'payment.html')
            #return render(request,'payment.html',{'val1':value1,'val2':value2,'msg':'True'})
        else:
            print("else")
            return render(request,'payment.html')


def otp(request):
    #global uname,amount_to_be_paid
    if request.method=="POST":
        request.session['otp'] = request.POST.get('otp')
        with open("test.txt",'r') as f: 
            rn=f.readline()
            ts=f.readline()
        now=datetime.datetime.now()
        ki = str(now)
        ko = ki.split('.')
        date_time_obj1 = datetime.datetime.strptime(ko[0], '%Y-%m-%d %H:%M:%S')
        date_time_obj2 = datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
        print(date_time_obj1)
        rn=int(rn)
        sec = (date_time_obj1-date_time_obj2).total_seconds()
        request.session['otp']=int(request.session['otp'])
        print(rn,request.session['otp'])
        print(type(rn),type(request.session['otp']))
        # print(len(rn),len(otp))
        if (sec > 40) :
            messages.error(request,"OTP has been expired")
            return HttpResponseRedirect('/otp')
        elif rn!=request.session['otp'] :
            messages.error(request,"Please enter valid OTP")
            return HttpResponseRedirect('/otp')
        else:
            messages.success(request,"Your payment has been completed successfully.")
            return HttpResponseRedirect('/thankyou')

    else:
        return render(request,'otp.html',{'msg':''})

def output(request):
    print(request.session['uname'])
    user = passenger.objects.get(username=request.session['uname'])
    url = "https://www.fast2sms.com/dev/bulk"
    print(url)
    a = random.randint(100000,1000000)
    t = datetime.datetime.now()
    print(a)
    num="8296668513"
    payload = "sender_id=FSTSMS&message=OTP for booking a ticket account is "+str(a)+"&language=english&route=p&numbers="+num#str(user.phone)
    #print(user.phone)
    headers = {
    'authorization': "G0zVAeKlvLk0KnqQX3d5Kr5MujI3TODWqR6IKE5BXsorXpBLZvv7uBmoqf27",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    rn=str(a)
    ts=str(t)
    k = ts.split('.')
    # print(k[0])
    date_time_obj = datetime.datetime.strptime(k[0], '%Y-%m-%d %H:%M:%S')
    print(date_time_obj)
    # print(k[0])
    with open("test.txt",'w+') as f:  
        f.write(str(a)+'\n')
        f.write(str(k[0]))
    print("DONE")
    #message = "OTP has been sent to your registered mobile number"
    #return render(request, 'otp.html', {'msg':message})
    messages.success(request,"OTP has been sent to your registered mobile number")
    return HttpResponseRedirect('/otp')


def cancel(request):
    if request.method=='POST':
        request.session['uname']=request.POST.get('uname')
        request.session['train']=request.POST.get('trainno')
        request.session['jdate']=request.POST.get('jdate')
        bookings.objects.filter(username_id=request.session['uname'],train_no_id=request.session['train'],journey_date=request.session['jdate']).delete()
        return redirect('/thankyou2')
    else:
        return render(request,'cancel.html')




def trains(request):
    data = trainDetails.objects.all()
    return render(request,'traindetails.html',{'data':data})

def thankyou(request):
    return render(request,'thankyou.html')

def thankyou2(request):
    return render(request,'thankyou2.html')