
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('user/',include('user.urls')),
    path('products/',include('products.urls')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.index_title='Greenco'
admin.site.site_header='Greenco'
admin.site.site_title='Greenco'