from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns= [
    path('admin/', admin.site.urls),
    path("calculateBMI/",views.calculateBMI,name="calculateBMI"),
    path('',views.calculateBMI,name="calculateBMI")
]