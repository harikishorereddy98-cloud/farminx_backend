import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Configuration for Animal Husbandry subcategories
husbandry_config = {
    34: { # Dairy Farming
        "prefix": ["Krishna", "Amulya", "Nandi", "MilkyWay", "Dhara"],
        "master_services": [
            {"name": "Milk Quality Analysis", "price": 200, "unit": "per sample"},
            {"name": "Automatic Milking Demo", "price": 500, "unit": "per visit"},
            {"name": "Cattle Shed Hygiene Kit", "price": 1500, "unit": "per kit"},
            {"name": "Crossbreed Consultation", "price": 1000, "unit": "per visit"},
            {"name": "Bulk Milk Cooling Unit", "price": 5000, "unit": "per day (rent)"},
            {"name": "Cattle Identification Tags", "price": 50, "unit": "per tag"}
        ]
    },
    35: { # Poultry Farming
        "prefix": ["EggCellent", "ChickMaster", "BroilerHub", "FeatherCare", "PoultryPro"],
        "master_services": [
            {"name": "Layer Farm Setup Design", "price": 5000, "unit": "per project"},
            {"name": "Chicks Health Check", "price": 800, "unit": "per 100 birds"},
            {"name": "Automated Feeder Repair", "price": 1200, "unit": "per visit"},
            {"name": "Egg Grading Service", "price": 100, "unit": "per 500 eggs"},
            {"name": "Biosecurity Audit", "price": 2000, "unit": "per visit"},
            {"name": "Poultry Waste Management", "price": 1500, "unit": "per visit"}
        ]
    },
    36: { # Fishing & Aquaculture
        "prefix": ["AquaSafe", "FishNet", "PondMaster", "MarineFlow", "BlueHarvest"],
        "master_services": [
            {"name": "Pond Water pH Testing", "price": 300, "unit": "per sample"},
            {"name": "Aerator Maintenance", "price": 1500, "unit": "per unit"},
            {"name": "Fish Seed Supply (Premium)", "price": 2, "unit": "per seed"},
            {"name": "Shrimp Health Diagnostic", "price": 2500, "unit": "per pond"},
            {"name": "Feeding Schedule Plan", "price": 500, "unit": "per month"},
            {"name": "Biofloc Tank Setup", "price": 12000, "unit": "per tank"}
        ]
    },
    37: { # Apiculture & Bee Farming
        "prefix": ["HoneyBee", "NectarHub", "BeeKeeper", "SweetFlow", "RoyalJelly"],
        "master_services": [
            {"name": "Bee Hive Box Setup", "price": 4500, "unit": "per unit"},
            {"name": "Queen Bee Supply", "price": 800, "unit": "per unit"},
            {"name": "Honey Extraction Service", "price": 200, "unit": "per kg"},
            {"name": "Bee Colony Health Check", "price": 600, "unit": "per visit"},
            {"name": "Pollen Collection Kit", "price": 1200, "unit": "per kit"},
            {"name": "Bee Farming Training", "price": 2500, "unit": "per course"}
        ]
    },
    38: { # Goat & Sheep Farming
        "prefix": ["PashuMaitri", "GoatGully", "ShepherdHub", "MeatMaster", "RuralFlock"],
        "master_services": [
            {"name": "Shed Construction Plan", "price": 3000, "unit": "per project"},
            {"name": "Weight Tracking Service", "price": 20, "unit": "per animal"},
            {"name": "Deworming Drive", "price": 40, "unit": "per animal"},
            {"name": "Breeding Cycle Chart", "price": 500, "unit": "per flock"},
            {"name": "Market Price Advisory", "price": 200, "unit": "per month"},
            {"name": "Grazing Land Audit", "price": 1000, "unit": "per visit"}
        ]
    },
    39: { # Goat & Sheep Breeding
        "prefix": ["GenAgro", "BreedStrong", "ElitePashu", "PureLine", "VikasBreed"],
        "master_services": [
            {"name": "Artificial Insemination", "price": 1200, "unit": "per animal"},
            {"name": "Buck/Ram Rental (Pure)", "price": 2000, "unit": "per service"},
            {"name": "Pregnancy Ultrasound", "price": 500, "unit": "per animal"},
            {"name": "Pedigree Verification", "price": 1500, "unit": "per animal"},
            {"name": "Newborn Care Kit", "price": 800, "unit": "per kit"},
            {"name": "Genetic Quality Report", "price": 2500, "unit": "per report"}
        ]
    },
    40: { # Fodder & Feed Supply
        "prefix": ["NutriFeed", "GreenFodder", "KisanFeed", "SuperSilage", "AnnaFeed"],
        "master_services": [
            {"name": "Corn Silage (Bale)", "price": 450, "unit": "per 50kg"},
            {"name": "Dry Straw Supply", "price": 1200, "unit": "per quintal"},
            {"name": "Mineral Block Supply", "price": 350, "unit": "per unit"},
            {"name": "Concentrate Pellets", "price": 1800, "unit": "per 50kg bag"},
            {"name": "Azolla Cultivation Kit", "price": 600, "unit": "per kit"},
            {"name": "TMR Feeding Plan", "price": 400, "unit": "per plan"}
        ]
    },
    41: { # Animal Health & Vaccination
        "prefix": ["VetCare", "AnimalHealth", "PashuDoc", "SafeHerd", "BioVet"],
        "master_services": [
            {"name": "FMD Vaccination", "price": 150, "unit": "per animal"},
            {"name": "General Health Checkup", "price": 500, "unit": "per visit"},
            {"name": "Emergency Vet Call", "price": 1200, "unit": "per call"},
            {"name": "Surgery Consultation", "price": 2000, "unit": "per animal"},
            {"name": "Wound Dressing", "price": 300, "unit": "per session"},
            {"name": "Digital Health Record", "price": 100, "unit": "per year"}
        ]
    },
    42: { # Wool Shearing Services
        "prefix": ["WoolMaster", "SoftClip", "ShearMagic", "FleeceHub", "SilkShear"],
        "master_services": [
            {"name": "Machine Shearing", "price": 80, "unit": "per sheep"},
            {"name": "Manual Shearing", "price": 50, "unit": "per sheep"},
            {"name": "Wool Cleaning (Raw)", "price": 200, "unit": "per 10kg"},
            {"name": "Hoof Trimming", "price": 30, "unit": "per animal"},
            {"name": "Parasite Treatment (Dip)", "price": 40, "unit": "per animal"},
            {"name": "Wool Quality Sorting", "price": 500, "unit": "per quintal"}
        ]
    },
    43: { # Goat & Sheep Transports
        "prefix": ["PashuSwift", "SheepMove", "HerderTransit", "RuralLogistics", "FlockCar"],
        "master_services": [
            {"name": "Small Livestock Carrier", "price": 1500, "unit": "per trip"},
            {"name": "Ventilated Large Truck", "price": 4000, "unit": "per day"},
            {"name": "Animal Loading Labor", "price": 200, "unit": "per trip"},
            {"name": "Safe Transit Bedding", "price": 300, "unit": "per truck"},
            {"name": "Long Distance Transit", "price": 25, "unit": "per km"},
            {"name": "Inter-state Permit help", "price": 1000, "unit": "per batch"}
        ]
    }
}

