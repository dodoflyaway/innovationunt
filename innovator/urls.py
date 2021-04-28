from django.contrib import admin
from django.urls import path
from django.urls import include
from .import views

urlpatterns = [

   
   path("signup/",views.signup,name="signup"),
   path("login/",views.login,name="login"),
   path("home/<int:tok>/<user>",views.home,name="home"),
   path("create",views.create,name="create"),
   path("detail/<int:product_id>/<username>",views.detail,name='detail'),
   path("subcriber/<int:product_id>/<username>/<creator>",views.subcriber,name='subcriber'),
   path("showsubs/<int:product_id>/<creator>",views.showsubs,name='showsubs'),
   path("commentmake/<int:product_id>/<username>",views.commentmake,name="commentmake"),
   path("commentshow/<int:product_id>/<creator>",views.commentshow,name="commentshow"),
   path("buytoken/<int:tok>/<username>",views.buytoken,name='buytoken'),



]
