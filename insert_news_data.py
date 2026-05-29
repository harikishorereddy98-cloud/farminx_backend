import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import News

data = [
    {
        "title": "Government Announces New Subsidy for Drip Irrigation",
        "date": "Oct 24, 2023",
        "category": "Policy",
        "author": "Rajesh Kumar",
        "sub": "Support for small-scale farmers",
        "content": "The agricultural department has announced a 50% subsidy for small-scale farmers to install drip irrigation systems. This initiative aims to conserve water and improve crop yield in drought-prone areas."
    },
    {
        "title": "Organic Farming: A Growing Trend in Andhra Pradesh",
        "date": "Oct 22, 2023",
        "category": "Trends",
        "author": "Anitha Reddy",
        "sub": "Transitioning to chemical-free agriculture",
        "content": "More farmers in Andhra Pradesh are switching to organic farming due to increasing demand for chemical-free produce and better market prices for organic crops."
    },
    {
        "title": "New Pest Control Techniques for Paddy Crops",
        "date": "Oct 20, 2023",
        "category": "Techniques",
        "author": "Dr. S. Murthy",
        "sub": "Sustainable pest management",
        "content": "Experts suggest integrated pest management techniques to control common paddy pests without excessive use of chemical pesticides, focusing on biological control and crop rotation."
    }
]

def run():
    try:
        # Clear existing news items to avoid duplicates with old schema
        News.objects.all().delete()
        for item in data:
            News.objects.create(**item)
        print("Successfully inserted updated news items!")
    except Exception as e:
        print(f"Error during insertion: {e}")

if __name__ == '__main__':
    run()
