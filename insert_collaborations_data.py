import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Collaboration

data = [
    {
        "title": "AgroChem Fertilizers",
        "sub": "Premium organic fertilizers",
        "icon": "flask-outline",
        "color": "#4B7FFF",
        "description": "Leading provider of sustainable farming inputs and soil enrichment products.",
        "link": "https://example.com/agrochem"
    },
    {
        "title": "Dr. Rajesh Kumar",
        "sub": "Soil Science Expert",
        "icon": "person-outline",
        "color": "#34C759",
        "description": "Renowned consultant specializing in high-yield farming and crop disease management.",
        "link": "https://example.com/dr-rajesh"
    },
    {
        "title": "GreenGrow Nutrients",
        "sub": "Sustainable solutions",
        "icon": "leaf-outline",
        "color": "#FF9F0A",
        "description": "Eco-friendly nutrient solutions for modern hydroponic and traditional farming.",
        "link": "https://example.com/greengrow"
    },
    {
        "title": "FarmTech Robotics",
        "sub": "Automation Experts",
        "icon": "cog-outline",
        "color": "#6C63FF",
        "description": "Developing cutting-edge autonomous machinery for large-scale farm operations.",
        "link": "https://example.com/farmtech"
    },
    {
        "title": "WeatherWise Agri",
        "sub": "Precision Forecasting",
        "icon": "cloud-outline",
        "color": "#007AFF",
        "description": "Real-time hyper-local weather alerts specifically designed for farming schedules.",
        "link": "https://example.com/weatherwise"
    }
]

def run():
    try:
        Collaboration.objects.all().delete()
        for item in data:
            Collaboration.objects.create(**item)
        print("Successfully inserted collaboration items with links!")
    except Exception as e:
        print(f"Error during insertion: {e}")

if __name__ == '__main__':
    run()
