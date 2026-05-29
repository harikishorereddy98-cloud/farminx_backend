import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

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
            {"name": "Fertilizer Delivery", "price": 499, "unit": "per trip"}
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
            {"name": "Loading Support", "price": 300, "unit": "per labor"}
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
            {"name": "Local Distribution", "price": 399, "unit": "per trip"}
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
            {"name": "Warehouse Shifting", "price": 1500, "unit": "per trip"}
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
            {"name": "Express Delivery", "price": 799, "unit": "per trip"}
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
            {"name": "Heavy Shifting", "price": 2500, "unit": "per trip"}
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
            {"name": "Container Truck", "price": 5500, "unit": "per day"}
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
            {"name": "Small Pickup", "price": 480, "unit": "per trip"}
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
            {"name": "Loading Labor", "price": 250, "unit": "per person"}
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
            {"name": "Regular Market Route", "price": 400, "unit": "per trip"}
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
            {"name": "Mini Truck", "price": 1100, "unit": "per day"}
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
            {"name": "Fodder Truck", "price": 1200, "unit": "per trip"}
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
            {"name": "Small Batch Delivery", "price": 440, "unit": "per trip"}
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
            {"name": "Aquaculture Pickup", "price": 1500, "unit": "per trip"}
        ]
    },
    {
        "name": "Adoni Cotton Carriers",
        "location": "Adoni, AP",
        "latitude": 15.6279, "longitude": 77.2749,
        "price": "₹720 onwards",
        "about": "Specialized in cotton bale transport to mills and markets.",
        "phone": "9876543715",
        "services": [
            {"name": "Bale Transport Truck", "price": 2800, "unit": "per trip"},
            {"name": "Regular Pickup", "price": 720, "unit": "per trip"}
        ]
    },
    {
        "name": "Tenali Farm Connect",
        "location": "Tenali, AP",
        "latitude": 16.2390, "longitude": 80.6458,
        "price": "₹490 onwards",
        "about": "Swift connections for vegetable farmers to regional hubs.",
        "phone": "9876543716",
        "services": [
            {"name": "Daily Market Trip", "price": 490, "unit": "per trip"},
            {"name": "Shared Loading", "price": 200, "unit": "per slot"}
        ]
    },
    {
        "name": "Proddatur Agri Haul",
        "location": "Proddatur, AP",
        "latitude": 14.7502, "longitude": 78.5481,
        "price": "₹530 onwards",
        "about": "General agricultural hauling and equipment moving services.",
        "phone": "9876543717",
        "services": [
            {"name": "Medium Duty Haul", "price": 1500, "unit": "per trip"},
            {"name": "Quick Drop", "price": 530, "unit": "per trip"}
        ]
    },
    {
        "name": "Chittoor Fruit Transit",
        "location": "Chittoor, AP",
        "latitude": 13.2172, "longitude": 79.1003,
        "price": "₹610 onwards",
        "about": "Specialized transit for mangoes and tomatoes in the Chittoor area.",
        "phone": "9876543718",
        "services": [
            {"name": "Fruit Crate Van", "price": 2200, "unit": "per day"},
            {"name": "Market Delivery", "price": 850, "unit": "per trip"}
        ]
    },
    {
        "name": "Hindupur Farm Movers",
        "location": "Hindupur, AP",
        "latitude": 13.8291, "longitude": 77.4914,
        "price": "₹420 onwards",
        "about": "Small scale movers for local farmers and rural households.",
        "phone": "9876543719",
        "services": [
            {"name": "Tricycle Carrier", "price": 300, "unit": "per trip"},
            {"name": "Auto Trolley", "price": 420, "unit": "per trip"}
        ]
    },
    {
        "name": "Bhimavaram Aqua Transport",
        "location": "Bhimavaram, AP",
        "latitude": 16.5449, "longitude": 81.5212,
        "price": "₹950 onwards",
        "about": "Specialized aquaculture and fish feed transport services.",
        "phone": "9876543720",
        "services": [
            {"name": "Fish Feed Supply", "price": 1200, "unit": "per trip"},
            {"name": "Cold Chain Truck", "price": 4500, "unit": "per day"}
        ]
    },
    {
        "name": "Madanapalle Tomato Express",
        "location": "Madanapalle, AP",
        "latitude": 13.5503, "longitude": 78.5029,
        "price": "₹580 onwards",
        "about": "Dedicated transport for one of Asia's largest tomato markets.",
        "phone": "9876543721",
        "services": [
            {"name": "Tomato Transport", "price": 12, "unit": "per crate"},
            {"name": "Bulk Pickup Truck", "price": 3200, "unit": "per trip"}
        ]
    },
    {
        "name": "Guntakal Agri Freight",
        "location": "Guntakal, AP",
        "latitude": 15.1678, "longitude": 77.3622,
        "price": "₹640 onwards",
        "about": "Freight services connecting rail hubs to remote agricultural lands.",
        "phone": "9876543722",
        "services": [
            {"name": "Rail Head Transit", "price": 1800, "unit": "per trip"},
            {"name": "Material Pickup", "price": 640, "unit": "per trip"}
        ]
    },
    {
        "name": "Dharmavaram Silk & Farm Transit",
        "location": "Dharmavaram, AP",
        "latitude": 14.4137, "longitude": 77.7126,
        "price": "₹470 onwards",
        "about": "Handling silk cocoon and local agricultural produce transport.",
        "phone": "9876543723",
        "services": [
            {"name": "Cocoon Transit", "price": 800, "unit": "per trip"},
            {"name": "General Farm Pickup", "price": 470, "unit": "per trip"}
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

        print(f"Successfully inserted {count} Transport providers!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
