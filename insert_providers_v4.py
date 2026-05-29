import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

data = [
    {
        "name": "Krishna Dairy Solutions",
        "subcategory_id": 34,
        "price": "₹499 onwards",
        "location": "Vijayawada, AP",
        "latitude": 16.5062,
        "longitude": 80.6480,
        "about": "Expert dairy farm management and milk production services. We provide cattle health checkups, milking equipment support, and fodder management advice.",
        "phone": "9876543601",
        "verified": True,
        "detailedServices": [
            {"name": "Milk Quality Testing", "price": 499, "unit": "per sample"},
            {"name": "Cattle Health Checkup", "price": 899, "unit": "per visit"},
            {"name": "Automated Milking Setup", "price": 4999, "unit": "per install"}
        ]
    },
    {
        "name": "Pashu Palan Expert Center",
        "subcategory_id": 34,
        "price": "₹399 onwards",
        "location": "Guntur, AP",
        "latitude": 16.3067,
        "longitude": 80.4365,
        "about": "Specialized in goat and cattle breeding. We help farmers set up modern animal husbandry units with high-yield breeds.",
        "phone": "9876543602",
        "verified": True,
        "detailedServices": [
            {"name": "Artificial Insemination", "price": 1200, "unit": "per session"},
            {"name": "Feed & Nutrition Plan", "price": 399, "unit": "per plan"},
            {"name": "Vaccination Drive", "price": 200, "unit": "per animal"}
        ]
    }
]

def run():
    try:
        for p_data in data:
            sub_id = p_data.pop('subcategory_id')
            services = p_data.pop('detailedServices')
            about = p_data.pop('about')

            subcat = SubCategory.objects.get(id=sub_id)
            provider = Provider.objects.create(subcategory=subcat, description=about, **p_data)

            for s in services:
                Service.objects.create(provider=provider, **s)
        print("Inserted Dairy providers successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
