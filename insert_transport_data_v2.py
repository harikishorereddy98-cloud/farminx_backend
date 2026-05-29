import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

# Delete existing transport providers to avoid duplicates with better data
Provider.objects.filter(subcategory_id=8).delete()

data = [
    {
        "name": "Andhra Agri Transport",
        "location": "Vijayawada, AP",
        "latitude": 16.5062, "longitude": 80.6480,
        "price": "₹499 onwards",
        "about": "Reliable transport for farm produce, fertilizers, and seeds across the Krishna district.",
        "phone": "9876543701",
        "services": [
            {"name": "Mini Truck Rental", "price": 1200, "unit": "per day"},
            {"name": "Crop Transport", "price": 15, "unit": "per km"},
            {"name": "Fertilizer Delivery", "price": 499, "unit": "per trip"},
            {"name": "Loading/Unloading", "price": 500, "unit": "per ton"},
            {"name": "Storage Transit", "price": 200, "unit": "per day"}
        ]
    },
    {
        "name": "Delta Crop Carriers",
        "location": "Guntur, AP",
        "latitude": 16.3067, "longitude": 80.4365,
        "price": "₹599 onwards",
        "about": "Specialized in bulk grain and chili transport from farms to markets with heavy-duty trucks.",
        "phone": "9876543702",
        "services": [
            {"name": "Heavy Truck (10ton)", "price": 4500, "unit": "per day"},
            {"name": "Market Delivery", "price": 999, "unit": "per trip"},
            {"name": "Loading Support", "price": 300, "unit": "per labor"},
            {"name": "Long distance haul", "price": 25, "unit": "per km"},
            {"name": "Secure tarp covering", "price": 150, "unit": "per trip"}
        ]
    },
    {
        "name": "Village Logistics Hub",
        "location": "Nellore, AP",
        "latitude": 14.4426, "longitude": 79.9865,
        "price": "₹399 onwards",
        "about": "Connecting small farmers to local distribution centers with efficient small-vehicle logistics.",
        "phone": "9876543703",
        "services": [
            {"name": "Auto Trolley Rental", "price": 600, "unit": "per day"},
            {"name": "Local Distribution", "price": 399, "unit": "per trip"},
            {"name": "Doorstep Pickup", "price": 100, "unit": "per visit"},
            {"name": "Bags weighing service", "price": 50, "unit": "per 10 bags"},
            {"name": "Packaging support", "price": 200, "unit": "per trip"}
        ]
    },
    {
        "name": "Rayalaseema Agri Transports",
        "location": "Kurnool, AP",
        "latitude": 15.8281, "longitude": 78.0373,
        "price": "₹699 onwards",
        "about": "Fast and safe transport for groundnuts and other local crops across Rayalaseema.",
        "phone": "9876543704",
        "services": [
            {"name": "Truck Transport", "price": 20, "unit": "per km"},
            {"name": "Warehouse Shifting", "price": 1500, "unit": "per trip"},
            {"name": "Night transit extra", "price": 500, "unit": "per trip"},
            {"name": "Groundnut bagging", "price": 5, "unit": "per bag"},
            {"name": "Medium pickup (4ton)", "price": 2200, "unit": "per day"}
        ]
    },
    {
        "name": "Godavari Farm Express",
        "location": "Rajahmundry, AP",
        "latitude": 17.0005, "longitude": 81.8040,
        "price": "₹550 onwards",
        "about": "Swift delivery for perishable fruits and vegetables using temperature-controlled mini-vans.",
        "phone": "9876543705",
        "services": [
            {"name": "Perishable Goods Van", "price": 1800, "unit": "per day"},
            {"name": "Express Delivery", "price": 799, "unit": "per trip"},
            {"name": "Crate rental", "price": 10, "unit": "per crate"},
            {"name": "Pre-cooling loading", "price": 300, "unit": "per hour"},
            {"name": "Market Price info", "price": 0, "unit": "Free"}
        ]
    },
    {
        "name": "Kadapa Farm Movers",
        "location": "Kadapa, AP",
        "latitude": 14.4673, "longitude": 78.8242,
        "price": "₹450 onwards",
        "about": "Providing tractor trolleys and trailers for local farm movements and heavy equipment shifting.",
        "phone": "9876543706",
        "services": [
            {"name": "Tractor Trolley", "price": 800, "unit": "per day"},
            {"name": "Heavy Shifting", "price": 2500, "unit": "per trip"},
            {"name": "Water tanker service", "price": 600, "unit": "per trip"},
            {"name": "Trailer attachment", "price": 200, "unit": "per day"},
            {"name": "Driver only service", "price": 500, "unit": "per day"}
        ]
    },
    {
        "name": "Coastal Agri Logistics",
        "location": "Kakinada, AP",
        "latitude": 16.9891, "longitude": 82.2475,
        "price": "₹750 onwards",
        "about": "Efficient transport of rice and fertilizers to and from port areas.",
        "phone": "9876543707",
        "services": [
            {"name": "Port Logistics", "price": 3000, "unit": "per trip"},
            {"name": "Container Truck", "price": 5500, "unit": "per day"},
            {"name": "Customs clearance help", "price": 1000, "unit": "per order"},
            {"name": "Bulk weighing", "price": 200, "unit": "per truck"},
            {"name": "Labor team (5 men)", "price": 2000, "unit": "per day"}
        ]
    },
    {
        "name": "Temple City Agri Carriers",
        "location": "Tirupati, AP",
        "latitude": 13.6288, "longitude": 79.4192,
        "price": "₹480 onwards",
        "about": "Local transport for flowers, milk, and seasonal crops in the Chittoor region.",
        "phone": "9876543708",
        "services": [
            {"name": "Milk Tanker", "price": 2500, "unit": "per trip"},
            {"name": "Small Pickup", "price": 480, "unit": "per trip"},
            {"name": "Flower box transit", "price": 300, "unit": "per trip"},
            {"name": "Irrigation pipe shift", "price": 400, "unit": "per trip"},
            {"name": "Village to Market", "price": 12, "unit": "per km"}
        ]
    },
    {
        "name": "Anantapur Harvest Haulers",
        "location": "Anantapur, AP",
        "latitude": 14.6819, "longitude": 77.6006,
        "price": "₹600 onwards",
        "about": "Handling large-scale crop harvest transport with modern fleet.",
        "phone": "9876543709",
        "services": [
            {"name": "Harvest Transport", "price": 18, "unit": "per km"},
            {"name": "Loading Labor", "price": 250, "unit": "per person"},
            {"name": "Farm cleanup", "price": 1000, "unit": "per acre"},
            {"name": "Night watch security", "price": 400, "unit": "per night"},
            {"name": "Empty bags supply", "price": 15, "unit": "per bag"}
        ]
    },
    {
        "name": "Vizianagaram Agri Link",
        "location": "Vizianagaram, AP",
        "latitude": 18.1067, "longitude": 83.3955,
        "price": "₹400 onwards",
        "about": "Reliable links between tribal farms and main town markets.",
        "phone": "9876543710",
        "services": [
            {"name": "Hill Area Pickup", "price": 900, "unit": "per trip"},
            {"name": "Regular Market Route", "price": 400, "unit": "per trip"},
            {"name": "Small produce pooling", "price": 100, "unit": "per farmer"},
            {"name": "Organic certification help", "price": 500, "unit": "per visit"},
            {"name": "Market return delivery", "price": 200, "unit": "per trip"}
        ]
    },
    {
        "name": "Eluru Farm Transit",
        "location": "Eluru, AP",
        "latitude": 16.7107, "longitude": 81.1035,
        "price": "₹520 onwards",
        "about": "Water-based and road-based transport solutions for coastal farms.",
        "phone": "9876543711",
        "services": [
            {"name": "Canal Boat Transport", "price": 2000, "unit": "per day"},
            {"name": "Mini Truck", "price": 1100, "unit": "per day"},
            {"name": "Paddy pooling", "price": 50, "unit": "per quintal"},
            {"name": "GPS tracking access", "price": 100, "unit": "per trip"},
            {"name": "Waterfront loading", "price": 300, "unit": "per hour"}
        ]
    },
    {
        "name": "Ongole Bull Transporters",
        "location": "Ongole, AP",
        "latitude": 15.5057, "longitude": 80.0499,
        "price": "₹850 onwards",
        "about": "Safe livestock and fodder transport with specialized vehicles.",
        "phone": "9876543712",
        "services": [
            {"name": "Livestock Carrier", "price": 3500, "unit": "per trip"},
            {"name": "Fodder Truck", "price": 1200, "unit": "per trip"},
            {"name": "Vet on call during transit", "price": 1000, "unit": "per trip"},
            {"name": "Animal loading ramp", "price": 200, "unit": "per animal"},
            {"name": "Feed supply delivery", "price": 500, "unit": "per trip"}
        ]
    },
    {
        "name": "Nandyal Seeds Logistics",
        "location": "Nandyal, AP",
        "latitude": 15.4779, "longitude": 78.4831,
        "price": "₹440 onwards",
        "about": "Fast and dry transport for seeds and pulses processing units.",
        "phone": "9876543713",
        "services": [
            {"name": "Dry Goods Van", "price": 1300, "unit": "per day"},
            {"name": "Small Batch Delivery", "price": 440, "unit": "per trip"},
            {"name": "Seed moisture check", "price": 100, "unit": "per batch"},
            {"name": "Labels and tagging", "price": 2, "unit": "per bag"},
            {"name": "Pallet rental", "price": 50, "unit": "per day"}
        ]
    },
    {
        "name": "Machilipatnam Agri Freight",
        "location": "Machilipatnam, AP",
        "latitude": 16.1875, "longitude": 81.1389,
        "price": "₹670 onwards",
        "about": "Bulk freight services for paddy and aquaculture products.",
        "phone": "9876543714",
        "services": [
            {"name": "Paddy Transport", "price": 16, "unit": "per km"},
            {"name": "Aquaculture Pickup", "price": 1500, "unit": "per trip"},
            {"name": "Ice box delivery", "price": 500, "unit": "per day"},
            {"name": "Weight verification", "price": 150, "unit": "per trip"},
            {"name": "Bulk discount (50ton+)", "price": 0, "unit": "Custom"}
        ]
    }
]

def run():
    try:
        subcat = SubCategory.objects.get(id=8)
        count = 0
        for p_data in data:
            services_data = p_data.pop('services')
            about = p_data.pop('about')

            provider = Provider.objects.create(
                subcategory=subcat,
                description=about,
                verified=True,
                rating=4.5,
                reviews=25,
                **p_data
            )

            for s in services_data:
                Service.objects.create(provider=provider, **s)
            count += 1

        print(f"Successfully re-inserted {count} Transport providers with 5 services each!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
