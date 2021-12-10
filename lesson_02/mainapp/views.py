from django.shortcuts import render

# Create your views here.

menu_links = [
    {'href': '/', 'name': 'домой'},
    {'href': '/products', 'name': 'продукты'},
    {'href': '/contact', 'name': 'контакты'},
]

def main(request):

    return render(request, 'mainapp/index.html', context={
        'menu_links': menu_links,
    })


def products(request):

    menu_products = [
        {'href': '#', 'name': 'все'},
        {'href': '#', 'name': 'дом'},
        {'href': '#', 'name': 'офис'},
        {'href': '#', 'name': 'модерн'},
        {'href': '#', 'name': 'классика'},
    ]

    return render(request, 'mainapp/products.html', context={
        'menu_links': menu_links, 'menu_products': menu_products,
    })


def contact(request):

    return render(request, 'mainapp/contact.html', context={
        'menu_links': menu_links,
    })


