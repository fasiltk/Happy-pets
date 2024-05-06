from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('user_login/',user_login,name='user_login'),
    path('register/',register,name='register'),
    path('customer/',customer,name='customer'),
    path('manager/',manager,name='manager'),
    path('cart/<id>',cart,name='cart'),
    path('cart_view/',cart_view,name='cart_view'),
    path('upload/',upload,name='upload'),
    path('aprove/<id>',aprove,name='aprove'),
    path('delete/<id>',delete,name='delete'),
    path('customer_cart/',customer_cart,name='customer_cart'),
    path('done/<id>',done,name='done'),
    path('confirm_view/',confirm_view,name='confirm_view'),
    path('logout_view/',logout_view,name='logout_view'),
    path('detail/<id>',detail,name='detail'),
    path('details/',details,name='details'),
    path('chat/',chat,name='chat'),
    path('chatmanager/',chatmanager,name='chatmanager')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)