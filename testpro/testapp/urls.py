from django.urls import path,include
from . import views

urlpatterns = [
    #path('',views.signup,name='signup'),
    path('',views.log_in,name='log_in'),
    path('logout/',views.log_out,name='logout'),
    path('main/',views.main, name='main'),
    path('main/logs/',views.logs,name='logs'),
    path('main/vender-details/',views.vender,name='vender'),
    
]

