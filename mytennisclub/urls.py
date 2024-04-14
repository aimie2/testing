from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from members import views
from mytennisclub import settings
from mytennisclub.settings import STATIC_ROOT, STATIC_URL


urlpatterns = [
    path('demo',views.showDemoPage),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

