import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Subcategory ID for Drone Spraying is 5
SUBCAT_ID = 5

# Clear existing providers if any (to avoid duplicates)
Provider.objects.filter(subcategory_id=SUBCAT_ID).delete()

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

names_prefixes = ["SkyAgri", "AeroFarm", "DroneForce", "PrecisionAir", "AgriFly", "CloudCrop", "WingAgro", "SkySpray", "HighReach", "FalconAgri"]
names_suffixes = ["Drone Services", "Aviation Hub", "Spray Solutions", "Tech Sprayers", "Flight Labs", "Precision Spraying", "Agro Drones"]

master_services = [
    {"name": "Pesticide Drone Spray", "price": 600, "unit": "per acre"},
    {"name": "Liquid Fertilizer Spray", "price": 700, "unit": "per acre"},
    {"name": "Micronutrient Foliar Spray", "price": 800, "unit": "per acre"},
    {"name": "Fungicide Targeted Spray", "price": 750, "unit": "per acre"},
    {"name": "Herbicide Precision Spray", "price": 650, "unit": "per acre"},
    {"name": "Crop Health Multi-spectral Imaging", "price": 1200, "unit": "per acre"},
    {"name": "Plant Population Counting", "price": 400, "unit": "per acre"},
    {"name": "Large Area Rapid Spraying", "price": 500, "unit": "per acre (>10 ac)"},
    {"name": "Orchard Specialized Spraying", "price": 1500, "unit": "per hour"},
    {"name": "Locust Swarm Control", "price": 2000, "unit": "per hour"},
    {"name": "Night Vision Spraying", "price": 1000, "unit": "per acre"},
    {"name": "Seed Sowing by Drone", "price": 1800, "unit": "per acre"},
    {"name": "Drone Pilot with DGCA License", "price": 1500, "unit": "per day"},
    {"name": "Battery Charging Support", "price": 300, "unit": "per cycle"},
    {"name": "Water Logged Area Spraying", "price": 900, "unit": "per acre"}
]

def run():
    try:
        subcat = SubCategory.objects.get(id=SUBCAT_ID)
        num_providers = random.randint(12, 28)
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
                price="₹400 onwards",
                description=f"DGCA certified drone spraying service in {city}. We use high-end agricultural drones for precise pesticide and fertilizer application, reducing wastage and increasing efficiency.",
                phone=f"98765405{i:02d}",
                verified=True,
                rating=random.uniform(4.5, 5.0),
                reviews=random.randint(15, 200)
            )

            num_services = random.randint(4, 12)
            selected_services = random.sample(master_services, num_services)

            for s in selected_services:
                Service.objects.create(provider=provider, **s)

        print(f"Successfully inserted {num_providers} Drone Spraying providers with 4-12 services each!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
