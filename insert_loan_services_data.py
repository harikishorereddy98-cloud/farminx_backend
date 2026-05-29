import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Clear existing if any
Provider.objects.filter(subcategory_id=16).delete()

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

names_prefixes = ["Rythu", "Kisan", "Gramin", "Agro", "Vikas", "Seva", "Maitri", "Bharat", "Jan", "Pragati"]
names_suffixes = ["Finserve", "Financial Hub", "Loan Assist", "Agri Credit", "Finance Point", "Credit Sahay", "Banking Mitra"]

master_services = [
    {"name": "KCC Card Processing", "price": 500, "unit": "per file"},
    {"name": "Agri Gold Loan", "price": 100, "unit": "per lakh"},
    {"name": "New Tractor Loan", "price": 1500, "unit": "per file"},
    {"name": "Poultry Farm Loan", "price": 2000, "unit": "per project"},
    {"name": "Short-term Crop Loan", "price": 300, "unit": "per acre"},
    {"name": "Dairy Unit Finance", "price": 1200, "unit": "per visit"},
    {"name": "Micro-finance for SHG", "price": 0, "unit": "Consultation"},
    {"name": "Warehouse Receipt Loan", "price": 800, "unit": "per receipt"},
    {"name": "Solar Pump Subsidy Loan", "price": 1000, "unit": "per application"},
    {"name": "Land Development Loan", "price": 1500, "unit": "per file"},
    {"name": "Debt Swap Consultation", "price": 500, "unit": "per hour"},
    {"name": "Machinery Purchase Loan", "price": 1100, "unit": "per file"},
    {"name": "Fencing & Border Loan", "price": 600, "unit": "per file"},
    {"name": "Post-Harvest Credit", "price": 400, "unit": "per month"},
    {"name": "Documentation Support", "price": 250, "unit": "per person"}
]

def run():
    try:
        subcat = SubCategory.objects.get(id=16)
        num_providers = random.randint(8, 30) # Using available cities in pool
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
                description=f"Leading agri-finance and loan consultancy in {city}. We assist farmers with KCC, machinery loans, and government subsidies with minimal documentation.",
                phone=f"98765480{i:02d}",
                verified=True,
                rating=random.uniform(4.0, 5.0),
                reviews=random.randint(10, 180)
            )

            num_services = random.randint(4, 12)
            selected_services = random.sample(master_services, num_services)

            for s in selected_services:
                Service.objects.create(provider=provider, **s)

        print(f"Successfully inserted {num_providers} Loan Services providers with 4-12 services each!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
