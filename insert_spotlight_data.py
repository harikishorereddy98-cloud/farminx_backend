import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Spotlight

data = [
    {
        "title": "Premium Seeds",
        "subtitle": "High-yield varieties",
        "link": "/agriculture/seeds"
    },
    {
        "title": "Farm Equipment",
        "subtitle": "Rent or buy machinery",
        "link": "/agriculture/equipment-rental"
    },
    {
        "title": "Soil Testing",
        "subtitle": "Expert analysis for your farm",
        "link": "/agriculture/soil-testing"
    },
    {
        "title": "Expert Consultation",
        "subtitle": "Get advice from top agronomists",
        "link": "/agriculture/expert-consultation"
    }
]

def run():
    try:
        # Clear existing spotlight items if any, or just add new ones
        # Spotlight.objects.all().delete()

        for item in data:
            Spotlight.objects.create(**item)
        print("Successfully inserted spotlight items!")
    except Exception as e:
        print(f"Error during insertion: {e}")

if __name__ == '__main__':
    run()
