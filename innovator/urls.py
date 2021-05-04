from django.contrib import admin
from django.urls import path
from django.urls import include
from .import views

urlpatterns = [

   
   path("signup/",views.signup,name="signup"),
   path("login/",views.login,name="login"),
   path("home/<int:tok>/<user>",views.home,name="home"),
   path("create",views.create,name="create"),
   path("detail/<int:product_id>/<username>/",views.detail,name='detail'),
   path("subcriber/<int:product_id>/<username>/<creator>",views.subcriber,name='subcriber'),
   path("showsubs/<int:product_id>/<creator>",views.showsubs,name='showsubs'),
   path("commentmake/<int:product_id>/<username>",views.commentmake,name="commentmake"),
   path("commentshow/<int:product_id>/<creator>",views.commentshow,name="commentshow"),
   path("buytoken/<int:tok>/<username>",views.buytoken,name='buytoken'),
   path("tokendonate/<int:product_id>/<username>/<creator>",views.tokendonate,name="tokendonate"),
   path("todoadd/<int:product_id>/<creator>",views.todoadd,name="todoadd"),
   path("manageproject/<int:product_id>/<creator>",views.manageproject,name="manageproject"),
   path("managetodo/<int:product_id>/<creator>",views.managetodo,name="managetodo"),
   path("manageaccount/<int:product_id>/<creator>",views.manageaccount,name="manageaccount"),
   path("encash/<int:product_id>/<creator>/<key>",views.encash,name="encash"),
   path("loginadmin/",views.loginadmin,name="loginadmin"),
   path("signupadmin/",views.signupadmin,name="signupadmin"),
   path("adminpagekey/",views.adminpagekey,name="adminpagekey"),
   path("adminmain/<adminname>",views.adminmain,name="adminmain"),
   


]
