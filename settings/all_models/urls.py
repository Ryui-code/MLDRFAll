from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='user_profile')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('students/', StudentsAPIView.as_view(), name='students-model'),
    path('house/', HouseAPIView.as_view(), name='house-model'),
    path('bank/', BankAPIView.as_view(), name='bank-model'),
    path('diabetes/', DiabetesAPIView.as_view(), name='diabetes-model'),
    path('avocado/', AvocadoAPIView.as_view(), name='avocado-model'),
    path('mushrooms-tree/', MushroomTreeAPIView.as_view(), name='mushrooms-tree'),
    path('mushrooms-logistic/', MushroomLogisticAPIView.as_view(), name='mushrooms-log'),
    path('telecom/', TelecomAPIView.as_view(), name='telecom-model'),
    path('hr/', HrAPIView.as_view(), name='hr-model'),
    path('', include(router.urls))
]