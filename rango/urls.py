# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 14:46:43 2023

@author: 16448
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
]