from django.contrib import admin
from .models import myUser,books
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea,TextInput

# Register your models here.
class UserAdminConfig(UserAdmin):
    
    search_fields = ('email','name')
    ordering = ('date_joined',)
    list_display = ('email','name','contact','date_joined','is_active','is_superuser')

    fieldsets = (
        (None,{'fields':('email',)}),
        ('Permissions',{'fields':('is_staff','is_active','is_superuser')}),
        ('Personal',{'fields':('name','contact')}),
    )

admin.site.register(myUser,UserAdminConfig)
admin.register(books)
