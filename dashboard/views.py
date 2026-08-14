from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from orders.models import Order, OrderItem
from products.models import Product, Category
from django.db.models import Sum

def admin_check(user):
    return user.is_staff

@user_passes_test(admin_check)
def dashboard_overview(request):
    total_orders = Order.objects.count()
    total_sales = Order.objects.filter(paid=True).aggregate(total=Sum('items__price'))['total'] or 0
    total_products = Product.objects.count()
    recent_orders = Order.objects.all().order_by('-created')[:10]
    
    return render(request, 'dashboard/overview.html', {
        'total_orders': total_orders,
        'total_sales': total_sales,
        'total_products': total_products,
        'recent_orders': recent_orders
    })
