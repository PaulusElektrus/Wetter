# ! Der Admin Bereich !
from django.contrib import admin
# ! Der Import von der urls.py aus der lookup App !
from django.urls import path, include

urlpatterns = [
    # ! Admin Seite !
    path('admin/', admin.site.urls),
    # ! Die Einbindung von den urls.py aus der lookup App !
    path('', include('lookup.urls')),
]
