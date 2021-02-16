from django.contrib import admin
from django.urls import path
from orders import views
from sell import views as vue
from credit import views as vu
from phone import views as v
from myprofile import views as vi
from stockinfo import views as vw
from inventory import views as v_inv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ordernow/',views.order_create),
    path('orderhistory/',views.orderHistory.as_view()),
    path('sell/',vue.sell_create),
    path('sellshistory/',vue.sellsHistory.as_view()),
    path('credit/',vu.credit_create),
    path('phone/',v.phoneView.as_view()),
    path('profile/',vi.myprofileView.as_view()),
    path('stockinfo/',vw.stockinfoView.as_view()),
    path('inventory/',v_inv.inventoryView.as_view()),
    
]
