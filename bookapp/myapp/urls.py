from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home,name='home'),
    path("register",views.register,name='home'),
    path("login",views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('sendpassword',views.sendpass,name='sendpass'),

    
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard/profile',views.profile,name='profile'),
    path('dashboard/addbook',views.addbook,name='addbook'),
    path('dashboard/allusers',views.allusers,name='allusers'),
    path('dashboard/allbook',views.allbooks,name='allbooks'),
    path('dashboard/mybooks',views.mybooks,name='allbooks'),
    path('dashboard/allnotes',views.allnotes,name='allnotes'),
    path('dashboard/addnote',views.addnote,name="addnote"),


    path('delete/',views.deletebook,name="deletebook"),
    path('deletenote/',views.deletenote,name="deletenote"),
    path('dashboard/deleteuser',views.deleteuser,name="deleteuser")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)