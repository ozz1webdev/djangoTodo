from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', views.LogoutView.as_view(), name='signup'),
    path('', include('base.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
