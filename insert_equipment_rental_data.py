import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Clear existing if any
Provider.objects.filter(subcategory_id=15).delete()

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
    ("Kadapa", 14.4673, 78.8242), ("Tadipatri", 14.9123, 78.0069),
    ("Tanuku", 16.7570, 81.6994), ("Gudivada", 16.4347, 80.9930),
    ("Srikalahasti", 13.7502, 79.7042), ("Narsapuram", 16.4421, 81.6961),
    ("Palakollu", 16.5204, 81.7259), ("Bobbil", 18.5714, 83.3639),
    ("Kavali", 14.9126, 79.9926), ("Tuni", 17.3541, 82.5414),
    ("Ponnur", 16.0664, 80.5540), ("Jaggaiahpet", 16.8925, 80.0988),
    ("Rayachoti", 14.0531, 78.7513), ("Mangalagiri", 16.4402, 80.5588),
    ("Kandukur", 15.2152, 79.9042), ("Samalkot", 17.0511, 82.1648),
    ("Parvathipuram", 18.7770, 83.4283), ("Sattenapalle", 16.3949, 80.1504),
    ("Vinukonda", 16.0560, 79.7347), ("Markapur", 15.7364, 79.2718)
]

names_prefixes = ["Rythu", "Kisan", "Green", "Agro", "Farm", "Modern", "Delta", "Annapurna", "Sri", "Super"]
names_suffixes = ["Equipment Rentals", "Machinery Hub", "Rental Services", "Tools & More", "Agri Rentals", "Machinery Point", "Hire Center"]

master_services = [
    {"name": "Mini Tractor", "price": 1500, "unit": "per day"},
    {"name": "Tractor (50 HP)", "price": 2500, "unit": "per day"},
    {"name": "Rotavator (6 ft)", "price": 1200, "unit": "per day"},
    {"name": "Power Tiller", "price": 1000, "unit": "per day"},
    {"name": "Combine Harvester", "price": 4500, "unit": "per hour"},
    {"name": "Power Sprayer (Backpack)", "price": 300, "unit": "per day"},
    {"name": "Disc Plough", "price": 800, "unit": "per day"},
    {"name": "Seed Drill Machine", "price": 1100, "unit": "per day"},
    {"name": "Brush Cutter", "price": 500, "unit": "per day"},
    {"name": "Laser Land Leveler", "price": 2000, "unit": "per hour"},
    {"name": "Mini Excavator", "price": 4000, "unit": "per day"},
    {"name": "Water Pump (Diesel)", "price": 400, "unit": "per day"},
    {"name": "Mulching Machine", "price": 1300, "unit": "per day"},
    {"name": "Thresher", "price": 1800, "unit": "per day"},
    {"name": "Tractor Trolley", "price": 700, "unit": "per day"}
]

def run():
    try:
        subcat = SubCategory.objects.get(id=15)
        num_providers = random.randint(8, 48)
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
                price="₹300 onwards",
                description=f"Authorized agricultural equipment rental center in {city}. Providing modern machinery and tools to farmers for daily and seasonal requirements.",
                phone=f"98765470{i:02d}",
                verified=True,
                rating=random.uniform(4.0, 5.0),
                reviews=random.randint(10, 250)
            )

            num_services = random.randint(4, 12)
            selected_services = random.sample(master_services, num_services)

            for s in selected_services:
                Service.objects.create(provider=provider, **s)

        print(f"Successfully inserted {num_providers} Equipment Rental providers with 4-12 services each!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
