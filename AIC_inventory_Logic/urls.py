from django.contrib import admin
from django.urls import path
from orders import views
from sell import views as vue
from credit import views as vu
from phone import views as v
from myprofile import views as vi
from stockinfo import views as vw
from inventory import views as v_inv
from ledgers import views as vled

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ordernow/',views.order_create),
    path('orderhistory/',views.orderHistory.as_view()),
    path('sell/',vue.sell_create.as_view()),
    path('sellshistory/',vue.sellsHistory.as_view()),
    path('credit/',vu.credit_create.as_view()),
    path('phone/',v.phoneView.as_view()),
    path('profile/',vi.myprofileView.as_view()),
    path('stockinfo/',vw.stockinfoView.as_view()),
    path('inventory/',v_inv.inventoryView.as_view()),
    path('inventory/<int:pk>/',v_inv.inventoryView.as_view()),
    path('inventoryCreate/',v_inv.inventoryCreate.as_view()),
    path('ledgers/',vled.ledgersView.as_view()),
    path('AICdebth/',vled.AICdebthView.as_view()),
    path('debth/',vled.debthView.as_view()),
    
]
