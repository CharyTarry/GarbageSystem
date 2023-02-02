from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.landing, name='landingpage'),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('collector', views.collector, name="collector"),
    path('recycler', views.recycler, name="recycler"),
    path('myposts', views.myposts, name="myposts"),
    path('sendrequest/<int:ID>/', views.sendrequest, name="sendrequest"),
    path('garbagerequests', views.garbagerequests, name="garbagerequests"),
    path('acceptgarbreq/<int:ID>/', views.acceptgarbreq, name="acceptgarbreq"),
    path('firm', views.firm, name="firm"),
    path('myrequests', views.myrequests, name="myrequests"),
    path('delfirm/<str:Name>/', views.delfirm, name="delfirm"),
    path('delgarb/<int:ID>/', views.delgarb, name="delgarb"),
    path('cancelreq/<int:ID>/', views.cancelreq, name="cancelreq"),

]