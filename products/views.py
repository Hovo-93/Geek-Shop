from django.shortcuts import render


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
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals'},
            {'name': 'Синяя куртка The North Face'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN'},
        ],
        'promotion': True,
        'promotion_of_products': [
            {'name': 'Черный рюкзак Nike Heritage'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN'},
        ],
    }
    return render(request, 'products/products.html', context)
