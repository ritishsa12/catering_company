from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from mainpage.models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from amazon import settings

def indexpage(request):
    j=images.objects.filter(id=1).first()
    return render(request,'index.html',{'j':j})

def signup(request):
   j=images.objects.filter(id=1).first()
   if request.method=="POST":
      a=request.POST["name"]
      b=request.POST["password"]
      c=request.POST["username"]
      d=request.POST["phone"]
      e=request.POST["email"]
      f=request.POST["address"]
      if User.objects.filter(username=c).exists():
         print ("user already exists")
         return redirect("/signup")
      else:  
         user=ExtendedUser.objects.create_user(first_name=a,username=c,password=b,email=e,phone=d,adress=f)
         user.save()
      return redirect('/login')
   return render(request,"signin.html")

def login(request):
      if request.method=="POST":
        a=request.POST['username']   
        b=request.POST['password'] 
        print(a,b)
        user=auth.authenticate(username=a,password=b)
        if user is not None:
           auth.login(request,user)
           if request.user.is_authenticated:
            return redirect('/')
        else:
           print("not filled")
      return render(request,'login.html')

def logout(request):
   auth.logout(request)
   return redirect('/')

def aboutpage(request):
   j=images.objects.filter(id=1).first()
   return render(request,"about.html",{'j':j})

def reviewpage(request):
   j=images.objects.filter(id=1).first()
   x=review.objects.all()
   return render(request,"review.html",{'j':j,'x':x})

def samplepage(request):
   x=product.objects.all()
   return render(request,"sample_main.html",{"x":x})

def servicepage(request):
   j=images.objects.filter(id=1).first()
   return render(request,"service.html",{'j':j})

def orderonline(request):
   return render(request,"order_online.html")

def contact(request):
   j=images.objects.filter(id=1).first()
   return render(request,'contacts.html',{'j':j})


def addedrev(request):
   j=images.objects.filter(id=1).first()
   if request.method=='POST':
      a=request.POST["name"]
      b=request.POST["review"]
      obj=review(name=a,message=b)
      obj.save()
   return redirect('/reviewpage')

def submitdata(request):
   j=images.objects.filter(id=1).first()
   if request.method=="POST":  
        c=request.POST["email"]
        html_content=render_to_string("email_template.html")
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(
        "subscribed successfully",
        text_content,
        settings.EMAIL_HOST_USER,
        [c,'goelritish1@gmail.com'],
                )
        email.attach_alternative(html_content,"text/html")
        print(settings.EMAIL_HOST_USER)
        email.send(fail_silently=False) 
        gmail1(mail=c).save()
   #  if request.method=="POST":
   #       c=request.POST["email"]
   #       html_content=render_to_string("email_template.html")
   #       text_content=strip_tags(html_content)
   #       email=EmailMultiAlternatives(
   #       "query registration",
   #       text_content,
   #       settings.EMAIL_HOST_USER,
   #       [c,'goelritish1@gmail.com'],
   #               )
   #       email.attach_alternative(html_content,"text/html")
   #       email.send(fail_silently=False) 
   #       obj=gmail1(mail=c)
   #       obj.save()
         # return render (request,"index.html",{'j':j})

   return redirect("/")

def submitbutton(request,myid):
   myproduct=product.objects.filter(id=myid).first()
   print(myproduct)
   return render(request,"item.html",{'myproduct':myproduct})