cities_pool = [
    ("Vijayawada", 16.5062, 80.6480), ("Guntur", 16.3067, 80.4365),
    ("Nellore", 14.4426, 79.9865), ("Kurnool", 15.8281, 78.0373),
    ("Anantapur", 14.6819, 77.6006), ("Ongole", 15.5057, 80.0499),
    ("Nandyal", 15.4779, 78.4831), ("Amaravati", 16.5131, 80.5165),
    ("Kadapa", 14.4673, 78.8242), ("Tirupati", 13.6288, 79.4192),
    ("Chittoor", 13.2172, 79.1003), ("Tenali", 16.2390, 80.6458),
    ("Bhimavaram", 16.5449, 81.5212), ("Srikakulam", 18.2949, 83.8938),
    ("Adoni", 15.6279, 77.2749), ("Kakinada", 16.9891, 82.2475)
]

def run():
    total_providers = 0
    total_services = 0
    try:
        for sub_id, config in husbandry_config.items():
            # Random count between 8 and 15 for animal husbandry
            num_providers = random.randint(8, 15)
            selected_cities = random.sample(cities_pool, min(num_providers, len(cities_pool)))

            subcat = SubCategory.objects.get(id=sub_id)
            # Clear existing data for these subcategories
            Provider.objects.filter(subcategory_id=sub_id).delete()

            for i in range(num_providers):
                city_data = selected_cities[i % len(selected_cities)]
                city, lat, lon = city_data
                p_name = f"{random.choice(config['prefix'])} {subcat.name} {city}"

                provider = Provider.objects.create(
                    subcategory=subcat,
                    name=p_name,
                    location=f"{city}, Andhra Pradesh",
                    latitude=lat,
                    longitude=lon,
                    price=f"₹{config['master_services'][0]['price']} onwards",
                    description=f"Specialized {subcat.name.lower()} center in {city}. Providing expert support for farmers and livestock owners in the region.",
                    phone=f"91223344{sub_id:02d}{i:02d}"[:10],
                    verified=True,
                    rating=random.uniform(4.0, 5.0),
                    reviews=random.randint(10, 150)
                )
                total_providers += 1

                # 4 to 6 services per provider
                num_s = random.randint(4, 6)
                selected_s = random.sample(config['master_services'], num_s)
                for s in selected_s:
                    Service.objects.create(provider=provider, **s)
                    total_services += 1

        print(f"Successfully inserted {total_providers} Animal Husbandry providers and {total_services} services!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
