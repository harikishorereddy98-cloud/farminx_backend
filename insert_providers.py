import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

data = [
  {
    "name": "Rythu Driver Services",
    "subcategory": 4,
    "price": "₹799 onwards",
    "location": "Anantapur, Andhra Pradesh",
    "latitude": "14.6819",
    "longitude": "77.6006",
    "about": "Rythu Driver Services provides experienced agricultural vehicle drivers for farming operations including tractor driving, harvest transportation, spraying support, and farm logistics. The provider helps farmers manage seasonal work efficiently through trained operators and timely field assistance.",
    "phone": "9876543401",
    "verified": True,
    "detailedServices": [
      {"name": "Tractor Driver Service", "price": "999", "unit": "per day"},
      {"name": "Harvester Operator Service", "price": "1499", "unit": "per day"},
      {"name": "Farm Goods Transport Driver", "price": "899", "unit": "per trip"}
    ]
  },
  {
    "name": "Green Field Driver Solutions",
    "subcategory": 4,
    "price": "₹699 onwards",
    "location": "Kadapa, Andhra Pradesh",
    "latitude": "14.4673",
    "longitude": "78.8242",
    "about": "Green Field Driver Solutions offers trained agricultural vehicle operators for farm transport, tractor operations, pesticide spraying vehicles, and equipment movement support.",
    "phone": "9876543402",
    "verified": True,
    "detailedServices": [
      {"name": "Tractor Operator", "price": "899", "unit": "per day"},
      {"name": "Sprayer Vehicle Driver", "price": "1199", "unit": "per day"},
      {"name": "Agricultural Equipment Driver", "price": "999", "unit": "per trip"}
    ]
  },
  {
    "name": "Farm Wheels Driver Center",
    "subcategory": 4,
    "price": "₹899 onwards",
    "location": "Kurnool, Andhra Pradesh",
    "latitude": "15.8281",
    "longitude": "78.0373",
    "about": "Farm Wheels Driver Center provides professional farm vehicle drivers for agricultural transport, harvesting support, and field machinery operations.",
    "phone": "9876543403",
    "verified": True,
    "detailedServices": [
      {"name": "Harvester Driver", "price": "1599", "unit": "per day"},
      {"name": "Tractor Trolley Driver", "price": "999", "unit": "per trip"},
      {"name": "Crop Transport Driver", "price": "899", "unit": "per trip"},
      {"name": "Farm Logistics Driver", "price": "1299", "unit": "per day"}
    ]
  },
  {
    "name": "Agri Wheels Driver Services",
    "subcategory": 4,
    "price": "₹749 onwards",
    "location": "Tirupati, Andhra Pradesh",
    "latitude": "13.6288",
    "longitude": "79.4192",
    "about": "Agri Wheels Driver Services supports farmers through trained agricultural drivers for machinery operation, irrigation vehicle handling, and crop transportation services.",
    "phone": "9876543404",
    "verified": True,
    "detailedServices": [
      {"name": "Tractor Driver", "price": "999", "unit": "per day"},
      {"name": "Water Tanker Driver", "price": "899", "unit": "per trip"},
      {"name": "Field Equipment Transport Driver", "price": "1199", "unit": "per trip"}
    ]
  },
  {
    "name": "Delta Farm Drivers",
    "subcategory": 4,
    "price": "₹799 onwards",
    "location": "Guntur, Andhra Pradesh",
    "latitude": "16.3067",
    "longitude": "80.4365",
    "about": "Delta Farm Drivers supplies trained agricultural vehicle operators for daily farming work including machinery handling, harvesting, transport, and pesticide spraying support.",
    "phone": "9876543405",
    "verified": True,
    "detailedServices": [
      {"name": "Pesticide Sprayer Vehicle Driver", "price": "1399", "unit": "per day"},
      {"name": "Tractor Driver", "price": "999", "unit": "per day"},
      {"name": "Farm Goods Delivery Driver", "price": "899", "unit": "per trip"}
    ]
  },
  {
    "name": "Village Agro Driver Hub",
    "subcategory": 4,
    "price": "₹699 onwards",
    "location": "Nellore, Andhra Pradesh",
    "latitude": "14.4426",
    "longitude": "79.9865",
    "about": "Village Agro Driver Hub provides local and experienced agricultural vehicle drivers helping farmers manage transport and equipment operations during seasonal demand.",
    "phone": "9876543406",
    "verified": True,
    "detailedServices": [
      {"name": "Crop Transport Driver", "price": "799", "unit": "per trip"},
      {"name": "Tractor Driver", "price": "999", "unit": "per day"},
      {"name": "Harvester Vehicle Operator", "price": "1599", "unit": "per day"}
    ]
  },
  {
    "name": "Smart Farm Driver Solutions",
    "subcategory": 4,
    "price": "₹899 onwards",
    "location": "Rajahmundry, Andhra Pradesh",
    "latitude": "17.0005",
    "longitude": "81.8040",
    "about": "Smart Farm Driver Solutions offers skilled drivers for farm logistics, agricultural transport, spraying operations, and seasonal crop movement support.",
    "phone": "9876543407",
    "verified": True,
    "detailedServices": [
      {"name": "Tractor Trolley Driver", "price": "1099", "unit": "per trip"},
      {"name": "Farm Machinery Driver", "price": "1299", "unit": "per day"},
      {"name": "Crop Delivery Driver", "price": "899", "unit": "per trip"}
    ]
  },
  {
    "name": "Crop Route Driver Services",
    "subcategory": 4,
    "price": "₹799 onwards",
    "location": "Chittoor, Andhra Pradesh",
    "latitude": "13.2172",
    "longitude": "79.1003",
    "about": "Crop Route Driver Services provides trusted farm drivers for agricultural machinery, crop movement, and seasonal harvest transport across nearby regions.",
    "phone": "9876543408",
    "verified": True,
    "detailedServices": [
      {"name": "Harvester Driver", "price": "1499", "unit": "per day"},
      {"name": "Farm Transport Driver", "price": "799", "unit": "per trip"},
      {"name": "Water Tanker Driver", "price": "999", "unit": "per trip"}
    ]
  },
  {
    "name": "Andhra Agri Driver Point",
    "subcategory": 4,
    "price": "₹699 onwards",
    "location": "Visakhapatnam, Andhra Pradesh",
    "latitude": "17.6868",
    "longitude": "83.2185",
    "about": "Andhra Agri Driver Point provides experienced farm drivers for tractor work, transport support, and agriculture machinery handling for efficient farming operations.",
    "phone": "9876543409",
    "verified": True,
    "detailedServices": [
      {"name": "Tractor Driver Service", "price": "999", "unit": "per day"},
      {"name": "Agriculture Equipment Driver", "price": "1099", "unit": "per day"},
      {"name": "Farm Material Transport Driver", "price": "899", "unit": "per trip"}
    ]
  },
  {
    "name": "Farm Mobility Driver Care",
    "subcategory": 4,
    "price": "₹799 onwards",
    "location": "Ongole, Andhra Pradesh",
    "latitude": "15.5057",
    "longitude": "80.0499",
    "about": "Farm Mobility Driver Care helps farmers hire trained agricultural vehicle operators for tractors, harvesters, crop transport, and seasonal field support.",
    "phone": "9876543410",
    "verified": True,
    "detailedServices": [
      {"name": "Tractor Operator", "price": "999", "unit": "per day"},
      {"name": "Crop Loading Vehicle Driver", "price": "1199", "unit": "per trip"},
      {"name": "Harvest Transport Driver", "price": "899", "unit": "per trip"}
    ]
  }
]

def run():
    try:
        subcat = SubCategory.objects.get(id=4)
        for p_data in data:
            services = p_data.pop('detailedServices')
            p_data.pop('subcategory') # removed because we use the object

            provider = Provider.objects.create(subcategory=subcat, description=p_data.pop('about'), **p_data)
            for s in services:
                Service.objects.create(provider=provider, **s)
        print("Successfully inserted all providers and services!")
    except Exception as e:
        print(f"Error during insertion: {e}")

if __name__ == '__main__':
    run()
