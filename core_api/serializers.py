from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Address, MainCategory, SubCategory, Provider, Service, Order, PaymentMethod, Video, News, Collaboration, Banner, Spotlight

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone', 'profile_image', 'land_area', 'land_location', 'farm_type']

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    phone = serializers.CharField(source='profile.phone')
    profileImage = serializers.SerializerMethodField()
    landArea = serializers.CharField(source='profile.land_area', required=False)
    landLocation = serializers.CharField(source='profile.land_location', required=False)
    farmType = serializers.CharField(source='profile.farm_type', required=False)
    language = serializers.CharField(source='profile.language', required=False)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'profileImage', 'landArea', 'landLocation', 'farmType', 'language']

    def get_profileImage(self, obj):
        if obj.profile.profile_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.profile.profile_image.url)
            return obj.profile.profile_image.url
        return None

class SubCategorySerializer(serializers.ModelSerializer):
    providerCount = serializers.SerializerMethodField()

    class Meta:
        model = SubCategory
        fields = ['id', 'main_category', 'name', 'slug', 'icon', 'providerCount']

    def get_providerCount(self, obj):
        return obj.providers.count()

    def validate_slug(self, value):
        # Strip leading slash if provided
        return value.lstrip('/')

class MainCategorySerializer(serializers.ModelSerializer):
    subCategories = SubCategorySerializer(many=True, source='subcategories', read_only=True)

    class Meta:
        model = MainCategory
        fields = ['id', 'name', 'slug', 'subCategories']

    def validate_slug(self, value):
        # Strip leading slash if provided
        return value.lstrip('/')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'label', 'text', 'latitude', 'longitude', 'phone']
        read_only_fields = ['user']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price', 'unit']

class ProviderSerializer(serializers.ModelSerializer):
    detailedServices = ServiceSerializer(source='detailed_services', many=True, required=False)
    services = serializers.SerializerMethodField()
    category = serializers.CharField(source='subcategory.slug', read_only=True)
    about = serializers.CharField(source='description', allow_blank=True, required=False)

    # Use standard ImageField for uploads, customize output in to_representation
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Provider
        fields = ['id', 'name', 'image', 'rating', 'reviews', 'price', 'location', 'latitude', 'longitude', 'verified', 'category', 'subcategory', 'services', 'detailedServices', 'about', 'phone']

    def to_representation(self, instance):
        """Convert image field to absolute URL during GET requests"""
        ret = super().to_representation(instance)
        if instance.image:
            request = self.context.get('request')
            if request:
                ret['image'] = request.build_absolute_uri(instance.image.url)
        return ret

    def get_services(self, obj):
        return [service.name for service in obj.detailed_services.all()]

    def create(self, validated_data):
        services_data = validated_data.pop('detailed_services', [])
        provider = Provider.objects.create(**validated_data)
        for service_data in services_data:
            Service.objects.create(provider=provider, **service_data)
        return provider

    def update(self, instance, validated_data):
        services_data = validated_data.pop('detailed_services', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if services_data is not None:
            instance.detailed_services.all().delete()
            for service_data in services_data:
                Service.objects.create(provider=instance, **service_data)
        return instance

class OrderSerializer(serializers.ModelSerializer):
    providerName = serializers.CharField(source='provider_name')

    class Meta:
        model = Order
        fields = ['id', 'providerName', 'services', 'date', 'time', 'total', 'status', 'progress', 'worker_name', 'worker_phone', 'worker_whatsapp', 'work_images', 'rating', 'review', 'created_at']
        read_only_fields = ['user', 'created_at']

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
        read_only_fields = ['user']

class VideoSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='youtube_id')

    class Meta:
        model = Video
        fields = ['id', 'title', 'url', 'thumbnail']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.thumbnail:
            request = self.context.get('request')
            if request:
                ret['thumbnail'] = request.build_absolute_uri(instance.thumbnail.url)
        return ret

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.image:
            request = self.context.get('request')
            if request:
                ret['image'] = request.build_absolute_uri(instance.image.url)
        return ret

class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.image:
            request = self.context.get('request')
            if request:
                ret['image'] = request.build_absolute_uri(instance.image.url)
        return ret

class BannerSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source='image_url')

    class Meta:
        model = Banner
        fields = ['id', 'image', 'title', 'subtitle', 'icon']

class SpotlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spotlight
        fields = ['id', 'title', 'subtitle', 'image', 'link', 'active']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.image:
            request = self.context.get('request')
            if request:
                ret['image'] = request.build_absolute_uri(instance.image.url)
        return ret
