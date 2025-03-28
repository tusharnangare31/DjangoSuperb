from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('services/', views.services, name='services'),
    path('product/', views.product, name='product'),
    path('products/', include('Products.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
