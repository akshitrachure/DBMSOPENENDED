from django.urls import path
from home import views
from home.views import *

urlpatterns=[
    path("",views.home, name="home"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('booking/', booking, name="booking"),
    path('thankyou/', thankyou, name="thankyou"),
    path('thankyou2/', thankyou2, name="thankyou2"),
    path('payment/', payment, name="payment"),
    path('otp/', otp, name="otp"),
    path('output/', output, name="output"),
    path('trains/', trains, name="trains"),
    path('cancel/', cancel, name="cancel"),
    path('link/', link, name="link"),

]