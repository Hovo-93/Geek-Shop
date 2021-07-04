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
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': 6090,
             'decsription': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни',
             'image': 'vendor/img/products/Adidas-hoodie.png',
             },
            {'name': 'Синяя куртка The North Face',
             'price': 23725,
             'decsription': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель',
             'image': 'vendor/img/products/Blue-jacket-The-North-Face.png'
             },
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 3390,
                'decsription': 'Материал с плюшевой текстурой. Удобный и мягкий',
                'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                },
            {'name': 'Черный рюкзак Nike Heritage',
             'price': 2340,
             'decsription': 'Черный рюкзак Nike Heritage',
             'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
             },
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': 13590,
             'decsription': 'Гладкий кожаный верх. Натуральный материал.',
             'image': 'vendor/img/products/Black-Dr-Martens-shoes.png',
             },
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': 2890,
             'decsription': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             },
        ],
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
