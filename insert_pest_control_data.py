import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Clear existing if any
Provider.objects.filter(subcategory_id=10).delete()

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

names_prefixes = ["Suraksha", "SafeGuard", "BioShield", "Kisan Raksha", "AgriGuard", "ZeroPest", "CropShield", "Modern", "Rural", "ProCare"]
names_suffixes = ["Pest Control", "Plant Protection", "Agro Services", "Pest Management", "Crop Safety", "Bio-Control", "Sanitization"]

master_services = [
    {"name": "General Pesticide Spray", "price": 800, "unit": "per acre"},
    {"name": "Termite Soil Treatment", "price": 2500, "unit": "per visit"},
    {"name": "Rodent Control Drive", "price": 1200, "unit": "per week"},
    {"name": "Fungal Infection Control", "price": 950, "unit": "per acre"},
    {"name": "Organic Pest Analysis", "price": 500, "unit": "per report"},
    {"name": "Locust Swarm Protection", "price": 1500, "unit": "per acre"},
    {"name": "Fruit Fly Traps (5pcs)", "price": 350, "unit": "pack"},
    {"name": "Neem Oil Spraying", "price": 600, "unit": "per acre"},
    {"name": "Pheromone Trap Setup", "price": 1200, "unit": "per visit"},
    {"name": "Larvae Control (Aqua)", "price": 1800, "unit": "per pond"},
    {"name": "Weed Management", "price": 700, "unit": "per acre"},
    {"name": "Bio-Insecticide Application", "price": 1100, "unit": "per acre"},
    {"name": "Stored Grain Fumigation", "price": 2000, "unit": "per godown"},
    {"name": "Anti-Viral Crop Spray", "price": 1300, "unit": "per acre"},
    {"name": "Soil Sterilization", "price": 3000, "unit": "per plot"}
]

def run():
    try:
        subcat = SubCategory.objects.get(id=10)
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
                price="₹350 onwards",
                description=f"Authorized crop protection and pest management experts in {city}. Specialized in both chemical and organic pest control methods.",
                phone=f"98765439{i:02d}",
                verified=True,
                rating=random.uniform(4.0, 5.0),
                reviews=random.randint(5, 120)
            )

            # Select 4 to 12 services
            num_services = random.randint(4, 12)
            selected_services = random.sample(master_services, num_services)

            for s in selected_services:
                Service.objects.create(provider=provider, **s)

        print("Successfully inserted 28 Pest Control providers with 4-12 services each!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
