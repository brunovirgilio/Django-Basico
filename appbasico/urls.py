from django.urls import path
from .views import index, titulos, postagem, exibepost
from django.conf.urls.static import static

from projbasico import settings


urlpatterns = [
    path('', index, name='index'), #(endereço,nomeview)
    path('titulos/<int:pk>',titulos, name='titulos'), #(endereço,nomeview)
    path('postagem/', postagem, name='postagem'),
    path('historias/', exibepost, name='historias'),
    ]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
