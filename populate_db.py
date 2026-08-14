import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from products.models import Category, Product
from accounts.models import CustomUser

def populate():
    # Create Superuser if not exists
    if not CustomUser.objects.filter(username='admin').exists():
        CustomUser.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser 'admin' created (pass: admin123)")

    # Categories
    electronics, _ = Category.objects.get_or_create(name='Electronics')
    fashion, _ = Category.objects.get_or_create(name='Fashion')
    home, _ = Category.objects.get_or_create(name='Home & Kitchen')

    # Products
    Product.objects.get_or_create(
        name='Premium Smartphone',
        defaults={
            'category': electronics,
            'description': 'A high-end smartphone with a stunning display and advanced camera.',
            'price': 999.99,
            'stock': 10,
            'available': True
        }
    )

    Product.objects.get_or_create(
        name='Wireless Headphones',
        defaults={
            'category': electronics,
            'description': 'Noise-canceling headphones with premium sound quality.',
            'price': 299.99,
            'stock': 50,
            'available': True
        }
    )

    Product.objects.get_or_create(
        name='Classic Leather Jacket',
        defaults={
            'category': fashion,
            'description': 'A timeless leather jacket made from premium materials.',
            'price': 199.99,
            'stock': 20,
            'available': True
        }
    )

    Product.objects.get_or_create(
        name='Modern Coffee Maker',
        defaults={
            'category': home,
            'description': 'Brew the perfect cup of coffee with this sleek machine.',
            'price': 89.99,
            'stock': 15,
            'available': True
        }
    )

    print("Demo data populated successfully.")

if __name__ == '__main__':
    populate()
