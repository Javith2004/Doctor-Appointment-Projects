from django.urls import path
from . import views
 
urlpatterns= [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('Appointmentorder',views.cart_page,name="cart"),
    path('remove_appointmnetorder/<str:cid>',views.remove_cart,name="remove_cart"),
    path('drcollections',views.collections,name="drcollections"),
    path('drcollections/<str:name>',views.collectionsview,name="drcollections"),
    path('drcollections/<str:cname>/<str:pname>',views.product_details,name="docter_details"),
    path('addtoappointment',views.add_to_cart,name="addtoappointment"),
]