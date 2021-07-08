from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "kingsres"

urlpatterns = [
    path('', views.home, name='home'),
    path('customer/order', views.customer_order, name='customer-order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)