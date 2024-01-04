from api.views import CancelView, SuccessView, CreateCheckoutSessionView, ProductLandingPageView, OrderView, CreateCheckoutSessionOrderView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order_checkout/<int:order_id>', CreateCheckoutSessionOrderView.as_view(), name='order_checkout'),
    path('order/<int:order_id>', OrderView.as_view(), name='order'),
    path('item/<int:item_id>', ProductLandingPageView.as_view(), name='item'),
    path('buy/<int:item_id>', CreateCheckoutSessionView.as_view(), name='buy'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]
