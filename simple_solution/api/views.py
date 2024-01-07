"""Views classes of my application"""

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from .models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductLandingPageView(TemplateView):
    """Class for product visualization"""
    template_name = "landing.html"

    def get_context_data(self, **kwargs) -> dict:
        """Creating context to transmit to template"""
        context = super().get_context_data(**kwargs)
        item_id = self.kwargs["item_id"]
        item = get_object_or_404(Item, id=item_id)
        context["item"] = item
        context.update({"STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLISHABLE_KEY})
        return context


class CreateCheckoutSessionOrderView(View):
    """Stripe Checkout for Orders"""
    def get(self, request, *args, **kwargs) -> JsonResponse:
        """Creating Stripe session for order"""
        order_id = self.kwargs["order_id"]
        DOMAIN: str = "http://127.0.0.1:8000"
        order = Order.objects.get(id=order_id)

        #Taxes and Discounts for Stripe are still under developing

        # tax_rates = []
        # for tax in order.tax.all():
        #     tax_rate = stripe.TaxRate.create(
        #         display_name=tax.name,
        #         description=tax.name,
        #         percentage=tax.rate,
        #         jurisdiction="RU",
        #         inclusive=False,
        #     )
        #     tax_rates.append(tax_rate.id)
        #
        # discounts = []
        # for discount in order.discount.all():
        #     discount_amount = stripe.Coupon.create(
        #         amount_off=discount.amount,
        #         duration='once',
        #         currency='usd',
        #         name=discount.name,
        #     )
        #     discounts.append(discount_amount.id)

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": order.get_total_cost() * 100,
                        "product_data": {
                            "name": order.__str__(),
                        },
                    },
                    "quantity": 1,
                },
            ],
            payment_intent_data={
                "metadata": {
                    "order_id": order.id,
                },
            },
            mode="payment",
            success_url=DOMAIN + "/success/",
            cancel_url=DOMAIN + "/cancel/",
            # tax_rates=tax_rates,
            # discounts=[{"discounts": '{{COUPON_ID}}'}],
        )
        return JsonResponse({"id": session.id})


class CreateCheckoutSessionView(View):
    """Stripe Checkout for single product"""
    def get(self, request, *args, **kwargs) -> JsonResponse:
        """Creating Stripe session for order"""
        item_id = self.kwargs["item_id"]
        DOMAIN: str = "http://127.0.0.1:8000"
        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": item.price * 100,
                        "product_data": {
                            "name": item.name,
                        },
                    },
                    "quantity": 1,
                },
            ],
            payment_intent_data={
                "metadata": {
                    "item_id": item.id,
                },
            },
            mode="payment",
            success_url=DOMAIN + "/success/",
            cancel_url=DOMAIN + "/cancel/",
        )
        return JsonResponse({"id": session.id})


class SuccessView(TemplateView):
    """Class for successful payment template"""
    template_name = "success.html"


class CancelView(TemplateView):
    """Class for cancelled payment template"""
    template_name = "cancel.html"


class OrderView(TemplateView):
    """Class for Order model"""
    model = Order
    template_name = "order.html"

    def get_context_data(self, **kwargs) -> dict:
        """Creating context to transmit to template"""
        context = super().get_context_data(**kwargs)
        order_id = self.kwargs["order_id"]
        order = get_object_or_404(Order, id=order_id)
        context["order"] = order
        context.update(
            {
                "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLISHABLE_KEY,
                "name": order.__str__(),
                "items": order.items,
                "total": order.get_total_cost(),
            }
        )
        return context
