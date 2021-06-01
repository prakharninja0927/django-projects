from django.contrib import messages
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
import smtplib
from .models import myUser,books,notes
from django.conf import settings
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def dashboard(request):
    updatebooks()
    admincount = len(myUser.objects.filter(is_superuser=1))
    membercount = len(myUser.objects.filter(is_superuser=0))
    allbook = len(books.objects.all())
    allnotes = len(notes.objects.all())
    mybooks =len(books.objects.filter(email=request.user.email))
    mynotes =len(notes.objects.filter(email=request.user.email))

    main_list = ['C','C++','C#','java','python','web(frontend)','web(backend)','data','ML','AI','cloud','cyber','statistics','database','other']

    db_list =[x[0]  for x in books.objects.values_list('type')]

    fre = {}
    for i in main_list:
        fre[i]=0
    
    for item in db_list:
        fre[item] +=1


    count = {
        'c_count':fre['C']+fre['C++']+fre['C#'],
        'java_count':fre['java'],
        'python_count':fre['python'],
        'web_count':fre['web(frontend)'] + fre['web(backend)'],
        'data_count':fre['data'] + fre['ML'] + fre['AI'] + fre['statistics'],
        'cc_count':fre['cloud']+fre['cyber'],
        'others_count':fre['other'],
        'db_count':fre['database']
    }
    
        
    context={
        'user_count' : admincount +membercount,
        'name':request.user.name,
        'allpdfs':allbook+allnotes,
        'allbooks':allbook,
        'allnotes':allnotes,
        'mybook':mybooks,
        'mynotes':mynotes,
        'count':count
    }
    return render(request,'dashboard/dashboard.html',context)

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        password1 = request.POST.get('password')
        password2 = request.POST.get('repeat-password')

        if myUser.objects.filter(email=email).exists():
            messages.warning(request,'email already exist!')
            return render(request,'register.html')
        else:
            if password1 != password2:
                messages.info(request, 'password are not match!')
                return render(request,'register.html')
            else:
                user = myUser.objects.create_user(
                    email = email,
                    name = name,
                    contact = contact,
                    password = password1,
                    backup = password1
                )
                subject = 'Thank You'
                message = f'Thank Your For Registration in Our BookApp'

                email_from = settings.EMAIL_HOST_USER                

                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email,]
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(email_from, 'prakhar123')
                server.sendmail(email_from, email ,message)
                server.close()

                return redirect('login')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            print("hello")
            return HttpResponseRedirect('dashboard')
        else:
            messages.error(request,"email or password is incorrect")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def sendpass(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if myUser.objects.filter(email=email).exists():
            user = myUser.objects.filter(email=email)
            backedpass =user[0].backup


            subject = 'Your Login Credentials'
            message = f'BookApp \nUsername = {user[0].email} \n Password = {backedpass} '

            email_from = settings.EMAIL_HOST_USER
            # recipient_list = [user[0].email, ]
            # send_mail( subject, message, email_from, recipient_list )

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(email_from, 'prakhar123')
            server.sendmail(email_from, email ,message)
            server.close()

            messages.success(request,"password sent check your mail")
            return render(request,'sendpass.html')
        else:
            messages.error(request,"User not exists")
            return render(request,'sendpass.html')

    return render(request,'sendpass.html')


@login_required(login_url='login')
def allusers(request):
    updatebooks()
    admins = myUser.objects.filter(is_superuser=1)
    members =myUser.objects.filter(is_superuser=0)

    context = {
        'admins':admins,
        'members':members
    }
    if request.user.is_superuser:
        return render(request,'dashboard/allusers.html',context)
    else:
        return redirect('/dashboard')


@login_required(login_url='login')
def profile(request):
    return render(request,'dashboard/profile.html')

@login_required(login_url='login')
def addbook(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        typ = request.POST.get('select')
        bookname = request.POST.get('bookname')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        pages = request.POST.get('pages')
        doc = request.FILES['pdf']
        u_name = ""
        book_type =""
        usr = myUser.objects.filter(email=email)
        if usr is not None:
            u_name = usr[0].name
           
        if typ =='C':
            if bookname.upper().find('C++')!=-1 or bookname.upper().find('C ++')!=-1 or bookname.lower().find('c plus plus')!=-1:
                book_type = 'C++'
            elif bookname.upper().find('C#')!=-1 or bookname.upper().find('C #')!=-1 or bookname.lower().find('c sharp')!=-1:
                book_type = 'C#'
            else:
                book_type = 'C'
        elif typ =='Data':
            if bookname.lower().find('statistics')!=-1 or bookname.lower().find('statistical')!=-1 or bookname.lower().find('linear algebra')!=-1 or bookname.lower().find('maths')!=-1 or bookname.lower().find('mathematics')!=-1 or bookname.lower().find('stats')!=-1 or bookname.lower().find('probability')!=-1:
                book_type = 'statistics'  
            elif bookname.lower().find('machine learning')!=-1 or bookname.upper().find('ML')!=-1 or bookname.lower().find('deep learning')!=-1 :
                book_type = 'ML'
            elif bookname.lower().find('data')!=-1 or bookname.lower().find('data science')!=-1:
                book_type = 'data'                      
            else:
                book_type = "AI"
        else:
            book_type = typ    
        
        if books.objects.filter(isbn=isbn).exists():
            messages.error(request,"Book Alreday Exists")
        else:
            book = books(
                email = email,
                isbn = isbn,
                type = book_type,
                book_name = bookname,
                author =author,
                u_name = u_name,
                no_pages = pages,
                file=doc
            )      
            book.save()
        updatebooks()
        
    return render(request,'dashboard/addbook.html')

@login_required(login_url='login')
def allbooks(request):
    allbooks = books.objects.all()  
    context = {
        'books':allbooks
    }
    return render(request,'dashboard/allbooks.html',context)

@login_required(login_url='login')
def mybooks(request):
    current_usr = request.user.email
    usr_books = books.objects.filter(email=current_usr)
    usr_notes = notes.objects.filter(email=current_usr)
    context={
        'mybooks':usr_books,
        'mynotes':usr_notes
    }
    return render(request,'dashboard/mybook.html',context)

def updatebooks():
    allemails = myUser.objects.values_list('email')
    obj=[]
    nts=[]
    for mail in allemails:
        obj.append(len(books.objects.filter(email=mail[0])))
        nts.append(len(notes.objects.filter(email=mail[0])))
    

    for count,note,mail in zip(obj,nts,allemails):
        usrobj = myUser.objects.get(email=mail[0])
        usrobj.no_of_books = count
        usrobj.no_of_notes = note
        usrobj.save()


@login_required(login_url='login')
def deletebook(request):
    if request.method == 'POST':
        isbn = request.POST.get('isbn')
        
        obj = books.objects.get(isbn=isbn)
        obj.delete()
        updatebooks()
        return JsonResponse({'status':1})
        
    else:
        return JsonResponse({'status':0})


@login_required(login_url='login')
def deletenote(request):
    if request.method =="POST":
        file_id = request.POST.get('file_id')
        obj = notes.objects.get(file_id=file_id)
        obj.delete()
        updatebooks()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

@login_required(login_url='login')        
def deleteuser(request):
    if request.method =='POST':
        email = request.POST.get('email')
        print(email)
        allbooks = len(books.objects.filter(email=email))
        if allbooks>0:
            bks = books.objects.get(email=email)
            bks.delete()

        allnotes = len(notes.objects.filter(email=email))
        if allnotes>0:
            nts = notes.objects.get(email=email)
            nts.delete()
    
        usr = myUser.objects.get(email=email)
        usr.delete()
        subject = 'Your Login Credentials'
        message = f'You Deleted Your BookApp Account'
        # auth.logout(request)
        email_from = settings.EMAIL_HOST_USER           
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_from, 'prakhar123')
        server.sendmail(email_from, email ,message)
        server.close()
        messages.error(request,"Your Account Is successfully Deleted")
        return HttpResponseRedirect("/login")

@login_required(login_url='login')
def addnote(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        notename = request.POST.get('notename')
        pages = request.POST.get('pages')
        doc = request.FILES['pdf']
        u_name = ""
        usr = myUser.objects.filter(email=email)
        if usr is not None:
            u_name = usr[0].name

        note = notes(
            email=email,
            note_name=notename,
            no_pages=pages,
            u_name=u_name,
            file = doc
        )
        note.save()


    return render(request,'dashboard/addnote.html')


@login_required(login_url='login')
def allnotes(request):
    allnotes = notes.objects.all()      
    context = {
        'notes':allnotes
    }
    return render(request,'dashboard/allnotes.html',context)
