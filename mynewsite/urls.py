from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views   # your app is "core"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),   # homepage route
    path('contact/', views.contact, name='contact'),   # NEW contact route
    path('contact/success/', views.contact_success, name='contact_success'),  # NEW success route
]

# serve uploaded images in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

