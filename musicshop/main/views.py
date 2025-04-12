from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.

def index(request):

    context = {
        'title': 'Главная',
        'content': 'Магазин пластинок',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': 'Про нас:',
        'text_on_page': 'Наш магазин предоставляет товар, в виде музыкальных пластинок всех жанров. Каждый сможет найти здесь музыку на свой вкус, за доступную цену и бесплатной доставкой!'
    }

    return render(request, 'main/about.html', context)

def contact_us(request):
    context = {
        'title': 'Связь',
        'content': 'Свяжитесь с нами',
        'text_on_page': 'верщорзщеорщрозерщкорзкщорзерщозеро',
    }

    return render(request, 'main/contact_us.html', context)

def delivery_and_payment(request):
    context = {
        'title': 'Доставка и оплата',
        'content': 'Доставка и оплата',
        'text_on_page': 'кпшрзщпшукопрхукшщзперухкзщшпр',
    }

    return render(request, 'main/delivery_and_payment.html', context)