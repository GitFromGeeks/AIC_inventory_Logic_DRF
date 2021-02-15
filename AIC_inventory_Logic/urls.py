from django.contrib import admin
from django.urls import path
from orders import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ordernow/',views.order_create),
    path('orderhistory',views.orderHistory.as_view()),
]
