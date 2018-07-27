from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order as OrderModel, ProductOrder
from products.models import Product
from usermanagement.models import UserProfile

from django.core.mail import send_mail
from django.conf import settings


class Order(APIView):
    def post(self, request, format=None):
        data = request.data
        order = OrderModel.objects.create(user=request.user, submitted=timezone.now(), notes=data['notes'], po=data['po'])
        for product in data['products']:
            if product['quantity'] > 0:
                product_obj = Product.objects.get(product_number=product['number'])
                ProductOrder.objects.create(order=order, product=product_obj, quantity=product['quantity'])

        subject = 'New Order'
        message = 'New order: http://104.236.73.253:8000/fulfillment/{0}/'.format(order.pk)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['james@facscosales.com', ]
        send_mail(subject, message, email_from, recipient_list)
        resp = {"status": "success"}
        return Response(resp)


@login_required
def order_details(request, pk):
    order = OrderModel.objects.get(pk=pk)
    profile = UserProfile.objects.get(user=order.user)
    products = ProductOrder.objects.filter(order=order)
    return render(request, "order.html", {'order': order, 'profile': profile, 'products': products})


@login_required
def order_list(request):
    filled = OrderModel.objects.filter(filled__isnull=False)
    taken = OrderModel.objects.filter(filled__isnull=True, taken__isnull=False)
    untaken = OrderModel.objects.filter(taken__isnull=True)
    return render(request, "order_list.html", {'taken': taken, 'filled': filled, 'untaken': untaken})


@login_required
def order_take(request, pk):
    order = OrderModel.objects.get(pk=pk)
    print(order)
    order.taken = request.user
    print(request.user)
    print(order)
    order.save()
    return redirect('/fulfillment/{0}/'.format(pk))


@login_required
def order_fill(request, pk):
    order = OrderModel.objects.get(pk=pk)
    order.filled = request.user
    order.save()
    return redirect('/fulfillment/{0}/'.format(pk))