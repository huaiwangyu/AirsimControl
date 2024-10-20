from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('airsim/', include('airsimcontrol.urls')),  # Include the urls from the airsimcontrol app
]