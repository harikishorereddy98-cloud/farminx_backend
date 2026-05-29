from django.db import models
from django.contrib.auth.models import User

# User Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    land_area = models.CharField(max_length=100, blank=True)
    land_location = models.CharField(max_length=255, blank=True)
    farm_type = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=10, default='en') # Preferred language code

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Category Structure
class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) # agriculture, gardening, animal_husbandry

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) # soil-testing, etc.
    icon = models.CharField(max_length=50, blank=True) # e.g. flask-outline

    def __str__(self):
        return f"{self.main_category.name} > {self.name}"

# Service Providers
class Provider(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='providers', null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='providers/', null=True, blank=True)
    rating = models.FloatField(default=0.0)
    reviews = models.IntegerField(default=0)
    price = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='detailed_services')
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.provider.name}"

# Address Management
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    label = models.CharField(max_length=50)
    text = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.label} - {self.user.username}"

# Orders & Bookings
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('assigned', 'Worker Assigned'),
        ('reached', 'Worker Reached'),
        ('started', 'Work Started'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    provider_name = models.CharField(max_length=255)
    services = models.JSONField()
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    total = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    progress = models.IntegerField(default=0) # 0 to 100
    worker_name = models.CharField(max_length=100, blank=True, null=True)
    worker_phone = models.CharField(max_length=15, blank=True, null=True)
    worker_whatsapp = models.CharField(max_length=15, blank=True, null=True)
    work_images = models.JSONField(default=list, blank=True) # List of image URLs
    rating = models.IntegerField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Payment Methods
class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_methods')
    type = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    details = models.CharField(max_length=255)

# Content Module
class Video(models.Model):
    title = models.CharField(max_length=255)
    youtube_id = models.CharField(max_length=50)
    url = models.URLField()
    thumbnail = models.ImageField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='General')
    author = models.CharField(max_length=100, default='Farminx Team')
    sub = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news/', null=True, blank=True)

    def __str__(self):
        return self.title

class Collaboration(models.Model):
    title = models.CharField(max_length=255)
    sub = models.CharField(max_length=255)
    icon = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='collaborations/', null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)

class Banner(models.Model):
    image_url = models.URLField()
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    icon = models.CharField(max_length=100)

class Spotlight(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.ImageField(upload_to='spotlight/', null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
