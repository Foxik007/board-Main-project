from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import never_cache
from django.views.static import serve

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls'))
]
