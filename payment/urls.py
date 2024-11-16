from django.urls import path
from .views import ConfirmPaymentView
from . import views

app_name = 'payment'

urlpatterns = [
    path('success/', views.success, name='success'),
    path('', views.create_payment, name='create_payment'),
    path('proceed/<int:amount>/', views.proceed_payment, name='proceed_payment'),
    path('confirm-payment/', ConfirmPaymentView.as_view(), name='confirm_payment'),
]