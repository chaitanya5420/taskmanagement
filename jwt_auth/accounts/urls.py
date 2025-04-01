from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),  # Use function-based view
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login & Get JWT Tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh Access Token   
    # path('profile/', UserProfileView.as_view(), name='profile'),
    # path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    # path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    # path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

]