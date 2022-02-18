
from django.urls import path, include

urlpatterns = [
    path('toys/',include('toys.urls')),
    path('admins/',include('admins.urls')),
    path('',include('accounts.urls'))

]
