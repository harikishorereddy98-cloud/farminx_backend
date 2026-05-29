import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farminx_core.settings')
django.setup()

from core_api.models import Video

data = [
    {
        "title": "Modern Irrigation Techniques",
        "youtube_id": "0K1_0O1Xq7c",
        "url": "https://www.youtube.com/watch?v=0K1_0O1Xq7c"
    },
    {
        "title": "Organic Pest Control at Home",
        "youtube_id": "rXmK9T9_v-k",
        "url": "https://www.youtube.com/watch?v=rXmK9T9_v-k"
    },
    {
        "title": "Smart Farming with Drones",
        "youtube_id": "h3Z7XvHn7Gg",
        "url": "https://www.youtube.com/watch?v=h3Z7XvHn7Gg"
    },
    {
        "title": "Soil Testing Guide for Beginners",
        "youtube_id": "oXf8E7Q7XU4",
        "url": "https://www.youtube.com/watch?v=oXf8E7Q7XU4"
    }
]

def run():
    try:
        # Video.objects.all().delete()
        for item in data:
            Video.objects.create(**item)
        print("Successfully inserted video items!")
    except Exception as e:
        print(f"Error during insertion: {e}")

if __name__ == '__main__':
    run()
