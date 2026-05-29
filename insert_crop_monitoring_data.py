import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Clear existing if any
Provider.objects.filter(subcategory_id=12).delete()

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

names_prefixes = ["Smart", "Agri", "Precision", "Tech", "Green", "Crop", "Field", "Vision", "Future", "Digital"]
names_suffixes = ["Monitoring Solutions", "Agro Insights", "Crop Health Center", "Analytics Hub", "Observation Point", "Surveillance", "Eye", "Watch"]

master_services = [
    {"name": "Satellite Crop Health Map", "price": 499, "unit": "per acre/month"},
    {"name": "Drone Multi-spectral Scan", "price": 1200, "unit": "per acre"},
    {"name": "Soil Moisture Sensor Setup", "price": 3500, "unit": "per unit"},
    {"name": "Real-time Weather Alert", "price": 100, "unit": "per month"},
    {"name": "Early Pest Detection Scan", "price": 800, "unit": "per visit"},
    {"name": "Yield Prediction Report", "price": 1500, "unit": "per crop"},
    {"name": "NDVI Vegetation Index", "price": 300, "unit": "per acre"},
    {"name": "IoT Agri Station Install", "price": 15000, "unit": "per install"},
    {"name": "Plant Stress Analysis", "price": 600, "unit": "per acre"},
    {"name": "Growth Stage Tracking", "price": 400, "unit": "per month"},
    {"name": "Nutrient Deficiency Report", "price": 550, "unit": "per visit"},
    {"name": "Water Management Plan", "price": 1000, "unit": "per plan"},
    {"name": "Disease Spreading Forecast", "price": 200, "unit": "per alert"},
    {"name": "Mobile App Dashboard Access", "price": 0, "unit": "per user"},
    {"name": "Consultancy with Agronomist", "price": 1200, "unit": "per hour"}
]

def run():
    try:
        subcat = SubCategory.objects.get(id=12)
        num_providers = random.randint(10, 28)
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
                price="₹100 onwards",
                description=f"High-tech crop monitoring and precision agriculture service in {city}. Using satellite imagery and IoT sensors to maximize your harvest yield.",
                phone=f"98765412{i:02d}",
                verified=True,
                rating=random.uniform(4.3, 5.0),
                reviews=random.randint(5, 150)
            )

            num_services = random.randint(5, 12)
            selected_services = random.sample(master_services, num_services)

            for s in selected_services:
                Service.objects.create(provider=provider, **s)

        print(f"Successfully inserted {num_providers} Crop Monitoring providers with 5-12 services each!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
