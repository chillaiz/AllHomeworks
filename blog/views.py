from django.shortcuts import render

# Create your views here.
from blog.models import Product


def get_posts(request):
    products = Product.objects.all()

    data = {
        'products': products
    }

    return render(request, 'index.html', context=data)


# Create your views here.
from blog.models import Product


def get_posts(request):
    products = Product.objects.all()

    data = {
        'products': products
    }

    return render(request, 'index.html', context=data)
def get_post(request, id):
    product = Product.objects.get(id=id)

    data = {
        'product': product
    }

    return render(request, 'post.html', context=data)


def add_course(request):
    return  render(request, 'add.html')
