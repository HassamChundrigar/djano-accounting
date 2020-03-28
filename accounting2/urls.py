from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('general_journal/', include('app_general_journal.urls')),
    path('statement/', include('app_statement.urls')),
    path('', include('core.urls'))
]
