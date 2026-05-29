import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Clear existing if any
Provider.objects.filter(subcategory_id=7).delete()

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
    ("Guntakal", 15.1678, 77.3622), ("Dharmavaram", 14.4137, 77.7126),
    ("Srikakulam", 18.2949, 83.8938), ("Narasaraopet", 16.2356, 80.0495),
    ("Tadepalligudem", 16.8122, 81.5273), ("Amaravati", 16.5131, 80.5165),
    ("Chilakaluripet", 16.0892, 80.1611), ("Bapatla", 15.9045, 80.4674),
    ("Kadapa", 14.4673, 78.8242), ("Tadipatri", 14.9123, 78.0069)
]

names_prefixes = ["Rythu", "Gramin", "Village", "Kisan", "Rural", "Desi", "Anna", "Pragati", "Seva", "Jan"]
names_suffixes = ["Labour Group", "Workforce", "Coolie Sangham", "Labour Services", "Field Workers", "Labour Point", "Agri Workers", "Seva Center"]

master_services = [
    {"name": "Land Clearing & Leveling", "price": 450, "unit": "per person/day"},
    {"name": "Pit Digging (Plantation)", "price": 50, "unit": "per pit"},
    {"name": "Manual Weeding", "price": 400, "unit": "per person/day"},
    {"name": "Fertilizer Application", "price": 350, "unit": "per person/day"},
    {"name": "Manual Harvesting", "price": 500, "unit": "per person/day"},
    {"name": "Loading & Unloading", "price": 5, "unit": "per bag"},
    {"name": "Fencing Support Labor", "price": 450, "unit": "per person/day"},
    {"name": "Irrigation Canal Cleaning", "price": 400, "unit": "per person/day"},
    {"name": "Pruning & Trimming", "price": 550, "unit": "per person/day"},
    {"name": "Cotton Picking Labor", "price": 15, "unit": "per kg"},
    {"name": "Chili Picking Labor", "price": 25, "unit": "per kg"},
    {"name": "Maize De-husking", "price": 300, "unit": "per quintal"},
    {"name": "General Farm Helper", "price": 400, "unit": "per day"},
    {"name": "Pesticide Spraying Helper", "price": 450, "unit": "per day"},
    {"name": "Warehouse Labor", "price": 400, "unit": "per day"}
]

def run():
    try:
        subcat = SubCategory.objects.get(id=7)
        num_providers = random.randint(15, 30)
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
                price="₹350 onwards",
                description=f"Reliable manual labour groups in {city} for all agricultural needs. We provide skilled and semi-skilled field workers for seasonal and daily tasks.",
                phone=f"98765471{i:02d}",
                verified=True,
                rating=random.uniform(4.0, 4.8),
                reviews=random.randint(10, 200)
            )

            num_services = random.randint(5, 12)
            selected_services = random.sample(master_services, num_services)

            for s in selected_services:
                Service.objects.create(provider=provider, **s)

        print(f"Successfully inserted {num_providers} Manual Labour providers with 5-12 services each!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
