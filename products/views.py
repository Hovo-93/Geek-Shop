from django.shortcuts import render
from products.models import Product,ProductCategory
import json
import os

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop Store',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals'},
            {'name': 'Синяя куртка The North Face'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN'},
        ]
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop Products',
        'products':Product.objects.all(),
        'categories':ProductCategory.objects.all(),
        'promotion': True,
        'promotion_of_products': [
            {'name': 'Черный рюкзак Nike Heritage',
             'price': 2340},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': 13590},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': 2890},
        ],
    }


    return render(request, 'products/products.html', context)
