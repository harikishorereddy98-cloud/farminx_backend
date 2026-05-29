import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Mapping of SubCategory IDs to Service Template Pools
subcategories_config = {
    18: { # Soil Preparation
        "prefix": ["RichSoil", "EarthMover", "NatureDig", "SoilExpert", "NutriGround"],
        "master_services": [
            {"name": "Manual Digging & Loosening", "price": 400, "unit": "per 100 sq ft"},
            {"name": "Organic Manure Mixing", "price": 250, "unit": "per plot"},
            {"name": "Soil pH Level Test", "price": 150, "unit": "per sample"},
            {"name": "Leveling & Grading", "price": 500, "unit": "per plot"},
            {"name": "Cocopeat Mixing", "price": 300, "unit": "per bag"},
            {"name": "Tiller Cultivation", "price": 800, "unit": "per hour"},
            {"name": "Raised Bed Creation", "price": 1200, "unit": "per unit"},
            {"name": "Weed Removal (Pre-Prep)", "price": 300, "unit": "per hour"}
        ]
    },
    19: { # Planting
        "prefix": ["GreenThumb", "NatureBloom", "PlantMaster", "FloralCare", "TreeMate"],
        "master_services": [
            {"name": "Avenue Tree Plantation", "price": 100, "unit": "per sapling"},
            {"name": "Flower Bed Planting", "price": 300, "unit": "per 50 sq ft"},
            {"name": "Vegetable Patch Setup", "price": 1500, "unit": "per plot"},
            {"name": "Potting & Repotting", "price": 50, "unit": "per pot"},
            {"name": "Lawn Grass Sodding", "price": 45, "unit": "per sq ft"},
            {"name": "Kitchen Garden Planning", "price": 1000, "unit": "per visit"},
            {"name": "Seedling Sowing", "price": 5, "unit": "per seedling"},
            {"name": "Climber Support Setup", "price": 400, "unit": "per unit"}
        ]
    },
    20: { # Pest Control (Gardening)
        "prefix": ["EcoShield", "PestAway", "SafeGreen", "BioGuard", "NatureRescue"],
        "master_services": [
            {"name": "Mealy Bug Treatment", "price": 450, "unit": "per visit"},
            {"name": "Aphid Control Spray", "price": 350, "unit": "per session"},
            {"name": "Anti-Termite Treatment", "price": 1200, "unit": "per garden"},
            {"name": "Organic Neem Oil Spray", "price": 250, "unit": "per visit"},
            {"name": "Ant Hill Removal", "price": 300, "unit": "per unit"},
            {"name": "Fungicide Application", "price": 400, "unit": "per visit"},
            {"name": "Fruit Fly Trap Setup", "price": 150, "unit": "per trap"},
            {"name": "Herbal Pest Repellent", "price": 600, "unit": "per plot"}
        ]
    },
    21: { # Watering
        "prefix": ["HydroFlow", "AquaLife", "WaterWise", "DropCare", "RainMaker"],
        "master_services": [
            {"name": "Drip Irrigation Install", "price": 5000, "unit": "per setup"},
            {"name": "Manual Watering Service", "price": 200, "unit": "per hour"},
            {"name": "Sprinkler System Repair", "price": 600, "unit": "per visit"},
            {"name": "Automatic Timer Setup", "price": 1500, "unit": "per point"},
            {"name": "Water Tank Cleaning", "price": 800, "unit": "per tank"},
            {"name": "Hydroponic Reservoir Check", "price": 1000, "unit": "per visit"},
            {"name": "Moisture Sensor Install", "price": 2500, "unit": "per unit"},
            {"name": "Mist System Setup", "price": 3500, "unit": "per unit"}
        ]
    },
    22: { # Cleaning
        "prefix": ["PureGarden", "CleanGreen", "NatureShine", "GardenFresh", "NeatPlot"],
        "master_services": [
            {"name": "Dry Leaf Removal", "price": 300, "unit": "per hour"},
            {"name": "Pathway Pressure Wash", "price": 800, "unit": "per 500 sq ft"},
            {"name": "Garden Debris Clearing", "price": 500, "unit": "per trip"},
            {"name": "Algae Removal", "price": 450, "unit": "per hour"},
            {"name": "Gutter Cleaning", "price": 600, "unit": "per visit"},
            {"name": "Dead Plant Removal", "price": 100, "unit": "per plant"},
            {"name": "Stone Dust Cleaning", "price": 400, "unit": "per visit"},
            {"name": "Lawn Moss Removal", "price": 700, "unit": "per plot"}
        ]
    },
    23: { # Pruning
        "prefix": ["SharpCut", "TreeTrim", "PrecisionLoop", "BranchMaster", "GreenShape"],
        "master_services": [
            {"name": "Hedge Trimming", "price": 500, "unit": "per 20 ft"},
            {"name": "Fruit Tree Pruning", "price": 250, "unit": "per tree"},
            {"name": "Bonsai Shaping", "price": 1500, "unit": "per hour"},
            {"name": "Deadwood Removal", "price": 400, "unit": "per visit"},
            {"name": "Rose Bush Pruning", "price": 50, "unit": "per plant"},
            {"name": "Topiary Art (Shapes)", "price": 2000, "unit": "per plant"},
            {"name": "Thinning Out Service", "price": 600, "unit": "per plot"},
            {"name": "Tool Sharpening", "price": 100, "unit": "per tool"}
        ]
    },
    24: { # Garden Design
        "prefix": ["EdenDraw", "VividLand", "StyleGreen", "ArchAgro", "PlatPixel"],
        "master_services": [
            {"name": "Balcony Garden Layout", "price": 2500, "unit": "per design"},
            {"name": "Vertical Garden Blueprint", "price": 3500, "unit": "per unit"},
            {"name": "Terrace Garden Planning", "price": 5000, "unit": "per design"},
            {"name": "3D Garden Visual", "price": 1500, "unit": "per view"},
            {"name": "Plant Selection Consultancy", "price": 800, "unit": "per hour"},
            {"name": "Rock Garden Theme", "price": 4000, "unit": "per project"},
            {"name": "Japanese Zen Theme", "price": 6000, "unit": "per project"},
            {"name": "Lighting Path Design", "price": 2000, "unit": "per design"}
        ]
    },
    25: { # Lighting Setup
        "prefix": ["GlowAgro", "LuminaFarm", "NightBloom", "BeamGreen", "SparkGate"],
        "master_services": [
            {"name": "Solar Path Lights", "price": 1500, "unit": "per 5 units"},
            {"name": "Tree Up-lighting", "price": 800, "unit": "per tree"},
            {"name": "Garden String Lights", "price": 600, "unit": "per 20 ft"},
            {"name": "Flood Light Install", "price": 1200, "unit": "per point"},
            {"name": "Motion Sensor Lights", "price": 1800, "unit": "per unit"},
            {"name": "RGB Smart Light Setup", "price": 5000, "unit": "per project"},
            {"name": "Underwater Pond Lights", "price": 2500, "unit": "per unit"},
            {"name": "Fairy Light Decoration", "price": 500, "unit": "per hour"}
        ]
    },
    26: { # Pesticides (Gardening)
        "prefix": ["EcoSpray", "NatureKill", "BugStop", "SafeLeaf", "PureAgro"],
        "master_services": [
            {"name": "Bio-Pesticide Kit", "price": 800, "unit": "per kit"},
            {"name": "Sticky Trap Rolls", "price": 350, "unit": "per 10m"},
            {"name": "Organic Fungicide", "price": 400, "unit": "per 500ml"},
            {"name": "Rose Health Spray", "price": 150, "unit": "per visit"},
            {"name": "Ant Powder Application", "price": 200, "unit": "per plot"},
            {"name": "Snail/Slug Bait", "price": 450, "unit": "per pack"},
            {"name": "Rat Repellent Cubes", "price": 300, "unit": "per pack"},
            {"name": "Consultancy on Chemical", "price": 500, "unit": "per visit"}
        ]
    },
    27: { # Greenhouse Setup
        "prefix": ["GlassDome", "GreenShelter", "ShieldGrow", "ClimateBox", "PolyExpert"],
        "master_services": [
            {"name": "Mini Polyhouse (10x10)", "price": 15000, "unit": "per unit"},
            {"name": "Shade Net Install", "price": 35, "unit": "per sq ft"},
            {"name": "Mist Chamber Setup", "price": 8000, "unit": "per setup"},
            {"name": "Fan & Pad Repair", "price": 2500, "unit": "per visit"},
            {"name": "Greenhouse Frame Welding", "price": 1200, "unit": "per hour"},
            {"name": "UV Stabilized Film", "price": 60, "unit": "per sq m"},
            {"name": "Thermostat Install", "price": 3000, "unit": "per unit"},
            {"name": "Hydroponic Tower Setup", "price": 12000, "unit": "per unit"}
        ]
    },
    28: { # Composting
        "prefix": ["EcoRot", "BlackGold", "EarthLoop", "WormHub", "FertileBin"],
        "master_services": [
            {"name": "Home Compost Bin Setup", "price": 2500, "unit": "per bin"},
            {"name": "Vermicompost Bed Setup", "price": 4500, "unit": "per 4x4 ft"},
            {"name": "Bokashi Method Kit", "price": 1800, "unit": "per kit"},
            {"name": "Compost Quality Check", "price": 300, "unit": "per sample"},
            {"name": "Worm Tea Liquid (5L)", "price": 600, "unit": "per can"},
            {"name": "Organic Waste Pickup", "price": 500, "unit": "per month"},
            {"name": "Earthworm Supply (1kg)", "price": 800, "unit": "per kg"},
            {"name": "Compost Aeration Visit", "price": 400, "unit": "per visit"}
        ]
    },
    29: { # Gardening Workshop
        "prefix": ["SkillGreen", "LearnGrow", "BotanyHub", "NatureClass", "PlantWise"],
        "master_services": [
            {"name": "Beginner Urban Garden", "price": 500, "unit": "per session"},
            {"name": "Succulent Care Masterclass", "price": 1200, "unit": "per person"},
            {"name": "Terrarium Building Lab", "price": 2500, "unit": "per person"},
            {"name": "Kitchen Waste to Compost", "price": 300, "unit": "per session"},
            {"name": "Kids Gardening Camp", "price": 3000, "unit": "per week"},
            {"name": "Hydroponics Deep Dive", "price": 5000, "unit": "per weekend"},
            {"name": "Garden Photography Course", "price": 1500, "unit": "per day"},
            {"name": "Indoor Plant Styling", "price": 1000, "unit": "per hour"}
        ]
    },
    30: { # Tool Rental
        "prefix": ["AgroTools", "HireGreen", "ToolMate", "RentGear", "ShaftTools"],
        "master_services": [
            {"name": "Lawn Mower (Electric)", "price": 800, "unit": "per day"},
            {"name": "Chainsaw (Petrol)", "price": 1200, "unit": "per day"},
            {"name": "Leaf Blower Rental", "price": 500, "unit": "per day"},
            {"name": "Hedge Trimmer", "price": 600, "unit": "per day"},
            {"name": "Garden Tiller (Mini)", "price": 1000, "unit": "per day"},
            {"name": "Pressure Washer", "price": 700, "unit": "per day"},
            {"name": "Pruning Saw & Ladder", "price": 300, "unit": "per day"},
            {"name": "Auger Bit (Post Hole)", "price": 1100, "unit": "per day"}
        ]
    },
    31: { # Plant Protection
        "prefix": ["SafeLeaf", "GuardGreen", "NatureShield", "PlantRescue", "BioSafe"],
        "master_services": [
            {"name": "Bird Netting (Large)", "price": 1500, "unit": "per unit"},
            {"name": "Frost Protection Cover", "price": 400, "unit": "per acre"},
            {"name": "Shade Net (50%) Install", "price": 40, "unit": "per sq ft"},
            {"name": "Tree Trunk Painting", "price": 100, "unit": "per tree"},
            {"name": "Fence Wire Mesh", "price": 50, "unit": "per ft"},
            {"name": "Heat Wave Protection", "price": 1000, "unit": "per visit"},
            {"name": "Monkey Scaring Tape", "price": 200, "unit": "per roll"},
            {"name": "Heavy Rain Shelter", "price": 3000, "unit": "per project"}
        ]
    },
    32: { # Plant Health Checkup
        "prefix": ["PlantDoc", "MedGreen", "HealthLeaf", "NatureClinic", "VitalAgro"],
        "master_services": [
            {"name": "General Health Audit", "price": 600, "unit": "per visit"},
            {"name": "Leaf Tissue Analysis", "price": 1500, "unit": "per plant"},
            {"name": "Root Rot Diagnostic", "price": 800, "unit": "per plot"},
            {"name": "Nutrient Deficiency Map", "price": 1200, "unit": "per report"},
            {"name": "Water Log Stress Test", "price": 500, "unit": "per session"},
            {"name": "Microscope Pest Check", "price": 1000, "unit": "per hour"},
            {"name": "Plant Vitality Index", "price": 400, "unit": "per report"},
            {"name": "Expert Advice Session", "price": 1200, "unit": "per hour"}
        ]
    },
    46: { # Seeds & Plants
        "prefix": ["NatureSeed", "RichGreen", "NurseryPoint", "SeedsGalore", "BloomStock"],
        "master_services": [
            {"name": "Hybrid Vegetable Seeds", "price": 40, "unit": "per packet"},
            {"name": "Exotic Flower Seeds", "price": 120, "unit": "per packet"},
            {"name": "Organic Heirloom Pack", "price": 500, "unit": "per kit"},
            {"name": "Fruit Tree Sapling", "price": 350, "unit": "per unit"},
            {"name": "Bonsai Starter Kit", "price": 2500, "unit": "per kit"},
            {"name": "Succulent Assortment", "price": 800, "unit": "per 5 units"},
            {"name": "Medicinal Herb Seeds", "price": 60, "unit": "per packet"},
            {"name": "Potted Decorative Plants", "price": 1200, "unit": "per unit"}
        ]
    }
}

