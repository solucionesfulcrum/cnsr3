"""CNSR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from rest_framework import routers, permissions
from Asistencial import views as viewsAsis

from rest_framework_simplejwt import views as jwt_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'paciente', viewsAsis.PacienteViewSet)
router.register(r'examen', viewsAsis.ExamenViewSet)
router.register(r'archivo', viewsAsis.ArchivoViewSet)
router.register(r'proveedores', viewsAsis.proveedorViewSet)
router.register(r'provMaq', viewsAsis.provMaqViewSet)
router.register(r'personal', viewsAsis.personalViewSet)
router.register(r'ambiente', viewsAsis.ambienteViewSet)
router.register(r'incidenciaDsi', viewsAsis.incidenciaDsiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)