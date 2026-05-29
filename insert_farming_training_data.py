import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Clear existing if any
Provider.objects.filter(subcategory_id=17).delete()

cities_pool = [
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
    ("Srikakulam", 18.2949, 83.8938), ("Narasaraopet", 16.2356, 80.0495),
    ("Amaravati", 16.5131, 80.5165), ("Kadapa", 14.4673, 78.8242),
    ("Dharmavaram", 14.4137, 77.7126), ("Guntakal", 15.1678, 77.3622),
    ("Tadipatri", 14.9123, 78.0069), ("Tanuku", 16.7570, 81.6994),
    ("Gudivada", 16.4347, 80.9930), ("Srikalahasti", 13.7502, 79.7042)
]

names_prefixes = ["Krishi", "Agri", "Modern", "Rural", "Green", "Precision", "Bharat", "Village", "Expert", "Smart"]
names_suffixes = ["Training Institute", "Skill Center", "Agri Academy", "Farming School", "Learning Hub", "Knowledge Point", "Kisan Pathshala"]

master_services = [
    {"name": "Organic Farming Workshop", "price": 1500, "unit": "per week"},
    {"name": "Hydroponics Basics", "price": 2500, "unit": "per course"},
    {"name": "Tractor Maintenance 101", "price": 800, "unit": "per session"},
    {"name": "Drone Spraying License", "price": 12000, "unit": "per person"},
    {"name": "Soil Health Management", "price": 500, "unit": "per day"},
    {"name": "Integrated Pest Management", "price": 1200, "unit": "per course"},
    {"name": "Drip Irrigation Setup", "price": 1000, "unit": "per day"},
    {"name": "Animal Husbandry Basics", "price": 1800, "unit": "per week"},
    {"name": "Seed Production Training", "price": 3000, "unit": "per course"},
    {"name": "Mushroom Cultivation", "price": 2000, "unit": "per 3-days"},
    {"name": "Agri-Business Startup", "price": 5000, "unit": "per course"},
    {"name": "Digital Marketing for Farmers", "price": 1200, "unit": "per week"},
    {"name": "Fodder Processing Techniques", "price": 900, "unit": "per day"},
    {"name": "Climate Resilient Farming", "price": 0, "unit": "Free Workshop"},
    {"name": "Bee-Keeping (Apiculture)", "price": 3500, "unit": "per course"}
]

def run():
    try:
        subcat = SubCategory.objects.get(id=17)
        num_providers = random.randint(12, 30) # Good variety for training
        selected_cities = random.sample(cities_pool, num_providers)

        for i in range(num_providers):
            city, lat, lon = selected_cities[i]
            prefix = random.choice(names_prefixes)
            suffix = random.choice(names_suffixes)
            p_name = f"{prefix} {suffix} {city}"

            provider = Provider.objects.create(
                subcategory=subcat,
                name=p_name,
                location=f"{city}, Andhra Pradesh",
                latitude=lat,
                longitude=lon,
                price="₹500 onwards",
                description=f"Authorized agricultural training and skill development center in {city}. We empower farmers with modern techniques, technology adoption, and sustainable practices.",
                phone=f"98765490{i:02d}",
                verified=True,
                rating=random.uniform(4.5, 5.0), # Training usually has high ratings
                reviews=random.randint(20, 350)
            )

            num_services = random.randint(5, 12)
            selected_services = random.sample(master_services, num_services)

            for s in selected_services:
                Service.objects.create(provider=provider, **s)

        print(f"Successfully inserted {num_providers} Farming Training providers with 5-12 courses each!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
