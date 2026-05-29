import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import MainCategory, SubCategory, Provider, News, Banner

def seed():
    print("Seeding data...")

    # 1. Categories
    agri, _ = MainCategory.objects.get_or_create(slug="agriculture", defaults={'name': "Agriculture"})
    gard, _ = MainCategory.objects.get_or_create(slug="gardening", defaults={'name': "Gardening"})

    # 2. SubCategories
    soil, _ = SubCategory.objects.get_or_create(
        slug="soil-testing",
        defaults={'main_category': agri, 'name': "Soil Testing", 'icon': "flask"}
    )
    tractor, _ = SubCategory.objects.get_or_create(
        slug="tractor-rental",
        defaults={'main_category': agri, 'name': "Tractor Rental", 'icon': "truck"}
    )
    seeds, _ = SubCategory.objects.get_or_create(
        slug="seeds-plants",
        defaults={'main_category': gard, 'name': "Seeds & Plants", 'icon': "leaf"}
    )

    # 3. Providers
    p1, _ = Provider.objects.get_or_create(
        name="Harik Soil Labs",
        defaults={'subcategory': soil, 'rating': 4.5, 'reviews': 120, 'price': "₹500", 'location': "Hyderabad", 'verified': True}
    )
    p2, _ = Provider.objects.get_or_create(
        name="Reddy Tractors",
        defaults={'subcategory': tractor, 'rating': 4.8, 'reviews': 85, 'price': "₹2000/day", 'location': "Suryapet", 'verified': True}
    )
    p3, _ = Provider.objects.get_or_create(
        name="Eco Soil Services",
        defaults={'subcategory': soil, 'rating': 4.2, 'reviews': 45, 'price': "₹450", 'location': "Vijayawada", 'verified': False}
    )

    # 4. News
    News.objects.get_or_create(
        title="New Subsidy for Farmers",
        defaults={'date': "May 20, 2026", 'sub': "Government announces 50% discount on seeds.", 'content': "The agricultural department has launched a new scheme..."}
    )

    # 5. Banners
    Banner.objects.get_or_create(
        title="Expert Soil Testing",
        defaults={'subtitle': "Get reports in 24 hours", 'image_url': "https://example.com/banner1.jpg", 'icon': "star"}
    )

    print(f"Success! Database populated.")

if __name__ == "__main__":
    seed()
