import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Clear existing if any
Provider.objects.filter(subcategory_id=9).delete()

cities = [
    ("Vijayawada", 16.5062, 80.6480), ("Guntur", 16.3067, 80.4365),
    ("Nellore", 14.4426, 79.9865), ("Kurnool", 15.8281, 78.0373),
    ("Rajahmundry", 17.0005, 81.8040), ("Kakinada", 16.9891, 82.2475),
    ("Tirupati", 13.6288, 79.4192), ("Anantapur", 14.6819, 77.6006),
    ("Vizianagaram", 18.1067, 83.3955), ("Eluru", 16.7107, 81.1035),
    ("Ongole", 15.5057, 80.0499), ("Nandyal", 15.4779, 78.4831),
    ("Machilipatnam", 16.1875, 81.1389), ("Adoni", 15.6279, 77.2749),
    ("Proddatur", 14.7502, 78.5481), ("Tenali", 16.2390, 80.6458),
    ("Madanapalle", 13.5503, 78.5029), ("Chittoor", 13.2172, 79.1003),
    ("Hindupur", 13.8291, 77.4914), ("Bhimavaram", 16.5449, 81.5212),
    ("Guntakal", 15.1678, 77.3622), ("Dharmavaram", 14.4137, 77.7126),
    ("Srikakulam", 18.2949, 83.8938), ("Narasaraopet", 16.2356, 80.0495),
    ("Tadepalligudem", 16.8122, 81.5273), ("Amaravati", 16.5131, 80.5165),
    ("Chilakaluripet", 16.0892, 80.1611), ("Bapatla", 15.9045, 80.4674)
]

names_prefixes = ["Sri Lakshmi", "Green Grow", "AgroCare", "Rayalaseema", "Delta", "Annapurna", "Kisan", "Modern", "Rural", "Quality"]
names_suffixes = ["Fertilizers", "Agro Agencies", "Suppliers", "Bio-Fertilizers", "Farm Solutions", "Inputs", "Traders"]

master_services = [
    {"name": "Urea (45kg Bag)", "price": 266, "unit": "bag"},
    {"name": "DAP (50kg Bag)", "price": 1350, "unit": "bag"},
    {"name": "MOP Potash (50kg)", "price": 1700, "unit": "bag"},
    {"name": "Complex 20-20-0-13", "price": 1250, "unit": "bag"},
    {"name": "Organic Manure", "price": 450, "unit": "quintal"},
    {"name": "Vermicompost (25kg)", "price": 350, "unit": "bag"},
    {"name": "Neem Cake (50kg)", "price": 850, "unit": "bag"},
    {"name": "Zinc Sulphate (5kg)", "price": 550, "unit": "pack"},
    {"name": "Boron (1kg)", "price": 250, "unit": "pack"},
    {"name": "Liquid Bio-NPK", "price": 400, "unit": "litre"},
    {"name": "Magnesium Sulphate", "price": 600, "unit": "bag"},
    {"name": "Humic Acid Liquid", "price": 300, "unit": "500ml"},
    {"name": "Phosphate Organic (PROM)", "price": 950, "unit": "bag"},
    {"name": "Gypsum (50kg)", "price": 400, "unit": "bag"},
    {"name": "Copper Oxychloride", "price": 450, "unit": "500g"}
]

def run():
    try:
        subcat = SubCategory.objects.get(id=9)
        for i in range(28):
            city, lat, lon = cities[i]
            prefix = random.choice(names_prefixes)
            suffix = random.choice(names_suffixes)
            p_name = f"{prefix} {suffix} {city}"

            provider = Provider.objects.create(
                subcategory=subcat,
                name=p_name,
                location=f"{city}, Andhra Pradesh",
                latitude=lat,
                longitude=lon,
                price="₹266 onwards",
                description=f"Leading distributor of high-quality fertilizers and soil nutrients in {city}. Authorized dealer for national brands.",
                phone=f"98765438{i:02d}",
                verified=True,
                rating=random.uniform(4.0, 5.0),
                reviews=random.randint(10, 150)
            )

            # Select 4 to 12 services
            num_services = random.randint(4, 12)
            selected_services = random.sample(master_services, num_services)

            for s in selected_services:
                Service.objects.create(provider=provider, **s)

        print("Successfully inserted 28 Fertilizer providers with 4-12 services each!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
