from django.contrib import admin
from .models import Profile, MainCategory, SubCategory, Provider, Service, Order, PaymentMethod, Video, News, Collaboration, Banner

@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon', 'main_category')
    list_filter = ('main_category',)
    search_fields = ('name', 'slug')

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'rating', 'reviews', 'price', 'verified')
    list_filter = ('subcategory', 'verified')
    search_fields = ('name', 'location')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'language', 'farm_type')
    list_filter = ('language', 'farm_type')
    search_fields = ('user__username', 'phone')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'price', 'unit')
    list_filter = ('provider',)
admin.site.register(Order)
admin.site.register(PaymentMethod)
admin.site.register(Video)
admin.site.register(News)
admin.site.register(Collaboration)
admin.site.register(Banner)
