import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Provider, Service, SubCategory

data = [
  {
    "name": "Rythu Machine Tools Hub",
    "subcategory": 5,
    "price": "₹999 onwards",
    "location": "Anantapur, Andhra Pradesh",
    "latitude": "14.6819",
    "longitude": "77.6006",
    "about": "Rythu Machine Tools Hub provides agricultural machinery rental and equipment support services for farmers including tractors, rotavators, cultivators, harvesters, and spraying tools. The provider helps improve farming efficiency and reduce labor dependency through affordable machine access.",
    "phone": "9876543501",
    "verified": True,
    "detailedServices": [
      { "name": "Tractor Rental", "price": "1999", "unit": "per day" },
      { "name": "Rotavator Machine Rental", "price": "1499", "unit": "per day" },
      { "name": "Cultivator Rental", "price": "1299", "unit": "per day" },
      { "name": "Power Sprayer Rental", "price": "799", "unit": "per day" }
    ]
  },
  {
    "name": "Green Agro Machinery Center",
    "subcategory": 5,
    "price": "₹899 onwards",
    "location": "Kadapa, Andhra Pradesh",
    "latitude": "14.4673",
    "longitude": "78.8242",
    "about": "Green Agro Machinery Center supports farmers with modern farming equipment rentals and agricultural machine assistance for cultivation, spraying, harvesting, and transport operations.",
    "phone": "9876543502",
    "verified": True,
    "detailedServices": [
      { "name": "Power Tiller Rental", "price": "1399", "unit": "per day" },
      { "name": "Seed Drilling Machine Rental", "price": "999", "unit": "per day" },
      { "name": "Mini Tractor Rental", "price": "1899", "unit": "per day" }
    ]
  },
  {
    "name": "Farm Tech Equipment Services",
    "subcategory": 5,
    "price": "₹1199 onwards",
    "location": "Kurnool, Andhra Pradesh",
    "latitude": "15.8281",
    "longitude": "78.0373",
    "about": "Farm Tech Equipment Services offers advanced agriculture tools and heavy farm machinery for planting, harvesting, irrigation support, and land preparation.",
    "phone": "9876543503",
    "verified": True,
    "detailedServices": [
      { "name": "Harvester Rental", "price": "4999", "unit": "per day" },
      { "name": "Threshing Machine Rental", "price": "2499", "unit": "per day" },
      { "name": "Water Pump Machine Rental", "price": "899", "unit": "per day" },
      { "name": "Mulching Machine Rental", "price": "1499", "unit": "per day" }
    ]
  },
  {
    "name": "Delta Agri Machine Hub",
    "subcategory": 5,
    "price": "₹999 onwards",
    "location": "Tirupati, Andhra Pradesh",
    "latitude": "13.6288",
    "longitude": "79.4192",
    "about": "Delta Agri Machine Hub provides reliable agricultural machine rentals helping farmers improve productivity and reduce manual workload through modern equipment access.",
    "phone": "9876543504",
    "verified": True,
    "detailedServices": [
      { "name": "Brush Cutter Rental", "price": "799", "unit": "per day" },
      { "name": "Mini Excavator Rental", "price": "3999", "unit": "per day" },
      { "name": "Power Weeder Rental", "price": "1199", "unit": "per day" }
    ]
  },
  {
    "name": "Harvest Machinery Solutions",
    "subcategory": 5,
    "price": "₹899 onwards",
    "location": "Guntur, Andhra Pradesh",
    "latitude": "16.3067",
    "longitude": "80.4365",
    "about": "Harvest Machinery Solutions helps farmers rent efficient agriculture machinery including harvesting equipment, spraying tools, cultivation machines, and land preparation tools.",
    "phone": "9876543505",
    "verified": True,
    "detailedServices": [
      { "name": "Combine Harvester Rental", "price": "5999", "unit": "per day" },
      { "name": "Crop Sprayer Machine Rental", "price": "999", "unit": "per day" },
      { "name": "Tractor Rental", "price": "1999", "unit": "per day" }
    ]
  },
  {
    "name": "Village Agro Machine Point",
    "subcategory": 5,
    "price": "₹799 onwards",
    "location": "Nellore, Andhra Pradesh",
    "latitude": "14.4426",
    "longitude": "79.9865",
    "about": "Village Agro Machine Point supplies farm machinery rentals for local farmers including ploughing equipment, irrigation tools, and transport support machines.",
    "phone": "9876543506",
    "verified": True,
    "detailedServices": [
      { "name": "Disc Plough Rental", "price": "1399", "unit": "per day" },
      { "name": "Power Tiller Rental", "price": "1499", "unit": "per day" },
      { "name": "Sprayer Machine Rental", "price": "899", "unit": "per day" }
    ]
  },
  {
    "name": "Smart Agri Equipment Rentals",
    "subcategory": 5,
    "price": "₹999 onwards",
    "location": "Rajahmundry, Andhra Pradesh",
    "latitude": "17.0005",
    "longitude": "81.8040",
    "about": "Smart Agri Equipment Rentals provides modern agricultural tools and heavy-duty machines for cultivation, harvesting, irrigation, and soil preparation work.",
    "phone": "9876543507",
    "verified": True,
    "detailedServices": [
      { "name": "Cultivator Rental", "price": "1299", "unit": "per day" },
      { "name": "Seed Planter Machine Rental", "price": "1499", "unit": "per day" },
      { "name": "Mini Loader Rental", "price": "2999", "unit": "per day" }
    ]
  },
  {
    "name": "Crop Machine Care Services",
    "subcategory": 5,
    "price": "₹899 onwards",
    "location": "Chittoor, Andhra Pradesh",
    "latitude": "13.2172",
    "longitude": "79.1003",
    "about": "Crop Machine Care Services supports farmers with machine rentals and field equipment for cultivation, pesticide spraying, crop cutting, and transport assistance.",
    "phone": "9876543508",
    "verified": True,
    "detailedServices": [
      { "name": "Power Sprayer Rental", "price": "799", "unit": "per day" },
      { "name": "Crop Cutting Machine Rental", "price": "1699", "unit": "per day" },
      { "name": "Mini Tractor Rental", "price": "1899", "unit": "per day" }
    ]
  },
  {
    "name": "Andhra Farm Machinery Hub",
    "subcategory": 5,
    "price": "₹1099 onwards",
    "location": "Visakhapatnam, Andhra Pradesh",
    "latitude": "17.6868",
    "longitude": "83.2185",
    "about": "Andhra Farm Machinery Hub provides professional-grade farming machinery and equipment rentals helping farmers modernize cultivation and harvesting operations.",
    "phone": "9876543509",
    "verified": True,
    "detailedServices": [
      { "name": "Rotavator Rental", "price": "1599", "unit": "per day" },
      { "name": "Tractor Trolley Rental", "price": "1499", "unit": "per day" },
      { "name": "Grass Cutter Rental", "price": "699", "unit": "per day" },
      { "name": "Water Pump Rental", "price": "899", "unit": "per day" }
    ]
  },
{
    "name": "Prime Agro Machinery Rentals",
    "subcategory": 5,
    "price": "₹999 onwards",
    "location": "Ongole, Andhra Pradesh",
    "latitude": "15.5057",
    "longitude": "80.0499",
    "about": "Prime Agro Machinery Rentals provides modern agricultural machines and equipment rentals for cultivation, harvesting, irrigation support, spraying, and farm productivity improvement.",
    "phone": "9876543510",
    "verified": True,
    "detailedServices": [
      { "name": "Tractor Rental", "price": "1999", "unit": "per day" },
      { "name": "Power Weeder Rental", "price": "1199", "unit": "per day" },
      { "name": "Water Pump Machine Rental", "price": "899", "unit": "per day" }
    ]
  },
  {
    "name": "Krishi Farm Equipment Center",
    "subcategory": 5,
    "price": "₹899 onwards",
    "location": "Kakinada, Andhra Pradesh",
    "latitude": "16.9891",
    "longitude": "82.2475",
    "about": "Krishi Farm Equipment Center supplies agricultural machinery rentals for soil preparation, crop care, harvesting, irrigation, and planting operations helping farmers reduce manual labor.",
    "phone": "9876543511",
    "verified": True,
    "detailedServices": [
      { "name": "Seed Drilling Machine Rental", "price": "1099", "unit": "per day" },
      { "name": "Disc Plough Rental", "price": "1499", "unit": "per day" },
      { "name": "Sprayer Machine Rental", "price": "799", "unit": "per day" },
      { "name": "Mini Tractor Rental", "price": "1899", "unit": "per day" }
    ]
  },
  {
    "name": "Harvest Tech Machinery Hub",
    "subcategory": 5,
    "price": "₹1199 onwards",
    "location": "Machilipatnam, Andhra Pradesh",
    "latitude": "16.1875",
    "longitude": "81.1389",
    "about": "Harvest Tech Machinery Hub provides reliable farm machine rentals for harvesting, spraying, crop maintenance, and cultivation support services.",
    "phone": "9876543512",
    "verified": True,
    "detailedServices": [
      { "name": "Combine Harvester Rental", "price": "5999", "unit": "per day" },
      { "name": "Crop Cutting Machine Rental", "price": "1699", "unit": "per day" },
      { "name": "Power Sprayer Rental", "price": "899", "unit": "per day" }
    ]
  },
  {
    "name": "Village Machinery Services",
    "subcategory": 5,
    "price": "₹799 onwards",
    "location": "Hindupur, Andhra Pradesh",
    "latitude": "13.8291",
    "longitude": "77.4914",
    "about": "Village Machinery Services supports farmers through affordable machine rentals for field preparation, irrigation, harvesting, and spraying operations.",
    "phone": "9876543513",
    "verified": True,
    "detailedServices": [
      { "name": "Rotavator Rental", "price": "1499", "unit": "per day" },
      { "name": "Water Pump Rental", "price": "899", "unit": "per day" },
      { "name": "Power Tiller Rental", "price": "1399", "unit": "per day" }
    ]
  },
  {
    "name": "Smart Crop Equipment Rentals",
    "subcategory": 5,
    "price": "₹1099 onwards",
    "location": "Nandyal, Andhra Pradesh",
    "latitude": "15.4779",
    "longitude": "78.4831",
    "about": "Smart Crop Equipment Rentals offers advanced agricultural machinery for planting, spraying, crop harvesting, and cultivation support helping farmers increase efficiency.",
    "phone": "9876543514",
    "verified": True,
    "detailedServices": [
      { "name": "Mini Loader Rental", "price": "2999", "unit": "per day" },
      { "name": "Mulching Machine Rental", "price": "1599", "unit": "per day" },
      { "name": "Seed Planter Rental", "price": "1499", "unit": "per day" }
    ]
  },
  {
    "name": "Farm Equipment Point",
    "subcategory": 5,
    "price": "₹899 onwards",
    "location": "Adoni, Andhra Pradesh",
    "latitude": "15.6279",
    "longitude": "77.2749",
    "about": "Farm Equipment Point provides dependable agriculture machine rentals for cultivation, harvesting, crop spraying, and irrigation work in farming regions.",
    "phone": "9876543515",
    "verified": True,
    "detailedServices": [
      { "name": "Grass Cutter Rental", "price": "699", "unit": "per day" },
      { "name": "Power Weeder Rental", "price": "1199", "unit": "per day" },
      { "name": "Tractor Trolley Rental", "price": "1499", "unit": "per day" }
    ]
  },
  {
    "name": "Agri Gear Machinery Rentals",
    "subcategory": 5,
    "price": "₹999 onwards",
    "location": "Proddatur, Andhra Pradesh",
    "latitude": "14.7502",
    "longitude": "78.5481",
    "about": "Agri Gear Machinery Rentals provides heavy-duty and small-scale agricultural tools for soil preparation, spraying, harvesting, and land management support.",
    "phone": "9876543516",
    "verified": True,
    "detailedServices": [
      { "name": "Cultivator Rental", "price": "1299", "unit": "per day" },
      { "name": "Mini Excavator Rental", "price": "3999", "unit": "per day" },
      { "name": "Crop Sprayer Rental", "price": "899", "unit": "per day" }
    ]
  },
  {
    "name": "Future Farm Tools Center",
    "subcategory": 5,
    "price": "₹899 onwards",
    "location": "Tenali, Andhra Pradesh",
    "latitude": "16.2390",
    "longitude": "80.6458",
    "about": "Future Farm Tools Center offers affordable machine rental services helping farmers improve field productivity and reduce labor costs through modern agricultural equipment.",
    "phone": "9876543517",
    "verified": True,
    "detailedServices": [
      { "name": "Power Sprayer Machine Rental", "price": "799", "unit": "per day" },
      { "name": "Seed Drilling Machine Rental", "price": "1099", "unit": "per day" },
      { "name": "Mini Tractor Rental", "price": "1899", "unit": "per day" }
    ]
  },
  {
    "name": "Rural Farm Machinery Point",
    "subcategory": 5,
    "price": "₹1099 onwards",
    "location": "Madanapalle, Andhra Pradesh",
    "latitude": "13.5503",
    "longitude": "78.5029",
    "about": "Rural Farm Machinery Point supplies reliable agricultural machinery rentals for land preparation, harvesting, spraying, and irrigation management.",
    "phone": "9876543518",
    "verified": True,
    "detailedServices": [
      { "name": "Harvester Rental", "price": "4999", "unit": "per day" },
      { "name": "Rotavator Rental", "price": "1499", "unit": "per day" },
      { "name": "Water Pump Machine Rental", "price": "899", "unit": "per day" },
      { "name": "Grass Cutter Rental", "price": "699", "unit": "per day" }
    ]
  }
]

def run():
    try:
        subcat = SubCategory.objects.get(id=5)
        count = 0
        for p_data in data:
            services_data = p_data.pop('detailedServices')
            about_text = p_data.pop('about')
            p_data.pop('subcategory')

            provider = Provider.objects.create(
                subcategory=subcat,
                description=about_text,
                **p_data
            )

            for s in services_data:
                Service.objects.create(provider=provider, **s)
            count += 1

        print(f"Successfully inserted {count} providers and their services into Category 5!")
    except Exception as e:
        print(f"Error during insertion: {e}")

if __name__ == '__main__':
    run()
