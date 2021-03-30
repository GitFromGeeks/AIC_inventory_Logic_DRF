from django.contrib import admin
from django.urls import path,include
from orders import views
from sell import views as vue
from credit import views as vu
from phone import views as v
from myprofile import views as vi
from stockinfo import views as vw
from inventory import views as v_inv
from ledgers import views as vled
from acc import views as acc_v
from accorder import views as acor_V
from accinventory import views as acin_v
from accsell import views as acse_v
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('credit/',vu.credit_create.as_view()),
    path('profile/',vi.myprofileView.as_view()),
    path('profile/?search=',vi.myprofileView.as_view()),
    path('stockinfo/',vw.stockinfoView.as_view()),
    path('ledgers/',vled.ledgersView.as_view()),
    path('AICdebth/',vled.AICdebthView.as_view()),
    path('debth/',vled.debthView.as_view()),
    path('sellsdetail/',vue.export_pdf.as_view()),
    path('sellsdetail/<str:pk>/',vue.export_pdf.as_view()),

    path('phone/',v.phoneView.as_view()),
    path('phone/?search=',v.phoneView.as_view()),
    path('ordernow/',views.order_create.as_view()),
    path('orderdelete/<int:pk>/',views.orderdelete.as_view()),
    path('orderhistory/',views.orderHistory.as_view()),
    path('inventory+/',views.inventoryadd.as_view()),
    path('sell/',vue.sell_create.as_view()),
    path('sellshistory/',vue.sellsHistory.as_view()),
    path('inventory/',v_inv.inventoryView.as_view()),
    path('inventoryCreate/',v_inv.inventoryCreate.as_view()),
    path('mobilestock/',v_inv.mobilestockView.as_view()),
    path('mobilestockCreate/',v_inv.mobilestockCreate.as_view()),

    path('acc/',acc_v.accView.as_view()),
    path('acc/?search=',acc_v.accView.as_view()),
    path('acordernow/',acor_V.accorder_create.as_view()),
    path('acorderdelete/<int:pk>/',acor_V.accorderdelete.as_view()),
    path('accorderhistory/',acor_V.accorderHistory.as_view()),
    path('accinventory+/',acor_V.accinventoryadd.as_view()),
    path('accsell/',acse_v.accsell_create.as_view()),
    path('accsellshistory/',acse_v.accsellsHistory.as_view()),
    path('accinventory/',acin_v.accinventoryView.as_view()),
    path('accinventoryCreate/',acin_v.accinventoryCreate.as_view()),
    path('accstock/',acin_v.accstockView.as_view()),
    path('accstockCreate/',acin_v.accstockCreate.as_view()),
    path('login/',obtain_auth_token),
    path('transfer/',v_inv.transfer.as_view()),
    path('returnstock/',v_inv.Returnstock.as_view()),

]