
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('custom_user/', include('custom_user.urls')),
    path('admin/', admin.site.urls),
    path('board/', include('board.urls'))
]
