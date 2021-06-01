from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,name,contact,backup,password, **other_fields):
        other_fields.setdefault('is_active',True)
        if not email:
            raise ValueError(_("Email must be provided"))

        email = self.normalize_email(email)
        user = self.model(
            email = email,
            name = name,
            contact = contact, 
            backup = backup,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,name,contact,password, **other_fields):

        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        backup = password

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must be assign is_staff=True'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must be assign is_superuser=True'))

        return self.create_user(email,name,contact,backup,password,**other_fields)

class myUser(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(_('email address'),unique=True)
    name  = models.CharField(max_length=150,blank=True)
    contact = models.CharField(max_length=10,blank=True)
    backup = models.CharField(max_length=150,blank=True)
    no_of_books = models.IntegerField(default=0)
    no_of_notes = models.IntegerField(default=0)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','contact']

    def __str__(self):
        return self.name

class books(models.Model):

    email = models.EmailField(_('email address'))
    isbn = models.CharField(max_length=13,unique=True)
    type = models.CharField(max_length=150,blank=True)
    book_name = models.CharField(max_length=150,blank=True)
    author = models.CharField(max_length=150,blank=True)
    u_name = models.CharField(max_length=150,blank=True)
    date_upload = models.DateTimeField(verbose_name='upload date',auto_now=True)
    no_pages = models.CharField(max_length=100,default='no data')
    file  = models.FileField(blank=True)

class notes(models.Model):

    file_id = models.AutoField(primary_key=True,default=None)
    email = models.EmailField(_('email address'))
    note_name = models.CharField(max_length=150,blank=True)
    u_name = models.CharField(max_length=150,blank=True)
    date_upload = models.DateTimeField(verbose_name='upload date',auto_now=True)
    no_pages = models.CharField(max_length=100,default='no data')
    file  = models.FileField(blank=True)








    
