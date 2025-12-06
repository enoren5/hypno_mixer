from django.contrib import admin
from django.urls import path, include
# from contents.views import CustomLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', CustomLoginView.as_view(),name='home'), 
    path('accounts/',include('django.contrib.auth.urls')),
    path('', include('contents.urls')),
    path(settings.ADMIN_PATH, admin.site.urls),
    # path('admin/', admin.site.urls),
    path("", include("gateway_defender.urls")),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Hypno Mixer'
admin.site.site_title = 'Hypno Mixer'