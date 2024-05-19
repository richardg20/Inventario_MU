"""
URL configuration for inventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from inventarioweb import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('productos/', views.productos, name="productos"),
    path('recepcion/<int:id>',views.recepcion, name="recepcion"),
    path('confirmar_recepcion/', views.confirmar_recepcion, name="confirmar_recepcion"),
    path('movimientos/', views.movimientos, name="movimientos"),
    path('historial/', views.historial, name="historial"),
    path('informe/', views.informe, name="informe")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)