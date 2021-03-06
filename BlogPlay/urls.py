"""BlogPlay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from conteudo.api.viewsets import TagViewSetViewSet, PaginaViewSetViewSet
from detonado.api.viewsets import JogoViewSetViewSet

router = routers.DefaultRouter()

router.register(r'jogos', JogoViewSetViewSet)
router.register(r'tag', TagViewSetViewSet)
router.register(r'pagina', PaginaViewSetViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),

    #url de app terceiro
    path('ckeditor/', include('ckeditor_uploader.urls')),

    #url de app
    path('conteudo/',include('conteudo.urls')),
    path('',include('detonado.urls')),
    path('api/', include(router.urls))


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

