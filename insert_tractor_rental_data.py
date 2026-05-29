import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# 1. Update the icon for Tractor Rental (ID 45)
try:
    subcat = SubCategory.objects.get(id=45)
    subcat.icon = 'tractor'
    subcat.save()
    print("Updated Tractor Rental icon to 'tractor'")
except SubCategory.DoesNotExist:
    print("Tractor Rental subcategory not found. Please check ID.")

# 2. Clear existing providers if any (to avoid duplicates)
Provider.objects.filter(subcategory_id=45).delete()

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
    ("Tadipatri", 14.9123, 78.0069), ("Tanuku", 16.7570, 81.6994),
    ("Gudivada", 16.4347, 80.9930), ("Srikalahasti", 13.7502, 79.7042)
]

names_prefixes = ["Mahindra", "John Deere", "Sonalika", "Swaraj", "New Holland", "Eicher", "Massey Ferguson", "Kubota", "Farmtrac", "Captain"]
names_suffixes = ["Tractor Rentals", "Farm Power Hub", "Agri Wheels", "Tractor Point", "Rental Services", "Tractor World", "Power Solutions"]

master_services = [
    {"name": "Standard Tractor (50 HP)", "price": 2500, "unit": "per day"},
    {"name": "Mini Tractor (25 HP)", "price": 1500, "unit": "per day"},
    {"name": "Heavy Duty Tractor (75 HP)", "price": 4000, "unit": "per day"},
    {"name": "Tractor with Rotavator", "price": 3500, "unit": "per day"},
    {"name": "Tractor with Disc Plough", "price": 3200, "unit": "per day"},
    {"name": "Tractor with Seed Drill", "price": 3000, "unit": "per day"},
    {"name": "Tractor Trolley Rental", "price": 800, "unit": "per day"},
    {"name": "Tractor for Leveling", "price": 600, "unit": "per hour"},
    {"name": "Tractor for Puddling", "price": 700, "unit": "per hour"},
    {"name": "Driver with Fuel service", "price": 1200, "unit": "extra/day"},
    {"name": "Narrow Track Orchard Tractor", "price": 2200, "unit": "per day"},
    {"name": "Backhoe Attachment Rental", "price": 1500, "unit": "per day"},
    {"name": "Tractor Mounted Sprayer", "price": 1000, "unit": "per day"},
    {"name": "Multi-crop Planter Rental", "price": 1200, "unit": "per day"},
    {"name": "Night Shift Surcharge", "price": 500, "unit": "per night"}
]

def run():
    try:
        subcat = SubCategory.objects.get(id=45)
        num_providers = random.randint(15, 28)
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
                price="₹600 onwards",
                description=f"Authorized tractor and farm machinery rental service in {city}. Providing a wide range of tractors from 20HP to 75HP with all required attachments.",
                phone=f"98765445{i:02d}",
                verified=True,
                rating=random.uniform(4.0, 4.9),
                reviews=random.randint(10, 180)
            )

            num_services = random.randint(4, 12)
            selected_services = random.sample(master_services, num_services)

            for s in selected_services:
                Service.objects.create(provider=provider, **s)

        print(f"Successfully inserted {num_providers} Tractor Rental providers with 4-12 services each!")
    except Exception as e:
        print(f"Error during run: {e}")

if __name__ == '__main__':
    run()
