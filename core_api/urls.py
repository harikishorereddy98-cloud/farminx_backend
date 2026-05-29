from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (LoginView, RegisterView, ForgotPasswordView, SendOtpView, VerifyOtpView, ChangePasswordView,
                    ProfileUpdateView, LanguageSettingsView, AddressViewSet, CategoryListView, CategoryDetailView, SubCategoryProvidersView,
                    ProviderDetailView, ProviderViewSet, OrderViewSet, PaymentMethodViewSet,
                    VideoViewSet, NewsViewSet, CollaborationViewSet, BannerViewSet, SpotlightViewSet,
                    AdminCategoryViewSet, AdminSubCategoryViewSet, AdminProviderViewSet, AdminServiceViewSet)

router = DefaultRouter()
router.register(r'user/addresses', AddressViewSet, basename='address')
router.register(r'providers', ProviderViewSet, basename='provider')
router.register(r'user/orders', OrderViewSet, basename='order')
router.register(r'user/payments', PaymentMethodViewSet, basename='payment')
router.register(r'content/videos', VideoViewSet, basename='video')
router.register(r'content/news', NewsViewSet, basename='news')
router.register(r'content/collaborations', CollaborationViewSet, basename='collaboration')
router.register(r'content/banners', BannerViewSet, basename='banner')
router.register(r'content/spotlight', SpotlightViewSet, basename='spotlight')

# Admin CRUD
router.register(r'admin/categories', AdminCategoryViewSet, basename='admin-category')
router.register(r'admin/subcategories', AdminSubCategoryViewSet, basename='admin-subcategory')
router.register(r'admin/providers', AdminProviderViewSet, basename='admin-provider')
router.register(r'admin/services', AdminServiceViewSet, basename='admin-service')

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('auth/send-otp/', SendOtpView.as_view(), name='send-otp'),
    path('auth/verify-otp/', VerifyOtpView.as_view(), name='verify-otp'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('user/profile/', ProfileUpdateView.as_view(), name='profile-update'),
    path('user/language/', LanguageSettingsView.as_view(), name='language-update'),

    # Provider & Category Hierarchy (Must be above router)
    path('providers/categories/', CategoryListView.as_view(), name='category-list'),
    path('providers/detail/<int:provider_id>/', ProviderDetailView.as_view(), name='provider-detail-direct'),
    path('providers/<slug:category_slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('providers/<slug:category_slug>/<slug:subcategory_slug>/', SubCategoryProvidersView.as_view(), name='subcategory-providers'),
    path('providers/<slug:category_slug>/<slug:subcategory_slug>/<int:provider_id>/', ProviderDetailView.as_view(), name='provider-detail'),

    path('', include(router.urls)),
]
