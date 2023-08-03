
from django.contrib import admin
from django.urls import path,include

urlpatterns = [ 
    path('', include('cmd1.urls')),
    path('admin/', admin.site.urls),

]