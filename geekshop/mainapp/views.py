from django.shortcuts import render, get_object_or_404
from .models import Product, CategoryProducts
from basketapp.models import Basket

# Create your views here.
products = Product.objects
PRODUCT_WITHOUT_MARK = products.filter(mark='')
PRODUCT_EXCLUSIVE = products.filter(mark='exclusive')
PRODUCT_TRENDING = products.filter(mark='trending')
URL_PAGE_PRODUCTS = 'mainapp:products_url:products:'

product_type = CategoryProducts.objects.all()


MENU = [
    {'href': 'mainapp:main', 'name': 'home', 'act':'main'},
    {'href': 'mainapp:products_url:products', 'name': 'products', 'act':'products',
     'namespace': 'mainapp:products_url'},
    {'href': 'mainapp:contacts', 'name': 'contacts', 'act':'contacts'},
]

# product_type = [
#     {'href': 'products_url:all', 'name': 'all'},
#     {'href': 'products_url:home', 'name': 'home'},
#     {'href': 'products_url:office', 'name': 'office'},
#     {'href': 'products_url:furniture', 'name': 'furniture'},
#     {'href': 'products_url:modern', 'name': 'modern'},
#     {'href': 'products_url:classic', 'name': 'classic'},
# ]



def main(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    products_shelf2 = PRODUCT_WITHOUT_MARK[:4]
    products_exclusive = PRODUCT_EXCLUSIVE[:2]
    products_trending = PRODUCT_TRENDING[:6]
    products_shelf6_max = PRODUCT_WITHOUT_MARK[4:5]
    products_shelf6_min = PRODUCT_WITHOUT_MARK[:4]

    context = {
        'title':'Главная',
        "list_menu": MENU,
        'products_shelf2': products_shelf2,
        'products_exclusive': products_exclusive,
        'products_trending': products_trending,
        'products_shelf6_max': products_shelf6_max,
        'products_shelf6_min': products_shelf6_min,
        'basket': basket,
    }

    return render(request, 'mainapp/index.html', context=context)


def contacts(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'Контакты',
        "list_menu": MENU,
        'basket': basket,
    }
    return render(request, 'mainapp/contacts.html', context=context)


def products(request, pk=None):
    title = 'Продукты'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk != None:
        if pk == 0:
            category = {'name': 'все'}
            products_ctg = Product.objects.all() # Сделать сортировку
        else:
            pk = int(pk)
            category = get_object_or_404(CategoryProducts, pk=pk)
            products_ctg = Product.objects.filter(category__pk=pk) # Сделать сортировку



        context = {
            'title': title,
            "list_menu": MENU,
            'product_list_menu': product_type,
            'products_ctg': products_ctg,
            'category': category,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', context=context)

    same_products = Product.objects.all()[:3]

    context = {
        'title': title,
        'list_menu': MENU,
        'product_list_menu': product_type,
        'products_ctg': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context)



def product(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'Продукт',
        "list_menu": MENU,
        'product_list_menu': product_type,
        'basket': basket,
    }
    return render(request, 'mainapp/product.html', context=context)