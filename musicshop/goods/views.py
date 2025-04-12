from django.shortcuts import render

# Create your views here.


def catalog(request):
    context = {
        "title": "Каталог",
        "goods": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Surrounded by Freaks",
                "description": "Дебютный и последний альбом группы Tribal Ink",
                "price": 150.00,
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "A Whole Lot Of Nothing",
                "description": "Альбом группы Clawfinger",
                "price": 120.00,
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "No Geography",
                "description": "Альбом группы The Chemicals Brothers",
                "price": 130.00,
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "The Works",
                "description": "Альбом автора Chris Rea",
                "price": 160.00,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
