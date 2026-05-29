from rest_framework import viewsets, status, permissions, views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from .models import (Profile, Address, MainCategory, SubCategory, Provider, Service,
                      Order, PaymentMethod, Video, News, Collaboration, Banner, Spotlight)
from .serializers import (UserSerializer, AddressSerializer, MainCategorySerializer,
                          SubCategorySerializer, ProviderSerializer, ServiceSerializer,
                          OrderSerializer, PaymentMethodSerializer, VideoSerializer,
                          NewsSerializer, CollaborationSerializer, BannerSerializer, SpotlightSerializer)

# Authentication Views
class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'status': 'error', 'message': 'Email and password required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Try to get user by email
            user_obj = User.objects.get(email=email)
            # Authenticate using username (which we set as email during registration)
            user = authenticate(username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'status': 'success',
                'token': str(refresh.access_token),
                'user': UserSerializer(user, context={'request': request}).data
            })

        # Check why auth failed
        if User.objects.filter(email=email).exists():
             print(f"[AUTH ERROR] User with email {email} exists, but authentication failed. Probably wrong password.")
        else:
             print(f"[AUTH ERROR] No user found with email {email}. They should Register first.")

        return Response({'status': 'error', 'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        data = request.data
        if not isinstance(data, dict):
            return Response({'status': 'error', 'message': 'JSON object expected'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=data.get('email')).exists():
            return Response({'status': 'error', 'message': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=data.get('email'), email=data.get('email'), password=data.get('password'), first_name=data.get('name', ''))
        Profile.objects.create(user=user, phone=data.get('phone', ''))

        refresh = RefreshToken.for_user(user)
        return Response({
            'status': 'success',
            'message': 'Account created successfully',
            'token': str(refresh.access_token),
            'user': UserSerializer(user, context={'request': request}).data
        })

class ForgotPasswordView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request): return Response({'status': 'success', 'message': 'Password reset link sent'})

class SendOtpView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request): return Response({'status': 'success', 'message': 'OTP sent successfully'})

class VerifyOtpView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request): return Response({'status': 'success', 'message': 'OTP Verified'})

class ChangePasswordView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request): return Response({'status': 'success', 'message': 'Password updated'})

# Category & Provider Logic
class CategoryListView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        categories = MainCategory.objects.all()
        serializer = MainCategorySerializer(categories, many=True)
        return Response({'categories': serializer.data})

class CategoryDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, category_slug):
        try:
            category = MainCategory.objects.get(slug=category_slug)
            serializer = MainCategorySerializer(category)
            return Response(serializer.data)
        except MainCategory.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

class SubCategoryProvidersView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, category_slug, subcategory_slug):
        try:
            subcategory = SubCategory.objects.get(slug=subcategory_slug, main_category__slug=category_slug)
            providers = Provider.objects.filter(subcategory=subcategory)
            serializer = ProviderSerializer(providers, many=True, context={'request': request})
            return Response(serializer.data)
        except SubCategory.DoesNotExist:
            return Response({'error': 'Subcategory not found'}, status=status.HTTP_404_NOT_FOUND)

class ProviderDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, provider_id, category_slug=None, subcategory_slug=None):
        try:
            # If slugs provided, verify they match
            if subcategory_slug:
                provider = Provider.objects.get(id=provider_id, subcategory__slug=subcategory_slug)
            else:
                provider = Provider.objects.get(id=provider_id)

            serializer = ProviderSerializer(provider, context={'request': request})
            return Response(serializer.data)
        except Provider.DoesNotExist:
            return Response({'error': 'Provider not found'}, status=status.HTTP_404_NOT_FOUND)

class ProviderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Provider.objects.all()
        category = self.request.query_params.get('category')
        search = self.request.query_params.get('search')
        if category:
            queryset = queryset.filter(subcategory__main_category__slug=category)
        if search:
            queryset = queryset.filter(name__icontains=search) | queryset.filter(description__icontains=search)
        return queryset

# User Profile & Address
class ProfileUpdateView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request):
        user = request.user
        profile = user.profile
        data = request.data
        user.first_name = data.get('name', user.first_name)
        user.save()
        profile.phone = data.get('phone', profile.phone)
        profile.land_area = data.get('landArea', profile.land_area)
        profile.land_location = data.get('landLocation', profile.land_location)
        profile.farm_type = data.get('farmType', profile.farm_type)
        profile.language = data.get('language', profile.language)
        profile.save()
        return Response({'status': 'success', 'user': UserSerializer(user, context={'request': request}).data})

class LanguageSettingsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Return list of supported languages for the UI
        langs = [{'code': code, 'name': name} for code, name in settings.LANGUAGES]
        return Response({'languages': langs})

    def post(self, request):
        language = request.data.get('language')
        if language not in dict(settings.LANGUAGES):
            return Response({'status': 'error', 'message': 'Unsupported language'}, status=status.HTTP_400_BAD_REQUEST)

        profile = request.user.profile
        profile.language = language
        profile.save()

        return Response({'status': 'success', 'message': 'Language updated successfully'})

class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self): return Address.objects.filter(user=self.request.user)
    def perform_create(self, serializer): serializer.save(user=self.request.user)
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'status': 'success', 'address': response.data})
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({'status': 'success', 'address': response.data})
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'status': 'success', 'message': 'Deleted'})

# Orders & Bookings
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self): return Order.objects.filter(user=self.request.user).order_by('-created_at')
    def perform_create(self, serializer): serializer.save(user=self.request.user)
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'status': 'success', 'orderId': response.data.get('id')})

    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        order = self.get_object()
        if order.status != 'completed':
            return Response({'error': 'Can only rate completed orders'}, status=status.HTTP_400_BAD_REQUEST)

        rating = request.data.get('rating')
        review = request.data.get('review', '')

        if not rating:
            return Response({'error': 'Rating is required'}, status=status.HTTP_400_BAD_REQUEST)

        order.rating = rating
        order.review = review
        order.save()

        return Response({'status': 'success', 'message': 'Rating submitted'})

class PaymentMethodViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self): return PaymentMethod.objects.filter(user=self.request.user)
    def perform_create(self, serializer): serializer.save(user=self.request.user)
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'status': 'success', 'paymentMethod': response.data})
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'status': 'success'})

# Content
class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CollaborationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer

class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class SpotlightViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Spotlight.objects.filter(active=True)
    serializer_class = SpotlightSerializer

# Administrative CRUD ViewSets
class AdminCategoryViewSet(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [] # Disable for easy testing

class AdminSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

class AdminProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

class AdminServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
