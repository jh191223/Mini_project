from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anonymization/', include('core.urls')),  # core 앱과 연결
]
