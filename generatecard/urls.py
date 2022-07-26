from django.urls import path

from . import views

urlpatterns = [
    path('', views.vcard_index, name="generatecard.vindex"),
    path('vform/', views.vcard_form, name='generatecard.vform'),
]
