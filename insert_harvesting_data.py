import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Clear existing if any
Provider.objects.filter(subcategory_id=11).delete()

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

names_prefixes = ["Golden Crop", "Rythu Mitra", "Super Harvest", "Mega Farm", "AgroTech", "Swift Cut", "Precision", "Annapurna", "Kisan Sahay", "FieldReady"]
names_suffixes = ["Harvesting Hub", "Farm Services", "Machinery Group", "Operators", "Harvest Solutions", "Field Services", "Crop Cutters"]

master_services = [
    {"name": "Combine Harvester (Rice)", "price": 2500, "unit": "per hour"},
    {"name": "Manual Labor (Harvesting)", "price": 400, "unit": "per person"},
    {"name": "Threshing Service", "price": 1200, "unit": "per acre"},
    {"name": "Maize Shelling Machine", "price": 800, "unit": "per quintal"},
    {"name": "Groundnut Digging Machine", "price": 1500, "unit": "per acre"},
    {"name": "Sorting & Grading", "price": 150, "unit": "per quintal"},
    {"name": "Bagging & Stitching", "price": 10, "unit": "per bag"},
    {"name": "Straw Bailing Machine", "price": 1100, "unit": "per hour"},
    {"name": "Sugarcane Cutting Team", "price": 600, "unit": "per ton"},
    {"name": "Chili Picking Labor", "price": 20, "unit": "per kg"},
    {"name": "Winnowing (Cleaning)", "price": 100, "unit": "per quintal"},
    {"name": "Harvest Transport (Field to Gate)", "price": 500, "unit": "per trip"},
    {"name": "Cotton Picking Service", "price": 12, "unit": "per kg"},
    {"name": "Paddy Reaping Machine", "price": 1800, "unit": "per acre"},
    {"name": "Post-Harvest Moisture Check", "price": 0, "unit": "Free"}
]

def run():
    try:
        subcat = SubCategory.objects.get(id=11)
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
                price="₹150 onwards",
                description=f"Professional harvesting and post-harvest management experts in {city}. Equipped with modern combine harvesters and experienced labor teams.",
                phone=f"98765440{i:02d}",
                verified=True,
                rating=random.uniform(4.2, 5.0),
                reviews=random.randint(20, 200)
            )

            # Select 4 to 12 services
            num_services = random.randint(4, 12)
            selected_services = random.sample(master_services, num_services)

            for s in selected_services:
                Service.objects.create(provider=provider, **s)

        print("Successfully inserted 28 Harvesting providers with 4-12 services each!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
