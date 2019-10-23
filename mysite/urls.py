from django.contrib import admin
from django.urls import path, include
from .routers import router, cliente_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(cliente_router.urls)),
    
]