cities_pool = [
    ("Vijayawada", 16.5062, 80.6480), ("Guntur", 16.3067, 80.4365),
    ("Nellore", 14.4426, 79.9865), ("Kurnool", 15.8281, 78.0373),
    ("Rajahmundry", 17.0005, 81.8040), ("Kakinada", 16.9891, 82.2475),
    ("Tirupati", 13.6288, 79.4192), ("Anantapur", 14.6819, 77.6006),
    ("Vizianagaram", 18.1067, 83.3955), ("Eluru", 16.7107, 81.1035),
    ("Ongole", 15.5057, 80.0499), ("Nandyal", 15.4779, 78.4831),
    ("Amaravati", 16.5131, 80.5165), ("Kadapa", 14.4673, 78.8242),
    ("Chittoor", 13.2172, 79.1003), ("Tenali", 16.2390, 80.6458)
]

def run():
    total_providers = 0
    total_services = 0
    try:
        for sub_id, config in subcategories_config.items():
            # Random count between 8 and 20 for gardening subcats to keep it manageable but rich
            num_providers = random.randint(8, 20)
            selected_cities = random.sample(cities_pool, min(num_providers, len(cities_pool)))

            subcat = SubCategory.objects.get(id=sub_id)
            # Clean existing for these gardening subcats
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
                    description=f"Professional {subcat.name.lower()} services in {city}. Expert care for home gardens, terrace units, and urban green spaces.",
                    phone=f"99887766{sub_id:02d}{i:02d}"[:10],
                    verified=True,
                    rating=random.uniform(4.0, 5.0),
                    reviews=random.randint(5, 120)
                )
                total_providers += 1

                # 4 to 8 services per gardening provider
                num_s = random.randint(4, 8)
                selected_s = random.sample(config['master_services'], num_s)
                for s in selected_s:
                    Service.objects.create(provider=provider, **s)
                    total_services += 1

        print(f"Successfully inserted {total_providers} Gardening providers and {total_services} services across 16 subcategories!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
