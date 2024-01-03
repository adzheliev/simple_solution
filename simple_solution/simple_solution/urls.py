from api.views import CancelView, SuccessView, CreateCheckoutSessionView, ProductLandingPageView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:id>', ProductLandingPageView.as_view(), name='item'),
    path('buy/<int:id>', CreateCheckoutSessionView.as_view(), name='buy'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]
