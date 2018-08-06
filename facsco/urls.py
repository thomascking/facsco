"""facsco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework.authtoken import views as rest_framework_views

from products.views import ListProducts, upload_products
from order.views import Order, order_details, order_list, order_take, order_fill, OrderDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', rest_framework_views.obtain_auth_token),
    path('products/', ListProducts.as_view()),
    path('order/', Order.as_view()),
    path('order/<int:pk>/', OrderDetails.as_view()),
    path('fulfillment/', order_list),
    path('fulfillment/<int:pk>/', order_details),
    path('fulfillment/<int:pk>/take/', order_take),
    path('fulfillment/<int:pk>/fill/', order_fill),
    path('upload/', upload_products),
]
