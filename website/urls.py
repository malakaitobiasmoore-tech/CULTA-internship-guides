from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('guides.urls')),          # home + guide pages
    path('guide/', include('guides.urls')),    # guide/<slug>/
    path('admin/', admin.site.urls),
]