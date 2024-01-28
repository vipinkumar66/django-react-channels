from django.contrib import admin
from django.urls import path, include
from account.views import JWTCookieTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path('api/token', JWTCookieTokenObtainPairView.as_view(), name="token_obtain_pair")

]
