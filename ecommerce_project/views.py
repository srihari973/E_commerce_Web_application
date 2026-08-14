from django.shortcuts import render
from products.models import Product, Category

def home(request):
    categories = Category.objects.all()[:4]
    latest_products = Product.objects.filter(available=True).order_by('-created')[:8]
    return render(request, 'home.html', {
        'categories': categories,
        'latest_products': latest_products
    })
