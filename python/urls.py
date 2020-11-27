from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'Python' ),
    path('code/', views.code, name= 'Steps into Python' ),
    path('expressions/', views.expressions, name= 'expressions' ),
    path('variables/', views.variables, name= 'variables' ),
    path('io/', views.io, name= 'io' ),
    path('functions/', views.functions, name= 'functions' ),

]

# hello