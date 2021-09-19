
from backend.settings import MEDIA_URL
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from backend.api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Root.as_view()),
    path('api/capture/', views.Capture.as_view()),
    path('api/checkout/', views.Checkout.as_view()),
    path('api/getcart/', views.GetCart.as_view()),
    path('api/start/', views.StartShoping.as_view()),
    path('api/inventory/', views.Inventory.as_view()),
]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
