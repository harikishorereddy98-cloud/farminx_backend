import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

data = [
  {
    "name": "Rural Tractor Driver Hub",
    "subcategory": 4,
    "price": "₹749 onwards",
    "location": "Kakinada, Andhra Pradesh",
    "latitude": "16.9891",
    "longitude": "82.2475",
    "about": "Rural Tractor Driver Hub provides experienced agricultural vehicle operators for farming activities including tractor handling, farm transport, spraying support, and seasonal harvesting logistics for farmers.",
    "phone": "9876543411",
    "verified": True,
    "detailedServices": [
      {"name": "Tractor Driver Service", "price": "999", "unit": "per day"},
      {"name": "Pesticide Spray Vehicle Driver", "price": "1299", "unit": "per day"},
      {"name": "Farm Equipment Transport Driver", "price": "899", "unit": "per trip"}
    ]
  },
  {
    "name": "Harvest Driver Solutions",
    "subcategory": 4,
    "price": "₹799 onwards",
    "location": "Machilipatnam, Andhra Pradesh",
    "latitude": "16.1875",
    "longitude": "81.1389",
    "about": "Harvest Driver Solutions supplies trained agricultural drivers for farm machinery operations, crop transport, irrigation vehicle handling, and harvesting support.",
    "phone": "9876543412",
    "verified": True,
    "detailedServices": [
      {"name": "Harvester Vehicle Operator", "price": "1599", "unit": "per day"},
      {"name": "Crop Transport Driver", "price": "899", "unit": "per trip"},
      {"name": "Water Tanker Driver", "price": "999", "unit": "per trip"}
    ]
  },
  {
    "name": "Agri Transport Driver Care",
    "subcategory": 4,
    "price": "₹699 onwards",
    "location": "Hindupur, Andhra Pradesh",
    "latitude": "13.8291",
    "longitude": "77.4914",
    "about": "Agri Transport Driver Care offers reliable agricultural drivers for tractor operations, field machinery movement, crop transportation, and seasonal farming support.",
    "phone": "9876543413",
    "verified": True,
    "detailedServices": [
      {"name": "Tractor Trolley Driver", "price": "1099", "unit": "per trip"},
      {"name": "Field Machinery Driver", "price": "1199", "unit": "per day"},
      {"name": "Crop Goods Transport Driver", "price": "899", "unit": "per trip"}
    ]
  },
  {
    "name": "Farm Track Driver Services",
    "subcategory": 4,
    "price": "₹899 onwards",
    "location": "Nandyal, Andhra Pradesh",
    "latitude": "15.4779",
    "longitude": "78.4831",
    "about": "Farm Track Driver Services supports farmers with trained drivers for harvesting machinery, irrigation support vehicles, and farm goods transportation.",
    "phone": "9876543414",
    "verified": True,
    "detailedServices": [
      {"name": "Tractor Driver", "price": "999", "unit": "per day"},
      {"name": "Harvester Driver", "price": "1499", "unit": "per day"},
      {"name": "Farm Produce Transport Driver", "price": "899", "unit": "per trip"}
    ]
  },
  {
    "name": "Village Farm Driver Network",
    "subcategory": 4,
    "price": "₹699 onwards",
    "location": "Adoni, Andhra Pradesh",
    "latitude": "15.6279",
    "longitude": "77.2749",
    "about": "Village Farm Driver Network provides local agricultural vehicle operators for farm transport, machinery movement, tractor work, and crop logistics assistance.",
    "phone": "9876543415",
    "verified": True,
    "detailedServices": [
      {"name": "Farm Transport Driver", "price": "799", "unit": "per trip"},
      {"name": "Tractor Operator", "price": "999", "unit": "per day"},
      {"name": "Water Supply Vehicle Driver", "price": "1099", "unit": "per trip"}
    ]
  },
  {
    "name": "Smart Agri Vehicle Drivers",
    "subcategory": 4,
    "price": "₹799 onwards",
    "location": "Proddatur, Andhra Pradesh",
    "latitude": "14.7502",
    "longitude": "78.5481",
    "about": "Smart Agri Vehicle Drivers offers skilled operators for agriculture transport, tractor driving, pesticide spraying support, and harvest season logistics.",
    "phone": "9876543416",
    "verified": True,
    "detailedServices": [
      {"name": "Pesticide Sprayer Vehicle Driver", "price": "1299", "unit": "per day"},
      {"name": "Tractor Driver Service", "price": "999", "unit": "per day"},
      {"name": "Harvest Crop Transport Driver", "price": "899", "unit": "per trip"}
    ]
  },
  {
    "name": "Crop Mobility Drivers",
    "subcategory": 4,
    "price": "₹749 onwards",
    "location": "Tenali, Andhra Pradesh",
    "latitude": "16.2390",
    "longitude": "80.6458",
    "about": "Crop Mobility Drivers helps farmers access trained agricultural vehicle operators for crop movement, machinery handling, and farm logistics support.",
    "phone": "9876543417",
    "verified": True,
    "detailedServices": [
      {"name": "Agricultural Equipment Driver", "price": "1199", "unit": "per day"},
      {"name": "Crop Delivery Driver", "price": "899", "unit": "per trip"},
      {"name": "Tractor Driver", "price": "999", "unit": "per day"}
    ]
  },
  {
    "name": "Prime Farm Driver Services",
    "subcategory": 4,
    "price": "₹799 onwards",
    "location": "Madanapalle, Andhra Pradesh",
    "latitude": "13.5503",
    "longitude": "78.5029",
    "about": "Prime Farm Driver Services provides experienced farm vehicle operators for tractors, harvest transport, spraying operations, and agriculture machinery support.",
    "phone": "9876543418",
    "verified": True,
    "detailedServices": [
      {"name": "Tractor Trolley Driver", "price": "999", "unit": "per trip"},
      {"name": "Harvest Vehicle Driver", "price": "1499", "unit": "per day"},
      {"name": "Farm Equipment Transport Driver", "price": "1099", "unit": "per trip"}
    ]
  }
]

def run():
    try:
        subcat = SubCategory.objects.get(id=4)
        count = 0
        for p_data in data:
            services_data = p_data.pop('detailedServices')
            # Handle about/description mapping
            about_text = p_data.pop('about')

            # Map subcategory key
            p_data.pop('subcategory')

            provider = Provider.objects.create(
                subcategory=subcat,
                description=about_text,
                **p_data
            )

            for s in services_data:
                Service.objects.create(provider=provider, **s)
            count += 1

        print(f"Successfully inserted {count} providers and their services!")
    except Exception as e:
        print(f"Error during insertion: {e}")

if __name__ == '__main__':
    run()
