from typing import Any, Dict
import stripe
from django.contrib.sessions.models import Session
from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from http import HTTPStatus
from config import settings
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import OrderForm
from django.urls import reverse, reverse_lazy
from Mixin.views import TitleMixin
from .models import Order
from django.views.decorators.csrf import csrf_exempt
from products.models import Basket

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/success.html'
    title = "Store - Спасибо за заказ!"


class CancelTemplateView(TemplateView):
    template_name = 'orders/cancel.html'


class OrderListView(TitleMixin, ListView):
    template_name = 'orders/orders.html'
    title = 'Store - Заказы'
    queryset = Order.objects.all()
    ordering = ('-created_at',)

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)
    

class OrderDetailView(DetailView):
    template_name = 'orders/order.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['title'] = f'Store - #{self.object.id}'
        return context
      

class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order_create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Store - Оформление заказа'

    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        baskets = Basket.objects.filter(user=self.request.user)
        line_items = []
        for basket in baskets:
           item ={
                'price': basket.product.stripe_product_price_id,
                'quantity': basket.quantity,
           }
           line_items.append(item)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1NXAvaHBJPkJKn5kZ6di89ec',
                    'quantity': 1,
                },
            ],
            metadata={'order_id': self.object.id},
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_canceled')),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)


@csrf_exempt
def stripe_webhook_view(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, settings.STRIPE_SECRET_WEBHOOK
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
    session = stripe.checkout.Session.retrieve(
      event['data']['object']['id'],
      expand=['line_items'],
    )

    line_items = session.line_items
    print(line_items)
    # Fulfill the purchase...
    fulfill_order(line_items)

  # Passed signature verification
  return HttpResponse(status=200)

def fulfill_order(line_items):
  order_id = int(Session.metadata_id)
  order = Order.objects.get(id=order_id)
  order.update_after_payment()