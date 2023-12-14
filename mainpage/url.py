from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('admin/', admin.site.urls),
path('',views.indexpage,name='indexpage'),
path('logout',views.logout,name='logout'),
path('signup',views.signup,name='signup'),
path('login',views.login,name='login'),
path('aboutpage',views.aboutpage,name='aboutpage'),
path('reviewpage',views.reviewpage,name='reviewpage'),
path('servicepage',views.servicepage,name='servicepage'),
path('samplepage',views.samplepage,name='samplepage'),
path('orderonline',views.orderonline,name='orderonline'),
path('contact',views.contact,name='contact'),
path('submitdata',views.submitdata,name='submitdata'),
path('addedrev',views.addedrev,name='addedrev'),

path('submitbutton/<int:myid>',views.submitbutton,name='submitbutton'),
path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
path('password_reset/sent/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


